#!python3
# -*- coding: utf-8 -*-
import base64
from salesforce_api import Salesforce

def session():
    client = Salesforce(username= "renato.fagaraz@greenpeace.org",
                        password= base64.b64decode("SG9tZXJAMzEyMjAzMjc=").decode("utf-8"),
                        security_token= "L0turnKP1tOU2sx3Nl19XA40",
                        is_sandbox=False)
    return client