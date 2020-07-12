import psycopg2
import os
try:
    # db_secret = os.environ["DATABASE_URL"]
    db_secret = 'postgres://glzbxnzyyvyqhx:26887d751f747f3d2e20460dc7079d2e0f687fb147e7ac5548a13c0bd16f495b@ec2-52-200-48-116.compute-1.amazonaws.com:5432/d72rnpp3ictjlb'
    connection = psycopg2.connect(db_secret)
    connection.set_session(autocommit=True)

    cur = connection.cursor()
    cur.execute("""
    SELECT table_name
    FROM information_schema.tables
    WHERE table_schema='public'
    AND table_type='BASE TABLE';
    """)
    rows = cur.fetchall()
    print('Table list:')
    for row in rows:
        print("   ", row[0])
    cur.close()

except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)

def get_student_data():

    cur = connection.cursor()
    cur.execute("""
    SELECT first_name,last_name ,age FROM student;
    """)
    rows = cur.fetchall()
    print('student firstname:')
    print(rows)
    cur.close()
    return rows
    
get_student_data()