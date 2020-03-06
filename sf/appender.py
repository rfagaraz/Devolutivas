#!python3
# -*- coding: utf-8 -*-

from glob import glob
import pandas as pd
from io import StringIO # p/ corrigir CSVs com separador ';'

def appender(Directory):
    df = pd.DataFrame()
    for files in glob(Directory):
        extension = files.split('.',2)[1]
        if extension == "csv":
            snippet = pd.read_csv(StringIO(''.join(i.replace(';', ',') for i in open(files))))
        elif extension == "xlsx":
            snippet = pd.read_excel(files)
        df = df.append(snippet, ignore_index=True).copy()
    print('Append finalizado')
    return df
       

 