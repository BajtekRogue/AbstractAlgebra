import copy
from polynomial import Polynomial
from monomialOrders import axis_order, divide_monomials, least_common_multiple, lex_order
from tqdm import tqdm

def polynomial_reduce(f: Polynomial, G: list[Polynomial], monomial_order = lex_order) -> tuple[list[Polynomial], Polynomial]:

    p = copy.deepcopy(f)
    r = Polynomial()
    alpha_list = [Polynomial({}) for _, _ in enumerate(G)]
    G_monomials_list = [g.leading_monomial(monomial_order) for g in G]
    G_leading_coefficients = [g.leading_coefficient(monomial_order) for g in G]

    while not p.is_zero():
        p_monomial = p.leading_monomial(monomial_order)
        p_coefficient = p.leading_coefficient(monomial_order)
        something_divided = False

        for i, g in enumerate(G):
            try:
                power = divide_monomials(p_monomial, G_monomials_list[i])
                coefficient = p_coefficient / G_leading_coefficients[i]
                alpha_list[i] += Polynomial({power: coefficient})
                p -= Polynomial({power: coefficient}) * g
                something_divided = True
                break  
            
            except ValueError:
                pass
        

        if not something_divided:
            r += Polynomial({p_monomial: p_coefficient})
            p -= Polynomial({p_monomial: p_coefficient})

    return alpha_list, r


def syzygy(f: Polynomial, g: Polynomial, monomial_order = lex_order) -> Polynomial:
    f_monomial = f.leading_monomial(monomial_order)
    f_coefficient = f.leading_coefficient(monomial_order)
    g_monomial = g.leading_monomial(monomial_order)
    g_coefficient = g.leading_coefficient(monomial_order)
    m = least_common_multiple(f_monomial, g_monomial)
    a = Polynomial({divide_monomials(m, f_monomial): 1 / f_coefficient})
    b = Polynomial({divide_monomials(m, g_monomial): 1 / g_coefficient})
    return a * f - b * g


# Buchberger's algorithm
def extend_to_groebner_basis(Basis: list[Polynomial], monomial_order = lex_order) -> list[Polynomial]:
    G = list(Basis)
    while True:
        H = list(G)  
        q += 1  
        for i in tqdm(range(len(G))):
            for j in range(i + 1, len(G)):
                _, r = polynomial_reduce(syzygy(G[i], G[j], monomial_order), G)
                if not r.is_zero():
                    H.append(r)

        if len(G) == len(H):
            return H
        else:
            G = H
        
        
def is_in_leading_terms_ideal(f: Polynomial, G: list[Polynomial], monomial_order = lex_order) -> bool:
    for g in G:
        if axis_order(g.leading_monomial(monomial_order), f.leading_monomial(monomial_order)):
            return True
    return False


# Reduces a Groebner basis to a minimal Groebner basis
def reduce_groebner_basis(G: list[Polynomial], monomial_order = lex_order, normalize_coefficients = True) -> list[Polynomial]:
    H = list(G)
    for g in G:
        H.remove(g)
        if not is_in_leading_terms_ideal(g, H, monomial_order):
            H.append(g)
    
    s = len(H)
    counter = 0
    while counter < s:

        counter = 0
        for i, h in enumerate(H):
            F = list(H)
            F.remove(h)
            _, r = polynomial_reduce(h, F)
            H[i] = r

            if r == h:
                counter += 1
    
    if normalize_coefficients:
        for i, h in enumerate(H):
            H[i] *= 1 / h.leading_coefficient(monomial_order)

    return H


def get_groebner_basis(G: list[Polynomial], monomial_order = lex_order, normalize_coefficients = True) -> list[Polynomial]:
    return reduce_groebner_basis(extend_to_groebner_basis(G, monomial_order), monomial_order, normalize_coefficients)