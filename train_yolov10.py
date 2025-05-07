import argparse
from ultralytics import YOLOv10
from prepare_data import create_merged_dataset


def train_yolov10(
    model_type,
    data_yaml,
    epochs,
    batch_size,
    img_size,
    export_format=None,
    prepare_data=True,
):
    # Prepare the dataset if requested
    if prepare_data:
        print("Preparing and merging datasets...")
        data_yaml = create_merged_dataset()
        print(f"Using merged dataset from: {data_yaml}")

    # Load the model
    if model_type.startswith("jameslahm/yolov10x"):
        model = YOLOv10.from_pretrained(model_type)
    else:
        model = YOLOv10(model_type)

    # Train the model
    model.train(
        data=data_yaml,
        epochs=epochs,
        batch=batch_size,
        imgsz=img_size,
    )

    # Export the model if specified
    if export_format:
        model.export(format=export_format)


def export_model(model_path, export_format):
    model = YOLOv10.from_pretrained(model_path)
    model.export(format=export_format, nms=True)


def main():
    print("Training YOLOv10 model")
    parser = argparse.ArgumentParser(description="Train YOLOv10 model")
    parser.add_argument(
        "--model",
        type=str,
        default="models/yolov10n.pt",
        help="Path to model or pretrained model name",
    )
    parser.add_argument(
        "--data",
        type=str,
        default="/app/datasets/warehouse-full/dataset_full.yaml",
        help="Path to data YAML file",
    )
    parser.add_argument(
        "--epochs", type=int, default=100, help="Number of epochs to train"
    )
    parser.add_argument("--batch", type=int, default=2, help="Batch size")
    parser.add_argument("--imgsz", type=int, default=640, help="Image size")
    parser.add_argument(
        "--export", type=str, choices=["onnx"], help="Export format (optional)"
    )
    parser.add_argument(
        "--skip-data-prep",
        action="store_true",
        help="Skip dataset preparation and use existing data YAML",
    )

    args = parser.parse_args()

    train_yolov10(
        args.model,
        args.data,
        args.epochs,
        args.batch,
        args.imgsz,
        args.export,
        not args.skip_data_prep,
    )


if __name__ == "__main__":
    main()
    # export_model("jameslahm/yolov10x", "onnx")
