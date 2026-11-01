"""Run a synthetic data-flow walkthrough; no training or research scores."""
import json
from src.preprocessing.data import configured_paths, load_records, resolve_image
from src.preprocessing.text import clean_caption
from src.text_models.features import token_counts
from src.image_models.inputs import load_rgb_image
from src.fusion.or_fusion import or_fusion
from src.evaluation.metrics import binary_report

def main():
    dataset, image_root = configured_paths()
    records = load_records(dataset)
    if not records:
        raise ValueError("The walkthrough requires at least one record")
    print("PUBLIC DATA-FLOW DEMO — not a research evaluation")
    print(f"Loaded {len(records)} records")
    print("Cleaned first caption:", clean_caption(records[0]["Caption"]))
    print("Frequent tokens:", token_counts(row["Caption"] for row in records).most_common(5))
    image = load_rgb_image(resolve_image(image_root, records[0]["Image_Path"]))
    print("Prepared first image:", image.mode, image.size)
    if not all("Demo_Text_Pred" in row and "Demo_Image_Pred" in row for row in records):
        print("No synthetic prediction fixtures supplied; no model inference was performed.")
        return
    print("Using supplied demonstration predictions, not trained-model predictions.")
    predictions = or_fusion([row["Demo_Text_Pred"] for row in records], [row["Demo_Image_Pred"] for row in records])
    actual = [int(row["Label"] == "Offensive") for row in records]
    print(json.dumps(binary_report(actual, predictions), indent=2))

if __name__ == "__main__":
    main()
