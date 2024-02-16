from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend


# this program will show that if you use the same key and iv in AES-CTR mode more than once, there will be some pattern of plaintext showing up without knowing the key and nonce.


class CipherAES_CTR:    # the class of AES-CTR mode

    def __init__(self, key, nonce):    # a function to initialize

        self.key = key   # set up the key
        self.nonce = nonce    # set up the nonce 
        self.counter = 0    # Initialize the counter 


    def encrypt_block(self, plaintext_block):   # single block encryptor
        
        nonce_int = int.from_bytes(self.nonce, byteorder='big')    # convert the iv to int
        updated_nonce = (nonce_int + self.counter).to_bytes(16, byteorder='big')    # combine the iv and counter value

        aes_context = Cipher(algorithms.AES(self.key), modes.CTR(updated_nonce), backend=default_backend())   # initilize the AES-CTR cipher with corresponding key and nonce
        encryptor = aes_context.encryptor()   # create the AES-CTR object
        ciphertext_block = encryptor.update(plaintext_block)    # run the algorithm

        self.counter += 1     # counter goes up

        return ciphertext_block


    def encrypt_blocks(self, plaintext_blocks):   # encrypt blocks

        ciphertext_blocks = []      # create an empty list to store ciphertext of each block
        for block in plaintext_blocks:   # for each block

            ciphertext_block = self.encrypt_block(block)    # run the AES-CTR algorithm
            ciphertext_blocks.append(ciphertext_block)    # put the result ciphertext ini the list

        return ciphertext_blocks


class UserInputHandler:    # a class that handler user's input

    @staticmethod     # it can be called without an instance/object
    def get_plaintext_blocks(num_blocks, use_hex=True):   # a method to get plaintext for each block from user

        plaintext_blocks = []    # an empty list to store plaintext for each block
        for i in range(num_blocks):   # for each block

            if use_hex:  # if the user wants to type hex string
                plaintext = UserInputHandler.get_hex_input(f"Enter plaintext for block {i + 1}: ")   # get user input for plaintext
                

            else:  # if the user want to type text message
                
                plaintext = input(f"Enter plaintext for block {i + 1}: ").encode('utf-8')  # convert it to binary

            
            plaintext_blocks.append(plaintext)   # append it to the list

        return plaintext_blocks
    


    @staticmethod
    def get_key_and_nonce():   # a method to set up the key and nonce

        key = UserInputHandler.get_hex_input("Enter the key in hexadecimal format: ")    # set user input as the key
        nonce = UserInputHandler.get_hex_input("Enter the nonce in hexadecimal format: ")  # set user input as the nonce

        return key, nonce
    

    @staticmethod
    def get_hex_input(prompt):  # a method to tell user to enter a valid hex string for key and nonce
        while True:  # an infinite loop , so keep repeating until it reaches the return statement

            value = input(prompt).strip()     # get rid of the space in user's input
            if all(c in "0123456789abcdefABCDEF" for c in value):    # in it's inside of these characters
                return bytes.fromhex(value)   # convert it to bytes
            
            print("Invalid input. Please enter a valid hexadecimal string.")   # if not, print this



if __name__ == "__main__":
    
    input_type = input("Do you want to use hexadecimal input? (yes/no): ").lower()
    use_hex = input_type.startswith('y')   # true if they say yes, false if they say no

    key, nonce = UserInputHandler.get_key_and_nonce()   # set up the key and nonce by calling the functions

    num_blocks = int(input("Enter the number of plaintext blocks: "))  # store how many blocks they want

    print("Enter plaintext blocks for cipher1:")   # get plaintexts of cipher1 from user
    cipher1_blocks = UserInputHandler.get_plaintext_blocks(num_blocks, use_hex)  # store the information of cipher 1


    print("Enter plaintext blocks for cipher2:")   # get plaintexts of cipher2 from user
    cipher2_blocks = UserInputHandler.get_plaintext_blocks(num_blocks, use_hex)    # store the information of cipher 2

    
    cipher1 = CipherAES_CTR(key, nonce)    # create cipher1 object using specific key and nonce
    cipher2 = CipherAES_CTR(key, nonce)   # create cipher2 object using specific key and nonce


    ciphertext_blocks1 = cipher1.encrypt_blocks(cipher1_blocks)  # encrypt the stuff in cipher1
    print(ciphertext_blocks1)

    for i, block in enumerate(ciphertext_blocks1):   # for every block in cipher1
        print(f"Ciphertext1 Block {i + 1}: {block.hex()}")   # print this block in hex


    ciphertext_blocks2 = cipher2.encrypt_blocks(cipher2_blocks)   # encrypt the stuff in cipher2

    for i, block in enumerate(ciphertext_blocks2):    # for every block in cipher2
        print(f"Ciphertext2 Block {i + 1}: {block.hex()}")   # print this block in hex




    xor_result_blocks = [bytes(x ^ y for x, y in zip(c1, c2)) for c1, c2 in zip(ciphertext_blocks1, ciphertext_blocks2)]   
    # XOR the ciphertext from same blocks in cipher 1 and 2




    for i, block in enumerate(xor_result_blocks):  # for each xor result
        print(f"XOR Result Block {i + 1}: {block.hex()}")  # print it in hex

        zero_positions = [j + 1 for j, byte in enumerate(block) if byte == 0]  # define the 0 position
        if zero_positions:  # if it's true
            print(f"For Block {i + 1}, the following byte positions are zero, meaning at those position, the plaintexts are the same: {zero_positions}")
    
    
    

    #
    for i, xor_result_block in enumerate(xor_result_blocks):  # for each xor result
       
        positions_of_interest = {}  # define this position of interest as a dictionary

        xor_result_hex = xor_result_block.hex()  # Convert the XOR result block to hex


        for j in range(0, len(xor_result_hex), 2):  # Iterate over the hexadecimal string two characters at a time

            byte_hex = xor_result_hex[j:j+2]  # Extract two characters to represent a byte
            
            if byte_hex == '0f':   # if it's 15
                
                positions_of_interest[j // 2 + 1] = [('06', '09'), ('07', '08')]   # assign this key to ('06', '09'), ('07', '08') value in dictionary
            
        
        for position, possible_pairs in positions_of_interest.items():  # for every key and values in that dictionary

            print(f"For Block {i + 1}, position {position} has a value of 15, meaning the possible pairs are {possible_pairs}.")  # print out the possibility

            

       

    




    







'''
Key 2b7e151628aed2a6abf7158809cf4f3c 

Init. Counter f0f1f2f3f4f5f6f7f8f9fafbfcfdfeff 

Block #1 

Input Block f0f1f2f3f4f5f6f7f8f9fafbfcfdfeff 

Output Block ec8cdf7398607cb0f2d21675ea9ea1e4 

Plaintext 6bc1bee22e409f96e93d7e117393172a 

Ciphertext 874d6191b620e3261bef6864990db6ce 

Block #2 

Input Block f0f1f2f3f4f5f6f7f8f9fafbfcfdff00 

Output Block 362b7c3c6773516318a077d7fc5073ae 

Plaintext ae2d8a571e03ac9c9eb76fac45af8e51 

Ciphertext 9806f66b7970fdff8617187bb9fffdff 

Block #3 

Input Block f0f1f2f3f4f5f6f7f8f9fafbfcfdff01 

Output Block 6a2cc3787889374fbeb4c81b17ba6c44 

Plaintext 30c81c46a35ce411e5fbc1191a0a52ef 

Ciphertext 5ae4df3edbd5d35e5b4f09020db03eab 



Block #4 

Input Block f0f1f2f3f4f5f6f7f8f9fafbfcfdff02 

Output Block e89c399ff0f198c6d40a31db156cabfe 

Plaintext f69f2445df4f9b17ad2b417be66c3710 

Ciphertext 1e031dda2fbe03d1792170a0f3009cee 


'''
