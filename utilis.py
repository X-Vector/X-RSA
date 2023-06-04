import binascii
import gmpy2



def Convert(decimal):
    hex_ = hex(decimal).replace("0x","").replace("L","")
    ascii = binascii.a2b_hex(hex_)
    print("\nPlainText in Decimal :",decimal)
    print("PlainText in hex :",hex_)
    print("PlainText in ascii :",ascii.decode("utf-8"))

def egcd(b, n):
    (x0, x1, y0, y1) = (1, 0, 0, 1)
    while n != 0:
        (q, b, n) = (b // n, n, b % n)
        (x0, x1) = (x1, x0 - q * x1)
        (y0, y1) = (y1, y0 - q * y1)
    return (b, x0, y0)
def modinv(a,m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

def inv_pow(c, e):
    low = -1
    high = c+1
    while low + 1 < high:
        m = (low + high) // 2
        p = pow(m, e)
        if p < c:
            low = m
        else:
            high = m
    m = high
    assert pow(m, e) == c
    return m
def division_euclidienne(a, b):
      return (a // b, a % b)
def fraction_continue(n, d):
    developpement = []
    a = n
    b = d
    while b != 0:
        (q,r) = division_euclidienne(a,b)
        developpement.append(q)
        a = b
        b = r
    return (developpement)
def reduites_fraction_continue(a):
    l=len(a)
    reduites=[]
    h0 = 1
    h1 = 0
    k0 = 0
    k1 = 1
    for count in range(l):
        h = a[count] * h1 + h0
        h0 = h1
        h1 = h
        k = a[count] * k1 + k0
        k0 = k1
        k1 = k
        reduites.append((k,h))
    return (reduites)

def floorSqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x


 
 
 

