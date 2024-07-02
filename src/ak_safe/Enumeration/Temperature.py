from typing import Literal

from ak_safe.utils.logger import log

eTemperature_dict: dict = {
    0:'NotApplicable',
    1:'F',
    2:'C'
}

class __ETemperature:
    def __init__(self, data: dict) -> None:
        self.__temperature = data
        
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
            log.warning(f'Error occured when calling `__ETemperature Call`:{str(e)}\n'
                            f'Unexpected value value={value}. Expected {self.__temperature.keys()} or {self.__temperature.values()}')
    
    @property
    def __reverse(self) -> dict:
        return {y:x for x, y in self.__temperature.items()}
    
    @property
    def list(self) -> dict[str]:
        return self.__temperature
    
eTemperature = __ETemperature(data = eTemperature_dict)