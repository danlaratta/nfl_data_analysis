
CREATE TABLE IF NOT EXISTS team_game_stats (
    PRIMARY KEY (team_id, game_id),
    team_id             INT REFERENCES team(team_id),
    game_id             INT REFERENCES games(game_id),
    points_scored       INT NOT NULL,
    total_points        INT NOT NULL,
    winner              TEXT NOT NULL
);