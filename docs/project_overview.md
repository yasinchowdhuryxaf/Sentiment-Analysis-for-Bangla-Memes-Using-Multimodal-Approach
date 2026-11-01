# Project overview

## Research objective

Identify offensive and non-offensive Bangla memes by considering both caption text and visual content. The work examines whether combining the two modalities improves classification compared with individual text or image models.

## Research contribution

The thesis describes manual collection of 6,835 memes and captions from public social media sources, binary annotation by four annotators, and comparison of traditional text classifiers, a transformer-based text classifier, and image CNNs. Ties between annotators were referred to an additional expert (§3.2).

The experimental work spans dataset organization, caption cleaning, feature preparation, model comparison, decision fusion, and interpretation through accuracy, precision, recall, F1, confusion matrices, and ROC curves.

## Technology used in the research

| Area | Tools / models |
|---|---|
| Data handling | Python, pandas, NumPy, Pillow |
| Traditional text classification | TF-IDF, SVM, Logistic Regression, Random Forest |
| Transformer experiments | PyTorch, Hugging Face Transformers, BERT family |
| Visual classification | TensorFlow / Keras, ResNet50, VGG19 |
| Evaluation and visualization | scikit-learn, Matplotlib, Seaborn |

The public requirements install only the dependencies used by the selected public code. They are not an environment lockfile for the private experiments.

## What this release demonstrates

Readable source modules, synthetic walkthrough notebooks, high-level diagrams, selected thesis results, and an explicitly approved partial release of original data. The source is a portfolio companion, not an export of the entire research environment.

## Scope

Although the thesis title uses “sentiment analysis,” its target labels are offensive and non-offensive content. The reported results concern that binary task rather than positive / neutral / negative sentiment.

Author: Yasin Chowdhury Amit. Institution: East Delta University. Supervisor: Mohammed Morshed Rana. Source: thesis Chapters 1, 3, and 4.
