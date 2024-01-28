import math


def get_alphabet_table(alphabet,shift,n):  # create an alphabet table according to the alphabet and shift

    alphabet_table = {}   # create an empty letter-to-number dictionary

    for i, letter in enumerate(alphabet):     # for each letter in the alphabet

        alphabet_table[letter] = (i + shift) % n    # assign the letter with preferred shift and store it in the dictionary

    return alphabet_table

def find_possible_a (n):  # find all the possible a we can use accoring to the shift

    a_list = []   # an empty list for possible a values
    for number in range(1,n):   # find all the numbers on the interval that is relative prime to n from 0 to n not including n

        if math.gcd(number,n) == 1:   # check which number is relative prime to n
            a_list.append(number)    # add it to the possible a list

    return a_list


def find_inverse(input,n):    # find inverse of a in a group with group size n
    
    a_inverse = 0   # initialize the a inverse
    for number in range(0,n-1):  # for each number in the group

        if (input * number) % n == 1:   # if a times this number mod n equals to the multiplicative identity 1
            a_inverse = number   # then this number is the inverse
    
    return a_inverse


def solve_for_a (x1, y1, x2, y2, n):  # find a when 2 pairs of x,y values are known
    
    difference_y = y2 - y1    # difference of 2 ys
    if difference_y < 0:      # if it's negative
        difference_y += n   # use mod operation
    
    difference_x = x2 - x1   # difference of 2 xs
    if difference_x < 0:    # if it's negative
        difference_x += n   # use mod operation

    difference_y_inverse = find_inverse(difference_x, n)   # find inverse of the difference of 2 ys

    a = (difference_y_inverse * difference_y) % n   # use this operation and we get a

    return a



def solve_for_b(a, x1, y1, n):    # find b after we know a

    difference = y1 - (a * x1)   # operation to find the difference 
    if difference < 0:   # if it's negative
        difference += n      # use mod operation

    b = difference % n   # use this operation and we get b

    return b


def text_to_number(text,alphabet_table):   # a function that can convert plaintext to its corresponding number version

    result = []     # create a list to store the number version later
    for letter in text:    # for each letter in the plaintext

        letter = alphabet_table[letter]     # assign the letter with its corresponding value in the dictionary
        result.append(letter)      # add the value to the result list
    

    return result


def decryption(n,a_inverse,ciphertext_number,b):  # convert number version of ciphertext to number version of plaintext
    
    plaintext_number = []   # create an empty list to store plaintext in number
    for y in ciphertext_number:   # for each number in number version of ciphertext

        d_k = (a_inverse * (y-b)) % n  # the operation to get plaintext number
        plaintext_number.append(d_k)   # put it in the list
    
    return plaintext_number









# we know 2 pairs of xys and want to find the key(a,b)
if __name__ == "__main__":  

    default_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  
        
    alphabet_choice = input("please type the alphabet you are using in uppercase\n type 1 if you want to use default alphabet\n")  # enter the alphabet we want to use
    if alphabet_choice == "1":  
        Alphabet = default_alphabet  # use default english alphabet
    else:
        Alphabet = alphabet_choice

    Letter1 = input("type the first letter you know in uppercase\n")   # ask user the first known letter
    Letter1_map = input("type the letter that the first letter maps to\n")  # ask user what the first letter maps to
    Letter2 = input("type the second letter you know in uppercase\n")  # ask user the second known letter
    Letter2_map = input("type the letter that the second letter maps to\n")  # ask user what the second letter maps to


    N = sum(1 for letter in Alphabet)   # calculate the size of the alphabet
    
    key_list = []  # en empty list to store all possible keys (in pairs)

    for shift in range(0,N):  # try any possible shift on the interval

        Alphabet_table = get_alphabet_table(Alphabet,shift,N)  # create an alphabet table based on the shift
            
        X1 = Alphabet_table[Letter1]  # find the number that represents the first known letter from the dictionary
        X2 = Alphabet_table[Letter2]  # find the number that represents the second known letter from the dictionary
        Y1 = Alphabet_table[Letter1_map]  # find the number that represents what the first known letter maps to
        Y2 = Alphabet_table[Letter2_map]  # find the numbe rthat represents what the second known letter maps to

        A_list = find_possible_a(N)   # get the list of all possible a values so that a inverse exists
        difference_y = Y2 - Y1    # difference of 2 ys
        if difference_y < 0:      # if it's negative
            difference_y += N   # use mod operation
    
        if difference_y in A_list:  # if y difference has an inverse

            a = solve_for_a(X1,Y1,X2,Y2,N)   # find a 
            b = solve_for_b(a,X1,Y1,N)      # find b
            print(f"if the shift is {shift}, the key is {a,b}")
            key_list.append((a,b))  # put it into the list in pairs

        else:  # if y difference doesn't have an inverse
            print("the y difference doesn't have aN inverse. please choose another 2 pairs\n")
            break    # stop the for loop

    A_inverse_list = []   # an empty list to store all possible a inverses
    for key in key_list:   # for each key in the possible key list

        a = key[0]   # grab the a

        A_inverse = find_inverse(a,N)  # get a inverse
        A_inverse_list.append(A_inverse)  # out it into the a inverse list
    
    decision = input("type 1 to continue, 0 to exit\n")   # ask if you want to keep decrypt
    if decision == "1":

        Ciphertext = input("type the ciphertext in uppercase you want to decrypt:\n")  # ask the user for the ciphertext to be decrypted
        
        i = 0   # initilize the iteration times
        for key in key_list:   # for each pair of key in the key list
            
            alphabet_table = get_alphabet_table(Alphabet, i, N)  # create the corresponding alphabet table (based on shift value)
        
            Ciphertext_number = text_to_number(Ciphertext, alphabet_table)  # convert ciphertext to number

            a_inverse = A_inverse_list[i]  # grab the a inverse from a inverse list based on the iteration number i
            b = key[1]   # grab b from the key pair

            Plaintext_number = decryption(N,a_inverse,Ciphertext_number,b)  # decrypt the number version of ciphertext to number version of plaintext
            
            Plaintext = []   # empty list to store future plaintext
            for number in Plaintext_number:   # for each number in the number version plaintext

                letter = [key for key, value in alphabet_table.items() if value == number]  # fine the letter that the number represents from the alphabet tabel
                Plaintext.append(letter)   # add the letter to the plaintext list

            Plaintext_list = [item for sublist in Plaintext for item in sublist]   # convert the list of lists to a simple list
            Plaintext = ''.join(Plaintext_list)   # combine all the letters in the list to get a string
            print(f"with shift {i}, the key is {key}, the plaintext is : {Plaintext}")


            i = i+1  # loop through
