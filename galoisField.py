
class GaloisField():
    
    prime = 2
    
    def __init__(self, number, prime = None) -> None:
        
        if prime == None:
            prime = self.prime
            self.number = number % self.prime
            return
        
        def is_prime(n):
            if n <= 1:
                return False
            elif n == 2:
                return True
            elif n % 2 == 0:
                return False
            else:
                for i in range(3, int(n ** 0.5) + 1, 2):
                    if n % i == 0:
                        return False
                return True
        
        if not is_prime(prime):
            raise ValueError("Not a prime")
        self.prime = prime
        self.number = number % GaloisField.prime
        
        
    def __str__(self) -> str:
        return f"{self.number}"

    
    def __repr__(self) -> str:
        return self.__str__()
    
    
    def __eq__(self, other) -> bool:
        if isinstance(other, GaloisField):
            return self.number == other.number
        else:
            return self.number == other
    
    
    def __pos__(self) -> "GaloisField":
        return self

    
    def __neg__(self) -> "GaloisField":
        return self.prime - self.number
    
    
    def __add__(self, other) -> "GaloisField":
        if isinstance(other, GaloisField):
            return GaloisField(self.number + other.number)
        elif isinstance(other, int):
            return GaloisField(self.number + other)
        else:
            return NotImplemented
    
    
    def __radd__(self, other) -> "GaloisField":
        return self.__add__(other)


    def __iadd__(self, other) -> "GaloisField":
        self = self + other
        return self


    def __sub__(self, other) -> "GaloisField":
        return self + (-other)
    
    
    def __rsub__(self, other) -> "GaloisField":
        return -self + other
    
    
    def __isub__(self, other) -> "GaloisField":
        self += -other
        return self
    
    
    def __mul__(self, other) -> "GaloisField":
        if isinstance(other, GaloisField):
            return GaloisField(self.number * other.number)
        elif isinstance(other, int):
            return GaloisField(self.number * other)
        else:
            return NotImplemented
        
    
    def __rmul__(self, other) -> "GaloisField":
        return self * other

    
    def __imul__(self, other) -> "GaloisField":
        self = self * other
        return self
    
    
    def __truediv__(self, other) -> "GaloisField":

        def extended_euclid(a, b):
            if b == 0:
                return a, 1, 0
            else:
                d, x, y = extended_euclid(b, a % b)
                return d, y, x - y * (a // b)
        
        if isinstance(other, GaloisField):
            _, x, _ = extended_euclid(other.number, self.prime)
            return self * GaloisField(x)
        elif isinstance(other, int):
            _, x, _ = extended_euclid(other, self.prime)
            return self * GaloisField(x)
        else:
            return NotImplemented
        

    def __rtruediv__(self, other) -> "GaloisField":
        return GaloisField(other) / self
    

    def __itruediv__(self, other) -> "GaloisField":
        self = self / other
        return self
    

    def __pow__(self, exponent) -> "GaloisField":
        if not isinstance(exponent, int):
            raise TypeError(f"Exponentiation is only supported with integer exponents")

        if exponent == 0:
            return GaloisField(1)
        elif exponent < 0:
            self = GaloisField(1) / self
            exponent = -exponent

        result = 1
        base = self

        while exponent > 0:
            if exponent % 2 == 1:
                result *= base
            base *= base
            exponent //= 2

        return result
    
    
    def __ipow__(self, exponent) -> "GaloisField":
        self = self ** exponent
        return self


    def __abs__(self) -> "GaloisField":
        return self.number

    
    def __int__(self) -> int:
        return self.number