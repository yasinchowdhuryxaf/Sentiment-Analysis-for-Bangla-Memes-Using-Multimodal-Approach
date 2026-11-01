# Model architecture

![System architecture](../assets/system_architecture.png)

## Text branch

| Model family | High-level representation | Role |
|---|---|---|
| Support Vector Machine | Caption TF-IDF features | Traditional baseline |
| Logistic Regression | Caption TF-IDF features | Traditional baseline |
| Random Forest | Caption TF-IDF features | Traditional baseline |
| BERT family, named BanglishBERT in the thesis | Tokenized caption | Contextual text classification |

Public `src/text_models/baselines.py` exposes small estimator factories for inspection. It does not include the private experiment's training pipeline, fitted parameters, or model weights. The transformer checkpoint naming distinction is documented in [methodology](methodology.md).

## Image branch

ResNet50 and VGG19 are the image backbones reported in the thesis. At a high level, each branch receives a prepared image, extracts visual features, and produces a binary decision. Public code demonstrates input handling; full CNN training definitions and training orchestration are withheld.

## Decision branch

Public OR fusion combines two binary decisions. The diagram intentionally shows only the high-level prediction flow. Selected learned fusion results appear in the results summary, but learned fusion architecture details, training logic, feature construction, and implementation are not included in this release.

## Public module boundaries

| Folder | Public functionality |
|---|---|
| `src/preprocessing/` | Read configured CSV / JSON / Excel inputs; clean captions |
| `src/text_models/` | Token inspection; optional baseline estimator setup |
| `src/image_models/` | RGB conversion and resizing |
| `src/fusion/` | OR decisions |
| `src/evaluation/` | Confusion counts and binary metrics |

Source: thesis §§3.4–3.7. This is an explanatory architecture view rather than a full reproducibility specification.
