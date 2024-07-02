from pathlib import Path

from ak_safe.utils.definitions import MasterClass, safe_exec

class Model(MasterClass):
    def __init__(self, SafeObject) -> None:
        super().__init__(SafeObject=SafeObject)
    
    def __str__(self) -> str:
        return f'Instance of `Model` Class'
    
    @safe_exec
    def locked(self, status: bool):
        """Locks or unlocks the model

        Args:
            status (bool): item is True if the model is to be locked and False if it is to be unlocked. 
        """
        return self.SapModel.SetModelIsLocked(status)
    
    @safe_exec
    def islocked(self) -> bool:
        return self.SapModel.GetModelIsLocked()
    
    @safe_exec
    def open(self, filepath: str|Path): 
        """Opens an existing file.

        Args:
            filepath (str | Path): full path of a model file to be opened in the application.
        """
        return self.SapModel.File.OpenFile(filepath)