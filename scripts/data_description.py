import pandas as pd;

class DataDescription():
    def __init__(self, df):
        self.df = df.copy()

    def get_columns_list(self):
        '''
        Return Column list of the Dataframe
        '''
        return self.df.columns.to_list()