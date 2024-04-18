using System;
// hopefully i fixed all the issues
class MainProgram
{
    static void Main(string[] args)
    {   
        // create an object of the scripture class
        Scripture scripture = new Scripture();
        // load the file from local folder
        scripture.LoadRandomVersesFromFile("Gosp
                                           el of Matthew1.txt");
        
        // while loop to iterate until the user want to quit
        while (true)
        {
            scripture.DisplayCurrentVerse();

            Console.WriteLine("Press Enter to reveal more scripture, or type 'quit' to exit.");

            string input = Console.ReadLine().ToLower();  // read the user input and convert capitals to lowercase
            
            // end the program if user type quit
            if (input == "quit") 
                break;

            Console.Clear(); // clear the console

            scripture.HideWords();   // keep hiding words
        }
    }
}

//-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                             

class Reference
{   
    // set up variables
    private string _book;
    private int _startChapter;
    private int _startVerse;
    private int _endVerse;

    // constructor
    public Reference(string book, int startChapter, int startVerse, int endVerse)
    {
        _book = book;
        _startChapter = startChapter;
        _startVerse = startVerse;
        _endVerse = endVerse;
    }
    
    
    
    // differentiate if it's one verse or 2 consecutive verses
    public string GetVerseReference()
    {
        if (_startVerse == _endVerse)
        {
            return $"{_book} {_startChapter}:{_startVerse}";
        }
        else
        {
            return $"{_book} {_startChapter}:{_startVerse}-{_endVerse}";
        }
    }
}
                                             

                                  
//---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


 class Scripture
{   
    // set up variables we need in this class
    private List<Word> _words;  // get thelist from Word class
    private Random _random;     // to be able to use built in class Random later
    
    // constructor
    public Scripture()
    {
        _words = new List<Word>();
        _random = new Random();
    }
    

    // a method that load the scipture file
    public void LoadRandomVersesFromFile(string filePath)
    {
        string[] lines = File.ReadAllLines(filePath);

        // Choose a random start line
        int startLine = _random.Next(0, lines.Length - 1);
        
        // Determine whether to select one or two consecutive verses
        int versesToSelect = _random.Next(1, 3);
        int endLine = startLine + versesToSelect - 1;

        // Extract chapter and verse numbers from the first selected line
        string[] startParts = lines[startLine].Split(':');
        string[] startVerseParts = startParts[0].Split(' ');
        int startChapter = 1; // i only have Matthew 1 
        int startVerse = startLine + 1;  // since the counts starts from 0


        // Extract chapter and verse numbers from the last selected line
        string[] endParts = lines[endLine].Split(':');
        string[] endVerseParts = endParts[0].Split(' ');
        int endVerse = endLine + 1;
        
        // create an reference object
        Reference reference = new Reference("Matthew", startChapter, startVerse, endVerse);
        // display the verse number
        Console.WriteLine ($"Verse: {reference.GetVerseReference()}");

        // loop through each line
        for (int i = startLine; i <= endLine; i++)
        {
            string[] parts = lines[i].Split(':');  // split by ":"
            // trim the verse and store store each word
            foreach (string word in parts[1].Trim().Split(' '))
            {
                _words.Add(new Word(word));   // add to the word list
            }
        }
    }



    // a method to display the random verse/verses it chooses
    public void DisplayCurrentVerse()
    {
        foreach (Word word in _words)
        {
            Console.Write(word.Display() + " ");
        }
        Console.WriteLine();
    }
    
    // a method to hide random words

    public void HideWords()
    {
        int wordsToHide = 2;
        while (wordsToHide > 0)
        {
            int index = _random.Next(_words.Count);
            if (!_words[index].GetIsHidden())
            {
                // Get the word to hide
                string wordToHide = _words[index].Display();
                // Check if it's a word or a symbol
                bool isWord = false;
                foreach (char c in wordToHide)
                {
                    if (char.IsLetter(c))
                    {
                        isWord = true;
                        break;
                    }
                }

                if (isWord)
                {
                    // Hide the word
                    _words[index].Hide();
                    wordsToHide--;

                    // Replace each character of the word with underscores
                    for (int i = 0; i < wordToHide.Length; i++)
                    {
                        _words.Insert(index + i + 1, new Word("_"));
                    }
                }
            }
        }

        if (AllHidden())
        {
            Console.WriteLine("All words have been hidden. Press Enter to exit.");
            Console.ReadLine();
            Environment.Exit(0);   // Exit the program
        }
    }



    // a method to check if all words are hidden
    private bool AllHidden()
    {
        foreach (Word word in _words)
        {
            // Check if the word is not hidden, not an underscore, and not a verse number
            if (!word.GetIsHidden() && !word.Display().Equals("_") && !IsVerseNumber(word.Display()))
            {
                return false;
            }
        }

        return true;
    }

    // Check if the word is a verse number
    private bool IsVerseNumber(string word)
    {
        //check if the word contains only digits and colon
        foreach (char c in word)
        {
            if (!char.IsDigit(c) && c != ':')
            {
                return false;
            }
        }
        return true;
    }



} 
                                           
//--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                           
class Word
{   
    // set up the variables, including a boolean value to check the status of word
    private string _text;
    private bool _isHidden;
    
    // constructor
    public Word(string text)
    {
        _text = text;
        _isHidden = false;   // set this boolean value to false as default
    }
    
    // getters and setters
    public bool GetIsHidden()
    {
        return _isHidden;
    }
    
    public void Hide()
    {
        _isHidden = true;
    }
    
    // a method to check the status of the word, therefore to show the text or nothing
    public string Display()
    {
        return _isHidden ? "" : _text;
    }
}
                              
