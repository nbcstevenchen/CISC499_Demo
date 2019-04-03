import logging
import mysql.connector
import const
import uuid
import time


class DataBase:
    def __init__(self):
        self.mconn = mysql.connector.connect(user=const.INI_DB_CONFIG_USER, passwd=const.INI_DB_CONFIG_PASSWORD, host=const.INI_DB_CONFIG_HOST, db=const.INI_DB_CONFIG_DATABASE)
        try:
            self.mconn.autocommit = True
        except Exception as e:
            logging.error(e.__str__())

    def disconnect_database(self):
        if self.mconn:
            self.mconn.close()

    def sql_command(self, name, text):
        current_time = int(time.strftime("%Y%m%d")) +100
        cursor = self.mconn.cursor(buffered=False)
        cursor.execute('select count(name) from conversation where name = "%s"' % name)
        for number in cursor:
            if number[0] == 0 :
                id = str(uuid.uuid4()).replace('-', '')
                insert = 'insert ignore into conversation(id, name, number_time, text) values(' \
                    '%s, %s,CURDATE(), %s )'
                cursor.execute(insert, (id, name, text))
            else:
                cursor.execute('select text from conversation where name = "%s"' % name)
                for txt in cursor:
                    oldtext = txt[0]
                cursor.execute('select number_time from conversation where name = "%s"' % name)
                for sub in cursor:
                    if sub[0]+3 > current_time:
                        newtext = oldtext + ' ' + text
                        cursor.execute('UPDATE conversation SET text = "%s", number_time = "%s" where name = "%s"'%(newtext, current_time, name))
                    else:
                        cursor.execute('UPDATE conversation SET text = "%s", number_time = "%s" where name = "%s"' % (
                        text, current_time, name))


