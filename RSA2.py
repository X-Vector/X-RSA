from banner import *
banner()


#c = 29846947519214575162497413725060412546119233216851184246267357770082463030225
#p = 238324208831434331628131715304428889871
#q = 296805874594538235115008173244022912163
#e = 3


try:
    import gmpy
    c = int(raw_input(">>> c = "))
    p = int(raw_input(">>> p = "))
    q = int(raw_input(">>> q = "))
    e = int(raw_input(">>> e = "))
    slowprint("\n[+] Please Wait ... \033[95m\n")
    n = p*q
    phi = (p-1)*(q-1)
    d = gmpy.invert(e,phi)
    m = hex(pow(c,d,n))[2:]
    decode = m.decode('hex')
    slowprint("[+] The PlainText = ")
    print(decode)

except ImportError:
    slowprint("\n[-] Module Not Setup")
except ValueError:
    slowprint("\n[-] c,p,q,e Must Be Integar Number")
except AssertionError:
    slowprint("\n[-] Wrong Data")
except KeyboardInterrupt:
    exit()
except:
    slowprint("\n[-] False Attack !")
