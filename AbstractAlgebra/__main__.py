
from AbstractAlgebra.polynomial import Polynomial
from AbstractAlgebra.groebnerBasis import get_groebner_basis, polynomial_reduce
from AbstractAlgebra.monomialOrders import set_lex_order_permutation, set_deafult_lex_order_permutation, graded_lex_order, lex_order
from AbstractAlgebra.fraction import RationalNumber
from AbstractAlgebra.galoisField import GaloisField

def main():

    Polynomial.field = RationalNumber
    Polynomial.number_of_variables = 3
    Polynomial.variables = ('x', 'y', 'z')
    set_lex_order_permutation([0, 1, 2])
    



    




if __name__ == "__main__":
   main()
   


