from gmpy2 import isqrt
from banner import *
def fermat(n):
    a = isqrt(n)
    b2 = a*a - n
    b = isqrt(n)
    while b*b != b2:
        a = a + 1
        b2 = a*a - n
        b = isqrt(b2)
        if b > n :
          print("\n%s[-] Sorry Can't Factorize Number%s"%(R,R))
          exit()
    p = a+b
    q = a-b
    print("%sp =%s"%(Y,G),p)
    print("%sq =%s"%(Y,G),q)


