from functools import cache
class Myint(int):
    def __init__(self, n):
        super().__init__()
        self.n = n
    def __repr__(self):
        return f"{self.n}"
    def __str__(self):
        return f"{self.n}"
    @classmethod
    @cache
    def is_prime(cls, n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n**0.5)+1, 2):
            if n % i == 0:
                return False
        return True
    
N = input()
numbers =  list(map(Myint, input().split()))
count = 0
for n in numbers:
    if Myint.is_prime(n):
        count += 1
        
print(count)