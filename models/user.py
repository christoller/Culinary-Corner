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

def get_posts_from_user(user_id):
    results = database.sql_select('SELECT posts.user_id, posts.post, posts.date_submitted, posts.category, users.first_name, users.last_name, users.location, users.avatar, posts.id FROM posts INNER JOIN users ON users.id = user_id WHERE user_id=%s ORDER BY posts.date_submitted DESC;', [user_id])
    return results
    
def update_user(id, name, email):
    pass

def delete_user(id):
    pass
