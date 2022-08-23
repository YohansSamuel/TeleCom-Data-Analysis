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