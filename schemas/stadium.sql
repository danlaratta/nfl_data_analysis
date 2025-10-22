CREATE TABLE IF NOT EXISTS stadium (
    stadium_id             INT PRIMARY KEY,
    stadium_name           TEXT NOT NULL,
    stadium_city           TEXT NOT NULL,
    stadium_state          VARCHAR(4) NOT NULL,
    stadium_country        TEXT NOT NULL
);