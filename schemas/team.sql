
CREATE TABLE IF NOT EXISTS team (
    team_id             INT PRIMARY KEY,
    team_name           TEXT NOT NULL,
    abbreviation        VARCHAR(5) NOT NULL,
    city                TEXT NOT NULL,
    home_or_away        TEXT NOT NULL,
    home_wins           INT DEFAULT 0
    away_wins           INT DEFAULT 0,
    overall_record      TEXT NOT NULL
);