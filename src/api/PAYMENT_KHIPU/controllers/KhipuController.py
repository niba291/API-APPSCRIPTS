# -*- coding: utf-8 -*-
# IMPORT ========================================================================================================================
from src.utils.status                                       import HTTP_200_OK, HTTP_400_BAD_REQUEST
from flask                                                  import Blueprint, jsonify, request
from src.api.APPSCRIPTS.models.AppScriptsModel              import AppScripts
from src.api.PAYMENT_KHIPU.models.KhipuModel                import Khipu

# BLUEPRINT =====================================================================================================================
payment_khipu                                               = Blueprint("payment_khipu", __name__)
# MIDDLEWARE ====================================================================================================================
TOKEN_API                                                   = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjRkYmRlOTQ1LThiNDMtNDhkNi1hYjhhLTlhODQ1ZTBhM2VkNCIsInJvbCI6W10sIm1vZHVsZXMiOltdfQ.cuA_n0p9LwVaBmUN0-8HjegZuuTIISCVkNvSXvq8GEU"
# ROUTE =========================================================================================================================
@payment_khipu.route("/payments/khipu/create/<string:id>", methods = ["POST"])
def payment_khipu_create(id : str = "") -> dict:
    """
        Return data from khipu
        Return      : dict
    """
    getIntegration      = AppScripts().request({
        "token"         : TOKEN_API,
        "action"        : "getJsonFile",
        "data"          : {
            "id"        : id,
        }
    })
    obj                 = Khipu()
    if not (obj.module in getIntegration):
        return {
            "error"     : True,
            "response"  : f"{obj.module} Key not found."
        }
    data                = getIntegration[obj.module]
    response            = obj.createPayment({**data, **request.json})
    
    return jsonify(response), HTTP_200_OK if ("error" in response) and not response["error"] else HTTP_400_BAD_REQUEST
    
@payment_khipu.route("/payments/khipu/get/<string:id>", methods = ["POST"])
def payment_khipu_get(id : str = "") -> dict:
    """
        Add element in sheet
        Return      : dict
    """

    getIntegration      = AppScripts().request({
        "token"         : TOKEN_API,
        "action"        : "getJsonFile",
        "data"          : {
            "id"        : id,
        }
    })

    obj                 = Khipu()
    if not (obj.module in getIntegration):
        return {
            "error"     : True,
            "response"  : f"{obj.module} Key not found."
        }
    data                = getIntegration[obj.module]
    response            = obj.getPayment(data, request.json["id"])

    return jsonify(response), HTTP_200_OK if ("error" in response) and not response["error"] else HTTP_400_BAD_REQUEST
