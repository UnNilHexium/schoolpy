import mysql.connector as c

mycon = m.connect(user="root", password="welcome", host="localhost")

mycur=mycon.cursor()

mycur.execute ("Create Database if not exist Dummy")
