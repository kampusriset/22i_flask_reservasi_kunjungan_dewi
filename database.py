import pymysql

class Database:
    def __init__(self):
        self.connection = pymysql.connect(
            host='localhost',
            user='root',
            password='',  # Replace with your MySQL root password
            database='reservasi_tiket',
            cursorclass=pymysql.cursors.DictCursor
        )
        self.cursor = self.connection.cursor()

    def execute(self, query, params=None):
        self.cursor.execute(query, params or ())

    def fetchone(self):
        return self.cursor.fetchone()

    def fetchall(self):
        return self.cursor.fetchall()

    def commit(self):
        self.connection.commit()

    def close(self):
        self.cursor.close()
        self.connection.close()

# Example usage
if __name__ == "__main__":
    db = Database()
    try:
        db.execute("SELECT * FROM users")
        users = db.fetchall()
        for user in users:
            print(user)
    finally:
        db.close()