"""Unfitted baseline examples only; no private experiment configuration."""

def make_baseline(name="logistic_regression"):
    from sklearn.pipeline import Pipeline
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.linear_model import LogisticRegression
    from sklearn.svm import LinearSVC
    from sklearn.ensemble import RandomForestClassifier

    choices = {
        "logistic_regression": lambda: LogisticRegression(max_iter=1000),
        "svm": lambda: LinearSVC(random_state=42),
        "random_forest": lambda: RandomForestClassifier(random_state=42),
    }
    if name not in choices:
        raise ValueError(f"Choose one of {sorted(choices)}")
    return Pipeline([("tfidf", TfidfVectorizer()), ("classifier", choices[name]())])
