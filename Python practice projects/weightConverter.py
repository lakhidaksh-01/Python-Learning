# Python Weight Converter

def weightconverter():
    weight=float(input("Enter the weight (in decimal):"))
    unit = input("In kilograms or pounds (K or L): ").strip().upper()


    if unit=="K":
        weight=weight * 2.205
        unit="Lbs"
        print(f"Your weight is {round(weight,3)} {unit}")
    elif unit=="L":
        weight=weight / 2.205
        unit="Kgs"
        print(f"Your weight is {round(weight,3)} {unit}")
    else:
        print(f"{unit} this is invaild")
        
    weightconverter()
    



if __name__ == "__main__":
    weightconverter()