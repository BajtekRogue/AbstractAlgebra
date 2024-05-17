
from functools import cmp_to_key
from itertools import combinations
from monomialOrders import lex_order, multiply_monomials
from fraction import Fraction

class Polynomial:
    
    variables = ('x', 'y', 'z')
    variance_from_zero_tolerance = 0.0001
    use_indexing = False
    
    def __init__(self, coefficients: dict = None) -> None:
        self.coefficients = coefficients if coefficients is not None else {}
        self.remove_zero_coefficients()
        
        
    def __str__(self) -> str:
        if len(self.coefficients) == 0:
            return '0'
        
        self.sort_coefficients()
                
        def to_superscript(num):
            superscripts = {'0': '⁰','1': '¹', '2': '²', '3': '³', '4': '⁴', '5': '⁵', '6': '⁶', '7': '⁷', '8': '⁸', '9': '⁹'}
            return ''.join(superscripts[digit] for digit in str(num))
        
        result = ''
        if not self.use_indexing and len(list(self.coefficients.keys())[0]) > len(self.variables):
            raise ValueError('Too many variables for using letters')
        
        for monomial, coefficient in self.coefficients.items():
            if isinstance(coefficient, float) and coefficient.is_integer():
                coefficient = int(coefficient)

            if isinstance(coefficient, complex) or coefficient > 0:
                result += ' + '
            else:
                result += ' - '
            
            if (coefficient != 1 and coefficient != -1) or monomial == (0,) * self.number_of_variables():
                result += f'{abs(coefficient)}*'
                
            for i, power in enumerate(monomial):
                if power == 0:
                    continue
                elif self.use_indexing:
                    result += f'x{i+1}'
                else:
                    result += f'{self.variables[i]}'
                
                if power > 1:
                    result += f'{to_superscript(power)}'
                result += f'*'
                
            result = result[:-1]
            
        if result[1] == '+':
            return result[3:]
        else:
            return result[1:]


    def __repr__(self):
        return self.__str__()
    
    
    def __eq__(self, other):
        p = self - other
        return p.is_zero()
    
    
    def __ne__(self, other) -> bool:
        return not self.__eq__(other)
    
    
    def __pos__(self):
        return self
    
    
    def __neg__(self):
        result = {}
        for monomial, coefficient in self.coefficients.items():
            result[monomial] = -coefficient
            
        return Polynomial(result)
    
    
    def __add__(self, other):
        result = {}
        
        for monomial, coefficient in self.coefficients.items():
                result[monomial] = coefficient
                
        if isinstance(other, Polynomial):
            for monomial, coefficient in other.coefficients.items():
                if monomial in result:
                    result[monomial] += coefficient
                else:
                    result[monomial] = coefficient
        
        elif isinstance(other, (int, float, complex, Fraction)):
            if (0,) * self.number_of_variables() in result:
                result[(0,) * self.number_of_variables()] += other
            else:
                result[(0,) * self.number_of_variables()] = other
        else:
            return NotImplemented
        
        return Polynomial(result)
    
    
    def __radd__(self, other):
        return self.__add__(other)


    def __iadd__(self, other):
        self = self + other
        return self


    def __sub__(self, other):
        return self + (-other)
    
    
    def __rsub__(self, other):
        return -self + other
    
    
    def __isub__(self, other):
        self += -other
        return self
    
    
    def __mul__(self, other):
        result = {}
        
        if isinstance(other, Polynomial):
            for monomial1, coefficient1 in self.coefficients.items():
                for monomial2, coefficient2 in other.coefficients.items():
                    new_monomial = multiply_monomials(monomial1, monomial2)
                    new_coefficient = coefficient1 * coefficient2
                    
                    if new_monomial in result:
                        result[new_monomial] += new_coefficient
                    else:
                        result[new_monomial] = new_coefficient
                        
        elif isinstance(other, (int, float, complex, Fraction)):
            for monomial, coefficient in self.coefficients.items():
                result[monomial] = coefficient * other
        else:
            return NotImplemented
        
        return Polynomial(result)
        
    
    def __rmul__(self, other):
        return self * other
    
    
    def __imul__(self, other):
        self = self * other
        return self
    
    
    def __pow__(self, exponent):
        if not isinstance(exponent, int) or exponent < 0:
            raise TypeError(f"Exponentiation is only supported with natural exponents")

        if exponent == 0:
            return Polynomial({(0,) * self.number_of_variables(): 1})


        result = Polynomial({(0,) * self.number_of_variables(): 1})
        base = self

        while exponent > 0:
            if exponent % 2 == 1:
                result *= base
            base *= base
            exponent //= 2

        return result
    
    
    def __ipow__(self, exponent):
        self = self ** exponent
        return self
    
    
    def number_of_variables(self):
        if len(self.coefficients) == 0:
            return 0
        else:
            return len(list(self.coefficients.keys())[0])
    
    
    def total_degree(self) -> int:
        if len(self.coefficients) == 0:
            return -1
        
        max_sum = 0
        for monomial in self.coefficients.keys():
            max_sum = max(max_sum, sum(monomial))
        
        return max_sum
    
    
    
    def leading_monomial(self, monomial_order = lex_order) -> tuple:
        if len(self.coefficients) == 0:
            return ()
             
        max_monomial = list(self.coefficients.keys())[0]
        for monomial in self.coefficients.keys():
            if monomial_order(max_monomial, monomial):
                max_monomial = monomial
        
        return max_monomial
    
    
    def leading_coefficient(self, monomial_order = lex_order) -> int:
        if len(self.coefficients) == 0:
            return 0
        else:
            return self.coefficients[self.leading_monomial(monomial_order)]
    
    
    def evaluate(self, point: tuple):
        result = 0
        for monomial, coefficient in self.coefficients.items():
            term = coefficient
            for i, power in enumerate(monomial):
                term *= point[i] ** power
            result += term
        
        return result
    
    
    def is_zero(self) -> bool:
        if len(self.coefficients) == 0:
            return True
        else:
            for coefficient in self.coefficients.values():
                if abs(coefficient) >= self.variance_from_zero_tolerance:
                    return False
            return True

    
    def remove_zero_coefficients(self):
        coefficients_to_remove = []
        
        for monomial, coefficient in self.coefficients.items():
            if abs(coefficient) < self.variance_from_zero_tolerance:
                coefficients_to_remove.append(monomial)

        for coefficient in coefficients_to_remove:
            self.coefficients.pop(coefficient)
        
        if len(self.coefficients) == 0:
            self.coefficients = {}
    
    
    def sort_coefficients(self, monomial_order=lex_order):

        def monomial_order_to_key(alpha: tuple, beta: tuple) -> int:
            if monomial_order(alpha, beta):
                return -1
            elif monomial_order(beta, alpha):
                return 1
            else:
                return 0

        key_function = cmp_to_key(monomial_order_to_key)
        self.coefficients = dict(sorted(self.coefficients.items(), key=lambda item: key_function(item[0]), reverse=True))
    
    
    def check_if_valid_polynomial(self) -> bool:
        number_of_variables = len(list(self.coefficients.keys())[0]) if len(self.coefficients) > 0 else 0

        try:
            for monomial, coefficient in self.coefficients.items():
                if not isinstance(monomial, tuple):
                    raise ValueError('Monomials must be tuples')
                elif not all(isinstance(power, int) for power in monomial) or not all(power >= 0 for power in monomial):
                    raise ValueError('All monomial powers must be natural numbers')
                elif not isinstance(coefficient, (int, float, complex, Fraction)):
                    raise ValueError('All coefficients must be integers, floats or complex numbers')
                elif len(monomial) != number_of_variables:
                    raise ValueError('All monomials must have the same number of variables')
                
        except ValueError as e:
            print(e)
            return False
        return True
    

    def partial_derivative(self, variable):
        if self.is_zero():
            return Polynomial()
        
        if isinstance(variable, str):
            index = self.variables.index(variable)
        else:
            index = variable
        
        if index < 0 or index >= self.number_of_variables():
            return Polynomial()
        
        result = {}
        for monomial, coefficient in self.coefficients.items():
            if monomial[index] == 0:
                continue
            
            new_monomial = list(monomial)
            new_monomial[index] -= 1
            new_coefficient = coefficient * monomial[index]
            
            new_monomial = tuple(new_monomial)
            result[new_monomial] = new_coefficient

        return Polynomial(result)


    @staticmethod
    def power_sum_polynomial(number_of_variables: int, degree: int):
        dict = {}
        for i in range(number_of_variables):
            monomial = tuple(degree if i == j else 0 for j in range(number_of_variables))
            dict[monomial] = 1
        
        return Polynomial(dict)
    
    
    @staticmethod
    def elementary_symetric_polynomial(number_of_variables: int, degree: int):
        if degree <= 0 or degree > number_of_variables:
            return Polynomial()
        
        dict = {}
        subsets = list(combinations(list(range(number_of_variables)), degree))
        binary_subsets = []

        for subset in subsets:
            binary_representation = [0] * number_of_variables
            for index in subset:
                binary_representation[index] = 1
            binary_subsets.append(tuple(binary_representation))
        
        for binary_subset in binary_subsets:
            dict[binary_subset] = 1
        
        return Polynomial(dict)