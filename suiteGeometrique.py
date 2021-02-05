s=0
n=0
V0=1.65
while 2**n  <= 16384 :
    s = 2**n * V0
    print(2**n, "euror(s)", "=", s, "dollar(s)")
    n+=1
