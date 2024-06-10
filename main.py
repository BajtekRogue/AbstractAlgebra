
from polynomial import Polynomial
from groebnerBasis import get_groebner_basis, polynomial_reduce
from monomialOrders import set_lex_order_permutation, set_deafult_lex_order_permutation, graded_lex_order, lex_order
from fraction import RationalNumber
from galoisField import GaloisField

def main():

    Polynomial.field = RationalNumber
    Polynomial.number_of_variables = 3
    Polynomial.variables = ('x', 'y', 'z')
    set_lex_order_permutation([1, 0, 2])
    
    x2 = (2, 0, 0)
    y2 = (0, 2, 0)
    z2 = (0, 0, 2)
    xy = (1, 1, 0)
    xz = (1, 0, 1)
    yz = (0, 1, 1)
    
    f = Polynomial({x2: 3, xy: 2, xz: 2, yz: 1})
    g = Polynomial({y2: 3, xy: 2, yz : 2, xz: 1})
    h = Polynomial({z2: 3, xz: 2, yz: 2, xy: 1})
    print(get_groebner_basis([f, g, h]))
    
    
 
    print()

    
    

    


    




if __name__ == "__main__":
   main()
   


