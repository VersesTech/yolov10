from pycocotools.coco import COCO
import json
import shutil
from pathlib import Path
from io import BytesIO
from tqdm import tqdm

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


def convert_coco_json_to_yaml(json_file, output_dir):
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
        img_id = ann["image_id"]
        if img_id not in img_to_anns:
            img_to_anns[img_id] = []
        img_to_anns[img_id].append(ann)

    # Process annotations
    for img in tqdm(data["images"], desc="Processing annotations"):
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

        # Write YOLO format annotation file
        output_file = output_dir / f"{str(img_id)+Path(filename).stem}.txt"
        with open(output_file, "w") as f:
            for ann in annotations:
                f.write(
                    f"{ann['class']} {ann['x_center']:.6f} {ann['y_center']:.6f} {ann['width']:.6f} {ann['height']:.6f}\n"
                )

    # Write YAML file
    yaml_file = output_dir / "dataset_full.yaml"
    with open(yaml_file, "w") as f:
        yaml.dump(yaml_data, f, sort_keys=False)

    print(f"Conversion complete. YAML file saved to {yaml_file}")


def merge_coco_json(json_files, output_file, target_image_dir):
    merged_annotations = {
        "info": {},
        "licenses": [],
        "images": [],
        "annotations": [],
        "categories": [],
    }

    image_id_offset = 0
    annotation_id_offset = 0
    category_id_offset = 0
    existing_category_ids = set()

    for idx, file in enumerate(json_files):
        # destination_folder =
        coco = COCO(file)

        # Update image IDs to avoid conflicts
        for image in coco.dataset["images"]:
            image["id"] += image_id_offset
            target_image_name = (
                target_image_dir
                + Path(file).parent.stem
                + Path(image["file_name"]).stem
                + ".jpg"
            )
            image["file_name"] = target_image_name

            # shutil.copy2(Path(file).parent / image["file_name"], target_image_name)
            merged_annotations["images"].append(image)

        # Update annotation IDs to avoid conflicts
        for annotation in coco.dataset["annotations"]:
            annotation["id"] += annotation_id_offset
            annotation["image_id"] += image_id_offset
            merged_annotations["annotations"].append(annotation)

        # # Update categories and their IDs to avoid conflicts
        for category in coco.dataset["categories"]:
            if category["id"] not in existing_category_ids:
                # category["id"] += category_id_offset
                merged_annotations["categories"].append(category)
                existing_category_ids.add(category["id"])

        image_id_offset = len(merged_annotations["images"])
        annotation_id_offset = len(merged_annotations["annotations"])
        category_id_offset = len(merged_annotations["categories"])

    # Save merged annotations to output file
    # with open(output_file, "w") as f:
    #     json.dump(merged_annotations, f)
    print("Saving merged annotations...")

    # Convert to bytes first
    json_bytes = json.dumps(merged_annotations).encode("utf-8")
    total_size = len(json_bytes)

    # Create a byte stream
    stream = BytesIO(json_bytes)
    chunk_size_mb = 1  # 1 MB chunks
    chunk_size = chunk_size_mb * 1024 * 1024

    with open(output_file, "w") as f:
        with tqdm(
            total=total_size, unit="B", unit_scale=True, desc="Writing JSON"
        ) as pbar:
            while True:
                chunk = stream.read(chunk_size).decode("utf-8")
                if not chunk:
                    break
                f.write(chunk)
                pbar.update(len(chunk.encode("utf-8")))


if __name__ == "__main__":

    # List of paths to COCO JSON files to merge
    # json_files = [
    #     "/home/vyasd/projects/warehouse-demo/data/data-from-fraunhofer/version_2/warehouse_3002-1280x720/train/train_pbr/000000/scene_gt_coco.json",
    #     "/home/vyasd/projects/warehouse-demo/data/data-from-fraunhofer/version_2/warehouse_3002-1280x720/train/train_pbr/000001/scene_gt_coco.json",
    # ]
    json_files = [
        # "/home/vyasd/projects/ARCHIVED/warehouse-demo/data/data-from-fraunhofer/version_2/warehouse_3002-1280x720/train/train_pbr/000000/scene_gt_coco.json",
        # "/home/vyasd/projects/ARCHIVED/warehouse-demo/data/data-from-fraunhofer/version_2/warehouse_3002-1280x720/train/train_pbr/000001/scene_gt_coco.json",
        # "/home/vyasd/projects/ARCHIVED/warehouse-demo/data/data-from-fraunhofer/version_2/warehouse_3002-1280x720/train/train_pbr/000002/scene_gt_coco.json",
        # "/home/vyasd/projects/ARCHIVED/warehouse-demo/data/data-from-fraunhofer/version_2/warehouse_3002-1280x720/train/train_pbr/000003/scene_gt_coco.json",
        # "/home/vyasd/projects/ARCHIVED/warehouse-demo/data/data-from-fraunhofer/version_2/warehouse_3002-1280x720/train/train_pbr/000004/scene_gt_coco.json",
        # "/home/vyasd/projects/ARCHIVED/warehouse-demo/data/data-from-fraunhofer/version_2/warehouse_3002-1280x720/train/train_pbr/000005/scene_gt_coco.json",
        # "/home/vyasd/projects/ARCHIVED/warehouse-demo/data/data-from-fraunhofer/version_2/warehouse_3002-1280x720/train/train_pbr/000006/scene_gt_coco.json",
        # "/home/vyasd/projects/ARCHIVED/warehouse-demo/data/data-from-fraunhofer/version_2/warehouse_3002-1280x720/train/train_pbr/000007/scene_gt_coco.json",
        # "/home/vyasd/projects/ARCHIVED/warehouse-demo/data/data-from-fraunhofer/version_2/warehouse_3002-1280x720/train/train_pbr/000008/scene_gt_coco.json",
        "/home/vyasd/projects/ARCHIVED/warehouse-demo/data/data-from-fraunhofer/version_2/warehouse_3002-1280x720/val/train_pbr/000000/scene_gt_coco.json",
        "/home/vyasd/projects/ARCHIVED/warehouse-demo/data/data-from-fraunhofer/version_2/warehouse_3002-1280x720/val/train_pbr/000001/scene_gt_coco.json",
        "/home/vyasd/projects/ARCHIVED/warehouse-demo/data/data-from-fraunhofer/version_2/warehouse_3002-1280x720/val/train_pbr/000002/scene_gt_coco.json",
        "/home/vyasd/projects/ARCHIVED/warehouse-demo/data/data-from-fraunhofer/version_2/warehouse_3002-1280x720/val/train_pbr/000003/scene_gt_coco.json",
        "/home/vyasd/projects/ARCHIVED/warehouse-demo/data/data-from-fraunhofer/version_2/warehouse_3002-1280x720/val/train_pbr/000004/scene_gt_coco.json",
        "/home/vyasd/projects/ARCHIVED/warehouse-demo/data/data-from-fraunhofer/version_2/warehouse_3002-1280x720/val/train_pbr/000005/scene_gt_coco.json",
        "/home/vyasd/projects/ARCHIVED/warehouse-demo/data/data-from-fraunhofer/version_2/warehouse_3002-1280x720/val/train_pbr/000006/scene_gt_coco.json",
        "/home/vyasd/projects/ARCHIVED/warehouse-demo/data/data-from-fraunhofer/version_2/warehouse_3002-1280x720/val/train_pbr/000007/scene_gt_coco.json",
        "/home/vyasd/projects/ARCHIVED/warehouse-demo/data/data-from-fraunhofer/version_2/warehouse_3002-1280x720/val/train_pbr/000008/scene_gt_coco.json",
    ]
    target_image_dir = "images/val/"

    # Output file path for merged annotations
    output_file = "./merged_coco_version_2_val_corrected.json"

    # Merge COCO JSON files
    merge_coco_json(json_files, output_file, target_image_dir)

    print("Merged COCO JSON files saved to", output_file)
# end main
