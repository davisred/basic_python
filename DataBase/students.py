import sqlite3
conn = sqlite3.connect('students.db')

cursor = conn.cursor()
# insert_query = 'insert into students values("Janny", "Brown", 21)'
# cursor.execute(insert_query)
# first_name = 'Davis'
# last_name = 'Black'
# age = 35
# jane = ('Jane', 'Air', '18')
# students = [
#     ('Jane', 'Air', 18),
#     ('Bob', 'Dylan', 56),
#     ('Kenny', 'McCormick', 8),
#     ('Billy', 'Jean', 32)
# ]
# Bad approach! SQL Injection danger!

# insert_query = f'insert into students values("{first_name}", "{last_name}", {age})'

# Good approach!

# insert_query = 'insert into students values(?, ?, ?);'

# cursor.execute(insert_query, (first_name,last_name,age))
# cursor.execute(insert_query, jane)

# for student in students:
#     cursor.execute(insert_query, student)

# cursor.executemany(insert_query, students)

# cursor.execute('select * from students where first_name is "Kenny";')
# cursor.execute('update students set first_name = "Stewie" where last_name="McCormick"')
cursor.execute('delete from students where last_name is "Jean"')

# for row in cursor:
#     print(row)
# print(cursor.fetchone())
# print(cursor.fetchall())
cursor.execute('select * from students')
data = cursor.fetchall()
[print(row) for row in data]
conn.commit()

conn.close()

