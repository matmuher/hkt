from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import app.models as models
import app.db_query as db_query
import app.db_init as db_init
import sqlite3
from sqlite3 import Error


app = FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection


def execute_query(query):
    connection = create_connection("./readind_diary.sqlite")

    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
        return True
    except Error as e:
        print(f"The error '{e}' occurred")
        return False


def execute_read_query(query):
    connection = create_connection("./readind_diary.sqlite")

    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")


execute_query(db_init.users)
execute_query(db_init.books)
execute_query(db_init.notes)


@app.post("/add-user")
def add_user(user : models.AddUser):
    add_user_db = db_query.get_add_user(user.name)

    ret = execute_query(add_user_db)

    return {"code": 200 if ret else 404}


@app.get("/users")
def get_users():
    get_users_db = db_query.get_users()
    users_db = execute_read_query(get_users_db)

    users = [{"id" : user_db[0], "name" : user_db[1]} for user_db in users_db]

    return users


@app.delete("/delete-user")
def delete_user(user: models.User):
    delete_user_db = db_query.get_delete_user(user.id)

    ret = execute_query(delete_user_db)
    
    return {"code": 200 if ret else 404}

def is_user_exist(id):
    users = get_users()
    return any([user["id"] == id for user in users])

def get_all_books():
    get_books_db = db_query.get_all_books()
    books_db = execute_read_query(get_books_db)

    return books_db
    

def is_book_exist(id):
    books = get_all_books()
    return any([book[0] == id for book in books])


@app.post("/books")
def get_books(user: models.User):
    if not is_user_exist(user.id):
        return {"message" : "invalid user"}

    get_books_db = db_query.get_books(user.id)
    books_db = execute_read_query(get_books_db)

    books = [{"id" : book_db[0], "name" : book_db[1]} for book_db in books_db]
    return books

@app.post("/add-book")
def add_book(book: models.AddBook):
    if not is_user_exist(book.user.id):
        return {"message" : "invalid user"}

    books = get_books(book.user)
    if any([book_db["name"] == book.name for book_db in books]):
        return {"code" : 403}
    
    add_book_db = db_query.add_book(book.user.id, book.name)
    ret = execute_query(add_book_db)

    return {"code": 200 if ret else 404}


@app.delete("/delete-book")
def delete_book(book: models.Book):
    delete_book_db = db_query.delete_book(book.id)
    ret = execute_query(delete_book_db)

    return {"code": 200 if ret else 404}

@app.post("/notes")
def get_notes(book: models.Book):
    if not is_book_exist(book.id):
        return {"message" : "invalid book"}

    get_notes_db = db_query.get_notes(book.id)
    notes_db = execute_read_query(get_notes_db)

    notes = [{"id" : note_db[0], "name" : note_db[1], "txt" : note_db[2]} for note_db in notes_db]
    return notes

@app.post("/add-note")
def add_note(note: models.AddNote):
    if not is_book_exist(note.book.id):
        return {"message" : "invalid book"}

    add_note_db = db_query.add_note(note.book.id, note.name, note.txt)
    ret = execute_query(add_note_db)

    return {"code": 200 if ret else 404}


@app.delete("/delete-note")
def delete_note(note: models.Note):
    delete_note_db = db_query.delete_note(note.id)
    ret = execute_query(delete_note_db)

    return {"code": 200 if ret else 404}


@app.get("/")
def root():
    return {"message": "Hello, World!"}
