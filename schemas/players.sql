
CREATE TABLE IF NOT EXISTS players (
    player_id       INT PRIMARY KEY,
    team_id         INT REFERENCES team(team_id)
    player_name     TEXT NOT NULL,
    jersey_number   INT NOT NULL,
    position        VARCHAR(2) NOT NULL
);
