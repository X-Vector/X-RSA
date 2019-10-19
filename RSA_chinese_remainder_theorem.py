from banner import *
banner()
"""
#Example

c = 62078086677416686867183857957350338314446280912673392448065026850212685326551183962056495964579782325302082054393933682265772802750887293602432512967994805549965020916953644635965916607925335639027579187435180607475963322465417758959002385451863122106487834784688029167720175128082066670945625067803812970871
p = 7901324502264899236349230781143813838831920474669364339844939631481665770635584819958931021644265960578585153616742963330195946431321644921572803658406281
q = 12802918451444044622583757703752066118180068668479378778928741088302355425977192996799623998720429594346778865275391307730988819243843851683079000293815051
dp = 5540655028622021934429306287937775291955623308965208384582009857376053583575510784169616065113641391169613969813652523507421157045377898542386933198269451
dq = 9066897320308834206952359399737747311983309062764178906269475847173966073567988170415839954996322314157438770225952491560052871464136163421892050057498651
"""




try:
    c = int(raw_input(">>> c = "))
    p = int(raw_input(">>> p = "))
    q = int(raw_input(">>> q = "))
    dp = int(raw_input(">>> dp = "))
    dp = int(raw_input(">>> dq = "))
    slowprint("\n[+] Please Wait ... \033[95m\n")

    def egcd(b, n):
        (x0, x1, y0, y1) = (1, 0, 0, 1)
        while n != 0:
            (q, b, n) = (b // n, n, b % n)
            (x0, x1) = (x1, x0 - q * x1)
            (y0, y1) = (y1, y0 - q * y1)
        return (b, x0, y0)
    def modinv(a,m):
        g, x, y = egcd(a, m)
        if g != 1:
            raise Exception('modular inverse does not exist')
        else:
            return x % m
    def chinese_remainder_theorem(p,q,dp,dq,chipher_text):
        q_inv = modinv(p , q)
        m1 = pow(chipher_text,dp,p)
        m2 = pow(chipher_text,dq,q)
        h = (q_inv*(m1-m2)) % p
        return m2 + h * q
    decode = hex(chinese_remainder_theorem(p,q,dp,dq,c))[2:].replace('L','')
    slowprint("[+] The PlainText = ")
    print decode.decode("hex")
except ValueError:
    slowprint("\n[-] c,p,q,dp,dq Must Be Integar Number")
except AssertionError:
    slowprint("\n[-] Wrong Data")
except KeyboardInterrupt:
    exit()
except:
    slowprint("\n[-] False Attack !")
