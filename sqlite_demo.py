import sqlite3
from employee import Employee

conn = sqlite3.connect('employee.db')

c = conn.cursor()

# c.execute("""CREATE TABLE employees (
#         first text,
#         last text,
#         pay integer
#         )""")

emp_1 = Employee('Kanye','West', 1000000)
emp_2 = Employee('Drizzy','Drake', 2000000)
emp_3 = Employee('Sean','Carter', 5000000)

print(emp_1.first)
print(emp_1.last)
print(emp_1.pay)

# c.execute("INSERT INTO employees VALUES ('Mary', 'X', 15000)")

# conn.commit()

c.execute("SELECT * FROM employees WHERE last='X'")

print(c.fetchall())

conn.commit()

conn.close()
