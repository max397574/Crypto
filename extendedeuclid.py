def extended_gcd(p,q):
    if p == 0:
        return (q, 0, 1)
    else:
        (gcd, u, v) = extended_gcd(q % p, p)
        return (gcd, v - (q // p) * u, u)

p = 20 
q = 10

gcd, u, v = extended_gcd(p, q)
print("p*u+q*v=gcd(p,q)")
print("[+] GCD: {}".format(gcd))
print("[+] u,v: {},{}".format(u,v))
