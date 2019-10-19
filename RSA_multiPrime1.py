from banner import *
banner()

"""
c= 3821925911648555519353747434606743159593808677487039861592438384426669998207423450606829031692403202928227703884307291926528640413305346863805555214851644456742958636273721157021584443312591620736285469414067076228984358550669307967587995994219000349054979046909041864106400708453105658165917613077273501
n= 6311257310749529896994764164885908074730315623107218148732436180339784730655096846277587690299624960654670853389184027362495475005388709090759335907428646246751073917955576737663877861242491426053238800688758573959939180213510980211538490409598005851282273664989880554327678869807688158210471903939248513
e= 65537
prime = [2160890461,2247289019,2250778319,2442210431,2458778093,2534226749,2535292559,2546035901,2651829007,2690421313,2737511971,2807722121,2985359177,3074912623,3142693039,3144852421,3159476069,3166527541,3269492927,3328687379,3493484429,3505945799,3538145749,3610828651,3699668617,3715792519,4036077043,4058968889,4089517513,4116792439,4262477123,4291039453]
"""

try:
    from ecm import *
    import binascii
    c = int(raw_input(">>> c = "))
    n = int(raw_input(">>> n = "))
    e = int(raw_input(">>> e = "))
    slowprint("\n[+] Please Wait ... ")
    prime = primefactors(n)
    phi = 1
    for i in prime:
        phi *= i-1
    def egcd(b, n):
        (x0, x1, y0, y1) = (1, 0, 0, 1)
        while n != 0:
            (q, b, n) = (b // n, n, b % n)
            (x0, x1) = (x1, x0 - q * x1)
            (y0, y1) = (y1, y0 - q * y1)
        return (b, x0, y0)
    def modinv(a, m):
        g, x, y = egcd(a, m)
        if g != 1:
            raise Exception('No modular inverse')
        return x%m
    d = modinv(e, phi)
    m = pow(c, d, n)
    def hex_pair(x):
        return ('0' * (len(x) % 2)) + x
    m_hex = '{:x}'.format(m)
    m_hex = hex_pair(m_hex)
    msg = binascii.unhexlify(m_hex)
    slowprint("\n[+] The PlainText = ")
    print(msg.decode(errors="ignore"))

except IndexError:
    slowprint("[-] Sorry Can't Factorize n ")
except ImportError:
    slowprint("\n[-] Module Not Setup")
except ValueError:
    slowprint("\n[-] c,n,e Must Be Integar Number")
except AssertionError:
    slowprint("\n[-] Wrong Data")
except Exception:
    slowprint("\n[-] Wrong Data")
except KeyboardInterrupt:
    exit()
except:
    slowprint("[-] False Attack !")
