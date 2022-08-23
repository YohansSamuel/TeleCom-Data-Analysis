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

    