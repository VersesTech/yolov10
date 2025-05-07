import json
import yaml
from pathlib import Path
from tqdm import tqdm
import os

os.environ["PYDEVD_CONTAINER_RANDOM_ACCESS_MAX_ITEMS"] = "1000000000"

category_dict = {
    0: "box0_small",
    1: "box0_medium",
    2: "box0_large",
    3: "box1_medium",
    4: "box1_large",
    5: "box2_medium",
    6: "box2_large",
    7: "box3_small",
    8: "box3_medium",
    9: "box3_large",
    10: "cart_0",
    11: "cart_1",
    12: "cone_1",
    13: "traffic cone",
    14: "crate_0_small",
    15: "crate_1_small",
    16: "crate_0_large",
    17: "crate_1_large",
    18: "ram",
    19: "dvere",
    20: "euro_pallet",
    21: "shelf",
    22: "piso mojado",
}


def get_key(dictionary, value):
    return [key for key, val in dictionary.items() if val == value][0]


def convert_coco_json_to_yaml(json_file, output_dir, image_dir_path):
    # Create output directory if it doesn't exist
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # Load JSON data
    with open(json_file, "r") as f:
        data = json.load(f)

    # Prepare YAML data
    yaml_data = {
        "path": str(Path(json_file).parent),
        "train": "images/train",
        "val": "images/val",
        "test": "",
        "names": {
            get_key(category_dict, cat["name"]): cat["name"]
            for cat in data["categories"]
        },
        "nc": len(data["categories"]),
    }

    # Create image to annotation mapping
    img_to_anns = {}
    for ann in data["annotations"]:
        ann["category_id"] = get_key(category_dict, ann["category_id"])
        image_id = ann["image_id"]
        if image_id not in img_to_anns:
            img_to_anns[image_id] = []
        img_to_anns[image_id].append(ann)

    # To read all the image names and use the same filename for labels by changing .jpg at the end to .txt
    directory = Path(image_dir_path)
    files = sorted(directory.glob("*.jpg"))

    # Process annotations
    for idx, img in enumerate(tqdm(data["images"], desc="Processing annotations")):
        img_id = img["id"]
        filename = img["file_name"]
        width, height = img["width"], img["height"]

        annotations = []
        if img_id in img_to_anns:
            for ann in img_to_anns[img_id]:
                category_id = ann["category_id"]  # YOLO format uses 0-indexed classes
                bbox = ann["bbox"]
                x_center = (bbox[0] + bbox[2] / 2) / width
                y_center = (bbox[1] + bbox[3] / 2) / height
                bbox_width = bbox[2] / width
                bbox_height = bbox[3] / height

                annotations.append(
                    {
                        "class": category_id,
                        "x_center": x_center,
                        "y_center": y_center,
                        "width": bbox_width,
                        "height": bbox_height,
                    }
                )

        # Write COCO format annotation file with same name as image but .txt extension

        output_file = str(Path(output_dir).joinpath(files[idx].stem)) + ".txt"

        with open(output_file, "w") as f:
            for ann in annotations:
                f.write(
                    f"{ann['class']} {ann['x_center']:.6f} {ann['y_center']:.6f} {ann['width']:.6f} {ann['height']:.6f}\n"
                )

    # Write YAML file
    yaml_file = output_dir / "dataset_euro_pallet.yaml"
    with open(yaml_file, "w") as f:
        yaml.dump(yaml_data, f, sort_keys=False)

    print(f"Conversion complete. YAML file saved to {yaml_file}")


if __name__ == "__main__":
    json_file = "/home/vyasd/projects/ARCHIVED/yolov10/merged_coco_version_2_val_corrected.json"
    output_dir = (
        "/home/vyasd/projects/ARCHIVED/yolov10/datasets/warehouse-full/labels/val"
    )
    image_dir_path = (
        "/home/vyasd/projects/ARCHIVED/yolov10/datasets/warehouse-full/images/val/"
    )
    convert_coco_json_to_yaml(json_file, output_dir, image_dir_path)
