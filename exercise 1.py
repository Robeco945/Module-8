import mysql.connector

def get_airport_name_and_location(ICAOs):
    sql = f"select name, iso_region, municipality From  airport where ident ='{ICAOs}'"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            print(row)
    return


connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='L3ftH0me187Maria',
         autocommit=True
         )
ICAOs = input("enter ICAO code of airport you want to retrieve: ")
get_airport_name_and_location(ICAOs)