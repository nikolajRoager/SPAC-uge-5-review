import pandas as pd 
from pandas import DataFrame


class Excel:
    df: DataFrame = None
    
    def __init__(self, file_path: str) -> None:
        self.df = pd.read_excel(file_path)