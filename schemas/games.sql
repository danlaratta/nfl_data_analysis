
CREATE TYPE game_season AS ENUM ('PRE_SEASON', 'SEASON', 'POST_SEASON');

CREATE TABLE IF NOT EXISTS games (
    game_id             INT PRIMARY KEY,
    home_team_id        INT REFERENCES team(team_id),
    away_team_id        INT REFERENCES team(team_id),
    stadium_id          INT REFERENCES stadium(stadium_id),
    game_type           game_season NOT NULL,
    season_week         INT NOT NULL,
    game_date_time      DATE NOT NULL,
    attendance          INT NOT NULL,
);