import mysql.connector

my_db = mysql.connector.connect(
    host = "localhost",
    user = "darishkaams",
    passwd = "Z1_May_2015",
    database = "books_notes"
)
mycursor = my_db.cursor()
#  Creating database and its content

# mycursor.execute("CREATE DATABASE books_notes")
# mycursor.execute("SHOW DATABASES")
# for x in mycursor:
#   print(x)

# mycursor.execute("CREATE TABLE micro_lib (author_name CHAR(255), note VARCHAR(255), rating BIT(2) )")
# mycursor.execute("SHOW TABLES")
# for x in mycursor:
#   print(x)

# mycursor.execute("ALTER TABLE micro_lib ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

# sql = "INSERT INTO micro_lib (author_name, note, rating) VALUES (%s, %s, %s)"
# val1 = ("Marine Old", "Wine. A tasting course - adding some new notes to your life", 0)
# val2 = ("Ashlee Vance", "Elon Musk.Shaping the Future - have ever thought that it is possible", 1)
# val3 = ("Nancy Etcoff", "Survival of the Pretiest - better say smartest", 1)
# mycursor.execute(sql, val1)
# my_db.commit()
# mycursor.execute(sql, val2)
# my_db.commit()
# mycursor.execute(sql, val3)
# my_db.commit()
# print(mycursor.rowcount, "record(s) inserted.")

#Read notes from file
def read_notes():
    mycursor.execute("SELECT note FROM micro_lib")
    myresult = mycursor.fetchall()
    print("Micro Library Notes:")
    for note in myresult:
        print (note)

read_notes()

#Add notes to file
def add(x):
    sql = "INSERT INTO micro_lib (author_name, note, rating) VALUES (%s, %s, %s)"
    mycursor.execute(sql, x)
    my_db.commit()
    print(mycursor.rowcount, "record inserted. Thank you!")

# add(("Grady Klein", "The Cartoon Introduction to Psychology - nice way to relax", 1))

#Get author with the highest rating
def highest_rating():
    sql = "SELECT author_name FROM micro_lib WHERE rating = 1"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    print("The Authors with the Highest Ratings: ")
    for author in myresult:
        print(author)
highest_rating()

#Get author with the lowest rating
def lowest_rating():
    sql = "SELECT author_name FROM micro_lib WHERE rating = 0"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    print("The Authors with the Lowest Ratings: ")
    for author in myresult:
        print(author)
lowest_rating()

#Get average rating
def average():
    sql = "SELECT AVG(rating) FROM micro_lib"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    print("The Average Rating: ")
    for rating in myresult:
        print(rating)
average()