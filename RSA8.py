from banner import *
banner()



# Example
#c = 74802199268254280440493690700608296874229186682164386879225634595063352871356558051619716745745659385094914838131944342112615526475056433710891149995541243955498341403563518984577892267288643941

try:
    import gmpy2
    import binascii
    gmpy2.get_context().precision=99999999999999999
    c = int(raw_input(">>> c = "))
    slowprint("\n[+] Please Wait ... \033[95m\n")
    m = gmpy2.iroot(c, 3)[0]
    assert pow(m,3) == c
    def hex_pair(x):
        return ('0' * (len(x) % 2)) + x
    m_hex = '{:x}'.format(m)
    m_hex = hex_pair(m_hex)
    msg = binascii.unhexlify(m_hex)
    slowprint("[+] The PlainText = ")
    print(msg.decode())
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
