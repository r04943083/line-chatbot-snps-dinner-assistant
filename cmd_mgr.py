import abc
from cmd import Strategy, db_map
from cmd_parser import CmdParser
from singleton_decorator import singleton

@singleton
class CmdMgr:
    def __init__(self, strategy = None):
        self._strategy = strategy
        self._parser = CmdParser() 
        
    def execute(self, event):
        print("CmdMgr > execute > event =>", event)
        self._strategy().action(event)
        
    
    def decode(self, event, text):
          _cmd = self._parser.decode(text)
          print("CmdMgr > decode > _cmd =>", _cmd)
          self._strategy = db_map[_cmd]
          print("CmdMgr > decode > _strategy =>", db_map[_cmd])
          self.execute(event)  
        

        