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
    # LunchEnum.W_NORMAL_ADD_1.name = 'W_NORMAL_ADD_1'
    # LunchEnum.W_NORMAL_ADD_1.value = '包周一般餐盒++'
  
@singleton
class CmdParser:
    def __init__(self):
        pass
        
    def decode(self, text):
        return LunchEnum(text)