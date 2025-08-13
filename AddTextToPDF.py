import fitz  # PyMuPDF

pdf_in  = r".\20250808_150601.pdf"
pdf_out = r".\20250808_150601_AddText.pdf"

doc = fitz.open(pdf_in)
page = doc[0]

# 1) Get the built-in CJK font (Droid Sans Fallback)
cjk = fitz.Font("cjk")

# 2) Register this font to the page and assign it a name (F0)
#    Note: use page.insert_font (not doc.insert_font)
page.insert_font(fontname="F0", fontbuffer=cjk.buffer)

# 3) Use the registered font name to write Chinese text
page.insert_text(
    (90, 200),                     # (x, y) position
    "中文內容",        # Chinese content
    fontname="F0",                 # Key: use the newly registered CJK font
    fontsize=9,
    color=(0, 0, 0)
)

doc.save(pdf_out)


doc.close()
print("OK ->", pdf_out)
