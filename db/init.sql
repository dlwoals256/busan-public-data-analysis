CREATE TABLE IF NOT EXISTS electronic_car_charger (
    id          SERIAL PRIMARY KEY,
    collected_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    payload     JSONB NOT NULL
);

