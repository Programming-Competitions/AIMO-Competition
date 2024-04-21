import re

def run_code_blocks(multiline_string):
    pattern = r'```(.*?)```'
    code_blocks = re.findall(pattern, multiline_string, re.DOTALL)

    for code_block in code_blocks:
        code_block = code_block.strip()
        try:
            exec(code_block)
        except Exception as e:
            print(f"Error executing code block:\n{code_block}\nError: {e}")

multiline_string = '''
This is a multiline string with code blocks.

```
x = 5
print(x)
```

And here's another code block:

```
from sympy import Symbol, cos

x = Symbol('x')
e = 1/cos(x)
print(e.series(x, 0, 10))
```
'''

run_code_blocks(multiline_string)
