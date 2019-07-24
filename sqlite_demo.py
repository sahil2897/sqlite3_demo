import sqlite3
from employee import employee

conn = sqlite3.connect('employee.db')

c = conn.cursor()
c.execute('''CREATE TABLE employee (first text, last text, pay integer)''')
c.execute('''INSERT INTO employee VALUES('sahil','sharma',50000)''')

def insert_emp(emp):
    with conn:
        c.execute('''INSERT INTO employee VALUES(?,?,?)''',(emp.first,emp.last,emp.pay))

def get_emps_by_name(firstname):
    with conn:
        c.execute('''SELECT * FROM employee WHERE first = :firstname''',{'firstname':firstname})
        print(c.fetchall())

def update_pay(emp,payment):
    with conn:
        c.execute('''UPDATE employee SET pay = :payment WHERE first = :first AND last = :last''',{'first':emp.first,'last':emp.last,'payment':payment})

def rem_emp(emp):
    with conn:
        c.execute('''DELETE FROM employee WHERE first = :first AND last = :last''',{'first':emp.first,'last':emp.last})

def print_table():
    with conn:
        c.execute('''SELECT * FROM employee''')
        print(c.fetchall())

emp1 = employee('Rahul','Sharma',80000)
emp2 = employee('Arvind','Jha',55000)

insert_emp(emp1)
insert_emp(emp2)

update_pay(emp1,90000)
rem_emp(emp2)

print_table()
get_emps_by_name('sahil')

conn.commit()
conn.close()
