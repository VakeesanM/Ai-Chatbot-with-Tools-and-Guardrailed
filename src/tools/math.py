from langchain_core.tools import tool


@tool
def add(num1, num2):
    """Adds two numbers together and returns their sum"""
    return num1 + num2

@tool
def multiply(num1, num2):
    """Multiplies two numbers together and return their produce"""
    return num1 * num2


@tool
def divide(dividend, divisor):
    """Divides the dividend by divisor and return the quotient"""
    try: 
        ans = dividend / divisor
        return ans
    except ZeroDivisionError as e:
        return f"Can't divide {dividend} by 0."

@tool
def subtract(num1, num2):
    """Subtracts num1 from num2 and returns the answer"""
    return num2 - num1

@tool
def power(number, power):
    """Returns the product of inputed number to the inputed power"""
    return number ** power

@tool
def root(number, root_power):
    """Returns the product of inputed number to the inputed root"""
    return number ** (1/power)