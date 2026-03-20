import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="KIIT"
)

cursor = conn.cursor()

roll = int(input("Enter Roll No: "))
name = input("Enter Name: ")
age = int(input("Enter Age: "))
marks = float(input("Enter Marks: "))

sql = "INSERT INTO Student (RollNo, Name, Age, Marks) VALUES (%s, %s, %s, %s)"
values = (roll, name, age, marks)

cursor.execute(sql, values)

conn.commit()

print("Record inserted successfully!")

cursor.close()
conn.close()