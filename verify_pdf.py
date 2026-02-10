from Analyse_pdf import extract_text_from_pdf
import os

pdf_path = "Trunal reaume 1.pdf"
if os.path.exists(pdf_path):
    text = extract_text_from_pdf(pdf_path)
    if text:
        print("Successfully extracted text from PDF.")
        print(f"Extracted {len(text)} characters.")
        print("First 200 characters:")
        print(text[:200])
    else:
        print("Failed to extract text.")
else:
    print(f"PDF file not found at {pdf_path}")
