from math import sqrt
x=2.0
s=1.0
tol= 10e-12
for k in range(1000):
    s0 = s 
    s = 0.5*(s + x/s)
    if (abs(s-s0)<tol):
        break
    print(f"at itteration {k+1}", f"value of s={s}")

print("Final value of root is:",s)
