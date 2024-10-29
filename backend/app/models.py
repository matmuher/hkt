from pydantic import BaseModel

class AddUser(BaseModel):
    name: str

class User(BaseModel):
    id: int

class AddBook(BaseModel):
    name: str
    user: User

class Book(BaseModel):
    id: int

class AddNote(BaseModel):
    name: str
    txt: str
    book: Book

class Note(BaseModel):
    id: int
