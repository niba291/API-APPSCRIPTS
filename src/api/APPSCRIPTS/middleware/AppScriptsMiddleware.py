# -*- coding: utf-8 -*-
# IMPORT ========================================================================================================================
from flask                                                  import request, jsonify

def app_scripts_middleware() -> dict:
    if "Authorization" not in request.headers:
        return jsonify({
            "error"     : True,
            "response"  : "Not exist 'Authorization' element in header"
        })