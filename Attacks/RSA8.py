from banner import *
from utilis import Convert
banner()



# Example
#c = 74802199268254280440493690700608296874229186682164386879225634595063352871356558051619716745745659385094914838131944342112615526475056433710891149995541243955498341403563518984577892267288643941

try:
    import gmpy2
    import binascii
    c = int(input(">>> c = "))
    m = gmpy2.iroot(c, 3)[0]
    assert pow(m,3) == c
    Convert(m)
except ImportError:
    slowprint("\n[-] Module Not Setup")
except ValueError:
    slowprint("\n[-] c Must Be Integar Number")
except AssertionError:
    slowprint("\n[-] Wrong Data")
except KeyboardInterrupt:
    exit()
except:
    slowprint("\n[-] False Attack !")
