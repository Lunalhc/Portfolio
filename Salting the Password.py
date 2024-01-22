import hashlib
import os         # random bytes generator
import base64  


def add_salt(password_bytes):  # add random salt to the password
    
    random_bytes = os.urandom(16)   # generate a 16 bytes random bytes
    
    salt = base64.b64encode(random_bytes)  # Encode the random bytes using base64.b64encode to get the salt
    
    new_password_bytes = salt + password_bytes  # add the password to the salt
    
    
    return new_password_bytes


def sha256(password_bytes):  # hash the password

    sha256_hasher = hashlib.sha256()   # create sha256 object

    sha256_hasher.update(password_bytes)  # put the password in sha256

    result = sha256_hasher.hexdigest()  # digest the things in sha256 to hash values

    return result




# test:
new_password = add_salt(b"alice1234")

hash_new_password = sha256(new_password)

print(hash_new_password)
