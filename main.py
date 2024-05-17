
from polynomial import Polynomial
from groebnerBasis import get_groebner_basis, polynomial_reduce
from monomialOrders import set_lex_order_permutation, set_deafult_lex_order_permutation, graded_lex_order, lex_order
from fraction import RationalNumber


def main():

    set_lex_order_permutation([0, 1, 2])
    p1 = Polynomial.power_sum_polynomial(3, 1) - 1
    p2 = Polynomial.power_sum_polynomial(3, 2) - 3
    p3 = Polynomial.power_sum_polynomial(3, 3) - 4
    G = get_groebner_basis([p1, p2, p3])
    
    print(G)
    
    n = 5
    set_deafult_lex_order_permutation(n)
    F = [Polynomial.power_sum_polynomial(n, i) for i in range(1, n + 1)]
    Polynomial.use_indexing = True
    print(F)
    G = [Polynomial.elementary_symetric_polynomial(n, i) for i in range(1, n + 1)]
    

    


    




if __name__ == "__main__":
   main()
   


