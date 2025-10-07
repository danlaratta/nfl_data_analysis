
CREATE TABLE IF NOT EXISTS team (
    team_id             INT PRIMARY KEY,
    team_name           TEXT NOT NULL,
    abbreviation        VARCHAR(2) NOT NULL,
    city                TEXT NOT NULL,
    home_or_away        TEXT NOT NULL,
    home_record         TEXT NOT NULL,
    away_record         TEXT NOT NULL,
    overall_record      TEXT NOT NULL
);