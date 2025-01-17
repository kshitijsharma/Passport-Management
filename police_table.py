from mysql.connector import connect, Error

'''dropping existing table'''
try:
    with connect(
        host="localhost",
        user="root",
        password="shrimad01",
        database="passport"
    )as connection:
        drop_table_query= "DROP TABLE police"
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
        create_table_query = "CREATE TABLE police(rank varchar(20),name varchar(10), password varchar(40), city varchar(40) )"
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
        add_records="""INSERT INTO police(rank,name, password, city) VALUES
                        ("inspector","niel","niel","chennai"),
                        ("inspector","kshitij","kshitij","delhi"),
                        ("DCP","manasa","manasa","hyderabad")"""
        with connection.cursor() as cursor:
            cursor.execute(add_records)
            connection.commit()
except Error as e:
    print(e)

'''see the records in the table'''
try:
    with connect(
              host="localhost",
              user="root",
            password="shrimad01",
            database="passport"
    )as connection:
        show_records="SELECT * FROM  police"
        with connection.cursor() as cursor:
            cursor.execute(show_records)
            result=cursor.fetchall()
            print(result)
except Error as e:
    print("5")