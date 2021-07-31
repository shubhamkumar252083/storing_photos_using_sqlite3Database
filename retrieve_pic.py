import sqlite3


def writeTofile(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open(filename, 'wb') as file:
        file.write(data)
    print("Stored blob data into: ", filename, "\n")


def readBlobData(pic_id):
    try:
        sqliteConnection = sqlite3.connect('pic_data.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sql_fetch_blob_query = """SELECT * from pic where id = ?"""
        cursor.execute(sql_fetch_blob_query, (pic_id,))
        record = cursor.fetchall()
        for row in record:
            print("Id = ", row[0])
            photo = row[1]
            print("Storing employee image and resume on disk \n")
            photoPath = "/home/shubham/Desktop/flask_rough/" + \
                f"{row[0]}" + ".jpg"
            writeTofile(photo, photoPath)
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read blob data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("sqlite connection is closed")


readBlobData(1)
