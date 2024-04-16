import re
import math
from sympy import * # sympy imports wont work?
x, y, z = symbols('x y z')
init_printing(use_unicode=True)

def evaluate_expression(expr, variables):
    # Evaluate the expression using eval(), and provide the variables dictionary
    return eval(expr, variables)

def main():
    tools = """
<<<[eval("abs(-5)"),x_a]>>>, regular answer example, <<<[eval("math.lcm(2*x_a+3)"),y_a]>>>, algebra with python math lib, <<<[eval("integrate(cos(x)+y_a*x, x).subs(x,1)"),ans]>>> # run sympy here too
"""

    variables = {}
    lines = tools.strip().split("\n")

    for line in lines:
        # Extract the inner array using regular expression
        match = re.search(r'<<<\[(.*?),(\w+)\]>>>', line)
        if match:
            # Extract expression and variable name
            expr = match.group(1)
            var_name = match.group(2)

            # Evaluate expression
            value = evaluate_expression(expr, variables)

            # Update variables dictionary
            variables[var_name] = value

            # Check if 'ans' is defined
            if 'ans' in variables:
                print(variables['ans'])
                break

if __name__ == "__main__":
    main()
