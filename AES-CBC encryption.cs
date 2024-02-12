using System;
using System.Text;
using System.Collections.Generic;
using System.Security.Cryptography;

public class Program  // main class
{

    public static void Main(string[] args)    // constructor
    {
        Program program = new Program();    // create an object of the main class "Program"
        InputHandler inputhandler = new InputHandler();  // create an object of the inputhandler class

        string plaintext = inputhandler.GetPlainTextFromUser();  // get plaintext and store as a string

        string key = inputhandler.GetKeyFromUser();  // get key and store as a string

        string iv = inputhandler.GetIVFromUser();  // get iv and store as a string


        byte[] ready_to_pad = program.StringToByteArray(plaintext);   // convert the plaintext to byte array  
        byte[] paddedPlaintext = program.ApplyPKCS7Padding(ready_to_pad);   // pad the plaintext(in bytes), should be 16 bytes
       
        
        byte[] keyBytes = program.StringToByteArray(key);   // convert the key to byte array
        byte[] ivBytes = program.StringToByteArray(iv);    // convert the iv to byte array


        
        program.Encrypt(paddedPlaintext, keyBytes, ivBytes);   // run the encryption method to get the final result

    }

    private byte[] ApplyPKCS7Padding(byte[] text_bytes)   // padding method, take plaintext(in bytes) as input
    {
    int blockSize = 16; // AES block size is 16 bytes
    int paddingLength = 0; // Initialize paddingLength

    if (text_bytes.Length % blockSize == 0)    // if number of bytes of the plaintext is already a multiple of 16
    {
        paddingLength = 0;   // no pad
    }
    else  // if it's not a multiple of 16
    {
        paddingLength = blockSize - (text_bytes.Length % blockSize);  // padding length will be the remainder
    }

    
    
    if (paddingLength != 0)   // if the padding length is not 0 (need padding)
    {
        Console.WriteLine($"Original plaintext length: {text_bytes.Length}");  // display the original length of plaintext before padding to user
        Console.WriteLine($"Padding length required: {paddingLength}");    // display how many bytes we need to pad


        byte[] paddedPlaintext = new byte[text_bytes.Length + paddingLength];   // create an empty new byte array with the number of combined plaintext length

    
        Array.Copy(text_bytes, paddedPlaintext, text_bytes.Length);  // copy the input plaintext(bytes) to paddedPlaintext array we just created, the last parameter indicates the number of elements we want to copy from the source

        byte paddingByte = (byte)paddingLength; // convert the padding length to a byte value

        
        for (int i = text_bytes.Length; i < paddedPlaintext.Length; i++)  // iterate each element in the pad part
        {
            paddedPlaintext[i] = paddingByte;   // set the padding part of plaintext to the bytes value 
        }

        Console.WriteLine($"Plaintext in bytes after padding: {BitConverter.ToString(paddedPlaintext)}");   //  display the plaintext(in bytes) after padding

        return paddedPlaintext;
    }
    else   // if the padding length is 0
    {
       
        Console.WriteLine("No padding required.");
        return text_bytes;   // doing nothing 
    }

    }



    private byte[] StringToByteArray(string hex)   // a method to convert string to byte, take a hex string as input
    {
        int numberChars = hex.Length;   // store the length of hex string as int
        byte[] bytes = new byte[numberChars / 2];   // divide it by 2, and store it as a byte

        for (int i = 0; i < numberChars; i += 2)   // iterate every first of the two numbers
        {
            bytes[i / 2] = Convert.ToByte(hex.Substring(i, 2), 16);   // convert the specific 2 charaters to bytes value
        }
        return bytes;
    }


    private static void PrintBytes(byte[] bytes)  // a method to print bytes value
    {
        foreach (byte b in bytes)   // interate each character in bytes
        {
            Console.Write($"{b:X2} "); // X2 format specifier ensures each byte is printed as two hexadecimal characters
        }
        Console.WriteLine(); // Add a new line after printing all bytes
    }

    private byte[] Encrypt(byte[] padded_text, byte[] keyBytes, byte[] ivBytes)   // a method to encrypt the plaintext(in bytes)
    {
        using (Aes aes = Aes.Create())    //  create an AES cipher object using the imported library
        {
            aes.Key = keyBytes;    //  set the key equals to what we want
            aes.IV = ivBytes;     // set the iv equals to what we want

            ICryptoTransform encryptor = aes.CreateEncryptor(aes.Key, aes.IV);    // create a AES algorithm based on the ic and key we have
            byte[] encryptedBytes = encryptor.TransformFinalBlock(padded_text, 0, padded_text.Length);    // run the AES algorithm

            
            int originalLength = padded_text.Length;  // store the length of ciphertext we want as an integer

            
            byte[] trimmedEncryptedBytes = new byte[originalLength];   //  Create a new byte array to hold the original length of the plaintext, ready to be trimmed
            Array.Copy(encryptedBytes, trimmedEncryptedBytes, originalLength);   // grab original length elements from ciphertext to the byte array we just created

            Console.WriteLine("The cipher text is:");
            PrintBytes(trimmedEncryptedBytes);  // print out the final result

            return trimmedEncryptedBytes;
        }
    }
}




//--------------------------------------------------------------------------------------------------------------------------------------


public class InputHandler   // a class to handle the user input
{
    public string GetKeyFromUser()   // ask the user the key
    {
        Console.Write("Enter the encryption key (32 hex characters (16 bytes)): ");
        string key = Console.ReadLine();
        return key;
    }

    public string GetIVFromUser()  // ask the iv from user
    {
        Console.Write("Enter the initialization vector (IV) (32 hex characters (16 bytes)): ");
        string iv = Console.ReadLine();
        return iv;
    }

    public string GetPlainTextFromUser()  // ask the user plaintext
    {
        Console.Write("Enter the plaintext:");  // no padding if it's a multuple  of 16 bytes(block size)
        string plaintext = Console.ReadLine();
        return plaintext;
    }
}



// test vectors:
/*
Set 1 vector 1
    mode=aes-128
    key=2b7e151628aed2a6abf7158809cf4f3c
    iv=000102030405060708090A0B0C0D0E0F
    plain=6bc1bee22e409f96e93d7e117393172a
    cipher=7649abac8119b246cee98e9b12e9197d

Set 1 vector 2
    mode=aes-128
    key=2b7e151628aed2a6abf7158809cf4f3c
    iv=7649ABAC8119B246CEE98E9B12E9197D
    plain=ae2d8a571e03ac9c9eb76fac45af8e51
    cipher=5086cb9b507219ee95db113a917678b2

Set 1 vector 3
    mode=aes-128
    key=2b7e151628aed2a6abf7158809cf4f3c
    iv=5086CB9B507219EE95DB113A917678B2
    plain=30c81c46a35ce411e5fbc1191a0a52ef
    cipher=73bed6b8e3c1743b7116e69e22229516

Set 1 vector 4
    mode=aes-128
    key=2b7e151628aed2a6abf7158809cf4f3c
    iv=73BED6B8E3C1743B7116E69E22229516
    plain=f69f2445df4f9b17ad2b417be66c3710
    cipher=3ff1caa1681fac09120eca307586e1a7

    
COUNT = 0
KEY = 80000000000000000000000000000000
IV = 00000000000000000000000000000000
PLAINTEXT = 00000000000000000000000000000000
CIPHERTEXT = 0edd33d3c621e546455bd8ba1418bec8

COUNT = 1
KEY = c0000000000000000000000000000000
IV = 00000000000000000000000000000000
PLAINTEXT = 00000000000000000000000000000000
CIPHERTEXT = 4bc3f883450c113c64ca42e1112a9e87

COUNT = 2
KEY = e0000000000000000000000000000000
IV = 00000000000000000000000000000000
PLAINTEXT = 00000000000000000000000000000000
CIPHERTEXT = 72a1da770f5d7ac4c9ef94d822affd97

COUNT = 3
KEY = f0000000000000000000000000000000
IV = 00000000000000000000000000000000
PLAINTEXT = 00000000000000000000000000000000
CIPHERTEXT = 970014d634e2b7650777e8e84d03ccd8

COUNT = 4
KEY = f8000000000000000000000000000000
IV = 00000000000000000000000000000000
PLAINTEXT = 00000000000000000000000000000000
CIPHERTEXT = f17e79aed0db7e279e955b5f493875a7

COUNT = 5
KEY = fc000000000000000000000000000000
IV = 00000000000000000000000000000000
PLAINTEXT = 00000000000000000000000000000000
CIPHERTEXT = 9ed5a75136a940d0963da379db4af26a

COUNT = 6
KEY = fe000000000000000000000000000000
IV = 00000000000000000000000000000000
PLAINTEXT = 00000000000000000000000000000000
CIPHERTEXT = c4295f83465c7755e8fa364bac6a7ea5

COUNT = 7
KEY = ff000000000000000000000000000000
IV = 00000000000000000000000000000000
PLAINTEXT = 00000000000000000000000000000000
CIPHERTEXT = b1d758256b28fd850ad4944208cf1155

COUNT = 8
KEY = ff800000000000000000000000000000
IV = 00000000000000000000000000000000
PLAINTEXT = 00000000000000000000000000000000
CIPHERTEXT = 42ffb34c743de4d88ca38011c990890b

COUNT = 9
KEY = ffc00000000000000000000000000000
IV = 00000000000000000000000000000000
PLAINTEXT = 00000000000000000000000000000000
CIPHERTEXT = 9958f0ecea8b2172c0c1995f9182c0f3

COUNT = 10
KEY = ffe00000000000000000000000000000
IV = 00000000000000000000000000000000
PLAINTEXT = 00000000000000000000000000000000
CIPHERTEXT = 956d7798fac20f82a8823f984d06f7f5

COUNT = 11
KEY = fff00000000000000000000000000000
IV = 00000000000000000000000000000000
PLAINTEXT = 00000000000000000000000000000000
CIPHERTEXT = a01bf44f2d16be928ca44aaf7b9b106b

COUNT = 12
KEY = fff80000000000000000000000000000
IV = 00000000000000000000000000000000
PLAINTEXT = 00000000000000000000000000000000
CIPHERTEXT = b5f1a33e50d40d103764c76bd4c6b6f8

COUNT = 13
KEY = fffc0000000000000000000000000000
IV = 00000000000000000000000000000000
PLAINTEXT = 00000000000000000000000000000000
CIPHERTEXT = 2637050c9fc0d4817e2d69de878aee8d

COUNT = 14
KEY = fffe0000000000000000000000000000
IV = 00000000000000000000000000000000
PLAINTEXT = 00000000000000000000000000000000
CIPHERTEXT = 113ecbe4a453269a0dd26069467fb5b5

COUNT = 15
KEY = ffff0000000000000000000000000000
IV = 00000000000000000000000000000000
PLAINTEXT = 00000000000000000000000000000000
CIPHERTEXT = 97d0754fe68f11b9e375d070a608c884

COUNT = 16
KEY = ffff8000000000000000000000000000
IV = 00000000000000000000000000000000
PLAINTEXT = 00000000000000000000000000000000
CIPHERTEXT = c6a0b3e998d05068a5399778405200b4

COUNT = 17
KEY = ffffc000000000000000000000000000
IV = 00000000000000000000000000000000
PLAINTEXT = 00000000000000000000000000000000
CIPHERTEXT = df556a33438db87bc41b1752c55e5e49

COUNT = 18
KEY = ffffe000000000000000000000000000
IV = 00000000000000000000000000000000
PLAINTEXT = 00000000000000000000000000000000
CIPHERTEXT = 90fb128d3a1af6e548521bb962bf1f05

COUNT = 19
KEY = fffff000000000000000000000000000
IV = 00000000000000000000000000000000
PLAINTEXT = 00000000000000000000000000000000
CIPHERTEXT = 26298e9c1db517c215fadfb7d2a8d691

COUNT = 20
KEY = fffff800000000000000000000000000
IV = 00000000000000000000000000000000
PLAINTEXT = 00000000000000000000000000000000
CIPHERTEXT = a6cb761d61f8292d0df393a279ad0380

COUNT = 21
KEY = fffffc00000000000000000000000000
IV = 00000000000000000000000000000000
PLAINTEXT = 00000000000000000000000000000000
CIPHERTEXT = 12acd89b13cd5f8726e34d44fd486108

COUNT = 22
KEY = fffffe00000000000000000000000000
IV = 00000000000000000000000000000000
PLAINTEXT = 00000000000000000000000000000000
CIPHERTEXT = 95b1703fc57ba09fe0c3580febdd7ed4


*/
