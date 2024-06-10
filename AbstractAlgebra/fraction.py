from typing import Union

class RationalNumber:
    # Fraction will be in reduced form with positive denominator
    def __init__(self, numerator: Union[int, float], denominator: int = 1) -> None:
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")
        
        if isinstance(numerator, float):
            numerator = round(numerator, 4)
            numerator = round(numerator * 10**4)
            denominator = 10**4
            
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


    def __str__(self) -> str:
        if self.denominator == 1:
            return f"{self.numerator}" 
        else:
            return f"{self.numerator}/{self.denominator}"  

    
    def __repr__(self) -> str:
        return self.__str__()
    
    
    def __eq__(self, other) -> bool:
        if isinstance(other, RationalNumber):
            return self.numerator == other.numerator and self.denominator == other.denominator
        elif isinstance(other, int):
            return self.numerator == other and self.denominator == 1
        elif isinstance(other, float):
            return (self.numerator / self.denominator - other) < 0.0001 # tolerance
        else:
            return False
    
    
    def __pos__(self) -> "RationalNumber":
        return self

    
    def __neg__(self) -> "RationalNumber":
        return RationalNumber(-self.numerator, self.denominator)
    
    
    def __add__(self, other) -> "RationalNumber":
        if isinstance(other, RationalNumber):
            return RationalNumber(self.numerator * other.denominator + other.numerator * self.denominator, self.denominator * other.denominator)
        elif isinstance(other, int):
            return RationalNumber(self.numerator + other * self.denominator, self.denominator)
        elif isinstance(other, float):
            return self + RationalNumber(other)
        else:
            return NotImplemented
    
    
    def __radd__(self, other) -> "RationalNumber":
        return self.__add__(other)


    def __iadd__(self, other) -> "RationalNumber":
        self = self + other
        return self


    def __sub__(self, other) -> "RationalNumber":
        return self + (-other)
    
    
    def __rsub__(self, other) -> "RationalNumber":
        return -self + other
    
    
    def __isub__(self, other) -> "RationalNumber":
        self += -other
        return self
    
    
    def __mul__(self, other) -> "RationalNumber":
        if isinstance(other, RationalNumber):
            return RationalNumber(self.numerator * other.numerator, self.denominator * other.denominator)
        elif isinstance(other, int):
            return RationalNumber(self.numerator * other, self.denominator)
        elif isinstance(other, float):
            return self * RationalNumber(other)
        else:
            return NotImplemented
        
    
    def __rmul__(self, other) -> "RationalNumber":
        return self * other
    
    
    def __imul__(self, other) -> "RationalNumber":
        self = self * other
        return self
    
    
    def __truediv__(self, other) -> "RationalNumber":
        if isinstance(other, RationalNumber):
            return self * RationalNumber(other.denominator, other.numerator)
        elif isinstance(other, int):
            return self * RationalNumber(1, other)
        elif isinstance(other, float):
            return self / RationalNumber(other)
        else:
            return NotImplemented
        

    def __rtruediv__(self, other) -> "RationalNumber":
        return RationalNumber(other) / self
    

    def __itruediv__(self, other) -> "RationalNumber":
        self = self / other
        return self
    

    def __pow__(self, exponent) -> "RationalNumber":
        if not isinstance(exponent, int):
            raise TypeError(f"Exponentiation is only supported with integer exponents")

        if exponent == 0:
            return RationalNumber(1)
        elif exponent < 0:
            self = RationalNumber(1) / self
            exponent = -exponent

        result = 1
        base = self

        while exponent > 0:
            if exponent % 2 == 1:
                result *= base
            base *= base
            exponent //= 2

        return result
    
    
    def __ipow__(self, exponent) -> "RationalNumber":
        self = self ** exponent
        return self


    def __lt__(self, other) -> bool:
        if isinstance(other, RationalNumber):
            return self.numerator * other.denominator < other.numerator * self.denominator
        elif isinstance(other, int):
            return self < RationalNumber(other, 1)
        elif isinstance(other, float):
            return self.numerator / self.denominator < other
        else:
            return NotImplemented
    

    def __le__(self, other):
        if isinstance(other, RationalNumber):
            return self.numerator * other.denominator <= other.numerator * self.denominator
        elif isinstance(other, int):
            return self <= RationalNumber(other, 1)
        elif isinstance(other, float):
            return self.numerator / self.denominator <= other
        else:
            return NotImplemented
        
    
    def __gt__(self, other) -> bool:
        if isinstance(other, RationalNumber):
            return self.numerator * other.denominator > other.numerator * self.denominator
        elif isinstance(other, int):
            return self > RationalNumber(other, 1)
        elif isinstance(other, float):
            return self.numerator / self.denominator > other
        else:
            return NotImplemented
    

    def __ge__(self, other) -> bool:
        if isinstance(other, RationalNumber):
            return self.numerator * other.denominator >= other.numerator * self.denominator
        elif isinstance(other, int):
            return self >= RationalNumber(other, 1)
        elif isinstance(other, float):
            return self.numerator / self.denominator >= other
        else:
            return NotImplemented
    
    
    def __abs__(self) -> "RationalNumber":
        return RationalNumber(abs(self.numerator), self.denominator)


    def __float__(self) -> float:
        return self.numerator / self.denominator
    
    
    def __int__(self) -> int:
        return self.numerator // self.denominator
