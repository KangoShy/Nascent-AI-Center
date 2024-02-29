import time
from typing import Optional


def this_time() -> int:
    return int(time.time())


class Response:

    def __init__(self, code: int, data: object, msg: str, success: bool, timestamp: int):
        self.msg = msg
        self.data = data
        self.code = code
        self.success = success
        self.timestamp = timestamp

    def success(data: object, code: Optional[int] = 0):
        return Response(code, data, '查询成功', True, this_time())

    def fail(code: Optional[int] = 9000):
        return Response(code, None, '查询失败', False, this_time())
