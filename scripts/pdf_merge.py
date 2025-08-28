import os
from PyPDF2 import PdfMerger

def merge_pdfs_from_input():
    base_dir = os.path.dirname(os.path.abspath(__file__))

    project_root = os.path.abspath(os.path.join(base_dir, ".."))

    input_dir = os.path.join(project_root, "input")
    output_dir = os.path.join(project_root, "output")

    os.makedirs(output_dir, exist_ok=True)

    merged_file = os.path.join(output_dir, "merged_output.pdf")

    pdf_files = [f for f in os.listdir(input_dir) if f.lower().endswith(".pdf")]
    pdf_files.sort()  

    if not pdf_files:
        print("⚠️ Nenhum PDF encontrado em:", input_dir)
        return

    merger = PdfMerger()

    for pdf in pdf_files:
        pdf_path = os.path.join(input_dir, pdf)
        print(f"Adicionando: {pdf}")
        merger.append(pdf_path)

    merger.write(merged_file)
    merger.close()
    print(f"\n✅ PDF final gerado em: {merged_file}")


if __name__ == "__main__":
    merge_pdfs_from_input()
