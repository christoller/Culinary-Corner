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
    results = database.sql_select("SELECT * FROM users where email=%s;",[email])
    database.sql_write('INSERT INTO users_info (user_id) values (%s);', [results[0][0]])


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
    
def get_user_info(user_id):
    results = database.sql_select('SELECT users.id, users.first_name, users.last_name, users.location, users.avatar, users_info.job_title, users_info.workplace, users_info.interests, users_info.bio FROM users INNER JOIN users_info ON users.id = user_id WHERE users.id=%s', [user_id])
    return results

def update_user(id, firstname, lastname, location, jobtitle, workplace, interests, bio, avatar):    
    database.sql_write('UPDATE users SET first_name=%s, last_name=%s, location=%s, avatar=%s WHERE id=%s', [firstname, lastname, location, avatar, id])
    database.sql_write('UPDATE users_info SET job_title=%s, workplace=%s, interests=%s, bio=%s WHERE user_id=%s', [jobtitle, workplace, interests, bio, id])
