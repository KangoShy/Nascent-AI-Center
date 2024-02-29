from pydantic import BaseModel
from typing import Optional


class BaseRequestForList(BaseModel):
    search: Optional[str] = None
    pageNum: int
    pageSize: int


class CrowdPackListRequest(BaseRequestForList):
    groupId: int
    areaId: int
