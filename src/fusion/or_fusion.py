"""Public decision-level OR example. No learned fusion implementation."""

def or_fusion(text_predictions, image_predictions):
    text_predictions = list(text_predictions)
    image_predictions = list(image_predictions)
    if len(text_predictions) != len(image_predictions):
        raise ValueError("Both prediction lists must refer to the same records")
    if any(value not in (0, 1) for value in text_predictions + image_predictions):
        raise ValueError("Predictions must be binary: 0 or 1")
    return [int(text or image) for text, image in zip(text_predictions, image_predictions)]
