CREATE TABLE IF NOT EXISTS raw_data (
    id          SERIAL PRIMARY KEY,
    collected_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    payload     JSONB NOT NULL
);

