from psycopg2 import sql

def sql_create_table(table_name):
    return sql.SQL('''CREATE TABLE IF NOT EXISTS {} ( 
                        index integer PRIMARY KEY,
                        user_id text NOT NULL,
                        user_name text NOT NULL,
                        normal_box integer,
                        vegan_box integer,
                        angel_box integer,
                        man_box integer,
                        place text
                );''').format(sql.Identifier(table_name))


def sql_select_table(table_name):
    return sql.SQL("SELECT * FROM {}").format(sql.Identifier(table_name))

def sql_select_table_by_user_id(table_name):
    return sql.SQL("SELECT * FROM {} WHERE user_id = %s") \
                .format(sql.Identifier(table_name))

def sql_insert_data(table_name):
    return sql.SQL(
                '''INSERT INTO {} (
                    index, 
                    user_id, 
                    user_name, 
                    normal_box,
                    vegan_box, 
                    angel_box, 
                    man_box,
                    place) 
                    VALUES ( %s, %s, %s, %s, %s, %s, %s, %s)'''
                ).format(sql.Identifier(table_name))

def sql_update_data(table_name, box_type):
    return sql.SQL(
                '''UPDATE {} SET {} = {} + 1
                   WHERE user_id = %s'''
        ).format(sql.Identifier(table_name), 
            sql.Identifier(box_type),
            sql.Identifier(box_type))

def sql_delete_table(table_name):
    return sql.SQL("DROP TABLE IF EXISTS {}").format(sql.Identifier(table_name))
