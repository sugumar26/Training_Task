from sqlalchemy import create_engine, Column, Integer, Numeric, Date, String, Float, and_, or_, func, desc, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

postgres_url = 'postgresql://postgres:sugu2002@localhost:5433/psqltask'
engine = create_engine(postgres_url, echo=True)
Base = declarative_base()

class Order(Base):
    __tablename__ = 'orders'

    ord_no = Column(Integer, primary_key=True)
    purch_amt = Column(Numeric)
    ord_date = Column(Date)
    customer_id = Column(Integer)
    salesman_id = Column(Integer)

class Salesman(Base):
    __tablename__ = 'salesman'

    salesman_id = Column(Integer, primary_key=True)
    name = Column(String)
    city = Column(String)
    commission = Column(Float)

class EmployeeHistory(Base):
    __tablename__ = 'employee_history'

    employee_id = Column(Integer, primary_key=True)
    start_date = Column(Date)
    end_date = Column(Date)
    job_id = Column(String)
    department_id = Column(Integer)

class Customer(Base):
    __tablename__ = 'customer'

    customer_id = Column(Integer, primary_key=True)
    cust_name = Column(String)
    city = Column(String)
    grade = Column(Integer)
    salesman_id = Column(Integer)

class Employee(Base):
    __tablename__ = 'employee'

    emp_idno = Column(Integer, primary_key=True)
    emp_fname = Column(String)
    emp_lname = Column(String)
    emp_dept = Column(Integer)

class Department(Base):
    __tablename__ = 'department'

    dpt_code = Column(Integer, primary_key=True)
    dpt_name = Column(String)
    dpt_allotment = Column(Integer)

Session = sessionmaker(bind=engine)
session = Session()

raw_query1a = """
    SELECT DISTINCT o.salesman_id, o.purch_amt
    FROM orders o
    WHERE o.purch_amt <= 2000
    ORDER BY o.purch_amt DESC
    LIMIT 5;
"""

results1a = session.execute(raw_query1a)

print("Query 1a Result")

for result in results1a:
    print(result[0])


raw_query1b = """
   SELECT DISTINCT o.salesman_id, MIN(o.purch_amt) AS min_purch_amt
FROM orders o
WHERE o.purch_amt > 100
GROUP BY o.salesman_id
ORDER BY min_purch_amt
LIMIT 5;
"""
results1b = session.execute(raw_query1b)
print("Query 1b Result")

for result in results1b:
    print(f"Salesperson ID: {result.salesman_id}, Min Purchase Amount: {result.min_purch_amt}")

query2a = """
    SELECT salesman_id, name, city, commission
FROM salesman
WHERE commission BETWEEN 0.10 AND 0.12;
"""
results2a = session.execute(query2a)
print("Query 2a Result")
for result in results2a:
    print(result)

query2b = """
    SELECT AVG(commission) AS avg_commission
FROM salesman
WHERE commission BETWEEN 0.12 AND 0.14;
"""
results2b = session.execute(query2b)
print("Query 2b Result")
for result in results2b:
    print(result.avg_commission)

query3a = """
    SELECT employee_id
    FROM employee_history
    GROUP BY employee_id
    HAVING COUNT(DISTINCT job_id) >= 2;
"""
results3a = session.execute(query3a)
print("Query 3a Result")
for result in results3a:
    print(result[0])

query4a = """
   SELECT 
    customer.cust_name, 
    customer.city AS cust_city, 
    customer.grade, 
    salesman.name AS salesman_name, 
    orders.ord_no, 
    orders.ord_date, 
    orders.purch_amt
FROM 
    customer
LEFT JOIN 
    salesman ON customer.salesman_id = salesman.salesman_id
LEFT JOIN 
    orders ON customer.customer_id = orders.customer_id
WHERE 
    (customer.salesman_id IS NOT NULL AND salesman.salesman_id IS NULL)
    OR 
    (orders.purch_amt >= 2000 AND orders.ord_no IS NULL)
    OR 
    customer.grade IS NOT NULL;
"""
results4a = session.execute(query4a)
print("Query 4a Result")
for result in results4a:
    print(result)

query4b = """
    SELECT 
    customer.cust_name, 
    customer.city, 
    orders.ord_no, 
    orders.ord_date, 
    orders.purch_amt
FROM 
    customer
INNER JOIN 
    orders ON customer.customer_id = orders.customer_id
WHERE 
    (customer.grade IS NOT NULL AND customer.salesman_id IS NOT NULL AND orders.purch_amt >= 2000)
    OR 
    (customer.grade IS NULL OR customer.salesman_id IS NULL);
"""
results4b = session.execute(query4b)
print("Query 4b Result")
for result in results4b:
    print(result)

query5a = """
    SELECT 
    employee.emp_fname, 
    employee.emp_lname
FROM 
    employee
INNER JOIN 
    department ON employee.emp_dept = department.dpt_code
WHERE 
    department.dpt_allotment > 50000;
"""
results5a = session.execute(query5a)
print("Query 5a Result")
for result in results5a:
    print(result)

query5b = text("""
    WITH RankedDepartments AS (
        SELECT
            dpt_code,
            dpt_name,
            dpt_allotment,
            RANK() OVER (ORDER BY dpt_allotment) AS rnk
        FROM
            department
    )
    SELECT
        employee.emp_fname,
        employee.emp_lname
    FROM
        employee
    JOIN
        department ON employee.emp_dept = department.dpt_code
    JOIN
        RankedDepartments rd ON rd.dpt_code = department.dpt_code
    WHERE
        rd.rnk = 2;
""")
results5b = session.execute(query5b)
print("Query 5b Result")
for row in results5b:
    print(row)
