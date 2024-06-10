# Field
choose field for polynomial from Q, R, C, GF(p). By deafult Q
```python
Polynomial.field = RationalNumber
```
# Variables
choose number of variables, deafult 3
Polynomial.number_of_variables = 3
choose variables names, you can also set Polynomial.use_indexing = True to have x1,...,xn
```python
Polynomial.variables = ('x', 'y', 'z')
```
# lex order
set permutation for lex order for example [1, 0, 2] corresponds to y > x > z
```python
set_lex_order_permutation([1, 0, 2])
```
you can also set permutation to x1 > ... > xn
```python
set_lex_order_permutation(n)
```
# Polynomial representation
Polynomials are stored as dicts where key is a tuple representing exponent and item is coefficient associviated with it so for example -11xz^5 would be
```python
{(1, 0, 5): -11} 
```
