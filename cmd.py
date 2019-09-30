from cmd_parser import CmdParser
from line_bot import LineBot

line_bot = LineBot()
line_bot_api = line_bot.line_bot_api

class Cmd:
    db_map ={
        W_NORMAL_ADD_1 = db_week_add_normal,
        W_VEGAN_ADD_1  = db_week_add_vegan,
        W_ANGEL_ADD_1  = db_week_add_angel,
        W_MAN_ADD_1    = db_week_add_man,
        M_NORMAL_ADD_1 = db_month_add_normal,
        M_VEGAN_ADD_1  = db_month_add_vegan,
        M_ANGEL_ADD_1  = db_month_add_angel,
        M_MAN_ADD_1    = db_month_add_man,
    }
    
    def __init__(self, event):
        self.event = event
        
    def db_week_add_normal:
        line_bot_api.TextSendMessage(event, W_NORMAL_ADD_1.value)
    
