# temp_conversion_tool.py

# Global 
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
CELSIUS_TO_FAHRENHEIT_ADDITION = 32
FAHRENHEIT_TO_CELSIUS_SUBTRACTION = 32

def convert_to_celsius(fahrenheit):
    
    return (fahrenheit - FAHRENHEIT_TO_CELSIUS_SUBTRACTION) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + CELSIUS_TO_FAHRENHEIT_ADDITION

def main():
    try:
        
        temp = float(input("Enter the temperature to convert: "))
        
        
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        
        
        if unit == 'C':
            converted_temp = convert_to_fahrenheit(temp)
            print(f"{temp}°C is {converted_temp}°F")
        elif unit == 'F':
            converted_temp = convert_to_celsius(temp)
            print(f"{temp}°F is {converted_temp}°C")
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

print(convert_to_fahrenheit)

if __name__ == "__main__":
    main()

