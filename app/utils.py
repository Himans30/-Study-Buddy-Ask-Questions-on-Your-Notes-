from docx import Document
import PyPDF2

def extract_text_from_pdf(path):
    text = ''
    with open(path, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            text += page.extract_text()
    return text

def extract_text_from_docx(path):
    doc = Document(path)
    return '\n'.join([p.text for p in doc.paragraphs])
