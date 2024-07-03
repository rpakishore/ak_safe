from dataclasses import dataclass
from typing import Any

from ak_safe.Database.Tables import Table

@dataclass
class Point:
    UniqueName: str
    IsAutoPoint: bool
    IsSpecial: bool
    X: float
    Y: float
    Z: float
    GUID: str
    db: Any
    
    def __post_init__(self):
        self.__table = Table(db = self.db, TableKey='Point Object Connectivity')
        
    def update(self):
        df = self.__table.read()
        