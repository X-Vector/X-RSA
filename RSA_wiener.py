from banner import *
banner()

#Example :
"""
n = 744818955050534464823866087257532356968231824820271085207879949998948199709147121321290553099733152323288251591199926821010868081248668951049658913424473469563234265317502534369961636698778949885321284313747952124526309774208636874553139856631170172521493735303157992414728027248540362231668996541750186125327789044965306612074232604373780686285181122911537441192943073310204209086616936360770367059427862743272542535703406418700365566693954029683680217414854103
e = 57595780582988797422250554495450258341283036312290233089677435648298040662780680840440367886540630330262961400339569961467848933132138886193931053170732881768402173651699826215256813839287157821765771634896183026173084615451076310999329120859080878365701402596570941770905755711526708704996817430012923885310126572767854017353205940605301573014555030099067727738540219598443066483590687404131524809345134371422575152698769519371943813733026109708642159828957941
c = 305357304207903396563769252433798942116307601421155386799392591523875547772911646596463903009990423488430360340024642675941752455429625701977714941340413671092668556558724798890298527900305625979817567613711275466463556061436226589272364057532769439646178423063839292884115912035826709340674104581566501467826782079168130132642114128193813051474106526430253192254354664739229317787919578462780984845602892238745777946945435746719940312122109575086522598667077632

"""
try:
    import random
    n = int(raw_input(">>> n = "))
    e = int(raw_input(">>> e = "))

    slowprint("\n[+] Please Wait ... \033[95m\n")

    def division_euclidienne(a, b):
      return (a // b, a % b)
    def fraction_continue(n, d):
      developpement = []
      a = n
      b = d
      while b != 0:
        (q,r) = division_euclidienne(a,b)
        developpement.append(q)
        a = b
        b = r
      return (developpement)
    def reduites_fraction_continue(a):
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
    def wiener(n, e):
      fc = fraction_continue(e, n)
      reduites = reduites_fraction_continue(fc)
      message_clair = random.randint(10**1,10**5)
      message_chiffre = pow(message_clair, e, n)
      l = len(reduites)
      i = 0
      while i < l and pow(message_chiffre, reduites[i][1], n) != message_clair:
        i += 1
      if i != l:
        slowprint("[+] Getting d ... \033[95m\n")
        return (reduites[i][1])
      else:
        print("[-] Sorry it's Not Wiener Attack\n")
        exit(0)

    d = wiener(n,e)
    print "\nd = ",d
    check = raw_input("\nYou Have Cipher [y/n] : ")
    if check == "y" or check == "yes":
        c = int(raw_input(">>> c = "))
        slowprint("[+] Getting PlainText ... \033[92m\n")
        decode = pow(c,d,n)
        output = (hex(decode)[2:].replace('L','')).decode("hex")
        slowprint("[+] The PlainText = \033[92m")
        print output
    else :
        slowprint("[+] Thanx For Using X-RSA \033[95m")
        exit()

except ImportError:
    slowprint("\n[-] Module Not Setup")
except ValueError:
    slowprint("\n[-] c,p,q,e Must Be Integar Number")
except AssertionError:
    slowprint("\n[-] Wrong Data")
except KeyboardInterrupt:
    exit()
except Exception:
    slowprint("\n[-] Wrong Data")
except:
    slowprint("\n[-] False Attack !")
