# Python Temperature Converter
def celsius_to_fahrenheit(temp):
    print(f"{round((temp * 9/5) + 32, 1)}°F")

def celsius_to_kelvin(temp):
    print(f"{round(temp + 273.15, 1)}K")

def fahrenheit_to_celsius(temp):
    print(f"{round((temp - 32) * 5/9, 1)}°C")

def fahrenheit_to_kelvin(temp):
    print(f"{round(((temp - 32) * 5/9) + 273.15, 1)}K")

def kelvin_to_celsius(temp):
    print(f"{round(temp - 273.15, 1)}°C")

def kelvin_to_fahrenheit(temp):
    print(f"{round(((temp - 273.15) * 9/5) + 32, 1)}°F")



def tempcalculator():
    print("Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Celsius to Kelvin")
    print("3. Fahrenheit to Celsius")
    print("4. Fahrenheit to Kelvin")
    print("5. Kelvin to Celsius")
    print("6. Kelvin to Fahrenheit")
    
    choice=int(input("Enter your choice (1-6):"))
    temp=float(input("Enter the temperature value:"))
    
    if choice==1:
        celsius_to_fahrenheit(temp)
    elif choice==2:
        celsius_to_kelvin(temp)
    elif choice==3:
        fahrenheit_to_celsius(temp)
    elif choice==4:
        fahrenheit_to_kelvin(temp)
    elif choice==5:
        kelvin_to_celsius(temp)
    elif choice==6:
        kelvin_to_fahrenheit(temp)
    else:
        print(f"{choice} is invailid enter the vaild number between 1-6")

    tempcalculator()    

if __name__ == "__main__":
    tempcalculator()