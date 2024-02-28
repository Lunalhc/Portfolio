import random

def generate_key(length):  # generate keys with given length

    key = [random.randint(0, 25) for _ in range(length)]  # generate a key with the length using numbers from 0-25 randomly

    return key


def encrypt(message_num, key):    # encryption function

    encrypted_message_num = []  # create an empty list to store the encypted message (in number)

    for i in range(len(message_num)):  # for each letter(in number) in the message

        encrypted_letter_num = (message_num[i] + key[i]) % 26    # add the letter(in numer) and the key together mod 26
        encrypted_message_num.append(encrypted_letter_num)     # put it into the list

    return encrypted_message_num


def decrypt(encrypted_message_num, key):  # decryption function

    decrypted_message_num = []  # create an empty list to store decrpted message (in number)
     
    for i in range(len(encrypted_message_num)):  # for each letter(in number) in the encrypted message

        decrypted_letter = (encrypted_message_num[i] - key[i]) % 26   # substract the key from the letter(in number)
        decrypted_message_num.append(decrypted_letter)  # put it into the list

    return decrypted_message_num



def main():

    message = input("Enter the message (uppercase): ")    # ask user for the plaintext
    message_num = [ord(char) - 65 for char in message]  # convert each letter to corresponding number using unicode conversion
    
    key = generate_key(len(message_num))  # generate a key according to the message's length

    Encrypted_message_num = encrypt(message_num, key)   # encrypt the message and store it as a list
    print("Encrypted message:", ''.join([chr(char + 65) for char in Encrypted_message_num]))   # convert each number to letter

    Decrypted_message_num = decrypt(Encrypted_message_num, key)  # decrypt the message and store it as a list
    print("Decrypted message:", ''.join([chr(char + 65) for char in Decrypted_message_num]))   # convert each number to letter



if __name__ == "__main__":
    main()
