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

# get the top manufacturers
def get_top_manufacturers(df,num):
    top_manufacturers = df['Handset Manufacturer'].value_counts().head(num)
    return top_manufacturers

def get_top_handset_by_top_manufacturer(self):
        top_3_manufacturers = self.get_top_manufacturers(3)

        manufacturers = self.df.groupby("Handset Manufacturer")

        for manufacturer in top_3_manufacturers.index:
            result = manufacturers.get_group(manufacturer).groupby("Handset Type")['MSISDN/Number'].nunique().nlargest(5)
            print(f"****{ manufacturer} ****")
            print(result)
            print() 