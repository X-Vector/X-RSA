import sys
import platform,os
from urllib2 import *
from platform import system
def slowprint(s):
    for c in s + '\n':
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
[ Version : 0.1 ]\033[92m
[ Author  : X-Vector ]\033[96m
[ Github  : github.com/X-Vector ]\033[93m
[ Twitter : twitter.com/@XVector11 ]\033[95m
[ Facebook: facebook.com/X.Vector1 ]\033[95m
[ GreeteZ : Karem Ali ]\033[94m

    """ % (R, W,R))
banner()
c1 = input(">>> c1 = ")
c2 = input(">>> c2 = ")
e1 = input(">>> e1 = ")
e2 = input(">>> e2 = ")
n  = input(">>> n = ")

slowprint("\n[+] Please Wait ... \033[95m\n")


from sys import setrecursionlimit
import codecs
class Comod(object):
    def accueil(self):
        slowprint("[+] Getting info ... ")
    setrecursionlimit(1000000)
    def xgcd(self, a, b):
      if a == 0:
        return (b, 0, 1)
      else:
        gcd, u, v = self.xgcd(b % a, a)
        return (gcd, v - (b // a) * u, u)
    def modinv(self, a, n):
      g, x, y = self.xgcd(a, n)
      return x % n
    def pow_mod(self, a, b, n):
      number = 1
      while b:
        if b & 1:
          number = number * a % n
        b >>= 1
        a = a * a % n
      return number
    def __init__(self, n, e1, e2, c1, c2):

      self.accueil()
      egcd = self.xgcd(e1, e2)
      u, v = egcd[1], egcd[2]
      if u >= 0:
        p1 = self.pow_mod(c1,u,n)
      else:
        p1 = self.modinv(self.pow_mod(c1,-u,n),n)
      if v >= 0:
        p2 = self.pow_mod(c2,v,n)
      else:
        p2 = self.modinv(self.pow_mod(c2,(-v),n),n)
      res = (p1 * p2) % n
      print "\n\t[+] Decimal plaintext: ",res,"\n"
      try:
        plaintext = codecs.decode(hex(res)[2:].replace('L',''))
        print "\t[+] Interpreted plaintext: ",plaintext,"\n"
      except:
        print "\t[-] The plaintext isn't interpretable\n"
Comod(n, e1, e2, c1, c2)
