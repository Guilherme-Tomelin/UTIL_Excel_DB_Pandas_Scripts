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
        SELECT pasta_id, localizador 
        FROM autojur_v2.pastas
        WHERE localizador IN ('7309855','1300029895','1000077649','1600345639','1700039341','1700406660','1700531229','1800724841','1900361238','1601211980','1900644601','2000026182','2000111129','2000124224','2000215416','2000212957','1600931550','1600958368','1600636903','1600822088','1600629027','2000432192','2000481876','2000601581','2000742934','2000752939','2100237591','2100242986','8242282','2100394297','2100414439','2100556438','2100588498','2100648127','2100853084','2200055613','2200073282','2200071197','2200094949','1600856305','1600720018','1600637555','1700556873','1600619948','1600621152','1600739084','1600626105','1600623942','1600628036','1600637194','1600636026','2200259019','2200270543','2200309297','2200316469','2200367311','2200374019','2200597078','2200628509','2200639810','2200737376','1800415873','2200745790','1800041691','2200783098','2200882672','2200900889','2200621657','2200976684','2300068769','2300203836','2300274306','2300306963','2300317614','2300363516','2300435912','2300557244','2300578833','2300804682','2300807428','2300845104','2300951589','2300944645','2301027850','2400044358','2400053921','2400107496','2400117121','2400481031','2400659365','1300039900','1600714469','1300033364','1800782963')
        AND numero_subpasta = '0';
        """
    
    output_dir = os.path.join(os.getcwd(), "output")
    os.makedirs(output_dir, exist_ok=True)  

    data_atual = datetime.now().strftime("%d_%m_%y_%Hh%Mm%Ss")
    output_file = os.path.join(output_dir, f"tabela_de_regras_{data_atual}.csv")
    
    app.execute_query_and_export(query, output_file)
