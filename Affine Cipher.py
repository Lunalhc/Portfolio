import math
import random



def setup(alphabet, shift):  # create an alphabet table according to the alphabet and shift

    alphabet_table = {}   # create an empty letter-to-number dictionary

    n = sum(1 for letter in alphabet)    # calculate how many letters in the entire alphabet

    for i, letter in enumerate(alphabet):     # for each letter in the alphabet

        alphabet_table[letter] = (i + shift) % n    # assign the letter with preferred shift and store it in the dictionary

    return n, alphabet_table


def text_to_number(text,alphabet_table):   # a function that can convert plaintext to its corresponding number version

    result = []     # create a list to store the number version later
    for letter in text:    # for each letter in the plaintext

        letter = alphabet_table[letter]     # assign the letter with its corresponding value in the dictionary
        result.append(letter)      # add the value to the result list
    

    return result


def find_possible_a (n):  # find all the possible a we can use accoring to the shift

    a_list = []   # an empty list for possible a values
    for number in range(1,n):   # find all the numbers on the interval that is relative prime to n from 0 to n not including n

        if math.gcd(number,n) == 1:   # check which number is relative prime to n
            a_list.append(number)    # add it to the possible a list
    

    return a_list



def encryption(a,b,n,plaintext_number):   # encrypt a number version plaintext to a number version ciphertext

    ciphertext_number = []    # create a empty list to store ciphertext numbers
    for x in plaintext_number:    # for each element in number version plaintext

        e_k = (a * x + b) % n    # modulus operation
        ciphertext_number.append(e_k)   # add the value to the ciphertext list
     
    return ciphertext_number  



def find_inverse(a,n):    # find inverse of a in a group 
    
    a_inverse = 0   # initialize the a inverse
    for number in range(0,n-1):  # for each number in the group

        if (a * number) % n == 1:   # if a times this number mod n equals to the multiplicative identity 1
            a_inverse = number   # then this number is the inverse
    
    return a_inverse


    
def decryption(n,a_inverse,ciphertext_number):
    
    plaintext_number = []
    for y in ciphertext_number:

        d_k = (a_inverse * (y-b) % n)
        plaintext_number.append(d_k)
    
    return plaintext_number







if __name__ == "__main__":

    choice = input("type 1 for encryption, 2 for decrption\n")  
    default_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if choice == "1":

        alphabet_choice = input("please type the alphabet you are using in uppercase\n type 1 if you want to use default alphabet\n")  # enter the alphabet we want to use
        if alphabet_choice == "1":  
            Alphabet = default_alphabet  # use default english alphabet
        else:
            Alphabet = alphabet_choice


        Shift = int(input("what shift number do you want to use?\n")) # enter how many shifts you want 
        N,_= setup(Alphabet,Shift)    # calculate the size of the alphabet

        _,Alphabet_table = setup(Alphabet,Shift)   # get the alphabet table according to shift
        print(f"with shift {Shift}, the letter-to-number table is : {Alphabet_table}\n")   # print out the dictionary
    

        Plaintext = input("type the plaintext that you want to encrypt in uppercase\n")   # enter your plaintext
        Plaintext_number = text_to_number(Plaintext, Alphabet_table)   # get the plaintext in number version
        print(f"the plaintext in number is : {Plaintext_number}\n")

        A_list = find_possible_a(N)   # get the list of all possible a values so that a inverse exists
        print(f"all possible a values: {A_list}\n")

        a = int(input("pick your a value from the list\n"))   # pick an a value
        print(f"the a value you pick this time is {a}")
        b = int(input(f"pick your b value (musy be an integer) from 0 to {N-1}\n"))  # pick a interger b from the interval 0 to n-1 including n-1
        print(f"the b value you pick this time is {b}\n")

        Ciphertext_number = encryption(a,b,N,Plaintext_number)   # find the Ciphertext in number
        print(f"the ciphertext in number is : {Ciphertext_number}\n")
        

        Ciphertext = []  # create an empty list to store letters in ciphertext
        for number in Ciphertext_number:   # for each number in the number version ciphertext

            letter = [key for key, value in Alphabet_table.items() if value == number]  # fine the letter that the number represents from the alphabet tabel
            Ciphertext.append(letter)   # add the letter to the ciphertext list

        Ciphertext_list = [item for sublist in Ciphertext for item in sublist]   # convert the list of lists to a simple list
        Ciphertext = ''.join(Ciphertext_list)   # combine all the letters in the list to get a string
        print(f"The Ciphertext is : {Ciphertext}")
    


    elif choice == "2":

        alphabet_choice = input("please type the alphabet you are using in uppercase\n type 1 if you want to use default alphabet\n")  # enter the alphabet we want to use
        if alphabet_choice == "1":  
            Alphabet = default_alphabet  # use default english alphabet
        else:
            Alphabet = alphabet_choice

        Shift = int(input("what shift number do you want to use?\n"))  # enter how many shifts you want 
        N,_= setup(Alphabet,Shift)    # calculate the size of the alphabet

        _,Alphabet_table = setup(Alphabet,Shift)   # get the alphabet table according to shift
        print(f"with shift {Shift}, the letter-to-number table is : {Alphabet_table}\n")   # print out the dictionary
        
        A_list = find_possible_a(N)   # get the list of all possible a values so that a inverse exists
        print(f"all possible a values: {A_list}\n")

        a = int(input("pick your a value from the list\n"))   # pick an a value
        print(f"the a value you pick this time is {a}")
        b = int(input(f"pick your b value (musy be an integer) from 0 to {N-1}\n"))   # pick a interger b from the interval 0 to n-1 including n-1
        print(f"the b value you pick this time is {b}\n")

        A_inverse = find_inverse(a,N)

        Ciphertext = input("type the ciphertext in uppercase\n")
        Ciphertext_number = text_to_number(Ciphertext, Alphabet_table)   # get the plaintext in number version
        print(f"the ciphertext in number is : {Ciphertext_number}\n")

        Plaintext_number = decryption(N,A_inverse,Ciphertext_number)
        print(f"the plaintext in number is {Plaintext_number}")
        
        
        Plaintext = []
        for number in Plaintext_number:   # for each number in the number version plaintext

            letter = [key for key, value in Alphabet_table.items() if value == number]  # fine the letter that the number represents from the alphabet tabel
            Plaintext.append(letter)   # add the letter to the plaintext list

        Plaintext_list = [item for sublist in Plaintext for item in sublist]   # convert the list of lists to a simple list
        Plaintext = ''.join(Plaintext_list)   # combine all the letters in the list to get a string
        print(f"The plaintext is : {Plaintext}")


    else:

        print("the choice number is not recognized")
