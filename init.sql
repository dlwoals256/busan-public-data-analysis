CREATE TABLE IF NOT EXISTS raw_data (
    id          SERIAL PRIMARY KEY,
    payload     JSONB NOT NULL,
    created_at  TIMESTAMPZ NOT NULL DEFAULT NOW()
);

