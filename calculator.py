import pandas as pd

class Calculator:
    @staticmethod
    def add_metrics(df: pd.DataFrame) -> pd.DataFrame:
        # Average of Length1, Length2, Length3
        df["AvgLength"] = df[["Length1","Length2","Length3"]].mean(axis=1)
        # Percentage of Height to Weight
        df["PctHeightToWeight"] = (df["Height"] / df["Weight"]) * 100.0
        return df

    @staticmethod
    def calc_from_input(weight, length1, length2, length3, height):
        avg_len = (length1 + length2 + length3) / 3.0
        pct = (height / weight) * 100.0 if weight != 0 else None
        return avg_len, pct
