import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s', filename="calculator.log")

"""Simple Calculator
Author: Pedro van Code
Last update: 02.01.2024
Any comments welcome :)
"""

def main():

    print_info()
    logging.info("\nStart calculator.py\n")

    while count_again():

        user_input_list = get_user_input()        
        if not input_ok(user_input_list):
            handle_wrong_input()
            continue
            
        number1 = convert_input_to_float(user_input_list[0])
        number2 = convert_input_to_float(user_input_list[2])
        operation = user_input_list[1]
        logging.info(f"Number 1: {number1} Number 2: {number2} Operation: {operation}")

        if is_string(number1) or is_string(number2):
            handle_input_is_string()
            continue

        result = calculate(float(number1), 
                           str(operation), 
                           float(number2))
        print_results(result)


def print_info():
    """Prints simple info of supported operations."""
    print("\n--- calculator.py ---"
          "\nEnter first number, operation and second number."
          "\ndivided by space (for example 2 + 3)"
          "\nsupperted operations: + - / * %\n")


def count_again():
    """While loop checking if user wants to count (returns True) or quit (returns False)"""
    while True:
        answer = input("Continue? Enter y to count or q to quit? ")
        answer = answer.strip().lower()
        if answer == "q" or answer == "quit":
            print("Ok. Quit")
            logging.info(f"User answer {answer} - Exit program")
            return False
        elif answer == "y" or answer == "yes":
            print("\nOk. Lets count.\n")
            logging.info(f"User answer {answer} - Program continue")
            return True
        else:
            print("Wrong answer.")
            logging.warning(f"User answer {answer} - Not recognized")


def get_user_input():
    """Get input string from user and returns as a splitted array."""
    user_input_string = input("Enter operation: ")
    logging.info(f"User input string: {user_input_string}")
    return user_input_string.split()
     
     
def input_ok(array):
    return True if len(array) == 3 else False


def handle_wrong_input():
    print("Your input contains more or less than three elements. Try again")
    logging.error("Input contains more or less than three elements. Trying again")
        
        
def convert_input_to_float(input):
    """Converts entered decimals with ',' to floats with '.' if possible."""
    if ',' in input:
        splitted = input.split(',')
        if len(splitted) == 2:
            converted = float(splitted[0]+'.'+splitted[1])
            return converted
        else:
            return input
    else:
        return input
    
  
def is_string(input):
    """Checks if input is float (returns False), int (returns False) or string (returns True)."""
    try:
        input = float(input)
        logging.info(f"{input} is float")
        return False
    except ValueError:
        try:
            input = int(input)
            logging.info(f"{input} is integer")
            return False
        except ValueError:
            print(f"\nInput {input} is not a correct number. Looks like string.\n")
            logging.error(f"{input} is string")
            return True
        
        
def handle_input_is_string():
    logging.error("Input is string. Trying again")
    
              
def calculate(number1, operation, number2):
    """Making a calculation, depending on operation type. Returns result"""
    if operation == "+":
        result = number1 + number2
    elif operation == "-":
        result = number1 - number2
    elif operation == "*":
        result = number1 * number2
    elif operation == "/":
        result = number1 / number2
    elif operation == "%":
        result = number1 % number2
    else:
        result = str("Wrong. Operation not supported.")
        logging.warning(f"Operation: {operation} - not recognized")
        print_info()
    return result
    
    
def print_results(result):
    """Prints calculation results and log to file."""
    print(f"Result: {result}\n")
    logging.info(f"Result: {result}")


main()