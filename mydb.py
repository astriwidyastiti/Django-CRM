#install Mysql on your computer
#httpsd://dev.mysql/downloads/installer/
#pip install mysql
#pip install mysql-connector
#pip install mysql-connector-python

import mysql.connector 
import pymysql

dataBase = pymysql.connect(
    host = 'localhost',
    user='root',
    passwd = 'Awey@127'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE tyco")

print("all done!")