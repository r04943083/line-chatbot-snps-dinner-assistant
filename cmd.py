from abc import ABC, abstractmethod
from cmd_parser import CmdParser, LunchEnum
from line_bot_mgr import LineBotMgr

line_bot = LineBotMgr()

class Cmd:
    def __init__(self, event):
        self.event = event
        
class Strategy(ABC):
    @abstractmethod
    def action(self, event):
        pass

class db_week_add_normal(Strategy):
    def action(self, event):
        print("db_week_add_normal", event, LunchEnum.W_NORMAL_ADD_1.value)
        line_bot.TextSendMessage(event, str(LunchEnum.W_NORMAL_ADD_1.value))

class db_week_add_vegan(Strategy):
    def action(self, event):
        line_bot.TextSendMessage(event, LunchEnum.W_VEGAN_ADD_1.value) 

class db_week_add_angel(Strategy):
    def action(self, event):
        line_bot.TextSendMessage(event, LunchEnum.W_ANGEL_ADD_1.value) 

class db_week_add_man(Strategy):
    def action(self, event):
        line_bot.TextSendMessage(event, LunchEnum.W_MAN_ADD_1.value) 

class db_month_add_normal(Strategy):
    def action(self, event):
        line_bot.TextSendMessage(event, LunchEnum.M_NORMAL_ADD_1.value) 

class db_month_add_vegan(Strategy):
    def action(self, event):
        line_bot.TextSendMessage(event, LunchEnum.M_VEGAN_ADD_1.value) 

class db_month_add_angel(Strategy):
    def action(self, event):
        line_bot.TextSendMessage(event, LunchEnum.M_ANGEL_ADD_1.value) 

class db_month_add_man(Strategy):
    def action(self, event):
        line_bot.TextSendMessage(event, LunchEnum.M_MAN_ADD_1.value) 

db_map ={
    LunchEnum.W_NORMAL_ADD_1 : db_week_add_normal,
    LunchEnum.W_VEGAN_ADD_1  : db_week_add_vegan,
    LunchEnum.W_ANGEL_ADD_1  : db_week_add_angel,
    LunchEnum.W_MAN_ADD_1    : db_week_add_man,
    LunchEnum.M_NORMAL_ADD_1 : db_month_add_normal,
    LunchEnum.M_VEGAN_ADD_1  : db_month_add_vegan,
    LunchEnum.M_ANGEL_ADD_1  : db_month_add_angel,
    LunchEnum.M_MAN_ADD_1    : db_month_add_man,
}


