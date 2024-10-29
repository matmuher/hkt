
def get_users():
    return "SELECT * from users"

def get_add_user(name):
    return f"""
    INSERT INTO
    users (name)
    VALUES
    ('{name}');
    """

def get_delete_user(id):
    return f"DELETE FROM users WHERE id = {id}"

def get_all_books():
    return "SELECT * from books"

def get_books(user_id):
    return f"SELECT * from books WHERE user_id = {user_id}"

def add_book(user_id, book_name):
    return f"""
    INSERT INTO
    books (name, user_id)
    VALUES
    ('{book_name}', {user_id});
    """

def delete_book(id):
    return f"DELETE FROM books WHERE id = {id}"

def get_notes(book_id):
    return f"SELECT * from notes WHERE book_id = {book_id}"

def add_note(book_id, name, txt):
    return f"""
    INSERT INTO
    notes (name, txt, book_id)
    VALUES
    ('{name}', '{txt}', {book_id});
    """

def delete_note(id):
    return f"DELETE FROM notes WHERE id = {id}"