from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import Optional
from ..serve import request_ai_control_service as service
from ..configs import data_source_mysql as mysql
from ..schemas import system_model_schema as sch

app = APIRouter()


def get_db():
    db = mysql.session
    try:
        yield db
    finally:
        db.close()


@app.post("/requestCrowdPackList")
def __request_list(db: Optional[Session] = Depends(get_db), request: Optional[sch.CrowdPackListRequest] = None) -> list:
    return service.__request_list(db, request)


@app.delete("/delete/{crowd_pack_id}")
def __delete_crowd_pack(db: Optional[Session] = Depends(get_db), crowd_pack_id: Optional[int] = None) -> bool:
    if crowd_pack_id is not None:
        service.__delete_crowd_pack(db, crowd_pack_id)
    return True


@app.get("/request")
def __request_chat_boot(user_input: str) -> str:
    return service.__request_chat_boot(user_input).text
