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
try:
    from Crypto.PublicKey import RSA
    import sympy as sp
    import math
except ImportError:
    slowprint("\n[-] Module Not Setup")
"""
#n = 441702548375597546265397060347208952276967475274905135912477869560482177333510361384285033947480946188145623354029215951664169885735094097025317925522966956898965174945445544364452506966796499944587005657873812585848386501149925011035458189838748181551356757610548391767844207725796544451539421763642181449329080300719368344152034024278647417306053843499995586981318017650558507022155655502745770884654996618443849292140572931614016663705074656028412717677339714961533961375052773639815540324868758969940933964991941461245158471917647200963814004656567184986255121144463936821101981682767655530654441359046234900674147458678928268719664791590208181725402425003322043157763682685830046581059368233541228450498829982145850640255968763746232611610641869191302389245779111356909617313529277007241602005067848947949307502548984897136138368091937447795052112684321369869694696022995282137270503420632588160475186971207198459134307608759756767731733884585073817881348559945137106821730698056732508316693757300672313883162959195685130393016049081156405669205548223148112949446059403857423978820671852027526778494740114169769151540080734651779260084907492653816632846142736609605163394526211986727369288330063666919831047575220019292555559557
#e = 65537
#d = 20929658227875938261058725840264131720240194797254721497929999366502087574029656881231720165783065592372637815940915666212613039099487922843233911353847485450062009142435445746729639472299106954973763080234456847113054478990804619551767588431261008218457316621723802599302359261042715498257923026077002571619206016545993843650901654469988654046781302853813921776892035397733517301594459235978192450212096281249109282450379464222318996342527212038893311335406614944259596938858799625134827471785811994514192796802507658154603626182055262115513322362471136252282318391917574551672482430283925389405151320872665308738881
#c =  223986220247071217870216666779014143338794244806897003439570261828585609461069625566993441707552858342245944642945164681672765137831785039339186019388055221324788275090628463675778644169814393286912058814837219760390476510773975243291075922094945253348123263684444264887680045467214228402806502985409400661033608167210517145287411533259812656955874094033211161421678440562053003042479607653554525213535393053262147643051962890823534380167045346153321162009201462563059751490608169219660707113678434438625268806729271472128212898965284892857326073914569265528121606803508514214189119223383833552072586814770466728871437446190820676075097507547134736007108263775508884871752392084557481102147503606249246354860813514035927154754953172611572565854652996865901035897405554136502508927222416891115275427864126981053248969607448749019664721233739296140343775145313825978714021202368146466869500962807323607852112530742349058090066478686837929805776585570594765868633295031229876778165218553418581369590926767847888849449544777172583513049998378026545824378239267780173494553559807077301106319453742180763436936829925045341906074598727300955137592558540978215844567601254095649299172760605263652690076724946138284654947266095386055238602230
"""

def premRSA(n,e,d,c):
    bitLenN = int(sp.floor(sp.log(n)/sp.log(2)) + 1)
    bitLenD0 = 2048

    assert bitLenD0 >= bitLenN/2

    d = halfdPartialKeyRecoveryAttack(d,2048,4096,n,e)
    c = pow(c,d,n)
    plaintext = str(bytearray(hex(c)[2:])).replace("L","")
    slowprint("[+] The PlainText = ")
    print(plaintext.decode("hex"))

def halfdPartialKeyRecoveryAttack(d0,d0BitSize,nBitSize,n="n",e="e"):
    test = pow(3, e, n)
    test2 = pow(5, e, n)
    for k in range(1,e):
        d = ((k * n + 1) // e)
        d >>= d0BitSize
        d <<= d0BitSize
        d |= d0
        if((e * d) % k == 1):
            if pow(test, d, n) == 3:
                if pow(test2, d, n) == 5:
                    totientN = (e*d - 1) // k
                    b = totientN - n - 1
                    discriminant = b*b - 4*n
                    root = floorSqrt(discriminant)
                    if(root*root != discriminant):
                        continue
                    p = (-b + root) // 2
                    q = n // p
                    return d


def extended_gcd(aa, bb):
    lastremainder, remainder = abs(aa), abs(bb)
    x, lastx, y, lasty = 0, 1, 1, 0
    while remainder:
        lastremainder, (quotient, remainder) = remainder, divmod(lastremainder, remainder)
        x, lastx = lastx - quotient*x, x
        y, lasty = lasty - quotient*y, y
    return lastremainder, lastx * (-1 if aa < 0 else 1), lasty * (-1 if bb < 0 else 1)

def modinv(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise ValueError
    return x % m

def floorSqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x




try:
    c = int(raw_input(">>> c = "))
    n = int(raw_input(">>> n = "))
    e = int(raw_input(">>> e = "))
    d = int(raw_input(">>> d = "))
    slowprint("\n[+] Please Wait ... \033[95m\n")
    premRSA(n,e,d,c)

except ValueError:
    slowprint("\n[-] c,n,d,e Must Be Integar Number")
except AssertionError:
    slowprint("\n[-] Wrong Data")
except KeyboardInterrupt:
    exit()
except:
    slowprint("\n[-] False Attack !")
