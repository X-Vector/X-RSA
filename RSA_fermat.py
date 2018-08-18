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

n = input(">>> n = ")
limit = input(">>> limit = ")

slowprint("\n[+] Please Wait ... \033[95m\n")


import sys
import math
import Crypto.PublicKey.RSA
import fractions
import random
import argparse
class Fermat(object):
    def accueil(self):
        slowprint("[+] Getting info ... ")
    def carre_parfait(self, x):
      if x < 1:
        return(False)
      sqrt_x = math.sqrt(x)
      return (sqrt_x == int(math.floor(sqrt_x)))
    def fermat(self,n):
      a = 2*math.ceil(math.sqrt(n)) + 1
      aux = 2 * a +1
      n4 = 4 * n
      c = pow(a, 2) - n4
      while not carre_parfait(c):
        c += aux
        a += 1
        aux += 2
      b = int(math.sqrt(c))
      p = (a - b) // 2
      q = (a + b) // 2
      if (p*q != n):
        slowprint("Error!")
        exit(0)
      return (p, q)
    def indicatrice_euler(self, p, q):
      return((p - 1) * (q - 1))
    def bezout(self, a, b):
        if a == 0 and b == 0:
          return (0, 0, 0)
        if b == 0:
          return (a // abs(a), 0, abs(a))
        (u, v, p) = self.bezout(b, a % b)
        return (v, (u - v * (a // b)), p)
    def inv_modulo(self, x, m):
      (u, _, p) = self.bezout(x, m)
      return u % abs(m)
    def __init__(self, n, e):
        self.accueil()
        try:
            (p, q) = self.fermat(n, e)
        except:
            slowprint("\n[-] Sorry This RSA public key isn't a valide candidate for a Fermat Attack\n")
            exit()
        print("\n\t[+] Factorization = {} * {}\n".format(p,q))
        phi = indicatrice_euler(p,q)
        self.d = inv_modulo(e, phi)
        print("[+] d = {}\n".format(d))

Fermat(n,limit)
