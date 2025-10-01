# scripts/doc_to_pdf.py
import os
import comtypes.client

def convert_doc_to_pdf(input_path, output_path):
    word = comtypes.client.CreateObject("Word.Application")
    word.Visible = False

    try:
        doc = word.Documents.Open(input_path)
        doc.SaveAs(output_path, FileFormat=17)  # 17 = wdFormatPDF
        doc.Close()
        print(f"✅ Convertido: {os.path.basename(input_path)} -> {os.path.basename(output_path)}")
    except Exception as e:
        print(f"❌ Erro ao converter {input_path}: {e}")
    finally:
        word.Quit()

def convert_all_docs():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(base_dir, ".."))

    input_dir = os.path.join(project_root, "input")
    output_dir = os.path.join(project_root, "output")
    os.makedirs(output_dir, exist_ok=True)

    doc_files = [f for f in os.listdir(input_dir) if f.lower().endswith((".doc", ".docx"))]

    if not doc_files:
        print("⚠️ Nenhum arquivo .doc ou .docx encontrado em:", input_dir)
        return

    for doc_file in doc_files:
        input_path = os.path.join(input_dir, doc_file)
        output_filename = os.path.splitext(doc_file)[0] + ".pdf"
        output_path = os.path.join(output_dir, output_filename)

        convert_doc_to_pdf(input_path, output_path)

if __name__ == "__main__":
    convert_all_docs()
