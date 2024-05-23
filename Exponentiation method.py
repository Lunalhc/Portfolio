# this is the code for for exponentiation method

#-------------------------------------------------------------------------
'''
# squre-and-multiply algorithm

exp = int(input("what's the exponent (square-and-multiply)?"))
bin_exp = bin(exp)[2:]   
l = len(bin_exp)

z = 1
for i in range(1,l):
    
    if bin_exp[i] == "0":
        z = z+z
        bin_z = bin(z) 
        i += 1     
    else:
        z = z+z+1
        bin_z = bin(z)
        i += 1

    print(bin_z[2:])
    
#-------------------------------------------------------------------------

# k-ary method

expo = int(input("what's the exponent (k_ary)?"))
bin_expo = bin(expo)[2:]
k = int(input("what's the k value?"))

pad_length = (k - len(bin_expo) % k) % k  
bin_expo_padded = '0' * pad_length + bin_expo
bin_expo_grouped = [bin_expo_padded[i:i+k] for i in range(0, len(bin_expo_padded), k)]
int_expo_grouped = [int(group, 2) for group in bin_expo_grouped]

expo_current = int_expo_grouped[0]
zero_str = '0' * k
for i in range (1,len(int_expo_grouped)):
    
    if bin_expo_grouped[i] == zero_str:

        for _ in range(k):
            expo_current = expo_current + expo_current
        bin_expo_current = bin(expo_current)[2:]
        pad_length_ = (k - len(bin_expo_current) % k) % k  
        bin_expo_current_padded = '0' * pad_length_ + bin_expo_current
        i += 1
    
    else:
        for _ in range(k):
            expo_current = expo_current + expo_current
        expo_current = expo_current + int_expo_grouped[i]
        bin_expo_current = bin(expo_current)[2:]
        pad_length_ = (k - len(bin_expo_current) % k) % k  
        bin_expo_current_padded = '0' * pad_length_ + bin_expo_current
        i += 1
    
    print(bin_expo_current_padded)

'''
    
#-----------------------------------------------------------------------

