class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("Please select an action:");
        Console.WriteLine("1. Start writing\n2. Load history\n3. Display the journal");

        int choice = int.Parse(Console.ReadLine());

        Journal journal = new Journal();
        string filePath = "myjournal.csv";

        switch (choice)
        {
            case 1:
                Console.WriteLine("What's your name?");
                string name = Console.ReadLine();

                do
                {
                    Prompt.DisplayRandomPrompt();
                    Console.WriteLine("Write your response (or type 'exit' to stop):");
                    string response = Console.ReadLine();

                    if (response.ToLower() == "exit")
                        break;

                    Entry entry = new Entry
                    {
                        _Date = DateTime.Now.ToShortDateString(),
                        _Name = name,
                        _Response = response
                    };

                    journal.AddEntry(entry);
                } while (true);

                journal.Save(filePath);
                Console.WriteLine("Entries have been saved to the file.");
                break;

            case 2:
                Console.WriteLine("Enter the date you want to see (date format: yyyy/MM/dd):");
                string selectDate = Console.ReadLine();
                journal.Load(filePath);

                var entriesForDate = journal.GetEntriesForDate(selectDate);

                if (entriesForDate.Any())
                {
                    foreach (var entry in entriesForDate)
                    {
                        Console.WriteLine($"Date: {entry._Date}, Name: {entry._Name}, Response: {entry._Response}");
                    }
                }
                else
                {
                    Console.WriteLine($"No entries found for date: {selectDate}");
                }
                break;

            case 3:
                journal.Load(filePath);
                journal.Display();
                break;

            default:
                Console.WriteLine("Invalid choice");
                break;
        }
    }
}



//-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

public class Entry
{
    public string _Date;
    public string _Name;
    public string _Response;
}


//-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

public class Journal
{
    public List<Entry> Entries = new List<Entry>();

    public void AddEntry(Entry entry)
    {
        Entries.Add(entry);
    }

    public List<Entry> GetEntriesForDate(string date)
    {
        return Entries.Where(entry => entry._Date == date).ToList();
    }

    public void Save(string filePath)
    {
        using (StreamWriter sw = File.AppendText(filePath))
        {
            foreach (Entry entry in Entries)
            {
                sw.WriteLine($"{entry._Date},{entry._Name},{entry._Response}");
            }
        }
    }

    public void Load(string filePath)
    {
        Entries.Clear();

        if (File.Exists(filePath))
        {
            string[] lines = File.ReadAllLines(filePath);
            foreach (string line in lines)
            {
                string[] parts = line.Split(',');
                Entry entry = new Entry
                {
                    _Date = parts[0],
                    _Name = parts[1],
                    _Response = parts[2]
                };
                Entries.Add(entry);
            }
        }
        else
        {
            Console.WriteLine("The specified file does not exist.");
        }
    }

    public void Display()
    {
        foreach (Entry entry in Entries)
        {
            Console.WriteLine($"Date: {entry._Date}, Name: {entry._Name}, Response: {entry._Response}");
        }
    }
}




//-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

public class Prompt
{
    private static List<string> prompts = new List<string>
    {
        "What was the best part of my day?",
        "What was the strongest emotion I felt today?",
        "If I could change one thing about today, what would it be?"
    };

    public static void DisplayRandomPrompt()
    {
        Random random = new Random();
        int randomIndex = random.Next(0, prompts.Count);
        string randomPrompt = prompts[randomIndex];
        Console.WriteLine(randomPrompt);
    }
}
