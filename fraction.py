class Fraction:
    def __init__(self, numerator, denominator = 1):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")
        
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        d = gcd(numerator, denominator)

        numerator //= d
        denominator //= d
        if denominator < 0:
            numerator = -numerator
            denominator = -denominator

        self.numerator = numerator
        self.denominator = denominator


    def __str__(self):
        if self.denominator == 1:
            return f"{self.numerator}"
        else:
            return f"{self.numerator}/{self.denominator}"
    

    def __repr__(self):
        return self.__str__()
    
    
    def __eq__(self, other):
        if isinstance(other, Fraction):
            return self.numerator == other.numerator and self.denominator == other.denominator
        elif isinstance(other, int):
            return self.numerator == other and self.denominator == 1
        elif isinstance(other, float):
            return (self.numerator / self.denominator - other) < 0.0001
        else:
            return NotImplemented
    
    
    def __ne__(self, other) -> bool:
        return not self.__eq__(other)
    
    
    def __pos__(self):
        return self
    
    
    def __neg__(self):
        return Fraction(-self.numerator, self.denominator)
    
    
    def __add__(self, other):
        if isinstance(other, Fraction):
            numerator = self.numerator * other.denominator + other.numerator * self.denominator
            denominator = self.denominator * other.denominator
            return Fraction(numerator, denominator)
        elif isinstance(other, int):
            return self + Fraction(other, 1)
        else:
            return NotImplemented
    
    
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
        if isinstance(other, Fraction):
            return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)
        elif isinstance(other, int):
            return Fraction(self.numerator * other, self.denominator)
        else:
            return NotImplemented
        
    
    def __rmul__(self, other):
        return self * other
    
    
    def __imul__(self, other):
        self = self * other
        return self
    
    
    def __truediv__(self, other):
        if isinstance(other, Fraction):
            return self * Fraction(other.denominator, other.numerator)
        elif isinstance(other, int):
            return self * Fraction(1, other)
        else:
            return NotImplemented
        

    def __rtruediv__(self, other):
        return Fraction(other) / self
    

    def __itruediv__(self, other):
        self = self / other
        return self
    

    def __pow__(self, exponent):
        if not isinstance(exponent, int) or exponent < 0:
            raise TypeError(f"Exponentiation is only supported with natural exponents")

        if exponent == 0:
            return Fraction(1)


        result = 1
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


    def __lt__(self, other):
        if isinstance(other, Fraction):
            return self.numerator * other.denominator < other.numerator * self.denominator
        elif isinstance(other, int):
            return self < Fraction(other, 1)
        elif isinstance(other, float):
            return self.numerator / self.denominator < other
        else:
            return NotImplemented
    

    def __le__(self, other):
        if isinstance(other, Fraction):
            return self.numerator * other.denominator <= other.numerator * self.denominator
        elif isinstance(other, int):
            return self <= Fraction(other, 1)
        elif isinstance(other, float):
            return self.numerator / self.denominator <= other
        else:
            return NotImplemented
        
    
    def __gt__(self, other):
        if isinstance(other, Fraction):
            return self.numerator * other.denominator > other.numerator * self.denominator
        elif isinstance(other, int):
            return self > Fraction(other, 1)
        elif isinstance(other, float):
            return self.numerator / self.denominator > other
        else:
            return NotImplemented
    

    def __ge__(self, other):
        if isinstance(other, Fraction):
            return self.numerator * other.denominator >= other.numerator * self.denominator
        elif isinstance(other, int):
            return self >= Fraction(other, 1)
        elif isinstance(other, float):
            return self.numerator / self.denominator >= other
        else:
            return NotImplemented
    
    
    def __abs__(self):
        return Fraction(abs(self.numerator), self.denominator)
