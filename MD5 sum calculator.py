import hashlib  

md5_hash = hashlib.md5()   # create an object called md5_hash

def MD5_sum(location_of_file):  # a function that calculates the MD5 sum using the path of a file as a parameter

    with open(location_of_file, "rb") as file:  # open the file in read binary mode and call it file
        
        chunk = file.read(1000)  # initialize the chunk value with read the first 1000 bytes in the file
        
        while chunk:   # while the chunk value is not an empty byte
    
            md5_hash.update(chunk)  # using MD5 hash the chunk and put it in MD5
            
            chunk = file.read(1000)   # read next 1000 bytes in the file and let it be the new chunk value

    hash_result = md5_hash.hexdigest()   # use hexdigest method to digest the data in MD5

    return hash_result

# test:
location = "test.txt"     

print(MD5_sum("test.txt"))
