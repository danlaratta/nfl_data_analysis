
CREATE TABLE IF NOT EXISTS game_leaders (
    PRIMARY KEY (team_id, game_id),
    team_id              INT REFERENCES team(team_id),
    game_id              INT REFERENCES games(game_id),
    player_id            INT REFERENCES players(player_id),
    category_name        TEXT NOT NULL,
    yards                INT NOT NULL,
    touchdowns           INT DEFAULT 0,
    completions          INT NOT NULL,
    incompletions        INT NOT NULL,
    interceptions        INT DEFAULT 0,
    carries              INT NOT NULL,
    catches              INT NOT NULL
);