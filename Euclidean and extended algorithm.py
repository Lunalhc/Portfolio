# Euclidean algorithm
# our goal is to find gcd(r_0,r_1)

q = []
r = []

r_0 = int(input("pick an integer r_0:"))
r_1 = int(input("pickan integer r_1 that is less than r_0:"))
r.append(r_0)
r.append(r_1)

q_1 = divmod(r_0,r_1)[0]
q.append(q_1)


for i in range(1000):

    print(f"iteration {i}:")

    q_current = divmod(r[i], r[i+1])[0]
    q.append(q_current)
    print(f"q = {q}")

    r_current = (divmod(r[i], r[i+1])[1])
    r.append(r_current)
    print(f"r = {r}")

    print(f"gcd({r[i],r[i+1]}) = gcd({r[i+1],r[i+2]})")
    
    if r_current == 0:
        gcd_result = r[i+1]
        print(f"gcd({r_0},{r_1} is {gcd_result})")
        break


print("--------------------------------------------------------------------------------------------------------------------")
# extended euclidean algorithm
# our goal is to find gcd(a,m) and inverse of a in Z_m

q = [q_1]
r = [r_0,r_1]
a = r_0
m = r_1
t = [0,1]

for i in range(1000):

    print(f"iteration {i}:")

    q_current = divmod(r[i], r[i+1])[0]
    q.append(q_current)
    print(f"q = {q}")

    t_current = t[i] - q_current * t[i+1]
    t.append(t_current)
    print(f"t = {t}")

    r_current = (divmod(r[i], r[i+1])[1])
    r.append(r_current)
    print(f"r = {r}")

    
    if r_current == 0:
        inverse_result = t[i+1] % a
        print(f"inverse of {m} is {inverse_result}.")
        break

