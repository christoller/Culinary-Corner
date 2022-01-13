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