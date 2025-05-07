"""
Configuration file for data sources and their target distribution in the final dataset.
Each data source should be a dictionary with the following keys:
- name: A descriptive name for the dataset
- path: Path to the dataset YAML file
- inclusion: Target percentage in the final dataset (should sum to 100)
"""

DATA_SOURCES = [
    {
        "name": "warehouse_full",
        "path": "<path to yaml file>",
        "inclusion": 50,  # Will make up 50% of the final dataset
    },
    {
        "name": "ghent_uni",
        "path": "<path to yaml file>",
        "inclusion": 50,  
    },
    
]
output_dir_suffix = "_".join([f"{ds['name']}_{ds['inclusion']}" for ds in DATA_SOURCES])
# Dataset settings
DATASET_SETTINGS = {
    "output_dir": f"~/projects/datasets/merged_{output_dir_suffix}",  
    "total_images": 1000,  # Total number of images in the final dataset
}


### MERGED Categories

"""
Merged categories from different data sources:
1. Warehouse synthetic
2. Warehouse real world
3. MSCOCO2017
"""

MERGED_CATEGORIES = {
    # Warehouse Synthetic Categories
    "box0_small": {"name": "box0_small", "supercategory": "box", "source": "warehouse_synthetic", "original_id": "box0_small", "id": 1},
    "box0_medium": {"name": "box0_medium", "supercategory": "box", "source": "warehouse_synthetic", "original_id": "box0_medium", "id": 2},
    "box0_large": {"name": "box0_large", "supercategory": "box", "source": "warehouse_synthetic", "original_id": "box0_large", "id": 3},
    "box1_medium": {"name": "box1_medium", "supercategory": "box", "source": "warehouse_synthetic", "original_id": "box1_medium", "id": 4},
    "box1_large": {"name": "box1_large", "supercategory": "box", "source": "warehouse_synthetic", "original_id": "box1_large", "id": 5},
    "box2_medium": {"name": "box2_medium", "supercategory": "box", "source": "warehouse_synthetic", "original_id": "box2_medium", "id": 6},
    "box2_large": {"name": "box2_large", "supercategory": "box", "source": "warehouse_synthetic", "original_id": "box2_large", "id": 7},
    "box3_small": {"name": "box3_small", "supercategory": "box", "source": "warehouse_synthetic", "original_id": "box3_small", "id": 8},
    "box3_medium": {"name": "box3_medium", "supercategory": "box", "source": "warehouse_synthetic", "original_id": "box3_medium", "id": 9},
    "box3_large": {"name": "box3_large", "supercategory": "box", "source": "warehouse_synthetic", "original_id": "box3_large", "id": 10},
    "cart_0": {"name": "cart_0", "supercategory": "cart", "source": "warehouse_synthetic", "original_id": "cart_0", "id": 11},
    "cart_1": {"name": "cart_1", "supercategory": "cart", "source": "warehouse_synthetic", "original_id": "cart_1", "id": 12},
    "cone_1": {"name": "cone_1", "supercategory": "cone", "source": "warehouse_synthetic", "original_id": "cone_1", "id": 13},
    "traffic_cone": {"name": "traffic cone", "supercategory": "cone", "source": "warehouse_synthetic", "original_id": "traffic cone", "id": 14},
    "crate_0_small": {"name": "crate_0_small", "supercategory": "crate", "source": "warehouse_synthetic", "original_id": "crate_0_small", "id": 15},
    "crate_1_small": {"name": "crate_1_small", "supercategory": "crate", "source": "warehouse_synthetic", "original_id": "crate_1_small", "id": 16},
    "crate_0_large": {"name": "crate_0_large", "supercategory": "crate", "source": "warehouse_synthetic", "original_id": "crate_0_large", "id": 17},
    "crate_1_large": {"name": "crate_1_large", "supercategory": "crate", "source": "warehouse_synthetic", "original_id": "crate_1_large", "id": 18},
    "ram": {"name": "ram", "supercategory": "ram", "source": "warehouse_synthetic", "original_id": "ram", "id": 19},
    "dvere": {"name": "dvere", "supercategory": "door", "source": "warehouse_synthetic", "original_id": "dvere", "id": 20},
    "euro_pallet": {"name": "euro_pallet", "supercategory": "pallet", "source": "warehouse_synthetic", "original_id": "euro_pallet", "id": 21},
    "shelf": {"name": "shelf", "supercategory": "shelf", "source": "warehouse_synthetic", "original_id": "shelf", "id": 22},
    "piso_mojado": {"name": "piso mojado", "supercategory": "floor", "source": "warehouse_synthetic", "original_id": "piso mojado", "id": 23},

    # Warehouse Real World Categories
    "pallet": {"name": "pallet", "supercategory": "warehouse", "source": "warehouse_real", "original_id": 1, "id": 24},
    "cardboard_box": {"name": "cardboard box", "supercategory": "warehouse", "source": "warehouse_real", "original_id": 2, "id": 25},
    "forklift": {"name": "forklift", "supercategory": "warehouse", "source": "warehouse_real", "original_id": 3, "id": 26},
    "warehouse_shelf": {"name": "warehouse shelf", "supercategory": "warehouse", "source": "warehouse_real", "original_id": 4, "id": 27},
    "person_safety_vest": {"name": "person in safety vest", "supercategory": "warehouse", "source": "warehouse_real", "original_id": 5, "id": 28},
    "loading_dock": {"name": "loading dock", "supercategory": "warehouse", "source": "warehouse_real", "original_id": 6, "id": 29},
    "shipping_container": {"name": "shipping container", "supercategory": "warehouse", "source": "warehouse_real", "original_id": 7, "id": 30},
    "hand_truck": {"name": "hand truck", "supercategory": "warehouse", "source": "warehouse_real", "original_id": 8, "id": 31},
    "pallet_jack": {"name": "pallet jack", "supercategory": "warehouse", "source": "warehouse_real", "original_id": 9, "id": 32},
    "storage_rack": {"name": "storage rack", "supercategory": "warehouse", "source": "warehouse_real", "original_id": 10, "id": 33},
    "warehouse_worker": {"name": "warehouse worker", "supercategory": "warehouse", "source": "warehouse_real", "original_id": 11, "id": 34},
    "package": {"name": "package", "supercategory": "warehouse", "source": "warehouse_real", "original_id": 12, "id": 35},
    "wooden_crate": {"name": "wooden crate", "supercategory": "warehouse", "source": "warehouse_real", "original_id": 13, "id": 36},
    "metal_container": {"name": "metal container", "supercategory": "warehouse", "source": "warehouse_real", "original_id": 14, "id": 37},
    "safety_cone": {"name": "safety cone", "supercategory": "warehouse", "source": "warehouse_real", "original_id": 15, "id": 38},
    "industrial_cart": {"name": "industrial cart", "supercategory": "warehouse", "source": "warehouse_real", "original_id": 16, "id": 39},
    "warehouse_door": {"name": "warehouse door", "supercategory": "warehouse", "source": "warehouse_real", "original_id": 17, "id": 40},
    "loading_bay": {"name": "loading bay", "supercategory": "warehouse", "source": "warehouse_real", "original_id": 18, "id": 41},
    "safety_barrier": {"name": "safety barrier", "supercategory": "warehouse", "source": "warehouse_real", "original_id": 19, "id": 42},

    # MSCOCO2017 Categories
    "person": {"name": "person", "supercategory": "person", "source": "mscoco2017", "original_id": 1, "id": 43},
    "bicycle": {"name": "bicycle", "supercategory": "vehicle", "source": "mscoco2017", "original_id": 2, "id": 44},
    "car": {"name": "car", "supercategory": "vehicle", "source": "mscoco2017", "original_id": 3, "id": 45},
    "motorcycle": {"name": "motorcycle", "supercategory": "vehicle", "source": "mscoco2017", "original_id": 4, "id": 46},
    "airplane": {"name": "airplane", "supercategory": "vehicle", "source": "mscoco2017", "original_id": 5, "id": 47},
    "bus": {"name": "bus", "supercategory": "vehicle", "source": "mscoco2017", "original_id": 6, "id": 48},
    "train": {"name": "train", "supercategory": "vehicle", "source": "mscoco2017", "original_id": 7, "id": 49},
    "truck": {"name": "truck", "supercategory": "vehicle", "source": "mscoco2017", "original_id": 8, "id": 50},
    "boat": {"name": "boat", "supercategory": "vehicle", "source": "mscoco2017", "original_id": 9, "id": 51},
    "traffic_light": {"name": "traffic light", "supercategory": "outdoor", "source": "mscoco2017", "original_id": 10, "id": 52},
    "fire_hydrant": {"name": "fire hydrant", "supercategory": "outdoor", "source": "mscoco2017", "original_id": 11, "id": 53},
    "stop_sign": {"name": "stop sign", "supercategory": "outdoor", "source": "mscoco2017", "original_id": 12, "id": 54},
    "parking_meter": {"name": "parking meter", "supercategory": "outdoor", "source": "mscoco2017", "original_id": 13, "id": 55},
    "bench": {"name": "bench", "supercategory": "outdoor", "source": "mscoco2017", "original_id": 14, "id": 56},
    "bird": {"name": "bird", "supercategory": "animal", "source": "mscoco2017", "original_id": 15, "id": 57},
    "cat": {"name": "cat", "supercategory": "animal", "source": "mscoco2017", "original_id": 16, "id": 58},
    "dog": {"name": "dog", "supercategory": "animal", "source": "mscoco2017", "original_id": 17, "id": 59},
    "horse": {"name": "horse", "supercategory": "animal", "source": "mscoco2017", "original_id": 18, "id": 60},
    "sheep": {"name": "sheep", "supercategory": "animal", "source": "mscoco2017", "original_id": 19, "id": 61},
    "cow": {"name": "cow", "supercategory": "animal", "source": "mscoco2017", "original_id": 20, "id": 62},
    "elephant": {"name": "elephant", "supercategory": "animal", "source": "mscoco2017", "original_id": 21, "id": 63},
    "bear": {"name": "bear", "supercategory": "animal", "source": "mscoco2017", "original_id": 22, "id": 64},
    "zebra": {"name": "zebra", "supercategory": "animal", "source": "mscoco2017", "original_id": 23, "id": 65},
    "giraffe": {"name": "giraffe", "supercategory": "animal", "source": "mscoco2017", "original_id": 24, "id": 66},
    "backpack": {"name": "backpack", "supercategory": "accessory", "source": "mscoco2017", "original_id": 25, "id": 67},
    "umbrella": {"name": "umbrella", "supercategory": "accessory", "source": "mscoco2017", "original_id": 26, "id": 68},
    "handbag": {"name": "handbag", "supercategory": "accessory", "source": "mscoco2017", "original_id": 27, "id": 69},
    "tie": {"name": "tie", "supercategory": "accessory", "source": "mscoco2017", "original_id": 28, "id": 70},
    "suitcase": {"name": "suitcase", "supercategory": "accessory", "source": "mscoco2017", "original_id": 29, "id": 71},
    "frisbee": {"name": "frisbee", "supercategory": "sports", "source": "mscoco2017", "original_id": 30, "id": 72},
    "skis": {"name": "skis", "supercategory": "sports", "source": "mscoco2017", "original_id": 31, "id": 73},
    "snowboard": {"name": "snowboard", "supercategory": "sports", "source": "mscoco2017", "original_id": 32, "id": 74},
    "sports_ball": {"name": "sports ball", "supercategory": "sports", "source": "mscoco2017", "original_id": 33, "id": 75},
    "kite": {"name": "kite", "supercategory": "sports", "source": "mscoco2017", "original_id": 34, "id": 76},
    "baseball_bat": {"name": "baseball bat", "supercategory": "sports", "source": "mscoco2017", "original_id": 35, "id": 77},
    "baseball_glove": {"name": "baseball glove", "supercategory": "sports", "source": "mscoco2017", "original_id": 36, "id": 78},
    "skateboard": {"name": "skateboard", "supercategory": "sports", "source": "mscoco2017", "original_id": 37, "id": 79},
    "surfboard": {"name": "surfboard", "supercategory": "sports", "source": "mscoco2017", "original_id": 38, "id": 80},
    "tennis_racket": {"name": "tennis racket", "supercategory": "sports", "source": "mscoco2017", "original_id": 39, "id": 81},
    "bottle": {"name": "bottle", "supercategory": "kitchen", "source": "mscoco2017", "original_id": 40, "id": 82},
    "wine_glass": {"name": "wine glass", "supercategory": "kitchen", "source": "mscoco2017", "original_id": 41, "id": 83},
    "cup": {"name": "cup", "supercategory": "kitchen", "source": "mscoco2017", "original_id": 42, "id": 84},
    "fork": {"name": "fork", "supercategory": "kitchen", "source": "mscoco2017", "original_id": 43, "id": 85},
    "knife": {"name": "knife", "supercategory": "kitchen", "source": "mscoco2017", "original_id": 44, "id": 86},
    "spoon": {"name": "spoon", "supercategory": "kitchen", "source": "mscoco2017", "original_id": 45, "id": 87},
    "bowl": {"name": "bowl", "supercategory": "kitchen", "source": "mscoco2017", "original_id": 46, "id": 88},
    "banana": {"name": "banana", "supercategory": "food", "source": "mscoco2017", "original_id": 47, "id": 89},
    "apple": {"name": "apple", "supercategory": "food", "source": "mscoco2017", "original_id": 48, "id": 90},
    "sandwich": {"name": "sandwich", "supercategory": "food", "source": "mscoco2017", "original_id": 49, "id": 91},
    "orange": {"name": "orange", "supercategory": "food", "source": "mscoco2017", "original_id": 50, "id": 92},
    "broccoli": {"name": "broccoli", "supercategory": "food", "source": "mscoco2017", "original_id": 51, "id": 93},
    "carrot": {"name": "carrot", "supercategory": "food", "source": "mscoco2017", "original_id": 52, "id": 94},
    "hot_dog": {"name": "hot dog", "supercategory": "food", "source": "mscoco2017", "original_id": 53, "id": 95},
    "pizza": {"name": "pizza", "supercategory": "food", "source": "mscoco2017", "original_id": 54, "id": 96},
    "donut": {"name": "donut", "supercategory": "food", "source": "mscoco2017", "original_id": 55, "id": 97},
    "cake": {"name": "cake", "supercategory": "food", "source": "mscoco2017", "original_id": 56, "id": 98},
    "chair": {"name": "chair", "supercategory": "furniture", "source": "mscoco2017", "original_id": 57, "id": 99},
    "couch": {"name": "couch", "supercategory": "furniture", "source": "mscoco2017", "original_id": 58, "id": 100},
    "potted_plant": {"name": "potted plant", "supercategory": "furniture", "source": "mscoco2017", "original_id": 59, "id": 101},
    "bed": {"name": "bed", "supercategory": "furniture", "source": "mscoco2017", "original_id": 60, "id": 102},
    "dining_table": {"name": "dining table", "supercategory": "furniture", "source": "mscoco2017", "original_id": 61, "id": 103},
    "toilet": {"name": "toilet", "supercategory": "furniture", "source": "mscoco2017", "original_id": 62, "id": 104},
    "tv": {"name": "tv", "supercategory": "electronic", "source": "mscoco2017", "original_id": 63, "id": 105},
    "laptop": {"name": "laptop", "supercategory": "electronic", "source": "mscoco2017", "original_id": 64, "id": 106},
    "mouse": {"name": "mouse", "supercategory": "electronic", "source": "mscoco2017", "original_id": 65, "id": 107},
    "remote": {"name": "remote", "supercategory": "electronic", "source": "mscoco2017", "original_id": 66, "id": 108},
    "keyboard": {"name": "keyboard", "supercategory": "electronic", "source": "mscoco2017", "original_id": 67, "id": 109},
    "cell_phone": {"name": "cell phone", "supercategory": "electronic", "source": "mscoco2017", "original_id": 68, "id": 110},
    "microwave": {"name": "microwave", "supercategory": "appliance", "source": "mscoco2017", "original_id": 69, "id": 111},
    "oven": {"name": "oven", "supercategory": "appliance", "source": "mscoco2017", "original_id": 70, "id": 112},
    "toaster": {"name": "toaster", "supercategory": "appliance", "source": "mscoco2017", "original_id": 71, "id": 113},
    "sink": {"name": "sink", "supercategory": "appliance", "source": "mscoco2017", "original_id": 72, "id": 114},
    "refrigerator": {"name": "refrigerator", "supercategory": "appliance", "source": "mscoco2017", "original_id": 73, "id": 115},
    "book": {"name": "book", "supercategory": "indoor", "source": "mscoco2017", "original_id": 74, "id": 116},
    "clock": {"name": "clock", "supercategory": "indoor", "source": "mscoco2017", "original_id": 75, "id": 117},
    "vase": {"name": "vase", "supercategory": "indoor", "source": "mscoco2017", "original_id": 76, "id": 118},
    "scissors": {"name": "scissors", "supercategory": "indoor", "source": "mscoco2017", "original_id": 77, "id": 119},
    "teddy_bear": {"name": "teddy bear", "supercategory": "indoor", "source": "mscoco2017", "original_id": 78, "id": 120},
    "hair_drier": {"name": "hair drier", "supercategory": "indoor", "source": "mscoco2017", "original_id": 79, "id": 121},
    "toothbrush": {"name": "toothbrush", "supercategory": "indoor", "source": "mscoco2017", "original_id": 80, "id": 122}
} 