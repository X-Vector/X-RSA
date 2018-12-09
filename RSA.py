#!/usr/bin/env python2
#-*- coding: utf-8 -*-
#
# author : X-Vector
# Tested on Kali Linux / Parrot Os / Ubuntu
# Simple script for RSA Attack
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

import binascii
import gmpy2



# Example 1 :
#c = 194048013822218245260658018019940874060627700835842604475987702337533801266490182061968998210807564778328557627772974110046885380635225974269865976518335375789734689098164529086561756412074742698644530189076800227300946408167039318949544794351233987752575608106800908043533012088081995031010618521695843625062
#n = 248501410365662412791489552646042256782092770118253438700194718631291036762726489658495565276550205113648626040596191969135846656414394584577305526761671104277390765264806022908497647300596494542202565022133435383403344333672279722534625284520459706609569974491538689429548817677759350947931780871046796607829
#e = 65537

# Example 2 :
#n = 95927091022214131235859313618337025685657931350656500630264132698389852599510198358308813869652616688807245375001990146888881030682552800587836982145527192151998189057703804830882536718184311723290034393819853924918814439601355616561237190273205228499357454477829605938284765657202538703493014172555332956153
#e = 3
#c = 74802199268254280440493690700608296874229186682164386879225634595063352871356558051619716745745659385094914838131944342112615526475056433710891149995541243955498341403563518984577892267288643941


c = input(">>> c = ")
n = input(">>> n = ")
e = input(">>> e = ")


gmpy2.get_context().precision=200
m = gmpy2.iroot(c, e)[0]
try:
    if pow(m,e) == c:
        slowprint("\n[+] Please Wait ... \033[95m\n")
        def hex_pair(x):
            return ('0' * (len(x) % 2)) + x
        m_hex = '{:x}'.format(m)
        m_hex = hex_pair(m_hex)
        msg = binascii.unhexlify(m_hex)
        slowprint("[+] The PlainText = ")
        print(msg.decode())
    else:
        slowprint("\n[+] Please Wait ... \033[95m\n")
        factordb = RSA.attacks.factordb(n)
        q = factordb[0]
        p = factordb[1]
        phi = (p-1)*(q-1)
        def egcd(a,b):
            if a == 0 :
                return(b,0,1)
            else:
                g,y,x = egcd(b%a,a)
                return (g,x-(b/a)*y,y)

        def modinv(a,m):
            g,x,y = egcd(a,m)
            if g != 1:
                raise Expection("RSA Hello")
            else :
                return x%m

        d = modinv(e,phi)
        decode = pow(c,d,n)
        output = (hex(decode)[2:].replace('L','')).decode("hex")
        slowprint("[+] The PlainText = ")
        print(output)

except IndexError:
    slowprint("[-] Sorry Can't Factorize n :( ")
    slowprint("\n[!] Try To Use MultiPrime Attack ")
except:
    slowprint("[-] False Attack !! ")
