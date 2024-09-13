import sqlite3

# connect to a database or create one if it isnt there
connection = sqlite3.connect("database_name.db")

cursor = connection.cursor()

# this command is creating a table with columns name, age and favourite colour
# only run this the first time and then can comment out as the table will be created.

cursor.execute("""CREATE TABLE newTable (
                name TEXT,
                age INTEGER,
                favouriteColour TEXT
            )""")

# This is inserting one row of data into the table
cursor.execute("INSERT INTO newTable VALUES ('Jack', 36, 'Blue')")


cursor.execute("SELECT * FROM newTable")
results = cursor.fetchall()

for result in results:
    print(result)


# commit changes etc
connection.commit()
# close connection
connection.close()
