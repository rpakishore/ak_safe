from typing import Literal

__eItemType: dict = {
    0:'Objects',
    1:'Group',
    2:'SelectedObjects',
}

class __EItemType:
    def __init__(self, __ItemType: dict) -> None:
        self.__ItemType = __ItemType
        
    def __str__(self) -> str:
        "eItemType Enumeration. See oAPI documentation"
    
    def __call__(self, value: str|Literal[0,1,2]):
        try:
            if isinstance(value, str):
                if value.isdigit():
                    return self.__ItemType[int(value)]
                else:
                    return self.__reverse[value.strip()]
            else:
                return self.__ItemType[int(value)]
        
        except Exception as e:
            AssertionError(f'Error occured when calling `__EItemType Call`:{str(e)}\n'
                            f'Unexpected value value={value}. Expected {self.__ItemType.keys()} or {self.__ItemType.values()}')
    
    @property
    def __reverse(self) -> dict:
        return {y:x for x, y in self.__ItemType.items()}
    
    @property
    def list(self) -> dict[str]:
        return self.__ItemType
    
eItemType = __EItemType(__ItemType = __eItemType)