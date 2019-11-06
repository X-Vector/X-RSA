from banner import *
from utilis import Convert,modinv
banner()

"""
c = 29846947519214575162497413725060412546119233216851184246267357770082463030225
p = 238324208831434331628131715304428889871
q = 296805874594538235115008173244022912163
e = 3
"""

try:
    c = int(input(">>> c = "))
    p = int(input(">>> p = "))
    q = int(input(">>> q = "))
    e = int(input(">>> e = "))

    n = p*q
    phi = (p-1)*(q-1)
    d = modinv(e,phi)
    m = pow(c,d,n)
    Convert(m)

except ImportError:
    slowprint("\n[-] Module Not Setup")
except ValueError:
    slowprint("\n[-] c,p,q,e Must Be Integar Number")
except AssertionError:
    slowprint("\n[-] Wrong Data")
except KeyboardInterrupt:
    exit()

