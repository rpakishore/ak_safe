import sys
from pathlib import Path
import comtypes.client

from ak_safe.utils.logger import log

__known_filepaths: list[str] = [
    r"C:\Program Files\Computers and Structures\SAFE 21\SAFE.exe"
]

class SAFEWrapper:
    def __init__(self, attach_to_instance: bool, program_path: str|Path|None = None) -> None:
        self.program_path: str|None=  str(Path(str(program_path)).absolute()) if program_path else None
        self.SafeObject = get_SafeObject(attach_to_instance=attach_to_instance, program_path=program_path)
        self.SapModel = self.SafeObject.SapModel

    def __str__(self) -> str:
        return 'Instance of SAFEWrapper.'
    
    def __del__(self) -> None:
        try:
            pass
        except Exception as e:
            log.error(e.__str__())
    
    def save(self, savepath: str|Path|None = None) -> bool:
        """Saves SAP model to the `savepath`.
        If no save path is provided, saves to the default path
        """
        try:
            if savepath:
                assert self.SapModel.File.Save(savepath) == 0
                log.info(f'Save success. Saved to {savepath}')
            else:
                assert self.SapModel.File.Save() == 0
                log.info('Save success. Saved to defaultpath')
            return True
        except Exception as e:
            log.critical(e)
            return False
    
    @property
    def api_version(self) -> str:
        """Retrieves the API version implemented by SAP2000."""
        return self.SafeObject.GetOAPIVersionNumber()
    
    def hide(self, status: bool=False) -> bool:
        """Hides the SAFE application. 
        When hidden it is not visible on the screen or on the Windows task bar.
        """
        try:
            if status:
                self.SafeObject.Hide() 
            else:
                self.SafeObject.Unhide()
            return True
        except Exception as e:
            log.critical(str(e))
            return False
        
    @property
    def ishidden(self) -> bool:
        return self.SafeObject.Visible()
    
    @property
    def version(self) -> str:
        return self.SapModel.GetVersion()[0]
        
def get_SafeObject(attach_to_instance: bool, program_path: str|Path|None = None, 
                    known_filepaths: list[str] = __known_filepaths):
    #create API helper object
    helper = (
        comtypes.client
        .CreateObject('SAFEv1.Helper')
        .QueryInterface(comtypes.gen.SAFEv1.cHelper)
        )
    
    if attach_to_instance:
        #attach to a running instance of SAFE
        try:
            #get the active SapObject
            SafeObject = helper.GetObject("CSI.SAFE.API.ETABSObject") 
            log.debug('Attached to existing Instance.')
            return SafeObject
        except (OSError, comtypes.COMError):
            log.error("No running instance of the program found or failed to attach.")
            sys.exit(-1)
        except Exception as e:
            log.error(str(e))
            sys.exit(-1)
            
    else:
        if program_path is None:
            for filepath in known_filepaths:
                if Path(filepath).is_file():
                    program_path = filepath
                    break
        
        assert program_path is not None, 'SAFE.exe file not found. Please pass the program_path to initialize instance'
    
        try:
            SafeObject = helper.CreateObject(program_path)
            SafeObject.ApplicationStart()
            SafeObject.SapModel.InitializeNewModel(6)   #initialize model
            log.debug(f'Created model from {program_path}.')
            return SafeObject
        except (OSError, comtypes.COMError):
            log.error("Cannot start a new instance of the program.")
            sys.exit(-1)
        except Exception as e:
            log.error(str(e))
            sys.exit(-1)


