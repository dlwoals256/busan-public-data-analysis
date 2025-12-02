CREATE TABLE IF NOT EXISTS raw_data (
    id          SERIAL PRIMARY KEY,
    source      VARCHAR(50) NOT NULL,
    collected_at  TIMESTAMPZ NOT NULL DEFAULT NOW(),
    payload     JSONB NOT NULL
);

