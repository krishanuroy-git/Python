def calculate_factorial(n):
       if n < 0:
           raise ValueError("Factorial is not defined for negative numbers.")
       elif n == 0:
           return 1
       else:
           factorial_value = 1
           for i in range(1, n + 1):
               factorial_value *= i
           return factorial_value
       
import math

def check_prime(number):
    if number <= 1:
        return False  # Numbers less than or equal to 1 are not prime
    if number == 2:
        return True   # 2 is the only even prime number
    if number % 2 == 0:
        return False  # Other even numbers are not prime

    # Check for divisibility from 3 up to the square root of the number
    # only checking odd numbers
    for i in range(3, int(math.sqrt(number)) + 1, 2):
        if number % i == 0:
            return False  # If divisible, it's not prime
    return True  # If no divisors found, it's prime

def calculate_area_of_circle(radius):
    """
    Calculates the area of a circle given its radius.

    Args:
        radius: The radius of the circle (a number).

    Returns:
        The area of the circle.
    """

    rad = float(radius) # Convert input to a floating-point number
    area = math.pi * radius ** 2  # Formula: π * r^2
    return area