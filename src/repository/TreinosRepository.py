class TreinosRepository:
    def __init__(self, cursor):
        self._cursor = cursor

    def fetch_all(self):
        self._cursor.execute("SELECT * FROM treinos")
        result = self._cursor.fetchall()
        return result
    
    def fetch_one(self,id):
        sql = "SELECT * FROM treinos where id=%s"
        self._cursor.execute(sql,(id,))
        result = self._cursor.fetchall()
        return result


    def fetch_by_category(self,category):
        sql = "SELECT * FROM treinos where categoria=%s"
        self._cursor.execute(sql,(category,))
        result = self._cursor.fetchall()
        return result
