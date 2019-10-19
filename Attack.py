from banner import *
banner()
print("""
[1] - Attacks
[2] - Factorization Number
""")
check = int(raw_input(">>> "))
if check == 2:
    import Factorization

elif check == 1: 
    banner()   
    print("""
[1] - Attack(c,n,e) \033[92m
[2] - Attack(c,p,q,e) \033[96m
[3] - Attack (c,n,e,{p or q})
[4] - Attack (c,n,e,dp)
[5] - Attack(c,n,d,e,phi) \033[93m
[6] - Attack(c1,c2,c3,n1,n2,n3,e=3) \033[95m    [ Hasted ]
[7] - Attack(c1,c2,e1,e2,n) \033[96m            [ Common Modulus ]
[8] - Attack(c,p,q,dp,dq) \033[93m              [ Chinese Remainder Theorem ]
[9] - Attack(n,e) \033[95m                      [ Wiener ]
[10] - Attack(c,n,d)\033[0m
[11] - Attack(c,d,n,e)\033[92m
[12] - Attack(c,n,e) \033[93m                   [ Multi Prime Number ]
[13] - Attack(c,e = 3)\033[0m
[14] - Attack(c1,c2,n1,n2,e) \033[96m            [ Common Factor ]
[0] - Exit \033[92m
        """)
    x = int(raw_input(">>> "))
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
        import RSA_common_modulus
    elif x == 8:
        os.system(clear)
        import RSA_chinese_remainder_theorem
    elif x == 9:
        os.system(clear)
        import RSA_wiener
    elif x == 10:
        os.system(clear)
        import RSA4
    elif x == 11:
        os.system(clear)
        import RSA5
    elif x == 12:
        os.system(clear)
        import RSA_multiPrime1
    elif x == 13:
        os.system(clear)
        import RSA8
    elif x == 14:
        os.system(clear)
        import RSA_common_exponent
    else:
        exit()
else:
    exit()
