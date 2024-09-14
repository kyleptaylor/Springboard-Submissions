-- from the terminal run:
-- psql < craigslist.sql

DROP DATABASE IF EXISTS craigslist_db;
CREATE DATABASE craigslist_db;
\c craigslist_db;

CREATE TABLE states (
    id SERIAL PRIMARY KEY,
    state TEXT NOT NULL
);

CREATE TABLE cities (
    id SERIAL PRIMARY KEY,
    city TEXT NOT NULL,
    state_id INT REFERENCES states ON DELETE CASCADE
);

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(15) UNIQUE NOT NULL,
    password VARCHAR(20) NOT NULL,
    city_id INT REFERENCES cities ON DELETE CASCADE
);

CREATE TABLE categories (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    title VARCHAR(25) NOT NULL,
    info TEXT,
    user_id INT REFERENCES users ON DELETE CASCADE,
    city_id INT REFERENCES cities ON DELETE CASCADE,
    category_id INT REFERENCES categories ON DELETE CASCADE
);

INSERT INTO states (state) VALUES
('California'),
('New York'),
('Texas'),
('Florida'),
('Illinois');

INSERT INTO cities (city, state_id) VALUES
('Los Angeles', 1),
('San Francisco', 1),
('New York City', 2),
('Houston', 3),
('Miami', 4);

INSERT INTO users (username, password, city_id) VALUES
('user123', 'password123', 1),
('johndoe', 'securepassword', 2),
('janedoe', 'janespass', 3),
('texan_hero', 'texas123', 4),
('florida_man', 'floridapass', 5);

INSERT INTO categories (name) VALUES
('Housing'),
('Jobs'),
('Services'),
('For Sale'),
('Community');

INSERT INTO posts (title, info, user_id, city_id, category_id) VALUES
('Apartment for Rent', '2-bed apartment available', 1, 1, 1),
('Software Developer Job', 'Looking for full-time devs', 2, 3, 2),
('Moving Services', 'Affordable moving help', 3, 4, 3),
('Used Car for Sale', '2010 Toyota Camry', 4, 4, 4),
('Local Event', 'Join us for a community clean-up', 5, 5, 5);

