from lib2to3.pgen2.pgen import DFAState
from turtle import pd


import pandas as pd

class UserOverview():
    def __init__(self) -> None:
        self.df = df 
    
# get the top handsets
def get_top_handsets(df,num):
    top_handsets = df['Handset Type'].value_counts().head(num)
    return top_handsets