import PyPDF2
from PyPDF2.errors import PdfReadError

class PdfValidater:
    def is_valid_pdf(self, file_path: str) -> bool:
        try:
            with open(file_path, "rb") as file:
                reader = PyPDF2.PdfReader(file)
                if reader.is_encrypted:
                    reader.decrypt('')
                if len(reader.pages) == 0:
                    return False
            return True
        except:
            return False