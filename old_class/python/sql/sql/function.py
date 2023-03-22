#%%
import pymysql

# def connect(conn,cur):
#     host_name = input('HOST:')
#     conn = pymysql.connect(host=host_name,
#                            user=user_name,
#                            password=password_str,
#                            db= db_name,
#                            charset='utf8')


class MysqlEditor:
    def __init__(self):

        host_name = input('HOST:')
        user_name = input('USER:')
        password_string = input('PASSWORD:')
        db_name = input('DATABASE:')
        
        try:
            self.conn = pymysql.connect(host=host_name,
                                user=user_name,
                                password=password_string,
                                db= db_name,
                                charset='utf8')
        except:
            print('잘못된 입력이 있습니다. 다시 입력하거라')
            self.__init__()
        
        self.cur = self.conn.cursor()
    
    def close(self):
        self.conn.close()

test = MysqlEditor()
# %%
