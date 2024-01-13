import string   # so that we can use ascii


def subsitute (n):  # create subsition table with n shifts

    encoding_dic = {}  # create an empty dictionary for encoding
    decoding_dic = {}  # create an empty dictionary for decoding

    
    for i in range(26):
        
        letter = string.ascii_uppercase[i]  # the original letter
        new_letter = string.ascii_uppercase[(i+n) %26]  # letter shifts n steps and mod 26

        encoding_dic[letter] = new_letter  # assign values for encoding dictionary
        decoding_dic[new_letter] = letter  # assign values for decoding dictonary

    return encoding_dic,decoding_dic


def encoder (original_text, encode_sub):  # encoder with original text and subsitution table as parameters

    cipher_text = ""  # initialize the cipher text
    
    for letter_ in original_text:  # each letter in original text
        
        if letter_ in encode_sub:  # if the letter is in the subsitution table

           cipher_text += encode_sub[letter_]  # assign the shift value for it 
           

        else:  # if it's not in the subsitution table
            
            cipher_text += letter_   # keep the letter 
    
    
    return cipher_text


def decoder (cipher_text, decode_sub):   # decoder function with parameter cipher text and decode subsitution table

    original_text = ""    # initialize the original text

    for letter_ in cipher_text:   # for each letter in cipher text parameter

        if letter_ in decode_sub:    # if the letter is in the decode subsitution table

            original_text += decode_sub[letter_]    # assign the values with n shift
        
        else:  # if it's not in th decode subsitutiontable

            original_text += letter_   # keep it the same
    
    return original_text



def printable_substitution(sub):  # print subsitution table with parameter of subsitution table
    
    mapping = sorted(sub.items())   # separatre the keys and values in pairs
    
    alphabet_line = " ".join(letter for letter, _ in mapping)   # grab the keys and put them in the first line
    cipher_line = " ".join(new_letter for _, new_letter in mapping)  # grab the values and put them in the second line
    
    return "{}\n{}".format(alphabet_line, cipher_line)  # with this format


# test if it works
if __name__ == "__main__":

    n = int(input("what's n? \n"))  # ask user the value of n

    subsitution = subsitute(n)   # create subsitution table with n shifts
    
    encode_sub = subsitution[0]   # separate the encoding table and decoding table
    decode_sub = subsitution[1]
    
    print("option 1: print encode subsitution table")
    print("option 2: print decode subsitution table")
    print("option 3: encode message")
    print("option 4: decode message")
    print("option 5: quit")

    option = input("type your option here:")  # store user input option

    if option == "1":

        encode_table = printable_substitution(encode_sub)  # create the encode table
        print(f"encode subsitution table: \n{encode_table}")   # print out the encode subsitution table
    
    elif option == "2":

        decode_table = printable_substitution(decode_sub)    # create the decode table
        print(f"decode subsitution table: \n{decode_table}")    # print out the decode subsitution table
    
    elif option == "3":

        message = input("type your message here:")  # store the input plaintext as message
        print("the cipher text is:\n")
        print(encoder(message,encode_sub))   # print out cipher text
    
    elif option == "4":

        message = input("type your message here:")   # store input cipher text as message
        print("the plain text is:\n")
        print(decoder(message,decode_sub))   # print out plain text

    elif option == "5":

        print("terminating")
        
    else:

        print("undefined option")  # when user give something else as option
