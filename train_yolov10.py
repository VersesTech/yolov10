import argparse
from ultralytics import YOLOv10
from ultralytics import YOLO

def train_yolo(
    model_type,
    data_yaml,
    epochs,
    batch_size,
    img_size,
    export_format=None,
):
    # Load the model
    if 'yolov10' in model_type:
        if model_type.startswith("jameslahm/yolov10m"):
            model = YOLOv10.from_pretrained(model_type)
        else:
            model = YOLOv10(model_type)
    elif 'yolov8' in model_type:
        model = YOLO(model_type)
    else:
        raise "Model not supported"

    # Train the model
    model.train(
        data=data_yaml,
        epochs=epochs,
        batch=batch_size,
        imgsz=img_size,
        patience=10,
        device=0,
        freeze=10,
        close_mosaic=15
    )

    # Export the model if specified
    if export_format:
        model.export(format=export_format)


def export_model(model_path, export_format):
    model = YOLOv10.from_pretrained(model_path)
    model.export(format=export_format, nms=True)


def main():
    print("Training YOLO model")
    parser = argparse.ArgumentParser(description="Train YOLO model")
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
    parser.add_argument("--batch", type=int, default=32, help="Batch size")
    parser.add_argument("--imgsz", type=int, default=640, help="Image size")
    parser.add_argument(
        "--export", type=str, choices=["onnx"], help="Export format (optional)"
    )

    args = parser.parse_args()

    train_yolo(
        args.model,
        args.data,
        args.epochs,
        args.batch,
        args.imgsz,
        args.export,
    )


if __name__ == "__main__":
    main()
    # export_model("jameslahm/yolov10x", "onnx")
