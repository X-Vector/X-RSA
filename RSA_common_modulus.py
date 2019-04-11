import sys
import platform,os
from urllib2 import *
from platform import system
def slowprint(s):
    for c in s :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(4. / 100)

clear = ""
if "Windows" in platform.system():
	clear = "cls"
if "Linux" in platform.system():
	clear = "clear"
os.system(clear)
is_windows = sys.platform.startswith('win')

# Console Colors
if is_windows:
    # Windows deserves coloring too :D
    G = '\033[92m'  # green
    Y = '\033[93m'  # yellow
    B = '\033[94m'  # blue
    R = '\033[91m'  # red
    W = '\033[0m'   # white
    try:
        import win_unicode_console , colorama
        win_unicode_console.enable()
        colorama.init()
        #Now the unicode will work ^_^
    except:
        print("[!] Error: Coloring libraries not installed, no coloring will be used")
        G = Y = B = R = W = G = Y = B = R = W = ''


else:
    G = '\033[92m'  # green
    Y = '\033[93m'  # yellow
    B = '\033[94m'  # blue
    R = '\033[91m'  # red
    W = '\033[0m'   # white


def banner():
    print("""%s

_____       ________________                  _____      _____
\    \     /    /\          \            _____\    \   /      |_
 \    |   |    /  \    /\    \          /    / \    | /         \\
  \    \ /    /    |   \_\    |        |    |  /___/||     /\    \\
   \    |    /     |      ___/      ____\    \ |   |||    |  |    \\
   /    |    \     |      \  ____  /    /\    \|___|/|     \/      \\
  /    /|\    \   /     /\ \/    \|    |/ \    \     |\      /\     \\
 |____|/ \|____| /_____/ |\______||\____\ /____/|    | \_____\ \_____\\
 |    |   |    | |     | | |     || |   ||    | |    | |     | |     |
 |____|   |____| |_____|/ \|_____| \|___||____|/      \|_____|\|_____|
  %s%s
[ Version : 0.2 ]\033[92m
[ Author  : X-Vector ]\033[96m
[ Github  : github.com/X-Vector ]\033[93m
[ Twitter : twitter.com/@XVector11 ]\033[95m
[ Facebook: facebook.com/X.Vector1 ]\033[95m
[ GreeteZ : Karem Ali ]\033[94m

    """ % (R, W,R))
banner()
try:
    import gmpy2
    from Crypto.Util.number import *
    c1 = int(raw_input(">>> c1 = "))
    c2 = int(raw_input(">>> c2 = "))
    e1 = int(raw_input(">>> e1 = "))
    e2 = int(raw_input(">>> e2 = "))
    n = int(raw_input(">>> n = "))

    slowprint("\n[+] Please Wait ... \033[95m\n")

    def egcd(a, b):
      if (a == 0):
        return (b, 0, 1)
      else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

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
