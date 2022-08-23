import pandas as pd;

class DataDescription():
    def __init__(self, df):
        self.df = df

    def df_columns_list(self):
        '''
        Return Column list of the DataFrame
        '''
        return self.df.columns.to_list()

    def df_detail_info(self):
        '''
        Display the detail of the DataFrame
        '''

        print(self.df.info())

    def df_null_counts(self):
        '''
        Display null counts of each column
        '''

        print(self.df.isnull().sum())

    def df_skewness(self):
        '''
        Display skewness of each column
        '''
        print(self.df.skew())

    def df_head(self,top = 5):
        '''
        Display top 5(also can accept from user) rows
        '''
        print(self.df.head(top))

    def df_size(self):
        '''
            Displays the size of the dataframe
        '''
        value = self.df.shape
        print(
            f"The DataFrame containes \n {value[0]} rows \n {value[1]} columns.")
        return value