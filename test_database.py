import mysql.connector

def get_employees_by_last_name(last_name):
    sql = f"SELECT Number, Last_name, First_name, Salary FROM Employee WHERE Last_name='{last_name}'"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount >0 :
        for row in result:
            print(f"Hello! I'm {row[2]} {row[1]}. My salary is {row[3]} euros per month.")
    return

# Main program
connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='people',
         user='root',
         password='L3ftH0me187Maria',
         autocommit=True
         )

last_name = input("Enter last name: ")
get_employees_by_last_name(last_name)
