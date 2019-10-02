from enum import Enum
from singleton_decorator import singleton

class LunchEnum(Enum):
    W_NORMAL_ADD_1 = '包周一般餐盒++'
    W_VEGAN_ADD_1  = '包周素食餐盒++'
    W_ANGEL_ADD_1  = '包周天使餐盒++'
    W_MAN_ADD_1    = '包周男子漢++'
    M_NORMAL_ADD_1 = '包月一般餐盒++'
    M_VEGAN_ADD_1  = '包月素食餐盒++'
    M_ANGEL_ADD_1  = '包月天使餐盒++'
    M_MAN_ADD_1    = '包月男子漢++'    
    @staticmethod
    def list():
        return list(map(lambda x: x.value, LunchEnum))

class DBManualEnum(Enum):
    BD_DELETE = 'db delete'
    @staticmethod
    def list():
        return list(map(lambda x: x.value, DBManualEnum))

#from aenum import MultiValueEnum

class CmdEnum(Enum):
    CMD_HELLO     = 'hello'
    CMD_PRINT_ALL = 'help'
    @staticmethod
    def list():
        return list(map(lambda x: x.value, CmdEnum))


@singleton
class CmdParser:
    def __init__(self):
        pass
        
    def decode(self, token):
        if any(x for x in LunchEnum if x.value == token):
            return LunchEnum(token)
        elif any(x for x in DBManualEnum if x.value == token):
            return DBManualEnum(token)
        elif any(x for x in CmdEnum if x.value == token):
            return CmdEnum(token)