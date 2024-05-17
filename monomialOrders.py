
LEX_ORDER_PERMUTATION = []

def lex_order(alpha: tuple, beta: tuple) -> bool:
    for i in LEX_ORDER_PERMUTATION:
        if alpha[i] < beta[i]:
            return True
        elif alpha[i] > beta[i]:
            return False
    return False


def graded_lex_order(alpha: tuple, beta: tuple) -> bool:
    alpha_sum = sum(alpha)
    beta_sum = sum(beta)
    
    if alpha_sum < beta_sum:
        return True
    elif alpha_sum > beta_sum:
        return False
    else:
        return lex_order(alpha, beta)


def reverse_graded_lex_order(alpha: tuple, beta: tuple) -> bool:
    alpha_sum = sum(alpha)
    beta_sum = sum(beta)
    
    if alpha_sum < beta_sum:
        return True
    elif alpha_sum > beta_sum:
        return False
    else:
        return not lex_order(alpha, beta)
    
    
def axis_order(alpha: tuple, beta: tuple) -> bool:
    for a, b in zip(alpha, beta, strict=True):
        if a > b:
            return False
    return True


def multiply_monomials(alpha: tuple, beta: tuple) -> tuple:
    return tuple([a + b for a, b in zip(alpha, beta, strict=True)])


def divide_monomials(alpha: tuple, beta: tuple) -> tuple:
    if axis_order(beta, alpha):
        return tuple([a - b for a, b in zip(alpha, beta, strict=True)])
    else:
        raise ValueError('Monomials do not divide')


def least_common_multiple(alpha: tuple, beta: tuple) -> tuple:
    return tuple([max(a, b) for a, b in zip(alpha, beta, strict=True)])


# sets lex order to the given permutation {0, 1, ..., n - 1}
def set_lex_order_permutation(permutation: list[int]) -> None:
    global LEX_ORDER_PERMUTATION 
    LEX_ORDER_PERMUTATION = permutation


# sets deafult lex order x > y > z > ...
def set_deafult_lex_order_permutation(number_of_variables: int) -> None:
    global LEX_ORDER_PERMUTATION
    LEX_ORDER_PERMUTATION = list(range(number_of_variables))