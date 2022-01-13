import database

def get_user_by_email(email):
    results = database.sql_select('SELECT * FROM users WHERE email=%s', [email])
    if len(results) > 0:
        return results[0]
    else:
        return None
    

def insert_user(firstname, lastname, email, password, location, avatar ):
    database.sql_write('INSERT INTO users (first_name, last_name, email, password, location, avatar) VALUES (%s, %s, %s, %s, %s, %s);', [
        firstname,
        lastname,
        email,
        password,
        location,
        avatar
    ])


def get_user(id):
    results = database.sql_select('SELECT * FROM users WHERE id=%s', [id])
    if len(results) > 0:
        return results
    else:
        return None
    

def get_all_users():
    results = database.sql_select('SELECT * FROM users', [])
    return results

def update_user(id, name, email):
    pass

def delete_user(id):
    pass
