##################Initialization information, do not modify ################
from cis2010utils import StartHere, EndHere
from imdb import IMDb
from colorama import Fore
import pandas as pd
import sqlite3

############################################################################
#
# Task 2a
StartHere( "Chike Ani", "S12", "Spr2023")
#
#
# Open up the database  ########## Do not modify these instructions#########
db_name =  "moviesUSA.db"
#    db_conn = sqlite3.connect("C:/Users/Shared/CIS2010/moviesUSA.db")
db_conn = sqlite3.connect(db_name)
#c = db_conn.cursor()
# display fields in 3 tables
# display fields in 3 tables
sqltxt = "SELECT COUNT(title) FROM movies" ; mz = pd.read_sql(sqltxt, db_conn) ; print("\nnumber of movies records\n", mz)
sqltxt = "SELECT COUNT(actor) FROM actors" ; az = pd.read_sql(sqltxt, db_conn) ; print("\nnumber of actors records\n", az)
sqltxt = "SELECT COUNT(genre) FROM genre" ; gz = pd.read_sql(sqltxt, db_conn) ; print("\nnumber of genre records\n", gz)
sqltxt = "pragma table_info('movies')" ; t1 = pd.read_sql(sqltxt, db_conn) ; print("movies table\n", t1)
sqltxt = "pragma table_info('actors')" ; t2 = pd.read_sql(sqltxt, db_conn) ; print("\nactors table\n", t2)
sqltxt = "pragma table_info('genre')" ; t3 = pd.read_sql(sqltxt, db_conn) ; print("\ngenre table\n",t3)
############################################################################
#
#
# Task w3a
sqlw3a = """
SELECT year FROM movies
"""
try :
    w3a = pd.read_sql(sqlw3a, db_conn); print( "\nw3a contains\n", w3a)
except :
    if len(sqlw3a.lstrip()) :
        print(Fore.RED + "\nYour SQL statement has an error that must be fixed" + Fore.BLUE )
        print( sqlw3a )
        print(Fore.BLACK + "Start by checking the spelling of each field in the list" )
        print("Also consider spelling of your table name, and SQL statements\n" )

#
# Task w3c
sqlw3c = """
SELECT DISTINCT year FROM movies
"""
try :
    w3c = pd.read_sql(sqlw3c, db_conn); print( "\nw3c contains\n", w3c)
except :
    if len(sqlw3c.lstrip()) :
        print(Fore.RED + "\nYour SQL statement has an error that must be fixed" + Fore.BLUE )
        print( sqlw3c )
        print(Fore.BLACK + "Start by checking the spelling of each field in the list" )
        print("Also consider spelling of your table name, and SQL statements\n" )

# Task w4a
sqlw4a = """
SELECT year, title, duration, worldwide_gross_income
FROM movies
WHERE title = 'Ghostbusters'
"""
try :
    w4a = pd.read_sql(sqlw4a, db_conn); print( "\nw4a contains\n", w4a)
except :
    if len(sqlw4a.lstrip()) :
        print(Fore.RED + "\nYour SQL statement has an error that must be fixed" + Fore.BLUE )
        print( sqlw4a )
        print(Fore.BLACK + "Start by checking the spelling of each field in the list" )
        print("Also consider spelling of your table name, and SQL statements\n" )


# Task w4b
sqlw4b = """
SELECT year, title, duration, worldwide_gross_income, budget
FROM movies
WHERE title LIKE 'Frozen%'
"""
try :
    w4b = pd.read_sql(sqlw4b, db_conn); print( "\nw4b contains\n", w4b)
except :
    if len(sqlw4b.lstrip()) :
        print(Fore.RED + "\nYour SQL statement has an error that must be fixed" + Fore.BLUE )
        print( sqlw4b )
        print(Fore.BLACK + "Start by checking the spelling of each field in the list" )
        print("Also consider spelling of your table name, and SQL statements\n" )

# Task w4c
sqlw4c = """
SELECT year, title, duration, worldwide_gross_income, budget
FROM movies
WHERE title LIKE 'Frozen%'
ORDER BY year
"""
try :
    w4c = pd.read_sql(sqlw4c, db_conn); print( "\nw4c contains\n", w4c)
except :
    if len(sqlw4c.lstrip()) :
        print(Fore.RED + "\nYour SQL statement has an error that must be fixed" + Fore.BLUE )
        print( sqlw4c )
        print(Fore.BLACK + "Start by checking the spelling of each field in the list" )
        print("Also consider spelling of your table name, and SQL statements\n" )

# Task w5a  This code generates an error
sqlw5a = """
 SELECT year, title, production_company, actor
FROM movies
WHERE title = 'Dolittle'
"""
try :
    w5a = pd.read_sql(sqlw5a, db_conn); print( "\nw5a contains\n", w5a)
except :
    if len(sqlw5a.lstrip()) :
        print(Fore.RED + "\nYour SQL statement has an error that must be fixed" + Fore.BLUE )
        print( sqlw5a )
        print(Fore.BLACK + "Start by checking the spelling of each field in the list" )
        print("Also consider spelling of your table name, and SQL statements\n" )

# Task w5b
sqlw5b = """
 SELECT year, title, production_company, actor
FROM movies INNER JOIN actors ON movies.imdb = actors.imdb
WHERE title = 'Dolittle' 
"""
try :
    w5b = pd.read_sql(sqlw5b, db_conn); print( "\nw5b contains\n", w5b)
except :
    if len(sqlw5b.lstrip()) :
        print(Fore.RED + "\nYour SQL statement has an error that must be fixed" + Fore.BLUE )
        print( sqlw5b )
        print(Fore.BLACK + "Start by checking the spelling of each field in the list" )
        print("Also consider spelling of your table name, and SQL statements\n" )

# Task w5c
sqlw5c = """
SELECT year, title, writer, worldwide_gross_income
FROM movies INNER JOIN actors ON movies.imdb = actors.imdb
WHERE title LIKE '%Dolittle%' AND actor = 'Eddie Murphy'

"""
try :
    w5c = pd.read_sql(sqlw5c, db_conn); print( "\nw5c contains\n", w5c)
except :
    if len(sqlw5c.lstrip()) :
        print(Fore.RED + "\nYour SQL statement has an error that must be fixed" + Fore.BLUE )
        print( sqlw5c )
        print(Fore.BLACK + "Start by checking the spelling of each field in the list" )
        print("Also consider spelling of your table name, and SQL statements\n" )

# Task w6a
sqlw6a = """
SELECT year, title, writer, MAX(worldwide_gross_income)
FROM movies INNER JOIN actors ON movies.imdb = actors.imdb
WHERE actor = 'Eddie Murphy'
"""
try :
    w6a = pd.read_sql(sqlw6a, db_conn); print( "\nw6a contains\n", w6a)
except :
    if len(sqlw6a.lstrip()) :
        print(Fore.RED + "\nYour SQL statement has an error that must be fixed" + Fore.BLUE )
        print( sqlw6a )
        print(Fore.BLACK + "Start by checking the spelling of each field in the list" )
        print("Also consider spelling of your table name, and SQL statements\n" )


# Task w6b
sqlw6b = """
SELECT year, title, writer, SUM(worldwide_gross_income)
FROM movies INNER JOIN actors ON movies.imdb = actors.imdb
WHERE actor = 'Eddie Murphy'
"""
try :
    w6b = pd.read_sql(sqlw6b, db_conn); print( "\nw6b contains\n", w6b)
except :
    if len(sqlw6b.lstrip()) :
        print(Fore.RED + "\nYour SQL statement has an error that must be fixed" + Fore.BLUE )
        print( sqlw6b )
        print(Fore.BLACK + "Start by checking the spelling of each field in the list" )
        print("Also consider spelling of your table name, and SQL statements\n" )


# Task w7a
sqlw7a = """
SELECT DISTINCT genre
FROM movies
INNER JOIN genre ON movies.title = genre.title
WHERE movies.title LIKE '%Shrek%'
"""
try :
    w7a = pd.read_sql(sqlw7a, db_conn); print( "\nw7a contains\n", w7a)
except :
    if len(sqlw7a.lstrip()) :
        print(Fore.RED + "\nYour SQL statement has an error that must be fixed" + Fore.BLUE )
        print( sqlw7a )
        print(Fore.BLACK + "Start by checking the spelling of each field in the list" )
        print("Also consider spelling of your table name, and SQL statements\n" )

# Task w7b
sqlw7b = """
SELECT DISTINCT genre, movies.title, writer
FROM movies
INNER JOIN genre ON movies.title = genre.title
WHERE movies.title LIKE '%Shrek%' AND writer LIKE '%Andrew Adamson%'
"""
try :
    w7b = pd.read_sql(sqlw7b, db_conn); print( "\nw7b contains\n", w7b)
except :
    if len(sqlw7b.lstrip()) :
        print(Fore.RED + "\nYour SQL statement has an error that must be fixed" + Fore.BLUE )
        print( sqlw7b )
        print(Fore.BLACK + "Start by checking the spelling of each field in the list" )
        print("Also consider spelling of your table name, and SQL statements\n" )

# Workshop END
#
###########################################################

#
# S12ccq Q5
sqlcc5 = """
SELECT COUNT(title)
FROM movies
WHERE title LIKE 'Frozen%'
"""
try :
    cc5 = pd.read_sql(sqlcc5, db_conn); print( "\ncc5 contains\n", cc5)
except :
    if len(sqlcc5.lstrip()) :
        print(Fore.RED + "\nYour SQL statement has an error that must be fixed" + Fore.BLUE )
        print( sqlcc5 )
        print(Fore.BLACK + "Start by checking the spelling of each field in the list" )
        print("Also consider spelling of your table name, and SQL statements\n" )
        
# S12ccq Q6
sqlcc6 = """
SELECT COUNT(title)
FROM movies
WHERE title LIKE 'Frozen%' AND production_company Like '%Walt Disney Animation Studios%'

"""
try :
    cc6 = pd.read_sql(sqlcc6, db_conn); print( "\ncc6 contains\n", cc6)
except :
    if len(sqlcc6.lstrip()) :
        print(Fore.RED + "\nYour SQL statement has an error that must be fixed" + Fore.BLUE )
        print( sqlcc6 )
        print(Fore.BLACK + "Start by checking the spelling of each field in the list" )
        print("Also consider spelling of your table name, and SQL statements\n" )

# S12ccq Q7
sqlcc7 = """
SELECT COUNT (DISTINCT actor)
FROM movies
INNER JOIN actors ON movies.imdb = actors.imdb
WHERE title LIKE 'Frozen%' AND production_company Like '%Walt Disney Animation Studios%'
"""
try :
    cc7 = pd.read_sql(sqlcc7, db_conn); print( "\ncc7 contains\n", cc7)
except :
    if len(sqlcc7.lstrip()) :
        print(Fore.RED + "\nYour SQL statement has an error that must be fixed" + Fore.BLUE )
        print( sqlcc7 )
        print(Fore.BLACK + "Start by checking the spelling of each field in the list" )
        print("Also consider spelling of your table name, and SQL statements\n" )


# S12ccq Q8
sqlcc8 = """
SELECT COUNT (title)
FROM movies
WHERE title LIKE '%Spider%'
"""
try :
    cc8 = pd.read_sql(sqlcc8, db_conn); print( "\ncc8 contains\n", cc8)
except :
    if len(sqlcc8.lstrip()) :
        print(Fore.RED + "\nYour SQL statement has an error that must be fixed" + Fore.BLUE )
        print( sqlcc8 )
        print(Fore.BLACK + "Start by checking the spelling of each field in the list" )
        print("Also consider spelling of your table name, and SQL statements\n" )



# S12ccq Q9
sqlcc9 = """
SELECT COUNT (DISTINCT production_company)
FROM movies
WHERE title LIKE 'Spider%' 
"""
try :
    cc9 = pd.read_sql(sqlcc9, db_conn); print( "\ncc9 contains\n", cc9)
except :
    if len(sqlcc9.lstrip()) :
        print(Fore.RED + "\nYour SQL statement has an error that must be fixed" + Fore.BLUE )
        print( sqlcc9 )
        print(Fore.BLACK + "Start by checking the spelling of each field in the list" )
        print("Also consider spelling of your table name, and SQL statements\n" )

# S12ccq Q10
sqlcc10 = """
SELECT genre
FROM movies
INNER JOIN genre ON movies.title = genre.title
WHERE movies.title LIKE 'Black Panther'
"""
try :
    cc10 = pd.read_sql(sqlcc10, db_conn); print( "\ncc10 contains\n", cc10)
except :
    if len(sqlcc10.lstrip()) :
        print(Fore.RED + "\nYour SQL statement has an error that must be fixed" + Fore.BLUE )
        print( sqlcc10 )
        print(Fore.BLACK + "Start by checking the spelling of each field in the list" )
        print("Also consider spelling of your table name, and SQL statements\n" )

# S12ccq Q11
sqlcc11 = """
SELECT DISTINCT genre
FROM movies
INNER JOIN genre ON movies.title = genre.title
WHERE production_company LIKE 'Marvel Studios'
"""
try :
    cc11 = pd.read_sql(sqlcc11, db_conn); print( "\ncc11 contains\n", cc11)
except :
    if len(sqlcc11.lstrip()) :
        print(Fore.RED + "\nYour SQL statement has an error that must be fixed" + Fore.BLUE )
        print( sqlcc11 )
        print(Fore.BLACK + "Start by checking the spelling of each field in the list" )
        print("Also consider spelling of your table name, and SQL statements\n" )


# S12ccq Q12
sqlcc12 = """
SELECT MAX(duration), title
FROM movies
INNER JOIN actors ON movies.imdb = actors.imdb
WHERE actor LIKE 'Jamie Foxx'
"""
try :
    cc12 = pd.read_sql(sqlcc12, db_conn); print( "\ncc12 contains\n", cc12)
except :
    if len(sqlcc12.lstrip()) :
        print(Fore.RED + "\nYour SQL statement has an error that must be fixed" + Fore.BLUE )
        print( sqlcc12 )
        print(Fore.BLACK + "Start by checking the spelling of each field in the list" )
        print("Also consider spelling of your table name, and SQL statements\n" )


# S12ccq Q13
sqlcc13 = """
SELECT duration, title, actor, director
FROM movies
INNER JOIN actors ON movies.imdb = actors.imdb
WHERE actor LIKE "Jamie Foxx"
ORDER BY duration

"""
try :
    cc13 = pd.read_sql(sqlcc13, db_conn); print( "\ncc13 contains\n", cc13)
except :
    if len(sqlcc13.lstrip()) :
        print(Fore.RED + "\nYour SQL statement has an error that must be fixed" + Fore.BLUE )
        print( sqlcc13 )
        print(Fore.BLACK + "Start by checking the spelling of each field in the list" )
        print("Also consider spelling of your table name, and SQL statements\n" )


#
# S12icq Q2
sqlic2 = """
SELECT MIN(year), title, director
FROM movies
INNER JOIN actors ON movies.imdb = actors.imdb
WHERE actor LIKE "Whoopi Goldberg"

"""
try :
    ic2 = pd.read_sql(sqlic2, db_conn); print( "\nic2 contains\n", ic2)
except :
    if len(sqlic2.lstrip()) :
        print(Fore.RED + "\nYour SQL statement has an error that must be fixed" + Fore.BLUE )
        print( sqlic2 )
        print(Fore.BLACK + "Start by checking the spelling of each field in the list" )
        print("Also consider spelling of your table name, and SQL statements\n" )

# S12icq Q3
sqlic3 = """
SELECT year, title, max(avg_vote)
FROM movies
INNER JOIN actors ON movies.imdb = actors.imdb
WHERE actor LIKE "Whoopi Goldberg"
"""
try :
    ic3 = pd.read_sql(sqlic3, db_conn); print( "\nic3 contains\n", ic3)
except :
    if len(sqlic3.lstrip()) :
        print(Fore.RED + "\nYour SQL statement has an error that must be fixed" + Fore.BLUE )
        print( sqlic3 )
        print(Fore.BLACK + "Start by checking the spelling of each field in the list" )
        print("Also consider spelling of your table name, and SQL statements\n" )

# S12icq Q4
sqlic4 = """
SELECT year, title, max(avg_vote)
FROM movies
WHERE writer LIKE '%Linda Woolverton%'
"""
try :
    ic4 = pd.read_sql(sqlic4, db_conn); print( "\nic4 contains\n", ic4)
except :
    if len(sqlic4.lstrip()) :
        print(Fore.RED + "\nYour SQL statement has an error that must be fixed" + Fore.BLUE )
        print( sqlic4 )
        print(Fore.BLACK + "Start by checking the spelling of each field in the list" )
        print("Also consider spelling of your table name, and SQL statements\n" )


# S12icq Q5
sqlic5 = """
SELECT year, title
FROM movies
WHERE title = 'The Lion King'
"""
try :
    ic5 = pd.read_sql(sqlic5, db_conn); print( "\nic5 contains\n", ic5)
except :
    if len(sqlic5.lstrip()) :
        print(Fore.RED + "\nYour SQL statement has an error that must be fixed" + Fore.BLUE )
        print( sqlic5 )
        print(Fore.BLACK + "Start by checking the spelling of each field in the list" )
        print("Also consider spelling of your table name, and SQL statements\n" )


# S12icq Q6
sqlic6 = """
SELECT DISTINCT genre
FROM movies
INNER JOIN genre ON movies.title = genre.title
WHERE director LIKE '%Rian Johnson%' 
"""
try :
    ic6 = pd.read_sql(sqlic6, db_conn); print( "\nic6 contains\n", ic6)
except :
    if len(sqlic6.lstrip()) :
        print(Fore.RED + "\nYour SQL statement has an error that must be fixed" + Fore.BLUE )
        print( sqlic6 )
        print(Fore.BLACK + "Start by checking the spelling of each field in the list" )
        print("Also consider spelling of your table name, and SQL statements\n" )


# S12icq Q7
sqlic7 = """
SELECT COUNT (DISTINCT actor)
FROM movies
INNER JOIN actors ON movies.imdb = actors.imdb
WHERE title LIKE 'Closer' 
"""
try :
    ic7 = pd.read_sql(sqlic7, db_conn); print( "\nic7 contains\n", ic7)
except :
    if len(sqlic7.lstrip()) :
        print(Fore.RED + "\nYour SQL statement has an error that must be fixed" + Fore.BLUE )
        print( sqlic7 )
        print(Fore.BLACK + "Start by checking the spelling of each field in the list" )
        print("Also consider spelling of your table name, and SQL statements\n" )
finally :
    db_conn.close()

###########################################################
#
#Individual Challenge: End
EndHere( globals())
#exit();
###########################################################
