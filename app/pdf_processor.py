import fitz  # PyMuPDF



class PDFProcessor:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def extract_text(self) -> str:
        text = ""
        with fitz.open(self.file_path) as doc:
            for page in doc:
                text += page.get_text()
        return text
