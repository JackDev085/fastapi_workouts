import sqlite3

class Connection:
    def __init__(self,db_name):
        self.db_name = db_name
        self._cursor = None
        self._connection = None

        try:
            self._connection = sqlite3.connect(self.db_name,check_same_thread=False)
            self._connection.row_factory=sqlite3.Row
            self._cursor = self._connection.cursor()

            print("Conexão estabelecida com o banco de dados")
        except sqlite3.Error as e:
            print(f"Erro ao conectar no banco de dados: {e}")
            

    def get_cursor(self):
        return self._cursor

    def execute_query(self, query,params:tuple=None):
        """Executa uma intrução sql"""
        if not self._cursor:
            print("Conexão não inicializada")  
            return
        try: 
            if not params:
                return self._cursor.execute(query)
            return self._cursor.execute(query,params)
        except sqlite3.Error as e:
            print(f"Erro ao realizar query no banco de dados: {e}")
        
    def fetch_all(self):
        
        if self._cursor:
            return self._cursor.fetchall()
        print("Nenhuma consulta foi realizada")
        return []
            
    def __del__(self):
        if self._connection:
            print("Encerrando conexão com o banco de dados")
            self._connection.close()

"""

import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

conn = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME"),
    auth_plugin="mysql_native_password",
)
cursor = conn.cursor(dictionary=True)

"""