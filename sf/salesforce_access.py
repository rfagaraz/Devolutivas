#!python3
# -*- coding: utf-8 -*-
import base64
from salesforce_api import Salesforce

def session():
    client = Salesforce(username= "",
                        password= base64.b64decode("").decode("utf-8"),
                        security_token= "",
                        is_sandbox=False)
    return client
