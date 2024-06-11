This program allow users to do enctyption in 4 ways---AES-ECB, AES-CBC, Casear cipher, and affine cipher.
The algorithem of the 2 modes we have here in AES are very complicated, so I import cryptography library to do it. 
For the casear cipher and affine cipher, they are just simple algorithem, so i can define it manually. 
It's too hard to explain how AES-ECB mode and CBC mode work, so i'll just skip it. 
Casear cipher is basically a subsitution algorithm, and affine cipher is a modulus algotithm.

here are the instructions for each way:

1. AES-CBC mode.
you will be asking for the plaintext, which should be 32 characters(16 bytes) in hexstring format.
you will also be asking for a key, which has the same length as plaintext.
Iv is initial vector, which is required in this mode, also 16 bytes, can be chose randomly.
to check the accuracy, there are test vectors i found from internet that is at the nbottom of this page.

2. AES-ECB mode.
you will be asking for the plaintext, which should be 32 characters(16 bytes) in hexstring format.
you will also be asking for a key, which has the same length as plaintext.
No IV is required for this mode.
to check the accuracy, there are test vectors i found from internet that is at the nbottom of this page.

3. Casear Cipher.
you will be asking for the plaintext, whihc could be letters. for example,"this is a test".
you will be asking for the shift number, which means how many shift of the alphabet table you want. for example, a shift of 1 will encrypt a to b.

4. Affine cipher.
you will be asking for the plaintext, whihc could be letters. for example,"this is a test".
you will be asking for a key a and a key b, whihc is part of the modulus algorithem. details can be found in the affine cipher encryption class.
Note that the key number has to be coprime to 26. for example, 2 won't work, but 17 is okay.


--------------------------------------------------------------------------------------------------------------------------------------------------

test vectors for AES-CBC mode:

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

--------------------------------------------------------------------------------------------------------------------------------------------

Test vectors for AES-ECB mode:

COUNT = 0
KEY = 00000000000000000000000000000000
PLAINTEXT = f34481ec3cc627bacd5dc3fb08f273e6
CIPHERTEXT = 0336763e966d92595a567cc9ce537f5e

COUNT = 1
KEY = 00000000000000000000000000000000
PLAINTEXT = 9798c4640bad75c7c3227db910174e72
CIPHERTEXT = a9a1631bf4996954ebc093957b234589

COUNT = 2
KEY = 00000000000000000000000000000000
PLAINTEXT = 96ab5c2ff612d9dfaae8c31f30c42168
CIPHERTEXT = ff4f8391a6a40ca5b25d23bedd44a597

COUNT = 3
KEY = 00000000000000000000000000000000
PLAINTEXT = 6a118a874519e64e9963798a503f1d35
CIPHERTEXT = dc43be40be0e53712f7e2bf5ca707209

COUNT = 4
KEY = 00000000000000000000000000000000
PLAINTEXT = cb9fceec81286ca3e989bd979b0cb284
CIPHERTEXT = 92beedab1895a94faa69b632e5cc47ce

COUNT = 5
KEY = 00000000000000000000000000000000
PLAINTEXT = b26aeb1874e47ca8358ff22378f09144
CIPHERTEXT = 459264f4798f6a78bacb89c15ed3d601

COUNT = 6
KEY = 00000000000000000000000000000000
PLAINTEXT = 58c8e00b2631686d54eab84b91f0aca1
CIPHERTEXT = 08a4e2efec8a8e3312ca7460b9040bbf




//-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
using System;

class Program 
{
    private InputHandlerBase _inputHandler;

    public Program(InputHandlerBase inputHandler)
    {
        _inputHandler = inputHandler;
    }

    public void Run()
    {
        Operations operations = new Operations(); // Create an instance of Operations class

        if (_inputHandler is CaesarCipherInputHandler)
        {
            CaesarCipherInputHandler caesarHandler = (CaesarCipherInputHandler)_inputHandler;
            string plaintext = caesarHandler.GetPlainText();
            int shift = caesarHandler.GetShift();

            byte[] plaintextBytes = System.Text.Encoding.UTF8.GetBytes(plaintext);
            byte[] encryptedBytes = caesarHandler.Encrypt(plaintextBytes, shift);

            string ciphertext = System.Text.Encoding.UTF8.GetString(encryptedBytes); // Convert byte array to string using UTF-8 encoding

            Console.WriteLine("Encrypted text:");
            Console.WriteLine(ciphertext);
        }
        else if (_inputHandler is AffineCipherInputHandler)
        {
            AffineCipherInputHandler affineHandler = (AffineCipherInputHandler)_inputHandler;
            string plaintext = affineHandler.GetPlainText();
            string keys = affineHandler.GetKey();
            int keyA, keyB;

            // Parse keys
            string[] keyParts = keys.Split(',');
            if (keyParts.Length != 2 || !int.TryParse(keyParts[0], out keyA) || !int.TryParse(keyParts[1], out keyB))
            {
                Console.WriteLine("Invalid key format. Please provide two integers separated by a comma.");
                return;
            }

            // Encrypt the plaintext using the Affine cipher
            string ciphertext = AffineCipher.Encrypt(plaintext, keyA, keyB);

            Console.WriteLine("Encrypted text:");
            Console.WriteLine(ciphertext);
        }
        else
        {
            string plaintextHex = _inputHandler.GetPlainText();
            string keyHex = _inputHandler.GetKey();
            string ivHex = _inputHandler.GetIV();

            byte[] paddedPlaintext = operations.ApplyPKCS7Padding(operations.StringToByteArray(plaintextHex));
            byte[] keyBytes = operations.StringToByteArray(keyHex);
            byte[] ivBytes = string.IsNullOrEmpty(ivHex) ? null : operations.StringToByteArray(ivHex);

            byte[] encryptedText = operations.Encrypt(paddedPlaintext, keyBytes, ivBytes);

            // Convert byte array to hexadecimal string with dashes
            string ciphertextWithDashes = BitConverter.ToString(encryptedText);

            // Trim dashes from the beginning and end of the string only if using ECB mode
            if (_inputHandler is ECBInputHandler)
            {
                
                ciphertextWithDashes = ciphertextWithDashes.Replace("-", "").Substring(0, 32);
            }

            Console.WriteLine("Encrypted text:");
            Console.WriteLine(ciphertextWithDashes); 
        }
    }



    public static void Main(string[] args)
    {
        InputHandlerBase inputHandler = null;

        while (inputHandler == null)
        {
            // manu
            Console.WriteLine("1. AES-CBC mode");
            Console.WriteLine("2. AES-ECB mode");
            Console.WriteLine("3. Casear cipher mode");
            Console.WriteLine("4. Affine cipher mode");
            Console.Write("Enter your choice: ");
            string choice = Console.ReadLine();

            switch (choice)
            {
                case "1":
                    inputHandler = new CBCInputHandler();
                    break;
                case "2":
                    inputHandler = new ECBInputHandler();
                    break;
                case "3":
                    inputHandler = new CaesarCipherInputHandler();
                    break;
                case "4":
                    inputHandler = new AffineCipherInputHandler();
                    break;
                
                default:
                    Console.WriteLine("Invalid choice. Please try again.");
                    break;
            }
        }

        Program program = new Program(inputHandler);
        program.Run();
    }
}

//--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

using System.Security.Cryptography;

public class Operations
{
    public byte[] ApplyPKCS7Padding(byte[] textBytes)
    {
        int blockSize = 16;
        int paddingLength = 0;

        if (textBytes.Length % blockSize == 0)
        {
            paddingLength = 0;
        }
        else
        {
            paddingLength = blockSize - (textBytes.Length % blockSize);
        }

        if (paddingLength != 0)
        {
            Console.WriteLine($"Original plaintext length: {textBytes.Length}");
            Console.WriteLine($"Padding length required: {paddingLength}");

            byte[] paddedPlaintext = new byte[textBytes.Length + paddingLength];
            Array.Copy(textBytes, paddedPlaintext, textBytes.Length);
            byte paddingByte = (byte)paddingLength;

            for (int i = textBytes.Length; i < paddedPlaintext.Length; i++)
            {
                paddedPlaintext[i] = paddingByte;
            }

            Console.WriteLine($"Plaintext in bytes after padding: {BitConverter.ToString(paddedPlaintext)}");
            return paddedPlaintext;
        }
        else
        {
            Console.WriteLine("No padding required.");
            return textBytes;
        }
    }

    public byte[] StringToByteArray(string hex)
    {
        int numberChars = hex.Length;
        byte[] bytes = new byte[numberChars / 2];

        for (int i = 0; i < numberChars; i += 2)
        {
            bytes[i / 2] = Convert.ToByte(hex.Substring(i, 2), 16);
        }
        return bytes;
    }


    public byte[] Encrypt(byte[] paddedText, byte[] keyBytes, byte[] ivBytes = null)
    {
        using (Aes aes = Aes.Create())
        {
            aes.Key = keyBytes;
            
            if (ivBytes != null)
            {
                aes.Mode = CipherMode.CBC; // Set mode to CBC if IV is provided
                aes.IV = ivBytes;
            }
            else
            {
                aes.Mode = CipherMode.ECB; 
            }

            ICryptoTransform encryptor = aes.CreateEncryptor();
            byte[] encryptedBytes = encryptor.TransformFinalBlock(paddedText, 0, paddedText.Length);

            return encryptedBytes; 
        }
    }


}

//----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

public class ECBInputHandler : InputHandlerBase
{
    public override string GetKey()
    {
        
        return GetInput("Enter the encryption key (32 hex characters (16 bytes)): ").Substring(0, 32);
    }


    public override string GetPlainText()
    {
        Console.Write("Enter the plaintext: ");
        return Console.ReadLine();
    }

    // ECB mode does not require an IV
    public override string GetIV()
    {
    
        return "";
    }
}

//---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

public class CBCInputHandler : InputHandlerBase
{
    public override string GetKey()
    {
        return GetInput("Enter the encryption key (32 hex characters (16 bytes)): ");
    }

    public override string GetIV()
    {
        return GetInput("Enter the initialization vector (IV) (32 hex characters (16 bytes)): ");
    }

    public override string GetPlainText()
    {
        Console.Write("Enter the plaintext: ");
        return Console.ReadLine();
    }
}



//-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

using System;

public class CaesarCipherInputHandler : InputHandlerBase
{
    public override string GetKey()
    {
        // Caesar cipher does not require a key
        return "";
    }

    public int GetShift()
    {
        Console.Write("Enter the shift value for Caesar Cipher: ");
        string shiftInput = Console.ReadLine();
        int shift;
        while (!int.TryParse(shiftInput, out shift))
        {
            Console.WriteLine("Invalid input. Please enter an integer.");
            Console.Write("Enter the shift value for Caesar Cipher: ");
            shiftInput = Console.ReadLine();
        }
        return shift;
    }

    public override string GetPlainText()
    {
        Console.Write("Enter the plaintext for Caesar Cipher: ");
        return Console.ReadLine();
    }

    // Caesar cipher does not require an IV
    public override string GetIV()
    {
        
        return "";
    }

    public byte[] Encrypt(byte[] plaintext, int shift)
    {
        byte[] encryptedBytes = new byte[plaintext.Length];
        for (int i = 0; i < plaintext.Length; i++)
        {
            // Apply the Caesar cipher shift to each byte
            encryptedBytes[i] = (byte)((plaintext[i] + shift) % 256);
        }
        return encryptedBytes;
    }
}

//------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

public abstract class InputHandlerBase
{
    protected string GetInput(string message)
    {
        Console.Write(message);
        return Console.ReadLine();
    }

    public abstract string GetKey();
    public abstract string GetIV();
    public abstract string GetPlainText();
}

//----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

public class AffineCipherInputHandler : InputHandlerBase
{
    public override string GetKey()
    {
        // Affine cipher requires two keys: a and b
        Console.Write("Enter the first key 'a' for Affine Cipher: ");
        int keyA = GetIntInput();

        Console.Write("Enter the second key 'b' for Affine Cipher: ");
        int keyB = GetIntInput();

        // Validate keys: 'a' must be coprime with 26
        while (!IsCoprime(keyA, 26))
        {
            Console.WriteLine("Invalid key 'a'. Key 'a' must be coprime with 26.");
            Console.Write("Enter the first key 'a' for Affine Cipher: ");
            keyA = GetIntInput();
        }

        return $"{keyA},{keyB}";
    }

    public override string GetPlainText()
    {
        Console.Write("Enter the plaintext for Affine Cipher: ");
        return Console.ReadLine();
    }

    // Affine cipher does not require an IV
    public override string GetIV()
    {
        
        return "";
    }

    private int GetIntInput()
    {
        int input;
        while (!int.TryParse(Console.ReadLine(), out input))
        {
            Console.WriteLine("Invalid input. Please enter an integer.");
            Console.Write("Enter again: ");
        }
        return input;
    }

    private bool IsCoprime(int a, int b)
    {
        while (b != 0)
        {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a == 1;
    }
}


//------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

using System;
using System.Text;

public static class AffineCipher
{
    public static string Encrypt(string plaintext, int keyA, int keyB)
    {
        StringBuilder ciphertext = new StringBuilder();

        foreach (char character in plaintext)
        {
            if (char.IsLetter(character))
            {
                char encryptedChar = (char)(((keyA * (character - 'A') + keyB) % 26) + 'A');
                ciphertext.Append(encryptedChar);
            }
            else
            {
                ciphertext.Append(character); // Keep non-alphabetic characters unchanged
            }
        }

        return ciphertext.ToString();
    }
}
//-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
