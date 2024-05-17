
from polynomial import Polynomial
from groebnerBasis import get_groebner_basis, polynomial_reduce
from monomialOrders import set_lex_order_permutation, set_deafult_lex_order_permutation, graded_lex_order, lex_order
from fraction import Fraction

def get_monomials(number_of_variables, max_exponent):
    monomials = {}

    for x_exp in range(max_exponent + 1):
        for y_exp in range(max_exponent + 1):
            for z_exp in range(max_exponent + 1):
                monomial_name = ''
                if x_exp > 0:
                    monomial_name += 'x'
                    if x_exp > 1:
                        monomial_name += f'^{x_exp}'
                if y_exp > 0:
                    monomial_name += 'y'
                    if y_exp > 1:
                        monomial_name += f'^{y_exp}'
                if z_exp > 0:
                    monomial_name += 'z'
                    if z_exp > 1:
                        monomial_name += f'^{z_exp}'
                if monomial_name == '':
                    monomial_name = '1'  # for the constant term
                monomials[monomial_name] = (x_exp, y_exp, z_exp)
    
    return monomials


def main():
    set_lex_order_permutation([0, 1, 2, 3, 4])
    Polynomial.variables = ('u', 'v', 'x', 'y', 'z')

    f = Polynomial({(1, 1, 0, 0, 0): 1, (0, 0, 1, 0, 0): -1})
    g = Polynomial({(0, 1, 0, 0, 0): 1, (0, 0, 0, 1, 0): -1})
    h = Polynomial({(2, 0, 0, 0, 0): 1, (0, 0, 0, 0, 1): -1})
    print(get_groebner_basis([f, g, h]))
    
    set_lex_order_permutation([0, 1])
    Polynomial.variables = ('x', 'y')
    fx = Polynomial({(2, 1): 1, (2, 0): 2, (0, 3): 1, (0, 2): 6})
    fy = Polynomial({(3, 0): 1, (1, 2): 1, (1, 1): 4, (1, 0): - 8})
    print(get_groebner_basis([fx, fy]))
    gx = Polynomial({(1, 2): 1, (3, 0): 1, (1, 0): -25})
    gy = Polynomial({(2, 1): 1, (0, 3): 1, (0, 1): -7})
    print(get_groebner_basis([gx, gy]))
    hx = Polynomial({(1, 2): 350, (1, 0): -450, (3, 0): 576})
    hy = Polynomial({(2, 1): 350, (0, 1): -450, (0, 3): 576})
    print(get_groebner_basis([hx, hy]))
    
    a = Fraction(350)
    b = Fraction(-450)
    c = Fraction(576)

    hx = Polynomial({(1, 2): a, (1, 0): b, (3, 0): c})
    hy = Polynomial({(2, 1): a, (0, 1): b, (0, 3): c})
    print(get_groebner_basis([hx, hy]))

    set_lex_order_permutation([0, 1, 2, 3])
    Polynomial.variables = ('l', 't', 'x', 'y')
    p = Polynomial({(0, 0, 1, 0): 1, (0, 2, 1, 0): 1, (0, 2, 0, 0): 1, (0, 0, 0, 0): -1})
    q = Polynomial({(0, 0, 0, 1): 1, (0, 2, 0, 1): 1, (0, 1, 0, 0): -2})
    r = Polynomial({(1, 4, 0, 0): 1, (1, 2, 0, 0): 2, (1, 0, 0, 0): 1, (0, 0, 0, 0): -1})
    print(get_groebner_basis([p, q, r]))


    



if __name__ == "__main__":
   main()
   


