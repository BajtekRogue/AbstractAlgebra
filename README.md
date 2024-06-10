## Field
You can choose the field over which the polynomial is defined. The default field is the set of rational numbers, $\mathbb{Q}$. 
```python
Polynomial.field = RationalNumber
```
Available Fields:
```python
supported_fields = (RationalNumber, float, complex, GaloisField)
```
- RationalNumber $\mathbb{Q}$
- float $\mathbb{R}$
- complex $\mathbb{C}$
- GaloisField $\mathbb{F_p}$
## Number of Variables
Set the number of variables for the polynomials. The default number is $3$.
```python
Polynomial.number_of_variables = 5
```
## Variable Names
You can specify the names of the variables
```python
Polynomial.variables = ('x', 'y', 'z')
```
## Use Indexed Variables
To have $x_1 > x_2 > \ldots > x_n$ set
```python
Polynomial.use_indexing = True 
```
## Lexicographic Order
Set the permutation for lexicographic order. For example 
```python
set_lex_order_permutation([1, 0, 2])
```
corresponds to $y > x > z$.
## Indexed Lexicographic Order
To set the permutation for variables in indexed order $x_1 > x_2 > \ldots > x_n$, use:
```python
set_lex_order_permutation(n)
```
## Polynomial representation
Polynomials are stored as dictionaries where the key is a tuple representing the exponent and the value is the coefficient associated with it. For example, the polynomial $-7x^3yz^5$ is represented as:
```python
{(3, 2, 5): -7} 
```
## Monomial orders
Available monomial orders are:
```python
lex_order, graded_lex_order, reverse_graded_lex_order
```
## Gröbner basis
To extend set G to a gröbner basis use 
```python
get_groebner_basis(G)
```
## Special polynmials
Power sum $p_k(x_1, \ldots x_n) = x_1^k + \ldots + x_n^k$
```python
power_sum_polynomial(n, k)
```
Elementary symmetric polynomial $e_k(x_1, \ldots x_n)$
```python
elementary_symetric_polynomial(n, k)
```
