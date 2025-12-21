from pydantic import BaseModel
from datetime import datetime

class EVChargerResponse(BaseModel):
    id: int
    stat_nm: str | None = None
    stat_id: str | None = None
    chger_id: str | None = None
    chger_type: str | None = None
    addr: str | None = None
    addr_detail: str | None = None
    location: str | None = None
    lat: float | None = None
    lng: float | None = None
    use_time: str | None = None
    busi_id: str | None = None
    bnm: str | None = None
    busi_nm: str | None = None
    busi_call: str | None = None
    stat: str | None = None
    stat_upd_dt: datetime | None = None
    last_ts_dt: datetime | None = None
    last_te_dt: datetime | None = None
    now_ts_dt: datetime | None = None
    output: int | None = None
    method: str | None = None
    zcode: str | None = None
    zscode: str | None = None
    kind: str | None = None
    kind_detail: str | None = None
    parking_free: str | None = None
    note: str | None = None
    limit_yn: str | None = None
    limit_detail: str | None = None
    del_yn: str | None = None
    del_detail: str | None = None
    traffic_yn: str | None = None
    year: str | None = None
    floor_num: str | None = None
    floor_type: str | None = None
    created_at: datetime

    class Config:
        from_attributes = True
    