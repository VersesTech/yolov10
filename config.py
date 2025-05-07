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
