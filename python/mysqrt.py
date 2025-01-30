from math import sqrt
x=4.0
s=1.0
tol= 0.00000000001
for k in range(1000):
    s0 = s 
    s = 0.5*(s + x/s)
    if (abs(s-s0)<tol):
        break
    print(f"at itteration {k+1}", f"value of s={s}")

print(s)
