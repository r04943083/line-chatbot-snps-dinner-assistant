from psycopg2 import sql

def sql_create_table(table_name):
    sql_cmd = sql.SQL(
                '''CREATE TABLE IF NOT EXISTS {} ( 
                        index integer PRIMARY KEY,
                        user_id text NOT NULL,
                        user_name text NOT NULL,
                        week_nornal_number integer,
                        week_vegan_number integer,
                        week_angel_number integer,
                        week_man_number integer,
                        place text
                );''').format(sql.Identifier(table_name))
    return sql_cmd

def sql_select_table(table_name):
    sql_cmd = sql.SQL("SELECT * FROM {}").format(sql.Identifier(table_name))
    return sql_cmd

def sql_insert_data(table_name):
    return sql.SQL(
                '''INSERT INTO {} (
                    index, 
                    user_id, 
                    user_name, 
                    week_nornal_number,
                    week_vegan_number, 
                    week_angel_number, 
                    week_man_number,
                    place) 
                    VALUES ( %s, %s, %s, %s, %s, %s, %s, %s)'''
                ).format(sql.Identifier(table_name))

def sql_delete_table(table_name):
    sql_cmd = sql.SQL("DROP TABLE IF EXISTS {}").format(sql.Identifier(table_name))
    return sql_cmd