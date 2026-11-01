"""Binary metrics with explicit label order: non-offensive, offensive."""

def binary_report(actual, predicted):
    actual, predicted = list(actual), list(predicted)
    if not actual or len(actual) != len(predicted):
        raise ValueError("Expected equal, non-empty label and prediction lists")
    if any(value not in (0, 1) for value in actual + predicted):
        raise ValueError("Labels and predictions must be 0 or 1")
    matrix = [[0, 0], [0, 0]]
    for truth, guess in zip(actual, predicted):
        matrix[truth][guess] += 1
    classes = {}
    for label in (0, 1):
        tp = matrix[label][label]
        support = sum(matrix[label])
        predicted_count = matrix[0][label] + matrix[1][label]
        precision = tp / predicted_count if predicted_count else 0.0
        recall = tp / support if support else 0.0
        f1 = 2 * precision * recall / (precision + recall) if precision + recall else 0.0
        classes[str(label)] = dict(precision=precision, recall=recall, f1=f1, support=support)
    return {
        "accuracy": (matrix[0][0] + matrix[1][1]) / len(actual),
        "confusion_matrix": matrix,
        "classes": classes,
        "macro_f1": sum(row["f1"] for row in classes.values()) / 2,
        "zero_division": 0,
    }
