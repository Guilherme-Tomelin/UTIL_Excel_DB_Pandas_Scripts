import os
import sys
import pandas as pd

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)

from db import DatabaseConnector

class ExcelToDB:
    def __init__(self):
        self.db_connector = DatabaseConnector()

    def insert_excel(self, excel_file_path, schema, table_name):
        try:
            df = pd.read_excel(excel_file_path)

            engine = self.db_connector.get_engine()
            if not engine:
                raise Exception("Conexão com o banco não foi estabelecida.")

            df.to_sql(
                table_name,
                con=engine,
                schema=schema,
                if_exists='append',  
                index=False
            )
            print(f"Dados inseridos com sucesso na tabela {schema}.{table_name}.")
        except Exception as e:
            print(f"Erro ao inserir dados: {e}")
        finally:
            self.db_connector.db_close()

if __name__ == "__main__":
    app = ExcelToDB()

    input_dir = os.path.join(os.getcwd(), "input")
    excel_filename = "Pasta1.xlsx" 
    excel_path = os.path.join(input_dir, excel_filename)

    schema = "protocolos"
    table = "regra_protocolo"

    app.insert_excel(excel_path, schema, table)