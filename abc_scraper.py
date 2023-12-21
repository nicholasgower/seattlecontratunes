# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 14:32:54 2023

@author: Nicholas
"""
import pandas as pd
from pathlib import Path
from docx import Document
from os.path import exists
import sqlite3
import datetime
from uuid import uuid4
def getDocxText(filename):
    doc = Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)




cols=["name","abc","description"]


db=sqlite3.connect("db.sqlite3")
df=pd.DataFrame()

pathList=Path("song_directory/internal_scripts/abctunes").rglob("*.docx")

database_proto=[]
#for file in pathList:
#    print(file)
for file in pathList:
    #print(file)
    #print(file.suffix)
    
    #print(file.parent)
    
    if ".rtf" not in file.stem:
        name=str(file.stem)
        text=""
        description=""
        if ".docx" in file.suffix:
            text=getDocxText(file)
            
            
        elif ".abc" in file.suffix:
            text_file=open(file,'r')
            text=text_file.readall()
            
            text_file.close()
        description_location= Path(file.parent,file.stem+".rtf.docx")
        if exists(description_location):
           
            description=getDocxText(description_location)
                
            
            
        print(text)
        print(description)
        database_proto.append({"name":name,"abc":text,"description":description,"uploader_id":3,
                               
                               
                               "uploaded_time":datetime.datetime.now().isoformat(),"url_code":str(uuid4()).replace("-","")})

df=pd.DataFrame(database_proto)


df.to_sql("song_directory_song",db,if_exists="append",index=False)
    
    #if 
    
    
db.close()