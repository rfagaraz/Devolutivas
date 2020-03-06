#!python3
# -*- coding: utf-8 -*-

from sf.salesforce_access import session
from sf.appender import appender
from sf.validacao import validacao

client = session()
df = appender("C:\\Users\\rfagaraz\\Documents\\Devolutiva das Agências\\*.csv") # Diretório dos arquivos


for x in range(len(df)):

    mapeamentoCM = {
            "Contact_Details_Changed__c"         : validacao(df["Contact Details Changed"][x]) ,
            "s360aie__Last_Call_Period__c"       : df["Last Call Period"][x]                   ,
            "s360aie__Number_of_Call_Attempts__c": int(df["Number of Call Attempts"][x])       ,
            "s360aie__Outcome__c"                : df["Outcome"][x]                            ,
            "Payment_Details_Changed__c"         : validacao(df["Payment Details Changed"][x]) ,
            "s360aie__Queue_Status__c"           : df["Queue Status"][x]                       ,
            "s360aie__ResponseCode__c"           : df["Response Code"][x]
            }

    client.sobjects.CampaignMember.update(df['Campaign Member ID'][x], mapeamentoCM)
