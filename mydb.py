import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '123456'
)


cursorObject = dataBase.cursor()

cursorObject.execute('CREATE DATABASE crm')
print("All Done!")