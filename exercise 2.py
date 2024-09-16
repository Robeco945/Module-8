print('exercise 2')
import mysql.connector
connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='L3ftH0me187Maria',
         autocommit=True
         )
sql = f"select name From  airport where iso_country ='FI' order by (type)"
print(sql)
cursor = connection.cursor()
cursor.execute(sql)
result = cursor.fetchall()
if cursor.rowcount > 0:
    for row in result:
        print(row)