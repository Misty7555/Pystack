import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="@Zxcvbnm098",
    database="KIIT"
)

cursor = conn.cursor()

sql = "INSERT INTO Student (RollNo, Name, Age, Marks) VALUES (%s, %s, %s, %s)"
values = (1, "Adya", 20, 88.5)

cursor.execute(sql, values)

conn.commit()

print("1 Record inserted successfully!")

cursor.close()
conn.close()