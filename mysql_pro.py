from datetime import datetime
import mysql.connector
mydb = mysql.connector.connect(
     host = 'sql6.freemysqlhosting.net',
     user = 'sql6481182',
     password = 'xxxxxxxxx',
     database = 'sql6481182')


mycursor = mydb.cursor()

#create table
mycursor.execute('CREATE TABLE movie(name VARCHAR(25), director VARCHAR(25),votes INT, star VARCHAR(25), release_year DATE)')

query = 'INSERT INTO movie(name, director, votes, star, release_year) values(%s, %s, %s, %s, %s)'

#insertvalue
val = ('The Batman', 'Matt Reeves', 272475, 'Robert Pattinson', datetime.strptime('2022', '%Y'))
mycursor.execute(query, val)

val = ('The Adam Project', 'Shavn Levy', 90563, 'Ryan Reynolds', datetime.strptime('2022', '%Y'))
mycursor.execute(query, val)

val = ('The Last Kingdom', '', 116188, 'Alexander', datetime.strptime('2021', '%Y'))
mycursor.execute(query, val)

mydb.commit()
#query without params
mycursor.execute('SELECT * FROM movie')

for movie in mycursor:
   print(movie)

#query by vote count
mycursor.execute('SELECT * FROM movie where votes > 10000')

for movie in mycursor:
   print(movie)

#query by director
mycursor.execute("SELECT * FROM movie where director = 'Shavn Levy'")

for movie in mycursor:
   print(movie)

#query by stars
mycursor.execute("SELECT * FROM movie where star = 'Alexander'")
for movie in mycursor:
   print(movie)

#query by movie
mycursor.execute("SELECT * FROM movie where name = 'The Batman'")
for movie in mycursor:
   print(movie)
