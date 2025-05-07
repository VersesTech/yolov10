import os
import yaml
import random
import shutil
from pathlib import Path
from tqdm import tqdm
from config import DATA_SOURCES, IMAGE_SETTINGS


def read_yaml(yaml_path):
    """Read and parse a YAML file."""
    with open(yaml_path, "r") as f:
        return yaml.safe_load(f)


def get_dataset_images(dataset_config):
    """Get all available images from a dataset."""
    dataset_yaml = read_yaml(dataset_config["path"])
    base_path = Path(dataset_yaml["path"])

    # Get all image files
    image_files = []
    for ext in IMAGE_SETTINGS["supported_formats"]:
        image_files.extend(list(base_path.glob(f"**/*{ext}")))

    return image_files


def process_dataset(dataset_config, output_dir, num_images):
    """Process a dataset to contribute the specified number of images."""
    dataset_yaml = read_yaml(dataset_config["path"])
    base_path = Path(dataset_yaml["path"])

    # Create output directories
    images_dir = Path(output_dir) / "images"
    labels_dir = Path(output_dir) / "labels"
    images_dir.mkdir(parents=True, exist_ok=True)
    labels_dir.mkdir(parents=True, exist_ok=True)

    # Get all available images
    available_images = get_dataset_images(dataset_config)

    if len(available_images) < num_images:
        print(
            f"Warning: Dataset {dataset_config['name']} has only {len(available_images)} images, "
            f"but {num_images} are requested. Using all available images."
        )
        selected_images = available_images
    else:
        selected_images = random.sample(available_images, num_images)

    processed_images = []
    for img_path in tqdm(selected_images, desc=f"Processing {dataset_config['name']}"):
        # Copy image
        new_img_path = images_dir / f"{dataset_config['name']}_{img_path.name}"
        shutil.copy2(img_path, new_img_path)

        # Copy corresponding label file if it exists
        label_path = img_path.parent / "labels" / f"{img_path.stem}.txt"
        if label_path.exists():
            new_label_path = (
                labels_dir / f"{dataset_config['name']}_{img_path.stem}.txt"
            )
            shutil.copy2(label_path, new_label_path)

        processed_images.append(str(new_img_path))

    return processed_images


def create_merged_dataset():
    """Create a merged dataset from all sources with specified distribution."""
    # Validate that inclusion percentages sum to 100
    total_inclusion = sum(ds["inclusion"] for ds in DATA_SOURCES)
    if (
        not abs(total_inclusion - 100) < 0.01
    ):  # Allow for small floating point differences
        raise ValueError(
            f"Inclusion percentages must sum to 100, got {total_inclusion}"
        )

    output_dir = Path(IMAGE_SETTINGS["output_dir"])
    output_dir.mkdir(parents=True, exist_ok=True)

    # Calculate number of images to take from each dataset
    total_images = IMAGE_SETTINGS["total_images"]
    dataset_allocations = {
        ds["name"]: int(total_images * ds["inclusion"] / 100) for ds in DATA_SOURCES
    }

    # Adjust for rounding errors to ensure we get exactly total_images
    current_total = sum(dataset_allocations.values())
    if current_total != total_images:
        diff = total_images - current_total
        # Add the difference to the largest dataset
        largest_dataset = max(dataset_allocations.items(), key=lambda x: x[1])[0]
        dataset_allocations[largest_dataset] += diff

    all_images = []
    for dataset in DATA_SOURCES:
        num_images = dataset_allocations[dataset["name"]]
        print(
            f"\nProcessing {dataset['name']} for {num_images} images ({dataset['inclusion']}% of total)"
        )
        images = process_dataset(dataset, output_dir, num_images)
        all_images.extend(images)

    # Create merged dataset YAML
    merged_yaml = {
        "path": str(output_dir),
        "train": str(output_dir / "images"),
        "val": str(output_dir / "images"),  # You might want to split this differently
        "names": {0: "object"},  # Update this based on your classes
    }

    with open(output_dir / "dataset.yaml", "w") as f:
        yaml.dump(merged_yaml, f)

    print(f"\nCreated merged dataset with {len(all_images)} images")
    print("Distribution of images:")
    for dataset in DATA_SOURCES:
        count = len(
            [
                img
                for img in all_images
                if img.startswith(str(output_dir / "images" / dataset["name"]))
            ]
        )
        print(f"- {dataset['name']}: {count} images ({count/len(all_images)*100:.1f}%)")

    return str(output_dir / "dataset.yaml")


if __name__ == "__main__":
    merged_yaml_path = create_merged_dataset()
    print(f"Merged dataset YAML created at: {merged_yaml_path}")
