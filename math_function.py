import math

a=65.65                  # output            reson
print(math.ceil(a))      # 66                incresed to convert into int

print(math.floor(a))     # 65                decrease to convert into int

b=35
c=16
print(math.factorial(c)) # 20922789888000
print(math.fmod(b,c))    # 3.0               rem

print(math.sqrt(c))      # 4.0               squreroot
print(math.isqrt(c))     # 4                 squreroot
print(math.gcd(b,c))     # 1

d=[10,3,2,4,56,6,4,33]  
print(math.fsum(d))      # 118.0             sum 
print(math.prod(d))      # 10644480          product

print(str(int(round(math.degrees(math.atan2(b,c)))))+'°')    # 65°    angle between mbc in a right angle triangel abc
