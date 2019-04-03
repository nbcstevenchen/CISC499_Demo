import platform
import logging
import time
import sys
class const:
    class ConstError(TypeError):
        pass

    def __setattr__(self,name,value):
        if name in self.__dict__:
            raise self.ConstError("Can't rebind const(%s)"%name)
        self.__dict__[name] = value

sys.modules[__name__] = const()
sysname = platform.system()



const.INI_DB_CONFIG_USER = 'root'
const.INI_DB_CONFIG_PASSWORD = 'chenyuhao1996'
const.INI_DB_CONFIG_HOST = 'localhost'
const.INI_DB_CONFIG_PORT = '3306'
const.INI_DB_CONFIG_DATABASE = 'cisc499'
