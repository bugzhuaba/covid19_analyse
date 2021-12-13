import pymysql

connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='123456',
                                 database='covid_19', )

cursor=connection.cursor()
sql='insert into test values(1)'
cursor.execute(sql)
connection.commit()
connection.close()

