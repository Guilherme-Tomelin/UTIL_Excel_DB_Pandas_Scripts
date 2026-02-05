import os
import sys
import pandas as pd

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)


def convert_excel_to_csv(input_path: str, output_path: str) -> None:
    df = pd.read_excel(input_path)
    df.to_csv(output_path, index=False, encoding="utf-8-sig")
    print(f"✅ Convertido: {os.path.basename(input_path)} -> {os.path.basename(output_path)}")


def convert_all_excels_from_input() -> None:
    base_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(base_dir, ".."))

    input_dir = os.path.join(project_root, "input")
    output_dir = os.path.join(project_root, "output")

    os.makedirs(output_dir, exist_ok=True)

    excel_files = [
        f for f in os.listdir(input_dir)
        if f.lower().endswith((".xlsx", ".xls"))
    ]

    if not excel_files:
        print("⚠️ Nenhum arquivo Excel encontrado em:", input_dir)
        return

    for excel_file in excel_files:
        input_path = os.path.join(input_dir, excel_file)
        output_filename = os.path.splitext(excel_file)[0] + ".csv"
        output_path = os.path.join(output_dir, output_filename)

        convert_excel_to_csv(input_path, output_path)


if __name__ == "__main__":
    convert_all_excels_from_input()