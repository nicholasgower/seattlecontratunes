# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 21:53:49 2023

@author: Nicholas
"""

import pandas
import sqlite3
import uuid
from datetime import datetime
import numpy as np

md5_hash=uuid.UUID("239512be226a8b7578b1578be5ee7bee") #Used to deterministically generate UUIDs


medley_categories=[
    "Contra",
    "Unplayed Contra",
    "Waltz",
    "Polka",
    "English Ceildh",
    "Northumbrian Pipe and Fiddle",
    "Another Stage Set",
    "Celebration Stage Set"
    ]


triggerRows=["MEDLEYS I WISH I'D PLAYED AT GIGS (but never got around to bringing in to a band) ",
 "WALTZES REGULARLY USED",
 "OPENING POLKAS",
 "ENGLISH CEILIDH MEDLEYS ",
 "NORTHUMBRIAN PIPE AND FIDDLE TUNES ",
 "ANOTHER STAGE SET ",
 "STAGE SET celebrating my 25th YEAR PERFORMING AT FOLKLIFE ",
 ]
#type_memory_options=["Unplayed Contra",]

db=sqlite3.connect("db.sqlite3")
#cur=db.Cursor()

#cur.execute("DELETE * FROM song_directory_medley")

sheet=pandas.read_excel("Medleys.xlsx")
medley_categories_index=0

columns=pandas.read_sql("SELECT * FROM song_directory_medley LIMIT 1",db).columns

database_columns=['Tune1', 'Tune2', 'Tune3', 'earliest_play', 'latest_play', 'bands', 'keys', 'comments', 'additional_notes', 'medley_type']
spreadsheet_columns=['Tune 1', 'Tune 2', 'Tune 3  ', 'Earliest (##)', 'Latest (##)', 'Band or Bands', 'Keys', 'Comments', 'Additional Comments']
      

output=[]
for i,row in enumerate(sheet.iloc):
    
    
    if row["Tune 1"] in triggerRows:
        medley_categories_index+=1
    elif row["Tune 1"] is np.nan or type(row["Earliest (##)"]) is float or row["Earliest (##)"][0]=="#":
        pass
    else:
        new_row={}
        
        for j,column in enumerate(spreadsheet_columns):
            new_row[database_columns[j]]=row[column]
        
        
        
        
        #new_row["id"]=uuid.uuid3(md5_hash,"{}{}{}{}{}".format(new_row["Tune1"],new_row["Tune2"],new_row["Tune3"],new_row["earliest_play"],new_row["bands"],new_row["keys"])).int >> 65
        new_row["medley_type"]=medley_categories[medley_categories_index]
        new_row["latest_play"]=None
        new_row["earliest_play"]=None
        if type(new_row["latest_play"]) is str and "_" in new_row["latest_play"]:
            try:
                early=new_row["earliest_play"].split("_")
                year=early[0]
                #month=early[6:8]
                new_row["earliest_play"]=datetime(int(year),1,1).strftime('%Y-%m-%d %H:%M:%S')
            except ValueError:
                pass
        if type(new_row["latest_play"]) is str and "_" in new_row["latest_play"]:
            try:
                latest=new_row["latest_play"].split("_")
                year=latest[0]
                #month=latest[6:8]
                new_row["latest_play"]=datetime(int(year),1,1).strftime('%Y-%m-%d %H:%M:%S')
            except ValueError:
                pass
        for item in ["Tune2","Tune3","additional_notes","comments","keys","bands"]:
            if type(new_row[item]) is not str:
                new_row[item]=""
        
            
        #new_row=[]
        
        output.append(new_row)
        pass
        
output_frame=pandas.DataFrame(output,columns=columns)        
        
output_frame.to_sql("song_directory_medley",db,if_exists="append",index=False)
        

