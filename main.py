# from .bmiText import * 
from bmiInput import bmiInput 
from bmiText import bmiText 
from bmicharts import bmicharts

a = input("czy chcesz wgrać dane z pliku dane_raw.txt? (y/n)")
if(a == "y"):
  bmiText()
a = input("czy chcesz wprowadzić dodatkowe pomiary? (y/n)")
if(a == "y"):
  bmiInput()
bmicharts()