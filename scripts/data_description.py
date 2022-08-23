import pandas as pd;

class DataDescription():
    def __init__(self, df):
        self.df = df.copy()

    def df_columns_list(self):
        '''
        Return Column list of the Dataframe
        '''
        return self.df.columns.to_list()

    def df_detail_info(self):
        '''
        Display the detail of the DataFrame information
        '''

        print(self.df.info())

    def df_null_counts(self):
        '''
        Display Null Counts of each column
        '''

        print(self.df.isnull().sum())