from typing import Literal

__eTemperature: dict = {
    0:'NotApplicable',
    1:'F',
    2:'C'
}

class __ETemperature:
    def __init__(self, __temperature: dict) -> None:
        self.__temperature = __temperature
        
    def __str__(self) -> str:
        "eTemperature Enumeration. See oAPI documentation"
    
    def __call__(self, value: str|Literal[0,1,2]):
        try:
            if isinstance(value, str):
                if value.isdigit():
                    return self.__temperature[int(value)]
                else:
                    return self.__reverse[value.strip()]
            else:
                return self.__temperature[int(value)]
        
        except Exception as e:
            AssertionError(f'Error occured when calling `__ETemperature Call`:{str(e)}\n'
                            f'Unexpected value value={value}. Expected {self.__temperature.keys()} or {self.__temperature.values()}')
    
    @property
    def __reverse(self) -> dict:
        return {y:x for x, y in self.__temperature.items()}
    
    @property
    def list(self) -> dict[str]:
        return self.__temperature
    
eTemperature = __ETemperature(__temperature = __eTemperature)