import os
import sys
from pathlib import Path
import clr

clr.AddReference("System.Runtime.InteropServices")
from System.Runtime.InteropServices import Marshal

if Path(R'C:\Program Files\Computers and Structures\SAFE 21').is_dir():
    clr.AddReference(R'C:\Program Files\Computers and Structures\SAFE 21\SAFEv1.dll')
elif Path(R'C:\Program Files\Computers and Structures\SAFE 20').is_dir():
    clr.AddReference(R'C:\Program Files\Computers and Structures\SAFE 20\SAFEv1.dll')
else:
    raise Exception('SAFE Folder not found')
from SAFEv1 import cOAPI, cHelper, Helper

from ak_safe.utils.logger import log

class SAFEWrapper:
    def __init__(self, program_path: str|Path|None = None) -> None:
        self.program_path: str|None=  str(Path(str(program_path)).absolute()) if program_path else None
        self.mySAFEObject = attach_to_model()
        self.SapModel = self.mySAFEObject.SapModel
    
    def __str__(self) -> str:
        return 'Instance of SAFEWrapper.".'
    
    def __repr__(self) -> str:
        return 'SAFEWrapper()'
    
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
        return self.mySAFEObject.GetOAPIVersionNumber()
    
    def hide(self) -> bool:
        """Hides the Sap2000 application. 
        When hidden it is not visible on the screen or on the Windows task bar.
        """
        try:
            self.mySAFEObject.Hide() 
            return True
        except Exception as e:
            log.critical(str(e))
            return False
    
    def unhide(self) -> bool:
        """Unhides the Sap2000 application. 
        When hidden it is not visible on the screen or on the Windows task bar.
        """
        try:
            self.mySAFEObject.Unhide()
            return True
        except Exception as e:
            log.critical(str(e))
            return False
    
    @property
    def ishidden(self) -> bool:
        return self.mySAFEObject.Visible()
    
    @property
    def version(self) -> str:
        return self.SapModel.GetVersion()[0]
        
def attach_to_model():
    helper = cHelper(Helper())
    return cOAPI(helper.GetObject("CSI.SAFE.API.ETABSObject"))