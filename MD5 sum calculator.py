import hashlib

md5_hash = hashlib.md5()

def MD5_sum(location_of_file):

    with open(location_of_file, "rb") as file:
        
        chunk = file.read(1000)
        while chunk:
    
            md5_hash.update(chunk)
            chunk = file.read(1000)

    hash_result = md5_hash.hexdigest()

    return hash_result

location = "test.txt"

print(MD5_sum("test.txt"))
