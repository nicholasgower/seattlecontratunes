# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 11:11:24 2023

@author: Nicholas
"""

import docx
import pathlib
import bs4
import os
from music21.converter import Converter
from music21.lily.translate import LilypondConverter
from music21.tempo import MetronomeMark


def getText(doc):
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)

path=pathlib.Path("abctunes")

music_conv=Converter

for file in path.rglob("*.docx"):
    #print(file)
    
    doc=docx.Document(str(file))
    
    text=getText(doc)
    
    if "X:" in text:
        index=text.find("X:")
        
        truncated_text=text[index:]
        music_abc=text[index:]
        music=Converter()
        try:
            music.parseData(music_abc)
            
        except:
            pass
        folder_dir=pathlib.Path("easy_viewing",file.with_suffix(""))
        midi_output=pathlib.Path(folder_dir,pathlib.Path(file.stem).with_suffix(".midi"))
        wav_output=pathlib.Path(folder_dir,pathlib.Path(file.stem).with_suffix(".wav"))
        pdf_output=pathlib.Path(folder_dir,pathlib.Path(file.stem).with_suffix(".xml"))
        #docx_output=pathlib.Path("easy_viewing",file.with_suffix(""),pathlib.Path(file.stem).with_suffix(".docx"))
        """
        try:
            music.stream[1][1].append(MetronomeMark("fast",180))
        except AttributeError:
            music.stream[1][5].append(MetronomeMark("fast",180))
            
        """
        try:
            folder_dir.mkdir(parents=True)
        except FileExistsError:
            pass
        
        #musimusi
        
        print(midi_output)
        print(pdf_output)
        try:
            music.stream.write("midi",str(midi_output))
            
        except:
            pass
        
        #music.stream.write("mp3",str(wav_output))
        music.stream.write("xml",str(pdf_output))
        #print("\n"+music_abc)
        