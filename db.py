import sqlite3


class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS details (id INTEGER PRIMARY KEY,student_name text,class_name text,email_addresss text,student_address text)")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM details")
        rows = self.cur.fetchall()
        return rows

    def add(self, name, className, email, address):
        self.cur.execute("INSERT INTO details VALUES(NULL,?,?,?,?)",
                         (name, className, email, address))
        self.conn.commit()

    def remove(self, id):
        self.cur.execute("DELETE FROM details WHERE id=?", (id,))
        self.conn.commit()

    def update(self, id, name, className, email, address):
        self.cur.execute("UPDATE details SET student_name=?,class_name=?,email_addresss=?,student_address=? WHERE id=?",
                         (name, className, email, address, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()


# db = Database('students.db')

# db.add('Suhas', 'Third year', 'SuhasKamble@gmail.com', 'On the Mars')
# print(db.fetch())
