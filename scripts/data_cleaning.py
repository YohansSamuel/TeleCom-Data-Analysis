import pandas as pd
import numpy as np;

class DataCleaning:
    def __init__(self, df: pd.DataFrame) -> None:
        """
        Returns a DataCleaning Object with the passed DataFrame
        ----------
        df:
            Type: pd.DataFrame

        Returns
        -------
        None
        """
        self.df = df

    def remove_unwanted_columns(self, columns: list) -> pd.DataFrame:
        """
        Returns a DataFrame where the specified columns in the list are removed
        Parameters
        ----------
        columns:
            Type: list

        Returns
        -------
        pd.DataFrame
        """
        self.df.drop(columns, axis=1, inplace=True)
        return self.df

    def drop_column_with_many_null_values(self):
        '''
        Return List of Columns which contain more than 30% of null values
        '''
        df_size = self.df.shape[0]
        
        columns_list = self.df.columns
        many_null_columns = []
        
        for column in columns_list:
            null_per_column = self.df[column].isnull().sum()
            percentage = round((null_per_column / df_size) * 100 , 2)
            
            if(percentage > 30):
                many_null_columns.append(column)
        
        return many_null_columns