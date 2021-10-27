import mysql.connector
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Tr6741449',
    database='full_stack_project_db'
)

mycursor = mydb.cursor()
# mycursor.execute('CREATE DATABASE full_stack_project_db')
# mycursor.execute('SHOW DATABASES')
# for db in mycursor:
#     print(db)

