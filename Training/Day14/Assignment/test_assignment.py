"""
test the conditions for factorial, prime number and area of circle with passign wrong paramters as 0
a) factorial by passing 4 and 0
b) prime number by passing 31, 17, 0
c) Area of a circle passing 4 , 0
"""

import testmath
import pytest
 
def test_factorial():
    assert testmath.calculate_factorial(4) == 24
    assert testmath.calculate_factorial(0) == 1
    with pytest.raises(ValueError):
        testmath.calculate_factorial(-1)
   
def test_prime():
    assert testmath.check_prime(31) == True
    assert testmath.check_prime(17) == True
    assert testmath.check_prime(0) == False
   
def test_area_of_circle():
    assert testmath.calculate_area_of_circle(0) == 0.0
    assert testmath.calculate_area_of_circle(4) == 50.26548245743669
   