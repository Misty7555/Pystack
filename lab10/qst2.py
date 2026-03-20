import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="@Zxcvbnm098",
    database="KIIT"
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Student (
    RollNo INT PRIMARY KEY,
    Name VARCHAR(100),
    Age INT,
    Marks FLOAT
)
""")

print("Table Student created successfully!")

cursor.close()
conn.close()