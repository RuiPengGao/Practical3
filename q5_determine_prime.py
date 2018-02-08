#determine and print prime number

import math

def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    for i in range(3,int(math.sqrt(n)) + 1,2):
        if n % i ==0:
            return False
    return True
    
prime = []
i = 2
while len(prime) < 1000:
    if is_prime(i) == True:
        prime.append(str(i))
    i += 1

for t in range(0,1000,10):
    print("\t".join(prime[t:t+10]))
