
CREATE TABLE IF NOT EXISTS games (
    game_id         INT PRIMARY KEY,
    home_team_id    INT REFERENCES team(team_id),
    away_team_id    INT REFERENCES team(team_id),
    stadium_id    INT REFERENCES stadium(stadium_id),
    season_week     INT NOT NULL,
    game_date       DATE NOT NULL,
    game_time       TIME NOT NULL,
    attendance      INT NOT NULL,
);