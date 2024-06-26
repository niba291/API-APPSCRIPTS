# -*- coding: utf-8 -*-
# IMPORT ========================================================================================================================
import jwt
from src.utils.status                                       import HTTP_200_OK, HTTP_400_BAD_REQUEST
from flask                                                  import Blueprint, jsonify, request, current_app
from src.api.APPSCRIPTS.models.AppScriptsModel              import AppScripts
# BLUEPRINT =====================================================================================================================
app_scripts                                                 = Blueprint("app_scripts", __name__)
# VARIABLES =====================================================================================================================
HOST                                                        = ""
# MIDDLEWARE ====================================================================================================================
@app_scripts.before_request
def before_request():
    HOST                                                    = request.headers.get("Host", "").split(":")[0]
    HOST                                                    = "localhost" if HOST == "127.0.0.1" else HOST.split(".")[0]
    token                                                   = request.cookies.get("x-access-tokens", "")
    try:
        jwtDecode                                           = jwt.decode(token, current_app.config["SECRET_KEY"], algorithms=["HS256"])
    except jwt.exceptions.InvalidSignatureError:
        return jsonify({
            "error"     : True,
            "response"  : "Signature verification failed"
        }), 401

# ROUTE =========================================================================================================================
@app_scripts.route("/googlesheet/get/<string:id>", methods = ["POST"])
def app_scripts_googlesheet_get(id : str = "") -> dict:
    """
        Return data google sheet
        Return      : dict
    """
    response            = AppScripts().request({
        "token"         : HOST,
        "action"        : "get",
        "data"          : {
            "id"        : id,
            "schema"    : request.json
        }
    })
    # response = {}
    return jsonify(response), HTTP_200_OK if not ("error" in response) else HTTP_400_BAD_REQUEST
    
@app_scripts.route("/googlesheet/create/<string:id>", methods = ["POST"])
def app_scripts_googlesheet_add(id : str = "") -> dict:
    """
        Add element in sheet
        Return      : dict
    """
    response            = AppScripts().request({
        "token"         : HOST,
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
        "token"         : HOST,
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
        "token"         : HOST,
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
        "token"         : HOST,
        "action"        : "getJsonFile",
        "data"          : {
            "id"        : id,
        }
    })
    return jsonify(response), HTTP_200_OK if not ("error" in response) else HTTP_400_BAD_REQUEST