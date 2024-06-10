# -*- coding: utf-8 -*-
# IMPORT ========================================================================================================================
from datetime                                                           import datetime
import requests
import re
# CALSS =========================================================================================================================
class BaseMixin:

    # id              = db.mapped_column(db.Integer, primary_key = True, sort_order = -1)
    # enabled         = db.Column(db.Boolean, default = True, nullable = False)
    # created_at      = db.Column(db.DateTime, default = datetime.now, nullable = False)
    # updated_at      = db.Column(db.TIMESTAMP, default = datetime.now, onupdate = datetime.now, nullable = False)
    # count           = 0
    # limitLoop       = 99999999999    

    @classmethod
    def request(self, args) -> dict:
        """
            Request in url
            Params      : [
                args    : paramerters class
            ]
            Return      : dict
        """
        print(args)
        response        = requests.post(
            self.__API_URL__,
            json        = args
        )
        print(response.text)
        return {}
        # return response.json()

    @classmethod
    def create(self, args) -> dict:
        """
            Create object in databases
            Params      : [
                args    : paramerters class
            ]
            Return      : dict
        """
        return {}

    @classmethod
    def update(self, args) -> dict:
        """
            Update object in databases
            Params      : [
                args    : paramerters class
            ]
            Return      : dict
        """
        return {}
        
    @classmethod
    def get(self, args) -> dict:
        """
            get objects in databases
            Params      : [
                args    : paramerters class
            ]
            Return      : dict
        """
        return {}

    @classmethod
    def delete(self, args) -> dict:
        """
            Delete or disabled object in databases
            Params      : [
                args    : paramerters class
            ]
            Return      : dict
        """
        return {}

    @property
    def serialize(self) -> dict:
        """
            Return data serialize
            Return : dict
        """
        return {}