import mysql.connector

# connectiong to database
db = mysql.connector.connect(
    host="mysql",
    user="mysql",
    password="A1245784512",
    database="noteData"
)
cursor = db.cursor()

# Selects all notes in database
def get_all_notes():
    cursor.execute("SELECT * FROM notes")
    return cursor.fetchall()

# Selects note by id
def get_note_by_id(note_id):
    cursor.execute("SELECT * FROM notes WHERE id = %s", (note_id,))
    return cursor.fetchone()

# add a new note
def add_note(title, content):
    cursor.execute("INSERT INTO notes (title, content) VALUES (%s, %s)", (title, content))
    db.commit()
    return cursor.lastrowid

# update existing note
def update_note(note_id, title, content):
    cursor.execute("UPDATE notes SET title = %s, content = %s WHERE id = %s", (title, content, note_id))
    db.commit()

# delete existing note
def delete_note(note_id):
    cursor.execute("DELETE FROM notes WHERE id = %s", (note_id,))
    db.commit()

# close connection to database
def close_connection():
    cursor.close()
    db.close()