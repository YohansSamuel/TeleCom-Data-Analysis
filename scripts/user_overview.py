import pandas as pd

class UserOverview():
    def __init__(self,df) -> None:
        self.df = df 
    
    # get the top handsets
    def get_top_handsets(self,num):
        top_handsets = self.df['Handset Type'].value_counts().head(num)
        return top_handsets

    # get the top manufacturers
    def get_top_manufacturers(self,num):
        top_manufacturers = self.df['Handset Manufacturer'].value_counts().head(num)
        return top_manufacturers
    # get the top handsets per top manufacturers
    def get_top_handset_by_top_manufacturer(self,handset_num,manufacturer_num):
            top_3_manufacturers = self.get_top_manufacturers(manufacturer_num)

            manufacturers = self.df.groupby("Handset Manufacturer")

            for manufacturer in top_3_manufacturers.index:
                result = manufacturers.get_group(manufacturer).groupby("Handset Type")['MSISDN/Number'].nunique().nlargest(handset_num)
                print(f"****{ manufacturer} ****")
                print(result)