import pandas as pd

from ak_safe.utils.logger import log
from ak_safe.utils.definitions import safe_exec

class Table:
    def __init__(self, db, TableKey: str) -> None:
        self.TableKey: str = TableKey
        self.DB = db
        
    def __str__(self) -> str:
        return f'Database Table for "{self.TableKey}"'
    
    def read(self) -> pd.DataFrame:
        log.debug(f'Reading Table Data for "{self.TableKey}"')
        response = self.DB.GetTableForDisplayArray (TableKey=self.TableKey, GroupName="")
        _data = {}
        headings = response[2]
        row_len = len(headings)
        table_vals = response[4]
        for i_h, heading in enumerate(headings):
            _data[heading] = []
            for i_r in range(i_h, len(table_vals), row_len):
                _data[heading].append(table_vals[i_r])
                
        return pd.DataFrame(_data)
    
    @safe_exec
    def write(self, df: pd.DataFrame):
        log.info(f'Writing Table Data to "{self.TableKey}"')
        log.debug(df)
        self.DB.SetTableForEditingArray(
            TableKey=self.TableKey, 
            FieldsKeysIncluded=list(df.columns), 
            NumberRecords=len(df), 
            TableData=df.values.flatten().tolist()
            )
        self.DB.ApplyEditedTables()
    
    @safe_exec
    def info(self) -> pd.DataFrame:
        log.debug(f'Reading Table Info for "{self.TableKey}"')
        res = self.DB.GetAllFieldsInTable(TableKey='Program Control')
        heading = ('FieldKey', 'FieldName ', 'Description ', 'UnitsString', 'IsImportable')
        _data = {x:y for x, y in zip(heading, res[2:-1])}
        return pd.DataFrame(_data)
    