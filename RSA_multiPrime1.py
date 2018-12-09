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


from Crypto.PublicKey import RSA
from Crypto.Util import asn1
import binascii
primes = []
def prime_factors(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            primes.append(i)
    if n > 1:
        primes.append(n)
    return primes


c = input(">>> c = ")
n = input(">>> n = ")
e = input(">>> e = ")

#https://www.alpertron.com.ar/ECM.HTM

#Example

#e=65537
#c=948626122185577940383278469624490186926710623520188126435501983438183336907186255794618530332289368021291789118954846772779855308711280972165698348170051078399678590370050111906031923460860172422708816752545784573579942145045344015318568999211937934532123400243017531300488990627956390410869348218289952
#primes = [2162771687,2180377501,2181902579,2183410837,2234829049,2259158687,2366491411,2494545509,2528730847,2591025083,2603976511,2691605771,2714412037,2808388853,2847171653,2870886637,2890555183,2939087189,3000625669,3175105811,3226441579,3265841311,3499273711,3544821197,3611944027,3677851391,3692380933,3696854989,4067996287,4133178029,4212919157,4224110131]

os.system(clear)
banner()

print("[!!] Ok , Now :\n1 - You Can Factorize (n) Auto With X-RSA \t[ it Take Much Time ]\n2 - You Can Factorize (n) in This Site https://www.alpertron.com.ar/ECM.HTM \t [ Recommend ]\n")
check = int(input(">>> "))
if check == 1:
    slowprint("\n[+] Please Wait ... \033[95m")
    slowprint("\n[+] it Take Much Time ... \033[95m\n")
    prime_factors(n)
elif check == 2:
    slowprint("\n[+] How Many Prime Number =  \033[95m\n")
    count = int(input(">>> "))
    print "\n"
    for i in range(count):
        print "Enter The",(i+1),"Number"
        i = int(input(">>> "))
        primes.append(i)

phi = 1
for prime in primes:
    phi *= (prime-1)


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    g, y, x = egcd(b%a,a)
    return (g, x - (b//a) * y, y)

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
