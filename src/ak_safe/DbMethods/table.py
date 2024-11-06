from abc import ABC, abstractmethod, abstractproperty
from functools import cached_property, lru_cache
from pathlib import Path

import forallpeople as si
import pandas as pd

si.environment("structural")


class _Db(ABC):
    @abstractmethod
    def load_table(self, name: str) -> pd.DataFrame:
        """Load db table and return as pandas dataframe with forallpeople units"""
        pass

    @property
    @abstractmethod
    def tables(self) -> pd.DataFrame:
        """Returns list of available tables"""
        pass

    def _apply_units_to_table(self, table: pd.DataFrame) -> pd.DataFrame:
        for i in range(len(table.columns)):
            table.iloc[1:, i] = table.iloc[1:, i] * self.__get_factor(table.iloc[0, i])
        return table.iloc[1:, :].reset_index(drop=True)

    @staticmethod
    def __get_factor(unit):
        """Converts Unit from Database Table to forallpeople units"""
        if str(unit) == "nan":
            return 1
        try:
            units = unit.split("-")
            factor = 1
            for each in units:
                factor = factor * getattr(si, each)
            return factor
        except Exception as e:
            print(e)
            return 1


class ExcelDb(_Db):
    def __init__(self, xlsx: Path) -> None:
        assert xlsx.exists(), f"File {xlsx} does not exist"
        self.xlsx: Path = xlsx

    def load_table(self, name: str) -> pd.DataFrame:
        """Load database table from xlsx file

        Returns:
            pd.DataFrame: 2D table with data in forallpeople format
        """
        assert name in self.tables, f"Table {name} does not exist"
        df = pd.read_excel(
            self.xlsx,
            header=1,
            converters={"Unique Name": str, "ages": str},
            sheet_name=name,
        )
        return self._apply_units_to_table(df)

    @cached_property
    def tables(self) -> list[str]:
        """Returns list of tables in xlsx file"""
        return [str(sheet) for sheet in pd.ExcelFile(self.xlsx).sheet_names]


class SafeDb(_Db):
    def __init__(self, SafeObject) -> None:
        # self.__SafeObject = SafeObject
        # self.__SapModel = SafeObject.SapModel
        self.DB = SafeObject.SapModel.DatabaseTables

    def load_table(self, name: str) -> pd.DataFrame:
        raise Exception("Feature not implemented")

    @cached_property
    def tables(self) -> list[str]:
        return self.DB.GetAvailableTables()[2]
