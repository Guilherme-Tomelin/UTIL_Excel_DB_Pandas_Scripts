import os
import sys
import pandas as pd
from datetime import datetime

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)

from db import DatabaseConnector

class QueryToExcel:
    def __init__(self):
        self.db_connector = DatabaseConnector()
    
    def execute_query_and_export(self, query, output_file):
        try:
            engine = self.db_connector.get_engine()
            if not engine:
                raise Exception("Conexão com o banco não foi estabelecida.")
            
            df = pd.read_sql_query(query, con=engine)
            
            df.to_excel(output_file, index=False)
            print(f"Arquivo Excel salvo em: {output_file}")
        except Exception as e:
            print(f"Erro ao executar a query ou salvar o Excel: {e}")
        finally:
            self.db_connector.db_close()

if __name__ == "__main__":
    app = QueryToExcel()
    
    query = """
        SELECT * 
        FROM minha_tabela
        WHERE alguma_coisa;
        """
    
    data_atual = datetime.now().strftime("%d_%m_%y_%Hh%Mm%Ss")
    output_file = os.path.join(os.getcwd(), f"registros com erros_{data_atual}.xlsx")
    
    app.execute_query_and_export(query, output_file)
