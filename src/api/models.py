from sqlalchemy import (
    Column, Integer,
    Float, String, DateTime,
    UniqueConstraint
)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class EVCharger(Base):
    __tablename__ = 'ev_chargers'
    __table_args__ = (
        UniqueConstraint('stat_id', 'chger_id', name='unique_charger'),
        {'schema': 'analytics'}
    )

    id = Column(Integer, primary_key=True, index=True)
    stat_nm = Column(String)
    stat_id = Column(String)
    chger_id = Column(String)
    chger_type = Column(String)
    addr = Column(String)
    addr_detail = Column(String)
    location = Column(String)
    lat = Column(Float)
    lng = Column(Float)
    use_time = Column(String)
    busi_id = Column(String)
    bnm = Column(String)
    busi_nm = Column(String)
    busi_call = Column(String)
    stat = Column(String)
    stat_upd_dt = Column(DateTime)
    last_ts_dt = Column(DateTime)
    last_te_dt = Column(DateTime)
    now_ts_dt = Column(DateTime)
    output = Column(Integer)
    method = Column(String)
    zcode = Column(String)
    zscode = Column(String)
    kind = Column(String)
    kind_detail = Column(String)
    parking_free = Column(String)
    note = Column(String)
    limit_yn = Column(String)
    limit_detail = Column(String)
    del_yn = Column(String)
    del_detail = Column(String)
    traffic_yn = Column(String)
    year = Column(String)
    floor_num = Column(String)
    floor_type = Column(String)
    created_at = Column(DateTime)