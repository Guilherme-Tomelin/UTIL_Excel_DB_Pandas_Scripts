import os
from dotenv import load_dotenv
from sqlalchemy import create_engine



load_dotenv()

class DatabaseConnector:
    def __init__(self):
        self.server = os.getenv('POSTGRES_HOST')
        self.database = os.getenv('POSTGRES_DATABASE')
        self.username = os.getenv('POSTGRES_USER')
        self.password = os.getenv('POSTGRES_PASSWORD')
        self.port = os.getenv('POSTGRES_PORT', '5432')
        self.engine = None
        self.connect()
    
    def connect(self):
        try:
            self.engine = create_engine(
                f'postgresql+psycopg2://{self.username}:{self.password}@{self.server}:{self.port}/{self.database}',
                connect_args={'client_encoding': 'utf8'}
            )
            print("Conexão com o banco de dados estabelecida com sucesso.")
        except Exception as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            self.engine = None

    def get_engine(self):
        return self.engine
    
    def db_close(self):
        if self.engine:
            self.engine.dispose()  
            print("Conexão com o banco de dados fechada.")