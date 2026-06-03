import os

try:
    import pypdf
    print("pypdf available")
    reader = pypdf.PdfReader("ref/VI.pdf")
    text = ""
    for i, page in enumerate(reader.pages):
        text += f"\n--- PAGE {i+1} ---\n" + page.extract_text()
    with open("pdf_text.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print("Extracted PDF text to pdf_text.txt")
except ImportError:
    try:
        import fitz  # PyMuPDF
        print("fitz available")
        doc = fitz.open("ref/VI.pdf")
        text = ""
        for i in range(len(doc)):
            text += f"\n--- PAGE {i+1} ---\n" + doc[i].get_text()
        with open("pdf_text.txt", "w", encoding="utf-8") as f:
            f.write(text)
        print("Extracted PDF text to pdf_text.txt")
    except ImportError:
        print("Neither pypdf nor fitz is available")
