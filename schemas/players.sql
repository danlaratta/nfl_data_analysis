
CREATE TABLE IF NOT EXISTS players (
    player_id       INT PRIMARY KEY,
    player_name     TEXT NOT NULL,
    position        VARCHAR(2) NOT NULL,
    jersey_number   INT NOT NULL,
    team_id         INT REFERENCES team(team_id)
);
