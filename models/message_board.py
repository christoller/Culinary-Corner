import database

def get_all_posts():
    results = database.sql_select('SELECT posts.post, posts.date_submitted, posts.category, users.first_name, users.last_name, users.location, users.avatar FROM posts INNER JOIN users ON users.id = user_id ORDER BY posts.date_submitted DESC;', [])
    print(results)

    return results

def create_post(user_id, post, date, category):
    database.sql_write('INSERT INTO posts (user_id, post, date_submitted, category) values(%s, %s, %s, %s );', [
        user_id,
        post,
        date,
        category
    ])