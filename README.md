# PDF Chinese Text Writer

This repository provides a simple example of using [PyMuPDF](https://pymupdf.readthedocs.io/) to insert Chinese text into an existing PDF file. The `AddTextToPDF.py` script opens a PDF, registers a CJK font and writes Chinese characters onto the first page.

## Setup

1. Install the dependencies:

```bash
pip install -r requirements.txt
```

2. Place the source PDF (e.g. `20250808_150601.pdf`) in the repository root.
3. Run the script to generate a new PDF with the added text:

```bash
python AddTextToPDF.py
```

The output file will be saved with the `_AddText` suffix (e.g. `20250808_150601_AddText.pdf`).
