from singleton_decorator import singleton
from cmd_parser import CmdParser

@singleton
class CmdMgr:
    def __init__(self, event=None, func=None):
        self.event = event
        self.parser = CmdParser()  
        self.execute = types.MethodType(func, self)
        
    def execute(self):
        pass
    
    def exe_str_cmd(self, event, text):
          _cmd = self.parser(text)
          

        
        

        