from config import OUTPUT_PATH

class DataSaver:
    @staticmethod
    def save(df):
        df.to_csv(OUTPUT_PATH, index=False)
        print(f"\nSaved updated file to: {OUTPUT_PATH}")
