# tools by AIME syllabus

Based on raw python and sympy

**Store all the syllabus parts definitions and examples, so that we can store them like a word bank for the ngram checker to use at checking time**

_Storing all the examples in a vector db could be an amazing quality signal_

- too close in fuzzy/vector search, youre probably doing something simple/stupid
- medium dist in fuzzy

## Arithmetic/pemdas

Just regular python and python sequences here

- x+2
- x-2
- x\*2
- x/2
- x^2
- (x)

## Algebra

### general

- solving equations: sympy algebraic solve()

### Polynomials

- Binomial theorem: I see no tool usage, but keep track of formula/definition/examples

formula: (x+y)^{n}=\sum _{k=0}^{n}{n \choose k}x^{n-k}y^{k}=\sum _{k=0}^{n}{n \choose k}x^{k}y^{n-k}

- Conjugate roots: definition tracking

def: if a polynomial P(x) in one variable with real coefficients has the root a + bi, then a - bi is also a root of the polynomial.

- Symmetric polynomials: Again covered b sympy, wouldnt hurt to show the model examples
- Vietas formulas: looks like general sympy coverage, probably should test tho
- Remainder theorem and factor theorem: keep in dictionary for word parse
- Rational Root Theorem: keep in dictionary for word parses
- sum of coeff: also just in dictionary usage
- dealing with integer division and polynomial division is just part of the sympy solver
- keep examples of sum and difference of factorizations

### Sequences Series Recurrances

- keep examples/def for Arithmetic, geometric, arithmeto-geometric series, but dependig on how they show up in questions, sympy has tools for them
- keep track of telescoping examples, but also probably comes out of the box with sympy
- while linear recurrances are rare, sympy has tools for that, same for recurrances with sums

### Complex Numbers

- should all be covered by sympy
