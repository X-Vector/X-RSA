from banner import *
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
