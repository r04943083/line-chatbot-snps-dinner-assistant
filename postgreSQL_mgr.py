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
        self._connection = psycopg2.connect(user = user, password = password, host = host, 
                                            port = port, database = database)
        self._cursor = self._connection.cursor()
        print("PostgreSQLMgr INIT")
        print("PostgreSQLMgr _connection", self._connection)
        print("PostgreSQLMgr _cursor", self._cursor)

    def create_table(self, table_name):
        try:
            self._cursor.execute(sql_cmd.sql_create_table(table_name))
            self._connection.commit()
        except (Exception, psycopg2.DatabaseError) as error :
            print ("Error while creating PostgreSQL table", error)

    def get_table(self, table_name):
        self._cursor.execute(sql_cmd.sql_select_table(table_name))
        return self._cursor.fetchall()
    
    def get_table_size(self, table_name):
        return len(self.get_table(table_name))

    def insert_record(self, table_name, event, normal, vegan, angel, man):
        s = sql_cmd.sql_insert_data(table_name)
        #group_id = event.source.groupId
        index = self.get_table_size(table_name) + 1
        user_id = event.source.user_id
        profile = line_bot.line_bot_api.get_profile(user_id)
        user_name = profile.display_name
        print ("insert_record: ", s)
        self._cursor.execute(s, (index, user_id, user_name, normal, vegan, angel, man, "1F"))
        self._connection.commit()

    def delete_table(self, table_name):
        self._cursor.execute(sql_cmd.sql_delete_table(table_name))
        self._connection.commit()

    def print_table(self, table_name):
        records = self.get_table(table_name)
        s = ""
        for row in records:
            s = s + str(row) + "\n"
            print(row)
        return s

