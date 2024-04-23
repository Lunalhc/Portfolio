# binary extended euclidean algorithm
# our goal is to compute gcd(r_0,r_1) and inverse of r_1 if r_0 r_1 are relatively prime

r_0 = int(input("pick an integer r_0:"))
r_1 = int(input("pick an integer r_1 that is less than r_0:"))

g = 1

while r_0 % 2 == 0 and r_1 % 2 == 0:

    r_0 = r_0//2  
    r_1 = r_1//2  
    g = 2*g   

u = r_0
v = r_1
A = 1
B = 0
C = 0
D = 1



for i in range(10):

    while u % 2 == 0:
        u = u/2   
        if A % 2 == 0 and B % 2 == 0:
            A = A//2
            B = B//2
        else:
            A = (A + r_1)//2   
            B = (B - r_0)//2   

      

    while v % 2 == 0:
        v = v//2
        if C % 2 == 0 and D % 2 == 0:
            C = C//2
            D = D//2
        else:
            C = (C + r_1)//2
            D = (D - r_0)//2
    
   
    if u >= v:
        u = u-v   
        A = A - C  
        B = B - D  
    else:
        v = v -u
        C = C - A
        D = D - B
    

    if u == 0:
        gcd_result = v * g   
        print(f"gcd = {gcd_result}")
        
        if gcd_result == 1:
            inverse_result = D % r_0
            print(f"inverse = {inverse_result}")
            break
        else:
            break
    else:
        i += 1
