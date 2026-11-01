# Data included in this release

## Original collection

The repository owner explicitly approved public upload of the Excel workbook and all 276 images from the local thesis folder.

| Path | Contents |
|---|---|
| `original/MEME_DATA_Excel.xlsx` | Original workbook: one sheet, 259 annotation rows |
| `original/MEME_DATA/` | All 276 original images: 241 JPG and 35 PNG |

The originals are copied byte-for-byte. Captions, annotations, filenames, and workbook paths are not corrected.

### Coverage and schema

The worksheet columns are `Caption`, `Label`, and `Image_Path`. Labels are `Offensive` (182) and `Non Offensive` (77). There are 47 literal `No Caption` entries. 202 caption cells contain garbled text encoding; no encoding repair has been applied.

Images cover numeric IDs 1–275. ID 143 occurs twice, as two different images (`image (143).jpg` and `image (143).png`). The workbook covers IDs 1–259; IDs 260–275 have no corresponding annotation rows. Do not invent labels or choose one ID-143 image automatically.

Workbook paths such as `MemeData\image-(01).jpg` do not directly match the released image names such as `MEME_DATA/image (1).jpg`. The configurable reader exposes the stored path unchanged. Explicitly map and review paths before using the original files for an experiment.

This is a partial collection. It is not the 6,835-record corpus reported in the thesis, and it cannot reproduce those historical results by itself.

## Synthetic walkthrough

`synthetic_samples.json` contains eight invented English / romanized Bangla captions with artificial labels and example text/image predictions. `synthetic_images/` contains eight geometric images created for the walkthrough. Captions are not extracted from real memes and image contents do not establish their artificial labels. The synthetic fixtures test data flow only, not model quality.

The demo uses these fixtures by default. It does not fit research models or access the original workbook.

## Configurable local paths

The public reader accepts `.json`, `.csv`, and `.xlsx` files with the same three required columns. It reads UTF-8 JSON / CSV. Excel reading uses `openpyxl` in read-only mode. It does not repair text, resolve ambiguous IDs, or silently rewrite image paths.

```powershell
$env:MEME_DATASET_PATH = "C:\my-data\annotations.json"
$env:MEME_IMAGE_ROOT = "C:\my-data"
```

```bash
export MEME_DATASET_PATH=/path/to/annotations.json
export MEME_IMAGE_ROOT=/path/to/images
```

Relative image paths are resolved beneath the configured root. The demonstration rejects paths outside that root. See `.env.example`; values must be set in the running process.

## Rights

Third-party meme images and embedded content retain their respective owners' rights. Inclusion does not assign a new dataset license. See [release scope](../docs/release_scope.md).
