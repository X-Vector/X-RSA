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
[ Version : 0.2 ]\033[92m
[ Author  : X-Vector ]\033[96m
[ Github  : github.com/X-Vector ]\033[93m
[ Twitter : twitter.com/@XVector11 ]\033[95m
[ Facebook: facebook.com/X.Vector1 ]\033[95m
[ GreeteZ : Karem Ali ]\033[94m
    """ % (R, W,R))
banner()

print("""
[1] - Attack(c,n,e) \033[92m
[2] - Attack(c,p,q,e) \033[96m
[3] - Attack (c,n,e,{p or q})
[4] - Attack (c,n,e,dp)
[5] - Attack(c,n,d,e,phi) \033[93m
[6] - Attack(c1,c2,c3,n1,n2,n3,e=3) \033[95m    [ Hasted ]
[7] - Attack(n,limit) \033[92m              [ Fermat ]
[8] - Attack(c1,c2,e1,e2,n) \033[96m        [ Common Modulus ]
[9] - Attack(c,p,q,dp,dq) \033[93m          [ Chinese Remainder Theorem ]
[10] - Attack(n,e) \033[95m                  [ Wiener ]
[11] - Attack(c,n,d)\033[0m
[12] - Attack(c,d,n,e)\033[92m
[13] - Attack(c,n,e) \033[93m                [ Multi Prime Number ]
[14] - Attack(c,e = 3)\033[0m
[0] - Exit \033[92m
    """)
x = int(input(">>> "))
if x == 1:
    os.system(clear)
    import RSA
elif x == 2:
    os.system(clear)
    import RSA2
elif x == 3:
    os.system(clear)
    import RSA6
elif x == 4:
    os.system(clear)
    import RSA7
elif x == 5:
    os.system(clear)
    import RSA3
elif x == 6:
    os.system(clear)
    import RSA_hasted
elif x == 7:
    os.system(clear)
    import RSA_fermat
elif x == 8:
    os.system(clear)
    import RSA_common_modulus
elif x == 9:
    os.system(clear)
    import RSA_chinese_remainder_theorem
elif x == 10:
    os.system(clear)
    import RSA_wiener
elif x == 11:
    os.system(clear)
    import RSA4
elif x == 12:
    os.system(clear)
    import RSA5
elif x == 13:
    os.system(clear)
    import RSA_multiPrime1
elif x == 14:
    os.system(clear)
    import RSA8
else:
    slowprint("\t\t\t[+] Thanx For using T00l <3")
    exit()
