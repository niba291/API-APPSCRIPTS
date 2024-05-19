# -*- coding: utf-8 -*-
# IMPORT ==============================================================================================
from src.utils.env                                                              import ENV
from src.utils.baseMixin                                                        import BaseMixin
# CALSS ===============================================================================================
class AppScripts(BaseMixin):
    # URL =============================================================================================
    __API_URL__             = ENV["API_URL"].format(ID_APP_SCRIPTS = ENV["ID_APP_SCRIPTS"])
    # ATRIBUTTES ======================================================================================
    """Attributes or column in table"""

    def __init__(self, id = 0):
        """
            Model constructor set data
            args            : [
            ]
        """        

    @property
    def module(self) -> str:
        """
            Return project code 
            Return : str
        """
        return "APP-APP-001"