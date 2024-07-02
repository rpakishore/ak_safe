from typing import Literal

from ak_safe.utils.logger import log

__eForce: dict = {
    0:'NotApplicable',
    1:'lb',
    2:'kip',
    3:'N',
    4:'kN',
    5:'kgf',
    6:'tonf'
}

class __EForce:
    def __init__(self, data: dict) -> None:
        self.__Force = data
        
    def __str__(self) -> str:
        "eForce Enumeration. See oAPI documentation"
    
    def __call__(self, value: str|Literal[0,1,2]):
        try:
            if isinstance(value, str):
                if value.isdigit():
                    return self.__Force[int(value)]
                else:
                    return self.__reverse[value.strip()]
            else:
                return self.__Force[int(value)]
        
        except Exception as e:
            log.warning(f'Error occured when calling `__EForce Call`:{str(e)}\n'
                            f'Unexpected value value={value}. Expected {self.__Force.keys()} or {self.__Force.values()}')
    
    @property
    def __reverse(self) -> dict:
        return {y:x for x, y in self.__Force.items()}
    
    @property
    def list(self) -> dict[str]:
        return self.__Force
    
eForce = __EForce(data = __eForce)