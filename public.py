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
[ Version : 0.1 ]\033[92m
[ Author  : X-Vector ]\033[96m
[ Github  : github.com/X-Vector ]\033[93m
[ Twitter : twitter.com/@XVector11 ]\033[95m
[ Facebook: facebook.com/X.Vector1 ]\033[95m
[ GreeteZ : Karem Ali ]\033[94m

    """ % (R, W,R))
banner()

import argparse
from Crypto.PublicKey import RSA

k = raw_input("Enter Path of Public Key : ")
try:
    key=RSA.importKey(open(k, 'r').read())
    slowprint("[+] Please Wait ... ")
    n = key.n
    e = key.e

    from CryptoLib.RSA import RSA
    import binascii


    factordb = RSA.attacks.factordb(n)
    q = factordb[0]
    p = factordb[1]

    slowprint("[+] Getting n,p,q,d,e ... ")


    print("\n[+] n = {}".format(str(n)))
    print("\n[+] e = {}".format(str(e)))
    print("\n[+] p = {}".format(str(p)))
    print("\n[+] q = {}".format(str(q)))

    import random
    import Crypto.PublicKey.RSA
    class Wiener(object):
        def accueil(self):
            slowprint("")

        def division_euclidienne(self, a, b):
          return (a // b, a % b)
        def fraction_continue(self, n, d):
          developpement = []
          a = n
          b = d
          while b != 0:
            (q,r) = self.division_euclidienne(a,b)
            developpement.append(q)
            a = b
            b = r
          return (developpement)
        def reduites_fraction_continue(self, a):
          l=len(a)
          reduites=[]
          h0 = 1
          h1 = 0
          k0 = 0
          k1 = 1
          count = 0
          while count < l:
            h = a[count] * h1 + h0
            h0 = h1
            h1 = h
            k = a[count] * k1 + k0
            k0 = k1
            k1 = k
            reduites.append((k,h))
            count += 1
          return (reduites)
        def wiener(self, n, e):
          fc = self.fraction_continue(e, n)
          reduites = self.reduites_fraction_continue(fc)
          message_clair = random.randint(10**1,10**5)
          message_chiffre = pow(message_clair, e, n)
          l = len(reduites)
          i = 0
          while i < l and pow(message_chiffre, reduites[i][1], n) != message_clair:
            i += 1
          if i != l:
            return (reduites[i][1])
          else:
            print("\t[-] This RSA public key isn't a valid candidate to a Wiener Attack\n")
            exit(0)
        def __init__(self, n, e):
            self.accueil()
            self.d = self.wiener(n, e)
            print ("[+] d = {}".format(self.d))
    Wiener(n,e)
    slowprint("\n[+] Thanx For Using X-RSA Tool <3  \033[95m\n")
except:
    slowprint("[-] False Attack !! ")
