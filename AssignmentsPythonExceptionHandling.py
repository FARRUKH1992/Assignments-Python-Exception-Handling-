# create wether forecast app that handles unexpected user input
# ask user to enter temps in Fahrenheit
# temp conversion to Celcius
# use else block 
# use finally executing this code



def fahrenheit_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius.
    """
    return (fahrenheit - 32) * 5 / 9

def main():
    try:
        # Task 1: Ask the user to enter the temperature in Fahrenheit
        fahrenheit_input = input("Enter the temperature in Fahrenheit: ")
        # Convert the input to a float
        fahrenheit = float(fahrenheit_input)
        
        # Task 2: Convert Fahrenheit to Celsius
        celsius = fahrenheit_to_celsius(fahrenheit)
    
    except ValueError:
        # Handle the case where conversion to float fails
        print("Invalid input. Please enter a numeric value.")
    
    else:
        # Task 3: Print the converted temperature in a user-friendly format
        print(f"{fahrenheit:.2f} degrees Fahrenheit is {celsius:.2f} degrees Celsius.")
    
    finally:
        # Task 4: Thank the user for using the application
        print("Thank you for using the weather forecast application.")

# Ensure that the main function runs when the script is executed
if __name__ == "__main__":
    main()