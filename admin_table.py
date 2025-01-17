from mysql.connector import connect, Error


'''dropping existing table'''
try:
    with connect(
        host="localhost",
        user="root",
        password="shrimad01",
        database="passport"
    )as connection:
        drop_table_query= "DROP TABLE admins"
        with connection.cursor() as cursor:
            cursor.execute(drop_table_query)
            connection.commit()
except Error as e:
    print("1")

'''creating the admin table'''
try:
    with connect(
        host="localhost",
        user="root",
        password="shrimad01",
        database="passport"
    )as connection:
        create_table_query = "CREATE TABLE admins(username varchar(10), password varchar(40), city varchar(40) )"
        with connection.cursor() as cursor:
            cursor.execute(create_table_query)
            connection.commit()
except Error as e:
    print("2")

'''chceking if table creation is successful'''
try:
    with connect(
              host="localhost",
              user="root",
            password="shrimad01",
            database="passport"
    )as connection:
        show_table="SHOW TABLES"
        with connection.cursor() as cursor:
            cursor.execute(show_table)
            result=cursor.fetchall()
            print(result)

except Error as e:
    print("3")

    '''adding records to the table'''
try:
    with connect(
              host="localhost",
              user="root",
            password="shrimad01",
            database="passport"
    )as connection:
        add_records="""INSERT INTO admins(username, password, city) VALUES
                        ("niel","niel","chennai"),
                        ("kshitij","kshitij","delhi"),
                        ("manasa","manasa","hyderabad")"""
        with connection.cursor() as cursor:
            cursor.execute(add_records)
            connection.commit()
except Error as e:
    print("4")

'''see the records in the table'''
try:
    with connect(
              host="localhost",
              user="root",
            password="shrimad01",
            database="passport"
    )as connection:
        show_records="SELECT * FROM  admins"
        with connection.cursor() as cursor:
            cursor.execute(show_records)
            result=cursor.fetchall()
            print(result)
except Error as e:
    print("5")