import fitz  # PyMuPDF

pdf_in  = r".\20250808_150601.pdf"
pdf_out = r".\20250808_150601_AddText.pdf"

doc = fitz.open(pdf_in)
page = doc[0]

# 1) 取得內建的 CJK 字型（Droid Sans Fallback）
cjk = fitz.Font("cjk")

# 2) 把這個字型「註冊到頁面」，取一個名字（F0）
#    注意是 page.insert_font（不是 doc.insert_font）
page.insert_font(fontname="F0", fontbuffer=cjk.buffer)

# 3) 用註冊好的字型名寫入中文
page.insert_text(
    (90, 200),                     # (x, y)
    "中文內容",        # 中文內容
    fontname="F0",                 # 關鍵：使用剛註冊的 CJK 字型
    fontsize=9,
    color=(0, 0, 0)
)

doc.save(pdf_out)


doc.close()
print("OK ->", pdf_out)
