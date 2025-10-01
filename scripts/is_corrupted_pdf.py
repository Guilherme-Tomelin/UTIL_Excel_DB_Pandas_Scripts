# scripts/check_pdfs.py
import os
from PyPDF2 import PdfReader

def is_pdf_corrupted(file_path: str) -> bool:
    try:
        reader = PdfReader(file_path)
        # Força leitura do primeiro objeto (às vezes só tentar abrir não acusa erro)
        _ = reader.pages[0]
        return False
    except Exception:
        return True

def check_all_pdfs():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(base_dir, ".."))

    input_dir = os.path.join(project_root, "input")

    pdf_files = [f for f in os.listdir(input_dir) if f.lower().endswith(".pdf")]

    if not pdf_files:
        print("⚠️ Nenhum arquivo .pdf encontrado em:", input_dir)
        return

    found_corrupted = False
    for pdf_file in pdf_files:
        input_path = os.path.join(input_dir, pdf_file)

        if is_pdf_corrupted(input_path):
            print(f"❌ PDF corrompido: {pdf_file}")
            found_corrupted = True

    if not found_corrupted:
        print("✅ Nenhum PDF corrompido encontrado.")

if __name__ == "__main__":
    check_all_pdfs()
