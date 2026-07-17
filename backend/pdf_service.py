import fitz
from pathlib import Path


def extract_text_from_pdf(pdf_path: Path):

    try:
        
        all_text = []

        # document = fitz.open(pdf_path)
        with fitz.open(pdf_path) as document:

       

            for page_number in range(document.page_count):
                page = document[page_number]
                text = page.get_text()
                all_text.append(text)

        return "\n".join(all_text)

    except Exception as e:
        print(e)
        return None