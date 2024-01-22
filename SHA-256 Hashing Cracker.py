import hashlib


def sha256(new_password_bytes):  # hash the password

    sha256_hasher = hashlib.sha256()   # create sha256 object

    sha256_hasher.update(new_password_bytes)  # put the password in sha256

    result = sha256_hasher.hexdigest()  # digest the things in sha256 to hash values

    return result




def generate_strings(alphabet, max_len):  # a function that generate all possible combinations with given alphabet and max length

    if max_len <= 0: 
        return

    result = list(alphabet)   # initilize the result list with all single letters in given alphabet

    for _ in range(2, max_len + 1):   #start with the length 2 to length max length +1 (not including max length + 1)
        
        temp_result = []  # create an empty temporary result list for future use

        for existing_result in result:  # for every existing result in the result list

            for letter in alphabet:  # iterate through each letter in given input alphabet
                temp_result.append(existing_result + letter)  # add the letter in alphabet to the existing result

        
        result.extend(temp_result)  # put the temoparary result into the result list


    return result   # return to the the list "result"





# test

if __name__ == "__main__":

    password = input("what's your original password?")  # ask user a simple password
    password_seed = password.encode('utf-8')  # convert it to bytes


    hashed_password = sha256(password_seed)  # use sha256 to hash the password
    print(f"the hashed password is {hashed_password}")


    full_alphabet = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"


    for generated_string in generate_strings(full_alphabet, 4):  # for each possibility with a specific max length (it will crash if it's too long)
        
        possibility = generated_string.encode('utf-8')  # convert it to bytes
    
        hashed_possibility = sha256(possibility)   # hash it using sha256

        if hashed_possibility == hashed_password:   # if it is the same as the right hased password
            print(f"the password is {generated_string}")   # print out the password
            break
    
    
