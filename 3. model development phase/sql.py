import sqlite3

# connect to database (this will create data.db)
conn = sqlite3.connect("data.db")
cur = conn.cursor()

# create table
cur.execute("""
CREATE TABLE IF NOT EXISTS STUDENTS(
    NAME TEXT,
    CLASS TEXT,
    MARKS INTEGER,
    COMPANY TEXT
)
""")

# insert records
cur.execute("INSERT INTO STUDENTS VALUES ('Sijo','BTech',75,'JSW')")
cur.execute("INSERT INTO STUDENTS VALUES ('Anu','MCom',82,'INFOSYS')")
cur.execute("INSERT INTO STUDENTS VALUES ('Ravi','BSc',90,'TCS')")
cur.execute("INSERT INTO STUDENTS VALUES ('Meena','MCom',88,'INFOSYS')")

# save and close
conn.commit()
conn.close()

print("Database created successfully")