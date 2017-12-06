## 3. Introduction to SymPy ##

import sympy

x,y = sympy.symbols('x y')

y = x^2 + 1

y

## 4. Limits Using SymPy ##

import sympy
x2,y = sympy.symbols('x2 y')

limit_one = sympy.limit((-x2**2 + 3*x2 - 1 + 1) / (x2 - 3), x2, 2.9)

## 5. Properties Of Limits I ##

import sympy
x,y = sympy.symbols('x y')

limit_two = sympy.limit((3*x**2 + 3*x - 3), x, 1)

## 6. Properties Of Limits II ##

import sympy
x,y = sympy.symbols('x y')

limit_three = sympy.limit(x**3, x, -1) + 2*sympy.limit(x**2, x, -1) - 10*sympy.limit(x, x, -1)

## 7. Undefined Limit To Defined Limit ##

import sympy
x2, y = sympy.symbols('x2 y')

y = (-x2**2 + 3*x2 -1 + 1) / (x2 - 3)
limit_four = sympy.limit(y, x2, 3)