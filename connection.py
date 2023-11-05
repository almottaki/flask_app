import sqlite3

try:
    sqliteConnection = sqlite3.connect('/home/mottaki/PycharmProjects/Flask_Blog/instance/site.db')
    cursor = sqliteConnection.cursor()
    print("Successfully Connected to SQLite")

    sqlite_insert_query = """INSERT INTO user
                          (id, username, email, image_file, password) 
                           VALUES 
                          (1,'James','james@pynative.com','xyz', 'abc')"""

    count = cursor.execute(sqlite_insert_query)
    sqliteConnection.commit()
    print("Record inserted successfully into SqliteDb_developers table ", cursor.rowcount)
    cursor.close()

except sqlite3.Error as error:
    print("Failed to insert data into sqlite table", error)
