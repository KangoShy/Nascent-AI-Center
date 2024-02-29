import requests
import json
import logging
import time
import random
from threading import Thread
from typing import Optional

from sqlalchemy import desc

from ..models import system_model as mod
from ..core import enums
from ..configs import config
from requests import Response

logger = logging.getLogger(__name__)


def __request_chat_boot(user_input: str) -> Optional[Response]:
    """ Request ChatAI server and log access.
    :param user_input: input param
    :return: response
    """
    baseChat = mod.BaseChat(config.gpt_conv_uid, config.gpt_chat_mode, config.gpt_model_name,
                            config.gpt_select_param,
                            user_input)

    start = time.time()
    order = random.randint(1, 100)
    logger.info('[%s]Start request', order)

    # Send request.
    try:
        responseStream = requests.post(config.gpt_url, data=json.dumps(baseChat.__dict__), stream=True)
        responseStream.encoding = 'utf-8'
    except Exception as e:
        logging.error(f'[{order}]Exec failed and msg => {e}')
        raise RuntimeError('System Error')
    finally:
        logger.info(f'[{order}]End request and consume = {time.time() - start}')

    # Log access.
    Thread(target=log_access_to_db) \
        .start()

    return responseStream


def __request_list(db, request) -> list:
    info = db.query(mod.CrowdPack) \
        .filter(mod.CrowdPack.area_id.__eq__(request.areaId)) \
        .filter(mod.CrowdPack.group_id.__eq__(request.groupId)) \
        .filter(mod.CrowdPack.state == enums.StateStatus.NORMAL.value)

    # 模糊匹配
    if request.search is not None:
        info = info.filter(mod.CrowdPack.pack_name.like(f'%{request.search}%'))

    return info.order_by(
        mod.CrowdPack.update_time.desc()).offset(request.pageNum). \
        limit(request.pageSize) \
        .all()


def __delete_crowd_pack(db, crowd_pack_id):
    info = db.query(mod.CrowdPack).filter(mod.CrowdPack.id.__eq__(crowd_pack_id)).first()
    if not info:
        return
    info.state = enums.StateStatus.DELETED.value
    db.commit()


def log_access_to_db():
    print('记录db')
    pass
