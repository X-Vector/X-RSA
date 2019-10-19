from banner import *
banner()

# Example :
#c = 194048013822218245260658018019940874060627700835842604475987702337533801266490182061968998210807564778328557627772974110046885380635225974269865976518335375789734689098164529086561756412074742698644530189076800227300946408167039318949544794351233987752575608106800908043533012088081995031010618521695843625062
#n = 248501410365662412791489552646042256782092770118253438700194718631291036762726489658495565276550205113648626040596191969135846656414394584577305526761671104277390765264806022908497647300596494542202565022133435383403344333672279722534625284520459706609569974491538689429548817677759350947931780871046796607829
#e = 65537

try:
    import binascii
    import gmpy2
    from factordb import *
    def factordb(n):
        f =  FactorDB(n)
        f.connect()
        return f.get_factor_list()

    c = int(raw_input(">>> c = "))
    n = int(raw_input(">>> n = "))
    e = int(raw_input(">>> e = "))
    slowprint("\n[+] Please Wait ... \033[95m\n")
    factordb = factordb(n)
    q = factordb[0]
    p = factordb[1]
    phi = (p-1)*(q-1)
    def egcd(b, n):
        (x0, x1, y0, y1) = (1, 0, 0, 1)
        while n != 0:
            (q, b, n) = (b // n, n, b % n)
            (x0, x1) = (x1, x0 - q * x1)
            (y0, y1) = (y1, y0 - q * y1)
        return (b, x0, y0)

    def modinv(a,m):
        g,x,y = egcd(a,m)
        if g != 1:
            raise Expection("RSA Hello")
        else :
            return x%m

    d = modinv(e,phi)
    decode = pow(c,d,n)
    output = (hex(decode)[2:].replace('L','')).decode("hex")
    slowprint("[+] The PlainText = ")
    print(output)

except IndexError:
    slowprint("[-] Sorry Can't Factorize n :( ")
    slowprint("\n[!] Try To Use MultiPrime Attack ")
except ImportError:
    slowprint("\n[-] Module Not Setup")
except ValueError:
    slowprint("\n[-] c, e, n Must Be Integar Number")
except AssertionError:
    slowprint("\n[-] Wrong Data")
except KeyboardInterrupt:
    exit()
except:
    slowprint("\n[-] False Attack !")
