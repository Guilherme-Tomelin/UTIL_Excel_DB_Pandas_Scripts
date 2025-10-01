import os
import sys
import pandas as pd
from datetime import datetime

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)

from db import DatabaseConnector

class QueryToCSV:
    def __init__(self):
        self.db_connector = DatabaseConnector()
    
    def execute_query_and_export(self, query, output_file):
        try:
            engine = self.db_connector.get_engine()
            if not engine:
                raise Exception("Conexão com o banco não foi estabelecida.")
            
            df = pd.read_sql_query(query, con=engine)
            
            df.to_csv(output_file, index=False, encoding="utf-8-sig")
            print(f"Arquivo CSV salvo em: {output_file}")
        except Exception as e:
            print(f"Erro ao executar a query ou salvar o CSV: {e}")
        finally:
            self.db_connector.db_close()

if __name__ == "__main__":
    app = QueryToCSV()
    
    query = """
    SELECT *
    FROM protocolos.tasks_queue
    WHERE tarefa_id IN (
        8880472,
        8880236,
        8880592,
        8880603,
        8880445,
        8880270,
        8880458,
        8880615,
        8880564,
        8880462
    );

        """
    
    output_dir = os.path.join(os.getcwd(), "output")
    os.makedirs(output_dir, exist_ok=True)  

    data_atual = datetime.now().strftime("%d_%m_%y_%Hh%Mm%Ss")
    output_file = os.path.join(output_dir, f"tabela_de_regras_{data_atual}.csv")
    
    app.execute_query_and_export(query, output_file)
