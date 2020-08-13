import psycopg2

def create():
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="mansi3911", host="localhost", port="5432")
    cur = conn.cursor()
    cur.execute (''' CREATE TABLE student(ID SERIAL,NAME TEXT, AGE TEXT, ADDRESS TEXT); ''')
    print("Table Created")
    conn.commit()
    conn.close()

def insert_data():
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="mansi3911", host="localhost", port="5432")
    cur = conn.cursor()
    name = input("enter name")
    age = input("enter age")
    address = input("enter address")
    query = '''INSERT INTO student(NAME, AGE, ADDRESS) VALUES(%s, %s, %s);'''
    cur.execute(query,(name, age, address))
    print("Data Inserted")
    conn.commit()
    conn.close()

insert_data()
