from typing import Literal

from ak_safe.utils.logger import log

__eUnit: dict = {
    1 : 'lb_in_F',
    2 : 'lb_ft_F',
    3 : 'kip_in_F',
    4 : 'kip_ft_F',
    5 : 'kN_mm_C',
    6 : 'kN_m_C',
    7 : 'kgf_mm_C',
    8 : 'kgf_m_C',
    9 : 'N_mm_C',
    10 : 'N_m_C',
    11 : 'Ton_mm_C',
    12 : 'Ton_m_C',
    13 : 'kN_cm_C',
    14 : 'kgf_cm_C',
    15 : 'N_cm_C',
    16 : 'Ton_cm_C',
}

class __EUnits:
    def __init__(self, data: dict) -> None:
        self.__units = data
        
    def __str__(self) -> str:
        "eUnits Enumeration. See oAPI documentation"
    
    @property
    def list(self) -> dict[str]:
        return self.__units
    
    def filter(self, 
                force: str|None = None, distance: str|None = None, 
                temp: str|None = None) -> dict[str]:
        assert force is not None and distance is not None and temp is not None, 'Define atleast 1 of `force`, `distance` or `temp`'
        _filtered = self.__units.copy()
        if force:
            assert force.casefold() in (x.casefold() for x in self.__forces), f'Unexpected value force={force}. Expected: {self.__forces}'
            _filtered = {{x:y for x, y in _filtered.items() if f"{force.casefold()}_" in y.lower()}}
        if distance:
            assert distance.casefold() in (x.casefold() for x in self.__distances), f'Unexpected value force={distance}. Expected: {self.__distances}'
            _filtered = {{x:y for x, y in _filtered.items() if f"_{distance.casefold()}_" in y.lower()}}
        if temp:
            assert temp.casefold() in (x.casefold() for x in self.__temps), f'Unexpected value force={temp}. Expected: {self.__temps}'
            _filtered = {{x:y for x, y in _filtered.items() if f"_{temp.casefold()}" in y.lower()}}
        return _filtered
    
    @property
    def __forces(self) -> tuple[str]:
        return {x.split('_')[0] for x in self.__units.values()}
    
    @property
    def __distances(self) -> tuple[str]:
        return {x.split('_')[1] for x in self.__units.values()}
    
    @property
    def __temps(self) -> tuple[str]:
        return {x.split('_')[2] for x in self.__units.values()}

    def __call__(self, value: str|Literal[0,1,2]):
        try:
            if isinstance(value, str):
                if value.isdigit():
                    return self.__units[int(value)]
                else:
                    return self.__reverse[value.strip()]
            else:
                return self.__units[int(value)]
        
        except Exception as e:
            log.warning(f'Error occured when calling `__EUnits Call`:{str(e)}\n'
                            f'Unexpected value value={value}. Expected {self.__units.keys()} or {self.__units.values()}')
    
    @property
    def __reverse(self) -> dict:
        return {y:x for x, y in self.__units.items()}
    
eUnits = __EUnits(data = __eUnit)