import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="@Zxcvbnm098"
)

cursor = conn.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS KIIT")

print("Database KIIT created successfully!")

cursor.close()
conn.close()