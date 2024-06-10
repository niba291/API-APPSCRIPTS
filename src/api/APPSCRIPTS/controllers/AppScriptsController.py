# -*- coding: utf-8 -*-
# IMPORT ========================================================================================================================
from src.utils.status                                       import HTTP_200_OK, HTTP_400_BAD_REQUEST
from flask                                                  import Blueprint, jsonify, request
from src.api.APPSCRIPTS.models.AppScriptsModel              import AppScripts
# BLUEPRINT =====================================================================================================================
app_scripts                                                 = Blueprint("app_scripts", __name__)
# MIDDLEWARE ====================================================================================================================
TOKEN_API                                                   = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjRkYmRlOTQ1LThiNDMtNDhkNi1hYjhhLTlhODQ1ZTBhM2VkNCIsInJvbCI6W10sIm1vZHVsZXMiOltdfQ.cuA_n0p9LwVaBmUN0-8HjegZuuTIISCVkNvSXvq8GEU"
# ROUTE =========================================================================================================================
@app_scripts.route("/googlesheet/get/<string:id>", methods = ["POST"])
def app_scripts_googlesheet_get(id : str = "") -> dict:
    """
        Return data google sheet
        Return      : dict
    """
    response            = AppScripts().request({
        "token"         : TOKEN_API,
        "action"        : "get",
        "data"          : {
            "id"        : id,
            "schema"    : request.json
        }
    })
    return jsonify(response), HTTP_200_OK if not ("error" in response) else HTTP_400_BAD_REQUEST
    
@app_scripts.route("/googlesheet/create/<string:id>", methods = ["POST"])
def app_scripts_googlesheet_add(id : str = "") -> dict:
    """
        Add element in sheet
        Return      : dict
    """
    response            = AppScripts().request({
        "token"         : TOKEN_API,
        "action"        : "create",
        "data"          : {
            "id"        : id,
            "schema"    : request.json
        }
    })
    return jsonify(response), HTTP_200_OK if not ("error" in response) else HTTP_400_BAD_REQUEST

@app_scripts.route("/googlesheet/update/<string:id>", methods = ["POST"])
def app_scripts_googlesheet_update(id : str = "") -> dict:
    """
        Update element in sheet
        Return      : dict
    """
    response            = AppScripts().request({
        "token"         : TOKEN_API,
        "action"        : "update",
        "data"          : {
            "id"        : id,
            "schema"    : request.json
        }
    })
    return jsonify(response), HTTP_200_OK if not ("error" in response) else HTTP_400_BAD_REQUEST

@app_scripts.route("/googlesheet/delete/<string:id>", methods = ["POST"])
def app_scripts_googlesheet_delete(id : str = "") -> dict:
    """
        Delete element in sheet
        Return      : dict
    """
    response            = AppScripts().request({
        "token"         : TOKEN_API,
        "action"        : "remove",
        "data"          : {
            "id"        : id,
            "schema"    : request.json
        }
    })
    return jsonify(response), HTTP_200_OK if not ("error" in response) else HTTP_400_BAD_REQUEST

@app_scripts.route("/googledrive/<string:id>", methods = ["POST"])
def app_scripts_googledrive_get(id : str = "") -> dict:
    """
        Return data google drive
        Return      : dict
    """
    response            = AppScripts().request({
        "token"         : TOKEN_API,
        "action"        : "getJsonFile",
        "data"          : {
            "id"        : id,
        }
    })
    return jsonify(response), HTTP_200_OK if not ("error" in response) else HTTP_400_BAD_REQUEST