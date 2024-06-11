# -*- coding: utf-8 -*-
# IMPORT ==============================================================================================
from src.utils.env                                                              import ENV
from src.utils.baseMixin                                                        import BaseMixin
from pykhipu.client                                                             import Client
# CALSS ===============================================================================================
class Khipu(BaseMixin):
    # URL =============================================================================================
    __API_URL__             = ENV["API_URL"].format(ID_APP_SCRIPTS = ENV["ID_APP_SCRIPTS"])
    __RECEIVER_ID__         = "receiver_id"
    __SECRET_ID__           = "secret_id"
    # ATRIBUTTES ======================================================================================
    """Attributes or column in table"""

    def __init__(self):
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
        return "PAY-KPU-001"
    
    @classmethod
    def createPayment(self, data = {}) -> dict:
        if not ( self.__RECEIVER_ID__ in data and self.__SECRET_ID__ in data ):
            return {
                "error"     : True,
                "response"  : f"{self.__RECEIVER_ID__} or {self.__SECRET_ID__} not found."
            }

        currency            = "CLP" if not ("currency" in data) else data["currency"]
        subject             = "subject" if not ("subject" in data) else data["subject"]
        amount              = 0 if not ("amount" in data) else data["amount"]
        client              = Client(data[self.__RECEIVER_ID__], data[self.__SECRET_ID__])
        
        if "currency" in data : del data["currency"]
        if "subject" in data : del data["subject"]
        if "amount" in data : del data["amount"]
        del data[self.__RECEIVER_ID__]
        del data[self.__SECRET_ID__]

        createPayment       = client.payments.post(subject, currency, amount, **data)

        return {
            "error"     : False,
            "response"  : {
                "url"   : createPayment.payment_url,
                "id"    : createPayment.payment_id
            }
        }

    @classmethod
    def getPayment(self, data = {}, payment_id = "" ) -> dict:

        if not ( self.__RECEIVER_ID__ in data and self.__SECRET_ID__ in data ):
            return {
                "error"     : True,
                "response"  : f"{self.__RECEIVER_ID__} or {self.__SECRET_ID__} not found."
            }
        
        client          = Client(data[self.__RECEIVER_ID__], data[self.__SECRET_ID__])
        getPaymentData  = client.payments.get_id(payment_id)

        return {
            "error"     : False,
            "response"  : {
                "status"    : getPaymentData.status,
                "currency"  : getPaymentData.currency
            }
        }
