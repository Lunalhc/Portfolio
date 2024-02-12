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

            Console.WriteLine("The cipher text is:\n");
            PrintBytes(trimmedEncryptedBytes);  // print out the final result

            return trimmedEncryptedBytes;
        }
    }
}

