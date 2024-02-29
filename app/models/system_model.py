from ..configs.data_source_mysql import Base
from sqlalchemy import Column, Integer, String, DateTime


class CrowdPack(Base):
    __tablename__ = "cdp_crowd_pack"
    id = Column(Integer, primary_key=True)
    state = Column(Integer)
    create_time = Column(DateTime)
    update_time = Column(DateTime)
    group_id = Column(Integer)
    area_id = Column(Integer)
    pack_source = Column(Integer)
    pack_name = Column(String)
    type = Column(Integer)
    crowd_total = Column(Integer)
    crowd_code = Column(String)
    crowd_config = Column(String)
    platform = Column(Integer)
    create_user_id = Column(Integer)


class BaseChat:

    def __init__(self, conv_uid, chat_mode, model_name, select_param, user_input):
        self.conv_uid = conv_uid
        self.chat_mode = chat_mode
        self.model_name = model_name
        self.select_param = select_param
        self.user_input = user_input
