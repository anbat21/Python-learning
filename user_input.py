class UserInput:
    @staticmethod
    def prompt():
        print("\n=== ENTER NEW FISH DATA ===")
        species = input("Species: ")
        weight = float(input("Weight: "))
        l1 = float(input("Length1: "))
        l2 = float(input("Length2: "))
        l3 = float(input("Length3: "))
        height = float(input("Height: "))
        width = float(input("Width: "))
        return {
            "Species": species,
            "Weight": weight,
            "Length1": l1,
            "Length2": l2,
            "Length3": l3,
            "Height": height,
            "Width": width
        }
