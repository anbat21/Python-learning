import pandas as pd
from config import CSV_PATH

class DataLoader:
    @staticmethod
    def load() -> pd.DataFrame:
        df = pd.read_csv(CSV_PATH)
        return df
