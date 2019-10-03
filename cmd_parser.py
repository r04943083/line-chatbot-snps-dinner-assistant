from enum import Enum
from aenum import MultiValueEnum
from singleton_decorator import singleton

class LunchEnum(MultiValueEnum):
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

class DBManualEnum(MultiValueEnum):
    BD_DELETE = 'db delete'
    @staticmethod
    def list():
        return list(map(lambda x: x.value, DBManualEnum))



class CmdEnum(MultiValueEnum):
    CMD_HELLO     = ('hello', 'Hi', '妳好','你好')
    CMD_PRINT_ALL = ('help', '幫幫我', '你可以幹嘛')
    CMD_COUNT     = '收單'
    @staticmethod
    def list():
        return list(map(lambda x: x.values, CmdEnum))


@singleton
class CmdParser:
    def __init__(self):
        pass
        
    def decode(self, token):
        if any(x for x in LunchEnum if token in x.values):
                return LunchEnum(token)
        elif any(x for x in DBManualEnum if token in x.values):
            return DBManualEnum(token)
        elif any(x for x in CmdEnum if token in x.values):
            return CmdEnum(token)
