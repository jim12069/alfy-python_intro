## BASIC CALCULATOR ##

def calc_math_expression(num1, num2, operator):

    # Boolean desginating type
    num1_is_int = isinstance(num1, int)
    num1_is_float = isinstance(num1, float)
    num2_is_int = isinstance(num2, int)
    num2_is_float = isinstance(num2, float)
    operator_is_real_operator = operator in ["+", "-", "*", ":"]

    # Input validation
    if (not((num1_is_int or num1_is_float) and (num2_is_int or num2_is_float) and operator_is_real_operator and num2 != 0)):
        return None

    # Calculation based on which operator was used
    else:
        match operator:
            case "+":
                return num1 + num2
            case "-":
                return num1 - num2
            case "*":
                return num1 * num2
            case ":":
                return num1 / num2
            case _:
                return "error"


def calc_math_expression_from_str(str_input):
    # 'str_input' is a string containing two spaces; e.g., "3 + 52"
    
    # Split string into the string representations of the two operands and operator
    argument_list = str_input.split()
    
    # Convert strings into appropriate type
    if "." in argument_list[0]:
        num_1st = float(argument_list[0])
    else:
        num_1st = int(argument_list[0])

    if "." in argument_list[2]:
        num_2nd = float(argument_list[2])
    else:
        num_2nd = int(argument_list[2])
    
    symbol = argument_list[1]
    
    # Do the calculation
    return calc_math_expression(num_1st, num_2nd, symbol)
    

## LARGEST AND SMALLEST NUMBERS ##

def find_largest_and_smallest_numbers(num1=0.0, num2=0.0, num3=0.0):
    num_list = [num1, num2, num3]
    return (max(num_list), min(num_list))


## QUADRATIC EQUATION SOLVER ##

def quadratic_equation_solver(a, b, c):
    root = (b ** 2) - (4 * a * c)
    if root < 0:
        return (None, None)
    elif root == 0:
        solution1 = (-b) / (2 * a)
        return (solution1, None)
    else:
        solution1 = ((-b) + ((b ** 2) - (4 * a * c)) ** 0.5) / (2 * a)
        solution2 = ((-b) - ((b ** 2) - (4 * a * c)) ** 0.5) / (2 * a)
        return (solution1, solution2)

def quadratic_equation_solver_from_user_input():
    abc_str = input("Provide a, b, and c as a single string: ")
    abc_list = abc_str.split()
    a = abc_list[0]
    b = abc_list[1]
    c = abc_list[2]
    return quadratic_equation_solver(a, b, c)


## TEMPERATURE CHECKER ##

def temp_checker(min_temp, temp_1, temp_2, temp_3):
    temp_list = [temp_1, temp_2, temp_3]
    count_warmer_than_min = 0

    for temp in temp_list:
        if temp > min_temp:
            count_warmer_than_min += 1

    if count_warmer_than_min >= 2:
        return True
    else:
        return False
