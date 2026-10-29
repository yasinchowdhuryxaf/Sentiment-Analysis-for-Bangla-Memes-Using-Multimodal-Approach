# Multimodal Bengali Meme Sentiment Analysis

A novel Deep Learning framework combining textual and visual data to automate content moderation for low-resource languages. This architecture achieves state-of-the-art accuracy by effectively fusing BanglishBERT and VGG19.

## 🚀 Key Achievement
* **Performance Breakthrough:** Achieved highest classification accuracy outperforming existing benchmarks using a custom multimodal late-fusion strategy.

## 📊 Methodology & Architecture
1. **Textual Pipeline:** Feature extraction utilizing BanglishBERT alongside traditional ML baselines (SVM, LR, RF).
2. **Visual Pipeline:** High-level feature representation extraction using ResNet50 and VGG19 CNNs.
3. **Fusion Layer:** Dual-modality late-fusion technique combining outputs to maximize distinction between Offensive and Non-Offensive content.

## 📁 Repository Structure
* `src/models/` - Custom late-fusion model definitions and architecture.
* `src/pipeline/` - Text preprocessing (BanglishBERT tokens) and Image processing pipelines.
* `data/` - *(Protected)* References to the unique 6,835 curated Bengali meme dataset. 

---
*Note: The core dataset and trained model weights are currently proprietary pending formal research paper publication. Source code structure is displayed for technical evaluation and portfolio review.*
