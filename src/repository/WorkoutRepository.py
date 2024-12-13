from src.db.connection import Connection

class WorkoutRepository:
    def __init__(self, cursor:Connection):
        self._cursor = cursor

    def fetch_all(self):
        self._cursor.execute_query("SELECT * FROM workouts_exercicio")
        result = self._cursor.fetch_all()
        return result
    
    def fetch_one(self,id):
        sql = "SELECT * FROM workouts_exercicio where id=(?)"
        self._cursor.execute_query(sql,(id,)) 
        result = self._cursor.fetch_all()
        return result


    def fetch_by_category(self,category):
        sql = "SELECT * FROM workout_exercicio where categoria=(?)"
        self._cursor.execute_query(sql,(category,))
        result = self._cursor.fetch_all()
        return result
