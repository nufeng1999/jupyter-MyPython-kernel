## %file:src/overwritefile.py
from typing import Dict, Tuple, Sequence,List
from .ISpecialID import IStag,IDtag,IBtag,ITag
import os
class MyOverwritefile(IBtag):
    kobj=None
    def getName(self) -> str:
        # self.kobj._write_to_stdout("setKernelobj setKernelobj setKernelobj\n")
        
        return 'MyOverwritefile'
    def getAuthor(self) -> str:
        return 'Author'
    def getIntroduction(self) -> str:
        return 'MyOverwritefile'
    def getPriority(self)->int:
        return 0
    def getExcludeID(self)->List[str]:
        return []
    def getIDBptag(self) -> List[str]:
        return ['overwritefile']
    def setKernelobj(self,obj):
        self.kobj=obj
        # self.kobj._write_to_stdout("setKernelobj setKernelobj setKernelobj\n")
        return
    def on_shutdown(self, restart):
        return
    def on_IBpCodescanning(self,magics,line) -> str:
        # self.kobj._write_to_stdout(line+" on_ISpCodescanning\n")
        self.kobj.addkey2dict(magics,'overwritefile')
        magics['overwritefile'] = ['true']
        return ''
    ##在代码预处理前扫描代码时调用     
    def on_Codescanning(self,magics,code)->Tuple[bool,str]:
        pass
        return False,code
    ##生成文件时调用
    def on_before_buildfile(self,code,magics)->Tuple[bool,str]:
        return False,''
    def on_after_buildfile(self,returncode,srcfile,magics)->bool:
        return False
    def on_before_compile(self,code,magics)->Tuple[bool,str]:
        return False,''
    def on_after_compile(self,returncode,binfile,magics)->bool:
        return False
    def on_before_exec(self,code,magics)->Tuple[bool,str]:
        return False,''
    def on_after_exec(self,returncode,srcfile,magics)->bool:
        return False
    def on_after_completion(self,returncode,execfile,magics)->bool:
        return False

    
