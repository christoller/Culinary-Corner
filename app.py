from flask import Flask, render_template
import os
import psycopg2

# Import Controllers
from controllers.user_controller import user_controller
from controllers.session_controller import session_controller
from controllers.message_board_controller import message_board_controller

DB_URL = os.environ.get("DATABASE_URL", "dbname=project_2")
SECRET_KEY = os.environ.get("SECRET_KEY", "MY_SECRET_KEY")


app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY


@app.route('/')
def index():
    conn = psycopg2.connect(DB_URL)
    cur = conn.cursor()
    cur.execute('SELECT 1', [])  # Query to check that the DB connected
    conn.close()
    return render_template('index.html')

# Register Contollers
app.register_blueprint(user_controller)
app.register_blueprint(session_controller)
app.register_blueprint(message_board_controller)




if __name__ == "__main__":
    app.run(debug=True)
