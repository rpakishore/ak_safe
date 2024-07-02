from .logger import log
from functools import wraps

def safe_exec(func):
    """Wrapper for running SAFE oAPI calls. 
    Will check for return response from SAP. 
    If not '0' will log and exit gracefully."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            log.debug(f'Running `{func.__qualname__}` with args: "{args}" and kwargs: "{kwargs}"')
            ret = func(*args, **kwargs)
            log.debug(f'Response received: {ret}')
            if isinstance(ret, list) or isinstance(ret, tuple):
                assert ret[-1] == 0, f'{ret=} indicates failure to complete command from {func.__qualname__}'
                if len(ret) == 2:
                    return ret[0]
                return ret[:-1]
            else:
                assert ret == 0, f'{ret=} indicates failure to complete command from {func.__qualname__}'
                return ret
        except Exception as e:
            log.critical(e)
    return wrapper

class MasterClass:
    def __init__(self, SafeObject) -> None:
        self.SafeObject = SafeObject
        self.SapModel = self.SafeObject.SapModel
        print(f'`{self.__class__.__name__}` instance initialized.')
    
    def __str__(self) -> str:
        return f'Instance of `MasterClass`. Holds collection of functions'
    
    def __repr__(self) -> str:
        return self.__str__()
    
    def __del__(self) -> None:
        try:
            self.SafeObject = None
            self.SapModel = None
        except Exception as e:
            log.warning(msg=f'Exception faced when deleting {self.__class__.__name__}\n{e}')