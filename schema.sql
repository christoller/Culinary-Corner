CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    first_name varchar(50) NOT NULL,
    last_name varchar(50) NOT NULL,
    email text NOT NULL,
    password text NOT NULL,
    location varchar(50) NOT NULL,
    avatar text
);

INSERT INTO users (first_name, last_name, location, email, password) VALUES ('Chris', 'Toller', 'chris@example.com', 'password', 'Melbourne');

CREATE TABLE posts (
    id serial PRIMARY KEY,
    user_id INTEGER,
    post TEXT,
    date_submitted TEXT,
    category TEXT,
    CONSTRAINT fk_user 
        FOREIGN KEY(user_id)
        REFERENCES users(id)   
);

INSERT INTO posts (user_id, post, date_submitted, category) VALUES (1, 'Looking for a full time chef in South Melbourne. Call 2343242', '2022-01-07 23:59:59', 'Job');
INSERT INTO posts (user_id, post, date_submitted, category) VALUES (2, 'What is your favourite bloody mary recipe?', '2022-05-07 12:59:59', 'Question');
INSERT INTO posts (user_id, post, date_submitted, category) VALUES (3, 'About to go make an idiot sandwich', '2022-01-09 16:35:59', 'General');
INSERT INTO posts (user_id, post, date_submitted, category) VALUES (4, 'Missing my fave bartender :(','2022-01-07 20:59:59', 'General');
INSERT INTO posts (user_id, post, date_submitted, category) VALUES (5, 'Looking for a a FOH job. Hit me up 32432234', '2022-01-10 10:59:59', 'Job');



INSERT INTO posts (user_id, post, date_submitted, category) values ( %s, %s, %s, %s );