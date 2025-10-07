CREATE TYPE leader_category AS ENUM ('PASSING', 'RUSHING', 'RECEIVING');

CREATE TABLE IF NOT EXISTS game_leaders (
    PRIMARY KEY (team_id, game_id),
    team_id             INT REFERENCES team(team_id),
    game_id             INT REFERENCES games(game_id),
    player_id           INT REFERENCES players(player_id),
    category            leader_category NOT NULL,
    yards               INT NOT NULL,
    touchdowns          INT,
    complete_throws     INT NOT NULL,
    incomplete_throws   INT NOT NULL,
    completion_pct      INT NOT NULL,
    interceptions       INT,
    carries             INT NOT NULL,
    catches             INT NOT NULL,
    fumbles             INT,
    completions         INT NOT NULL
);