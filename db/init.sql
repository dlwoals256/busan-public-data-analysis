CREATE TABLE IF NOT EXISTS raw_data (
    id          SERIAL PRIMARY KEY,
    collected_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    payload     JSONB NOT NULL
);

CREATE SCHEMA IF NOT EXISTS analytics;

CREATE TABLE IF NOT EXISTS analytics.ev_chargers (
    id SERIAL PRIMARY KEY,
    stat_nm TEXT,
    stat_id TEXT,
    chger_id TEXT,
    chger_type TEXT,
    addr TEXT,
    addr_detail TEXT,
    location TEXT,
    lat NUMERIC(12, 9),
    lng NUMERIC(12, 9),
    use_time TEXT,
    busi_id TEXT,
    bnm TEXT,
    busi_nm TEXT,
    busi_call TEXT,
    stat TEXT,
    stat_upd_dt TIMESTAMP,
    last_ts_dt TIMESTAMP,
    last_te_dt TIMESTAMP,
    now_ts_dt TIMESTAMP,
    output INTEGER,
    method TEXT,
    zcode TEXT,
    zscode TEXT,
    kind TEXT,
    kind_detail TEXT,
    parking_free TEXT,
    note TEXT,
    limit_yn TEXT,
    limit_detail TEXT,
    del_yn TEXT,
    del_detail TEXT,
    traffic_yn TEXT,
    year TEXT,
    floor_num TEXT,
    floor_type TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT unique_charger UNIQUE (stat_id, chger_id)
);