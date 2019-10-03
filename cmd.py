from abc import ABC, abstractmethod
from cmd_parser import CmdParser, LunchEnum, DBManualEnum, CmdEnum
from line_bot_mgr import LineBotMgr
from postgreSQL_mgr import PostgreSQLMgr

line_bot = LineBotMgr()
sql_mgr = PostgreSQLMgr()

TABLE_NAME = 'SNPS_10_W1'
TABLE_W_NAME = 'SNPS_W'
TABLE_M_NAME = 'SNPS_M'

class Strategy(ABC):
    @abstractmethod
    def action(self, event):
        pass

class db_week_add_normal(Strategy):
    def action(self, event):
        update_table(event, TABLE_W_NAME, 1, 0, 0, 0, 'normal_box')

class db_week_add_vegan(Strategy):
    def action(self, event):
        update_table(event, TABLE_W_NAME, 0, 1, 0, 0, 'vegan_box')

class db_week_add_angel(Strategy):
    def action(self, event):
        update_table(event, TABLE_W_NAME, 0, 0, 1, 0, 'angel_box') 

class db_week_add_man(Strategy):
    def action(self, event):
        update_table(event, TABLE_W_NAME, 0, 0, 0, 1, 'man_box') 

class db_month_add_normal(Strategy):
    def action(self, event):
        update_table(event, TABLE_M_NAME, 1, 0, 0, 0, 'normal_box')

class db_month_add_vegan(Strategy):
    def action(self, event):
        update_table(event, TABLE_M_NAME, 0, 1, 0, 0, 'vegan_box')

class db_month_add_angel(Strategy):
    def action(self, event):
        update_table(event, TABLE_M_NAME, 0, 0, 1, 0, 'angel_box')

class db_month_add_man(Strategy):
    def action(self, event):
        update_table(event, TABLE_M_NAME, 0, 0, 0, 1, 'man_box')  

def update_table(event, table_name, nornal, vegan, angel, man, box_type):
    sql_mgr.create_table(table_name)
    sql_mgr.insert_record(table_name, event, nornal, vegan, angel, man, box_type)
    s = sql_mgr.print_table(table_name)
    line_bot.TextSendMessage(event, s)

class db_delete_table(Strategy):
     def action(self, event):
        sql_mgr.delete_table(TABLE_W_NAME)
        sql_mgr.delete_table(TABLE_M_NAME)
        line_bot.TextSendMessage(event, DBManualEnum.BD_DELETE.value)

class db_hello(Strategy):
     def action(self, event):
        line_bot.TextSendMessage(event, "妳好 我是可愛的助手小迪 <3")

class bd_print_all_command(Strategy):
     def action(self, event):
        cmds = "訂餐指令: "   + str(LunchEnum.list()) + '\n' + \
               "資料庫指令: " + str(DBManualEnum.list()) + '\n' + \
               "系統指令: "   + str(CmdEnum.list())
        line_bot.TextSendMessage(event, cmds)

db_map ={
    LunchEnum.W_NORMAL_ADD_1 : db_week_add_normal,
    LunchEnum.W_VEGAN_ADD_1  : db_week_add_vegan,
    LunchEnum.W_ANGEL_ADD_1  : db_week_add_angel,
    LunchEnum.W_MAN_ADD_1    : db_week_add_man,
    LunchEnum.M_NORMAL_ADD_1 : db_month_add_normal,
    LunchEnum.M_VEGAN_ADD_1  : db_month_add_vegan,
    LunchEnum.M_ANGEL_ADD_1  : db_month_add_angel,
    LunchEnum.M_MAN_ADD_1    : db_month_add_man,
    DBManualEnum.BD_DELETE   : db_delete_table,
    CmdEnum.CMD_HELLO        : db_hello,
    CmdEnum.CMD_PRINT_ALL    : bd_print_all_command,
}


