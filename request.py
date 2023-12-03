import mysql.connector
import sys

import os
from email.message import EmailMessage
import ssl
import smtplib


def send_mail(to, subject, body):
    sender = "clickviralng@gmail.com"
    recipient = to
    password = "wflwidljzrykjswq"

    mail = EmailMessage()
    mail["From"] = sender
    mail["To"] = recipient
    mail["Subject"] = subject

    mail.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(sender, password)
        smtp.sendmail(sender, recipient, mail.as_string())

# Establish a connection to the MySQL server
database = {
    'host': 'database-1.cyyfrhxbvso9.eu-north-1.rds.amazonaws.com',
    'database': 'cronjob',
    'username': 'admin',
    'password': 'admin-root'
}

def query(sql):

    connection = mysql.connector.connect(
        host=database['host'],
        database=database['database'],
        user=database['username'],
        password=database['password']
    )

    if connection.is_connected():

        # Create a cursor object to execute SQL queries
        cursor = connection.cursor()

        # Execute a SELECT query
        cursor.execute(sql)

        # Fetch all rows from the result set
        rows = cursor.fetchall()
        connection.commit()
        return rows

    else:
        print("MySQL connection is not connected")

    # Close cursor and connection
    cursor.close()
    connection.close()

def main (argv=sys.argv):
    
    if argv[1] == 'write':
        write()
    elif argv[1] == 'read':
        read()

    elif argv[1] == 'del_all':
        del_all()
    else:
        print('Invalid argument')

def write():
    with open('/home/ubuntu/caesar/visit.txt') as f:
        data = f.read().splitlines()

    for line in data:
        line = line.split(' : ')

        sql = "INSERT INTO requests (route, ip) VALUES ('{}', '{}')".format(line[0], line[1])

        query(sql)

def read():

    sql = "SELECT * FROM requests"

    rows = query(sql)
    atbash = query("SELECT count(*) FROM requests WHERE route = '/atbash'")[0][0]
    caesar = query("SELECT count(*) FROM requests WHERE route = '/caesar'")[0][0]
    rot13 = query("SELECT count(*) FROM requests WHERE route = '/rot13'")[0][0]
    crot13 = query("SELECT count(*) FROM requests WHERE route = '/crot13'")[0][0]

    data = ""

    for row in rows:
        data+=f"IP: {row[1]} Route: {row[2]} Time: {row[3]}\n"

    count = f"atbash: {atbash} caesar: {caesar} rot13: {rot13} crot13: {crot13}"

    send_mail("adeyeriopeoluwa05@gmail.com", "Request Data", f"{data}\n\n{count}")

def del_all():

    sql = "DELETE FROM requests"

    query(sql)

if __name__ == '__main__':
    main()