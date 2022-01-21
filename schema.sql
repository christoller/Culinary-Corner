CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    first_name varchar(50) NOT NULL,
    last_name varchar(50) NOT NULL,
    email text NOT NULL unique,
    password text NOT NULL,
    location varchar(50) NOT NULL,
    avatar text
);

CREATE TABLE posts (
    id serial PRIMARY KEY,
    user_id INTEGER,
    post TEXT,
    date_submitted TIMESTAMP,
    category TEXT,
    CONSTRAINT fk_user 
        FOREIGN KEY(user_id)
        REFERENCES users(id)   
);

CREATE TABLE users_info (
    id serial PRIMARY KEY,
    user_id INTEGER,
    job_title TEXT,
    workplace TEXT,
    interests TEXT,
    bio TEXT,
    CONSTRAINT fk_user 
        FOREIGN KEY(user_id)
        REFERENCES users(id)   
);
