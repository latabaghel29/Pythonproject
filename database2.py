# importing the module
import mysql.connector as sql

# opening a database connection
conn = sql.connect(host='localhost',
                        database='mydatabase',
                        user='root',
                        password='')

# define a cursor object
cursor = conn.cursor()

# query
query ="create table internship(id int(10),name varchar(20))"

# execute query
cursor.execute(query)
print("Table created successfully")

# close object
cursor.close()

# close connection
conn.close()
'''
import mysql.connector as sql
mycon=sql.connect(host="localhost",user="root",passwd="",database="mydatabase")
if mycon.is_connected():
    print("Successfully Connected to MySQL database.")
else:
    print("Check yo inputs, they really correct?")'''