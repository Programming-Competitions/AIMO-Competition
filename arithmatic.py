from sympy import *
x, y, z = symbols('x y z')
init_printing(use_unicode=True)

import math

#Basic Arithmetic

def add(x, y):
  total = x + y
  return total

def subtract(x, y):
  total = x - y
  return total

def multiply(x, y):
  total = x * y
  return total

def divide(x, y):
  total = x / y
  return total

def exponent(x, y):
  total = x ** y
  return total

def percent(x, y):
  total = (x / y) * 100
  return total

def radical(x, y):
  total = x ** (1/y)
  return total

#Algebra

def solve_linear_equation(a, b):
  """Solves ax + b = 0 and returns x (None if a is zero)"""
  return -b / a if a else None

def solve_quadratic_equation(a, b, c):
  """Solves ax^2 + bx + c = 0 and returns solutions (x1, x2)"""
  discriminant = b**2 - 4 * a * c
  if discriminant < 0:
    return None
  elif discriminant == 0:
    return -b / (2 * a)
  else:
    root = math.sqrt(discriminant)
    x1 = (-b + root) / (2 * a)
    x2 = (-b - root) / (2 * a)
    return x1, x2

def slope_and_intercept(a, b):
  """Calculates slope (m) and y-intercept (b) of ax + b = y"""
  return a, b

def factorial(n):
  """Calculates n! (factorial)"""
  if n < 0:
    return None  # Factorial is not defined for negative numbers
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)

def gcd(a, b):
  """Calculates the greatest common divisor of a and b"""
  while b != 0:
    old_b = b
    b = a % b
    a = old_b
  return a

def lcm(a, b):
  """Calculates the least common multiple of a and b"""
  return (a * b) // gcd(a, b)

def is_prime(n):
  """Checks if a number is prime (n > 1)"""
  if n <= 1:
    return False
  for i in range(2, int(math.sqrt(n)) + 1):
    if n % i == 0:
      return False
  return True

def absolute_value(x):
  """Calculates the absolute value of a number"""
  return abs(x)

def logarithm(value, base=math.e):
  """Calculates logarithm of value to base (default base is e)"""
  return math.log(value, base)

def round_number(number, decimals=0):
  """Rounds a number to a specified number of decimal places"""
  return round(number, decimals)

def ceiling(number):
  """Calculates the ceiling of a number (smallest integer greater than or equal to number)"""
  return math.ceil(number)

def floor(number):
  """Calculates the floor of a number (largest integer less than or equal to number)"""
  return math.floor(number)

#Counting
def permutations(data):
  """Calculates the number of permutations of a list"""
  return math.factorial(len(data))

def combinations(data, k):
  """Calculates the number of combinations of k elements from a list"""
  return math.factorial(len(data)) // (math.factorial(k) * math.factorial(len(data) - k))

def combinations_with_replacement(data, k):
  """Calculates the number of combinations with replacement of k elements from a list"""
  return (len(data)**k)

def ordered_partitions(n, k):
  """Calculates the number of ordered partitions of n into k parts (stars and bars method)"""
  return math.factorial(n - 1) // math.factorial(k - 1) * math.factorial(n - k)

def unordered_partitions(n):
  """Calculates the number of unordered partitions of n (Bell numbers)"""
  

def binomial_coefficient(n, k):
  """Calculates the binomial coefficient (n choose k)"""
  return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))




#Geometry
#Area of Different Shapes

""" Area for Triangle"""

def distance_formula(x1, y1, x2, y2):
  return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def area_base_height(base, height):
  return 0.5 * base * height

def area_three_sides(a, b, c):
  """Calculate the area of a triangle using the three side lengths."""
  s = (a + b + c) / 2
  return math.sqrt(s * (s - a) * (s - b) * (s - c))

def area_three_points(x1, y1, x2, y2, x3, y3):
  """Calculate the area of a triangle using the coordinates of the three vertices."""
  return 0.5 * abs((x1 * (y2 - y3)) + (x2 * (y3 - y1)) + (x3 * (y1 - y2)))

def area_two_sides_angle(a, b, C):
  """Calculate the area of a triangle using two side lengths and the included angle."""
  return 0.5 * a * b * math.sin(math.radians(C))

# Calculus https://docs.sympy.org/latest/tutorials/intro-tutorial/calculus.html
def diffOneVar(y, x):
  return diff(y, x)
  