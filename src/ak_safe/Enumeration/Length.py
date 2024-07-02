from typing import Literal

__eLength: dict = {
    0:'NotApplicable',
    1:'inch',
    2:'ft',
    3:'micron',
    4:'mm',
    5:'cm',
    6:'m'
}


class __ELength:
    def __init__(self, __Length: dict) -> None:
        self.__Length = __Length
        
    def __str__(self) -> str:
        "eLength Enumeration. See oAPI documentation"
    
    def __call__(self, value: str|Literal[0,1,2]):
        try:
            if isinstance(value, str):
                if value.isdigit():
                    return self.__Length[int(value)]
                else:
                    return self.__reverse[value.strip()]
            else:
                return self.__Length[int(value)]
        
        except Exception as e:
            AssertionError(f'Error occured when calling `__ELength Call`:{str(e)}\n'
                            f'Unexpected value value={value}. Expected {self.__Length.keys()} or {self.__Length.values()}')
    
    @property
    def __reverse(self) -> dict:
        return {y:x for x, y in self.__Length.items()}
    
    @property
    def list(self) -> dict[str]:
        return self.__Length
    
eLength = __ELength(__Length = __eLength)