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

    def df_null_column_percentage(self):
        '''
        Display toal null percentage of the columns
        '''

        num_rows, num_columns = self.df.shape
        df_size = num_rows * num_columns
        
        null_size = (self.df.isnull().sum()).sum()
        percentage = round((null_size / df_size) * 100, 2)
        print(f"The dataset contains { percentage }% missing values.")

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
        print(f"The DataFrame containes  {value[0]} rows and {value[1]} columns")
        # print(self.df.shape)