# -*- coding: utf-8 -*-
# IMPORT ========================================================================================================================
from flask                                                  import Flask
from flask_cors                                             import CORS

from src.api.APPSCRIPTS.controllers.AppScriptsController    import app_scripts
from src.api.PAYMENT_KHIPU.controllers.KhipuController      import payment_khipu
# APP ============================================================================================================================
app                                                         = Flask(__name__)
app.json.sort_keys                                          = False

CORS(app)

app.register_blueprint(app_scripts)
app.register_blueprint(payment_khipu)

if __name__ == "__main__": 
    app.run(debug = True)