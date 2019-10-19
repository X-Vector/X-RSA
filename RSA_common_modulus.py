from banner import *
banner()
try:
    import gmpy2
    from Crypto.Util.number import *
    
    def egcd(b, n):
        (x0, x1, y0, y1) = (1, 0, 0, 1)
        while n != 0:
            (q, b, n) = (b // n, n, b % n)
            (x0, x1) = (x1, x0 - q * x1)
            (y0, y1) = (y1, y0 - q * y1)
        return (b, x0, y0)

    # Calculates a^{b} mod n when b is negative
    def neg_pow(a, b, n):
    	assert b < 0
    	assert GCD(a, n) == 1
    	res = int(gmpy2.invert(a, n))
    	res = pow(res, b*(-1), n)
    	return res


    def common_modulus(e1, e2, n, c1, c2):
    	g, a, b = egcd(e1, e2)
    	if a < 0:
    		c1 = neg_pow(c1, a, n)
    	else:
    		c1 = pow(c1, a, n)
    	if b < 0:
    		c2 = neg_pow(c2, b, n)
    	else:
    		c2 = pow(c2, b, n)
    	ct = c1*c2 % n
    	m = int(gmpy2.iroot(ct, g)[0])
    	return long_to_bytes(m)

    c1 = int(raw_input(">>> c1 = "))
    c2 = int(raw_input(">>> c2 = "))
    e1 = int(raw_input(">>> e1 = "))
    e2 = int(raw_input(">>> e2 = "))
    n = int(raw_input(">>> n = "))

    slowprint("\n[+] Please Wait ... \033[95m\n")
    slowprint("[+] The PlainText = ")
    print common_modulus(e1, e2, n, c1, c2)
except ImportError:
    slowprint("\n[-] Module Not Setup")
except ValueError:
    slowprint("\n[-] e1, e2, n, c1, c2 Must Be Integar Number")
except AssertionError:
    slowprint("\n[-] Wrong Data")
except KeyboardInterrupt:
    exit()
except:
    slowprint("\n[-] False Attack !")
