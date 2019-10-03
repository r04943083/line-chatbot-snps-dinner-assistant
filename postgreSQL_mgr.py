from singleton_decorator import singleton
import os
import psycopg2
import sql_cmd

from line_bot_mgr import LineBotMgr
line_bot = LineBotMgr()
@singleton
class PostgreSQLMgr:
    def __init__(self):
        user = str(os.getenv('DB_USER'))
        password = str(os.getenv('DB_PASSWORD'))
        host = str(os.getenv('DB_HOST'))
        port = str(os.getenv('DB_PORT'))
        database = str(os.getenv('DB_DATABASE'))
        self.__connection = psycopg2.connect(user = user, password = password, host = host, 
                                            port = port, database = database)
        self.__cursor = self.__connection.cursor()
        print("PostgreSQLMgr INIT")
        print("PostgreSQLMgr _connection", self.__connection)
        print("PostgreSQLMgr _cursor", self.__cursor)

    def create_table(self, table_name):
        try:
            self.__cursor.execute(sql_cmd.sql_create_table(table_name))
            self.__connection.commit()
        except (Exception, psycopg2.DatabaseError) as error :
            print ("Error while creating PostgreSQL table", error)

    def get_table(self, table_name):
        self.__cursor.execute(sql_cmd.sql_select_table(table_name))
        return self.__cursor.fetchall()
    
    def get_table_size(self, table_name):
        return len(self.get_table(table_name))

    def insert_record(self, table_name, event, normal, vegan, angel, man, box_type):
        existing_data = self.get_data_by_user_id(table_name, event)
        if existing_data:
            self.update_existing_data(table_name, event, box_type)
            pass
        else:
            s = sql_cmd.sql_insert_data(table_name)
            #group_id = event.source.groupId
            index = self.get_table_size(table_name) + 1
            user_id = event.source.user_id
            profile = line_bot.line_bot_api.get_profile(user_id)
            user_name = profile.display_name
            print ("insert_record: ", s)
            self.__cursor.execute(s, (index, user_id, user_name, normal, vegan, angel, man, "1F"))
            self.__connection.commit()
    
    def get_data_by_user_id(self, table_name, event):
        s = sql_cmd.sql_select_table_by_user_id(table_name)
        self.__cursor.execute(s, (event.source.user_id,))
        return self.__cursor.fetchall()

    def update_existing_data(self, table_name, event, box_type):
        s = sql_cmd.sql_update_data(table_name, box_type)
        self.__cursor.execute(s, (event.source.user_id,))

        pass

    def delete_table(self, table_name):
        self.__cursor.execute(sql_cmd.sql_delete_table(table_name))
        self.__connection.commit()

    def print_table(self, table_name):
        records = self.get_table(table_name)
        s = ""
        for row in records:
            s = s + str(row) + "\n"
        return s 

