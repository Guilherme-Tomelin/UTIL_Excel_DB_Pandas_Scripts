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
            SELECT 
        tarefa_id, 
        localizador, 
        referencia, 
        status, 
        status_detalhado, 
        inserted_at, 
        andamento_processual
    FROM atualizacao_referencia_gcpj.tasks_queue
    WHERE referencia = 'CI-PLAN ECON-JUNTADA PROPOSTA'
    AND status NOT IN ('sucesso', 'canceled');
        """
    
    output_dir = os.path.join(os.getcwd(), "output")
    os.makedirs(output_dir, exist_ok=True)

    data_atual = datetime.now().strftime("%d_%m_%y_%Hh%Mm%Ss")
    output_file = os.path.join(output_dir, f"output_{data_atual}.xlsx")
    
    app.execute_query_and_export(query, output_file)
