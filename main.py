from dataloader import DataLoader
from explorer import DataExplorer
from calculator import Calculator
from saver import DataSaver
from user_input import UserInput

def main():
    # 1) Load
    df = DataLoader.load()

    # 2) Explore
    DataExplorer.report(df)

    # 3) Calculate & append metrics
    df = Calculator.add_metrics(df)

    # 4) Save back to file
    DataSaver.save(df)

    # 5) Accept user input and display per-fish metrics
    rec = UserInput.prompt()
    avg, pct = Calculator.calc_from_input(rec["Weight"], rec["Length1"], rec["Length2"], rec["Length3"], rec["Height"])
    print("\n=== RESULTS FOR NEW FISH ===")
    print(f"Species: {rec['Species']}")
    print(f"Average Length: {avg:.2f}")
    if pct is None:
        print("Height/Weight (%): N/A (weight=0)")
    else:
        print(f"Height/Weight (%): {pct:.2f}%")

if __name__ == "__main__":
    main()
