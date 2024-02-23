from fastapi import APIRouter
from pydantic import BaseModel
import requests
import logging
import random
import time
import json

app = APIRouter()
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


class BaseChat:

    def __init__(self, conv_uid, chat_mode, model_name, select_param, user_input):
        self.conv_uid = conv_uid
        self.chat_mode = chat_mode
        self.model_name = model_name
        self.select_param = select_param
        self.user_input = user_input


@app.post("/request", summary="请求DB-GPT对话", response_model=None)
async def __request_chat_boot(bean: BaseChat):
    responseStr = ""
    if bean.user_input is None:
        return responseStr

    bean.__init__('c5c85b50-cfce-11ee-a9c4-0242c0a10002', 'chat_knowledge', 'wenxin_proxyllm', 'test',
                  bean.user_input)

    start = time.time()
    order = random.randint(1, 100)
    url = "http://192.168.200.214:5000/api/v1/chat/completions"
    logging.info('[%s]开始执行对话请求', order)

    # Send request.
    try:
        responseStream = requests.post(url, data=json.dumps(bean), stream=True)
    except Exception as e:
        logging.error(f'[{order}]执行对话请求失败，错误信息=> {e}')
        raise RuntimeError('System Error')
    finally:
        end = time.time()

    logging.info(f'[{order}]结束执行对话请求，耗时{end - start}')

    # Read EventStream
    for line in responseStream.iter_lines(decode_unicode=True):
        if line:
            responseStr += line
            print(line)

    return responseStr

# 异步记录
# asyncio.run()
