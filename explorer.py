class DataExplorer:
    @staticmethod
    def report(df):
        rows, cols = df.shape
        print("\n=== BASIC DATA EXPLORATION ===")
        print(f"Total rows: {rows}")
        print(f"Total columns: {cols}")
        print("\nColumn data types:")
        print(df.dtypes)
        print("\nMissing values per column:")
        print(df.isna().sum())
