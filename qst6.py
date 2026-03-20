import sqlite3

# Connect to KIIT database
conn = sqlite3.connect("KIIT.db")

# Create cursor object
cursor = conn.cursor()

# Rename table Student to StudentDetails
cursor.execute("""
ALTER TABLE Student
RENAME TO StudentDetails
""")

# Commit changes
conn.commit()

print("Table renamed successfully!")

# Close connection
conn.close()