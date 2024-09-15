-- from the terminal run:
-- psql < soccer_league.sql

DROP DATABASE IF EXISTS soccer_league_db;
CREATE DATABASE soccer_league_db;
\c soccer_league_db;

CREATE TABLE teams (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    city TEXT NOT NULL
);

CREATE TABLE players (
    id SERIAL PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    team_id INT REFERENCES teams ON DELETE CASCADE,
    position TEXT,
    jersey_number INT
);

CREATE TABLE referees (
    id SERIAL PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL
);

CREATE TABLE matches (
    id SERIAL PRIMARY KEY,
    home_team_id INT REFERENCES teams ON DELETE CASCADE,
    away_team_id INT REFERENCES teams ON DELETE CASCADE,
    referee_id INT REFERENCES referees ON DELETE SET NULL,
    match_date DATE NOT NULL,
    home_team_score INT DEFAULT 0,
    away_team_score INT DEFAULT 0
);

CREATE TABLE goals (
    id SERIAL PRIMARY KEY,
    match_id INT REFERENCES matches ON DELETE CASCADE,
    player_id INT REFERENCES players ON DELETE CASCADE,
    goal_time TIME,
    team_id INT REFERENCES teams ON DELETE CASCADE -- The team for which the goal was scored
);

CREATE TABLE seasons (
    id SERIAL PRIMARY KEY,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL
);

CREATE TABLE team_rankings (
    id SERIAL PRIMARY KEY,
    season_id INT REFERENCES seasons ON DELETE CASCADE,
    team_id INT REFERENCES teams ON DELETE CASCADE,
    wins INT DEFAULT 0,
    losses INT DEFAULT 0,
    draws INT DEFAULT 0,
    points INT DEFAULT 0 -- Total points (e.g., 3 for a win, 1 for a draw)
);

CREATE TABLE league (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL
);