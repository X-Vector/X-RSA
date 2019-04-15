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
"""
e = 65537
n = 642313240848064014975043934308658242447312485152342673610756859535090103704610472004913349502648157091104463303511131278665176160214474038294042375555935567033107229886104534241324327133387923226576002115108963521725703773387678635509903034467838260875686083768549775481391190161412646384559222421917626615323
dp = 17765378008759755288183210466105878526943875374957170036175281330288884608317141953683920408636506981101765935449140323585600732241535721917282237462133813
c = 147903288008907053469880199469959588903705520519775597541160700501753344741954421604588338524905987922631822425828587114084662512860181022047137469441292833823381362238861070683420786510831001513730638949486694641768638258876688738949817816449109334961820861920165271653627904957302093274915248851406573361863
"""

try:
    c = int(raw_input(">>> c = "))
    n = int(raw_input(">>> n = "))
    e = int(raw_input(">>> e = "))
    dp = int(raw_input(">>> dp = "))

    mp = (dp * e) - 1
    for i in range(2,1000000):
       p = (mp / i) + 1
       if n % p == 0:
           break
    q = n/p
    slowprint("\n[+] Please Wait ... \033[95m\n")
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
            raise Expection("[-] Sorry")
        else :
            return x%m

    d = modinv(e,phi)
    decode = pow(c,d,n)
    output = (hex(decode)[2:].replace('L','')).decode("hex")
    slowprint("[+] The PlainText = ")
    print(output)

except ValueError:
    slowprint("\n[-] c,n,e,dp Must Be Integar Number")
except AssertionError:
    slowprint("\n[-] Wrong Data")
except KeyboardInterrupt:
    exit()
except:
    slowprint("\n[-] False Attack !")
