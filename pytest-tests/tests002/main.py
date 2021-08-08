from datetime import datetime
import psycopg2


def execute_simple_select():
    conn = psycopg2.connect(
        host="localhost",
        port="5432",
        dbname="test_db",
        user="test_user",
        password="password"
    )

    cur = conn.cursor()

    query: str = "select * from cars"

    cur.execute(query)

    records = cur.fetchall()

    print(records)


def execute_simple_insert():
    conn = psycopg2.connect(
        host="localhost",
        port="5432",
        dbname="test_db",
        user="test_user",
        password="password"
    )

    cur = conn.cursor()

    query: str = 'insert into cars (internal_name, modified) values( %s, %s) RETURNING *'

    cur.execute(query=query, vars=("Car XXX", datetime.now()))

    record = cur.fetchone()

    print(record)

    conn.commit()


execute_simple_insert()
