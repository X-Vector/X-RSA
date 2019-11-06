from banner import *
from utilis import egcd,modinv,Convert
from Factorizations.factordb import *
banner()

"""
# Example :
c = 194048013822218245260658018019940874060627700835842604475987702337533801266490182061968998210807564778328557627772974110046885380635225974269865976518335375789734689098164529086561756412074742698644530189076800227300946408167039318949544794351233987752575608106800908043533012088081995031010618521695843625062
n = 248501410365662412791489552646042256782092770118253438700194718631291036762726489658495565276550205113648626040596191969135846656414394584577305526761671104277390765264806022908497647300596494542202565022133435383403344333672279722534625284520459706609569974491538689429548817677759350947931780871046796607829
e = 65537
"""

try:
    
    def factordb(n):
        f =  FactorDB(n)
        f.connect()
        return f.get_factor_list()

    c = int(input(">>> c = "))
    n = int(input(">>> n = "))
    e = int(input(">>> e = "))

    factordb = factordb(n)
    q = factordb[0]
    p = factordb[1]
    phi = (p-1)*(q-1)
    d = modinv(e,phi)
    decode = pow(c,d,n)
    Convert(decode)

except IndexError:
    slowprint("[-] Sorry Can't Factorize n ")
    slowprint("\n[!] Try To Use MultiPrime Attack ")
except ImportError:
    slowprint("\n[-] Module Not Setup")
except ValueError:
    slowprint("\n[-] c, e, n Must Be Integar Number")
except AssertionError:
    slowprint("\n[-] Wrong Data")
except KeyboardInterrupt:
    exit()
except requests.exceptions.ConnectionError:
    slowprint("\n[-] Check Your Internet")
except:
    slowprint("False Attack")
