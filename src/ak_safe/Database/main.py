from ak_safe.utils.logger import log

from .Tables import Table

class Database:
    def __init__(self, SafeObject) -> None:
        self.__SafeObject = SafeObject
        self.__SapModel = SafeObject.SapModel
        self.DB = SafeObject.SapModel.DatabaseTables
    
    def __str__(self) -> str:
        return f'`{self.__class__.__name__}` Instance'
    
    def __repr__(self) -> str:
        return self.__str__()
    
    def __del__(self) -> None:
        try:
            self.__SafeObject = None
            self.__SapModel = None
            self.DB = None
        except Exception as e:
            log.warning(msg=f'Exception faced when deleting {self.__class__.__name__}\n{e}')
            
    def get_table(self, TableKey: str) -> Table:
        assert TableKey in self.DB.GetAllTables()[2]
        assert TableKey in self.DB.GetAvailableTables()[2]
        return Table(db=self.DB, TableKey=TableKey)