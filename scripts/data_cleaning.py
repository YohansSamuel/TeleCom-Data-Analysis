import pandas as pd
import numpy as np;

class DataCleaning:
    def __init__(self, df):
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

    def drop_column_with_many_null_values(self)-> pd.DataFrame:
        '''
        drop list of columns which contain more than 30% of null values and 
        returns a dataframe
        '''
        df_size = self.df.shape[0]
        
        columns_list = self.df.columns
        many_null_columns = []
        
        for column in columns_list:
            null_per_column = self.df[column].isnull().sum()
            percentage = round((null_per_column / df_size) * 100 , 2)
            
            if(percentage > 30):
                many_null_columns.append(column)
        
        print(many_null_columns)
        self.df.drop(many_null_columns, axis=1, inplace=True)
        return self.df

    def remove_duplicates(self) -> pd.DataFrame:
        """
        Returns a DataFrame where duplicate rows are removed
        Parameters
        ----------
        None

        Returns
        -------
        pd.DataFrame
        """
        removables = self.df[self.df.duplicated()].index
        self.df.drop(index=removables,inplace=True) # self.df.drop(index=removables,axis=0,inplace=True)
        return self.df

    def convert_to_datetime(self, df):
        """
        convert start and end column to datetime
        """

        df['Start'] = pd.to_datetime(df['Start'])
        df['End'] = pd.to_datetime(df['End'])

        return df

    def fill_numerical_column(self, column):
        '''
        Fill numerical null values with column median
        '''
 
        for col in column:
            self.df[col] = self.df[col].fillna(self.df[col].median())
         
        return self.df

    def fill_categorical_column(self, column):
        '''
        Fill categorical null values with column Mode
        '''
 
        for col in column:
            mode = self.df[col].mode()[0]
            self.df[col] = self.df[col].fillna(mode)
        
        return self.df

    def save_cleaned_data(self, name: str):
        """
        The objects dataframe gets saved with the specified name 
        Parameters
        ----------
        name:
            Type: str

        Returns
        -------
        None
        """
        try:
            self.df.to_csv(name)

        except:
            print("Failed to save data")

    def fix_outlier(df, column):
        df[column] = np.where(df[column] > df[column].quantile(0.95), df[column].mode(),df[column])
        return df[column]

    