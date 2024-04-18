using System;

class Program
{
    static void Main(string[] args)
    {   
        // Create an instance of main program
        Program program = new Program(); 
        // Call Run method
        program.Run(); 
    }
    
    // a method would show the menu and let the user choose 
    public void Run()
    {
        while (true)  // continuing show user the menu
        {
            ShowMenu();  // show user the menu

            int choice = GetChoice();  // call GetChoice method to get the choice number

            Activity currentActivity = null;   // initialize the current activity object
            
            // a switch statement that separated each option
            switch (choice)
            {
                case 1: // when the user choose breathing activity

                    
                    currentActivity = new BreathingActivity(3,"This activity will help you relax by walking your through breathing in and out slowly. Clear your mind and focus on your breathing.");
                    // assign the current activity to the new created BreathingActivity object
                    // the parameters are duration and starting message respectively
                    break;

                case 2:  // when the user choose reflection activity

                    currentActivity = new ReflectionActivity(3,"This activity will help you reflect on times in your life when you have shown strength and resilience. This will help you recognize the power you have and how you can use it in other aspects of your life.");
                    // assign the current activity to the new created ReflectionActivity object
                    // the parameters are duration and starting message respectively
                    break;

                case 3: // when the user choose Listing activity

                    currentActivity = new ListingActivity(3, "This activity will help you reflect on the good things in your life by having you list as many things as you can in a certain area.");
                    // assign the current activity to the new created ListingActivity object
                    // the parameters are duration and starting message respectively
                    break;

                case 4:  // when the user choose to quit
                    Console.WriteLine("Exiting program...");   // show the message
                    return;

                default:  // a default option when the user doesn't enter a number
                    Console.WriteLine("Invalid choice. Please enter a number between 1 and 4.");
                    break;
            }

            if (currentActivity != null)    // if the currentActivity is not null, meaning the object is successfully created
            {
                currentActivity.StartActivity();  // call the startactivity method from Activity class, which is the base class
            }
        }
    }
    
    // a method to display the menu to the user
    public void ShowMenu()
    {
        Console.WriteLine("Menu:");
        Console.WriteLine(" 1. Breathing Activity");
        Console.WriteLine(" 2. Reflection Activity");
        Console.WriteLine(" 3. Listing Activity");
        Console.WriteLine(" 4. Quit");
    }
    

    // a method to strore user's choice
    public int GetChoice()
    {
        Console.Write("Enter your choice: ");

        int choice;  // initialize the variable choice

        while (!int.TryParse(Console.ReadLine(), out choice))  // check if the user enter an interger
        {
            Console.WriteLine("Invalid input. Please enter a number.");
            Console.Write("Enter your choice: ");
        }

        return choice;
    }
}
//---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

// base class
public class Activity
{
    protected string _description;
    protected int _duration;
    protected DateTime _startTime;  // create this variable so that i can use it in different methods in this class
    
    // constructor
    public Activity(int duration, string description)
    {
        _duration = duration;
        _description = description;
    }
    
    // a method that showing the user the starting steps
    public virtual void StartActivity()
    {
        Console.WriteLine("Let's begin!");  // starting message
        ShowSpinner(2000);  // rotating spiner 2 seconds
        Console.WriteLine(_description);  // show user the description message
        ShowSpinner(2000);  // rotating spinner 2 seconds
        _startTime = DateTime.Now;  // store the start time
    }
    
    // a method that shoing the user the ending messages
    public virtual void ShowEndingMessage()
    {
        ShowSpinner(3000); // rotating the spinner 3 seconds after finishing activity

        Console.WriteLine($"You have completed the activity.");  

        ShowSpinner(2000);  // rotating spinner 2 seconds

        DateTime endTime = DateTime.Now;  // get the time now after completing this activity
        TimeSpan totalTime = endTime - _startTime;  // calculate the time spans

        Console.WriteLine($"Total time spent: {totalTime.TotalSeconds} seconds");  // show user the time they span
        ShowSpinner(2000); // rotating spinner 2 sec
        Console.WriteLine("Good job!");   // ending message
        Thread.Sleep(2000); // rotating spinner 2 sec
    }


    // a method to show the rotating spinner so that i can easily use it in wherever i want
    protected void ShowSpinner(int duration)
    {
        DateTime startTime = DateTime.Now;  // initialize a start time for spinning

        while ((DateTime.Now - startTime).TotalMilliseconds < duration) 
        //calculates the time difference between the current time and the startTime
        //compares the total elapsed time with the specified duration
        {   
            //display the spinner
            Console.Write("/");
            Thread.Sleep(100);
            Console.Write("\b");
            Console.Write("-");
            Thread.Sleep(100);
            Console.Write("\b");
            Console.Write("\\");
            Thread.Sleep(100);
            Console.Write("\b");
            Console.Write("|");
            Thread.Sleep(100);
            Console.Write("\b");
        }
    }
}


//--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

// derived class
public class BreathingActivity : Activity
{
    // constructor
    public BreathingActivity(int duration, string description) : base(duration, description)
    {

    }

    public override void StartActivity()
    {
        base.StartActivity(); // call the base class's method
        Console.WriteLine("Get ready to start breathing.");
        ShowSpinner(4000); // rotating spinner 4 sec
        
        // a for loop that can display the breathing instruction
        for (int i = _duration; i >= 2 && i < 5; i++)  // counting number starts from duration number 3 until it hits 4
        {
            Console.WriteLine("Breathe in...");
            DisplayCountdown(i);
            Console.WriteLine("Breathe out...");
            DisplayCountdown(i);
        }

        base.ShowEndingMessage(); //call the base class's method to show ending message
    }

    // a method that will make the countdown work
    private void DisplayCountdown(int seconds)
    {
        for (int i = seconds; i >= 1; i--)
        {
            Console.Write($"{i} ");
            Thread.Sleep(1000); // Pause for 1 second
            Console.Write("\b \b"); // Erase the spinner
        }
        Console.WriteLine(); // display an empty line
    }
}



//--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

// derived class
public class ListingActivity : Activity
{   
    // list of prompts
    private string[] prompts = {
        "Who are people that you appreciate?",
        "What are personal strengths of yours?",
        "Who are people that you have helped this week?",
        "When have you felt the Holy Ghost this month?",
        "Who are some of your personal heroes?"
    };

    // constructor
    public ListingActivity(int duration, string description) : base(duration, description)
    {
    }

    // a method to start the activity
    public override void StartActivity()
    {
        base.StartActivity();  // cal the base class method
        Console.WriteLine("Get ready to start listing");
        ShowSpinner(2000);   // rotating spinner 2 sec
        
        Random random = new Random(); // create random object for future use
        string prompt = prompts[random.Next(prompts.Length)]; // randomly select prompt
        Console.WriteLine(prompt);  // display the prompt
        ShowSpinner(2000); // rotating spinner 2 sec

        List<string> items = new List<string>(); // create a list pbjet to store the items the user enter

        string input = "";  // initialize the input
        while (input.ToLower() != "done")  // check if the user enter "done"
        {
            Console.Write("Enter an item (or 'done' to finish): ");  // instruction message
            input = Console.ReadLine(); // store user input

            if (input.ToLower() != "done")  // if user  didn't enter done
            {
                items.Add(input);  // append the input to the list
            }
        }

        Console.WriteLine($"You entered {items.Count} items:");  // show user how many items they enter
        ShowSpinner(1000); //rotating spinner 1 sec

        foreach (string item in items)  // keep giving instructions to user to enter more items
        {
            Console.WriteLine(item); // show the user the items they entered
        }
        
        base.ShowEndingMessage();  // call the base class's method to show ending message
    }
}


//-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

// derived class
public class ReflectionActivity : Activity
{
    // list of prompts
    private string[] prompts = {
        "Think of a time when you stood up for someone else.",
        "Think of a time when you did something really difficult.",
        "Think of a time when you helped someone in need.",
        "Think of a time when you did something truly selfless."
    };
    
    // list of questions followed by the prompt showing
    private string[] questions = {
        "Why was this experience meaningful to you?",
        "Have you ever done anything like this before?",
        "How did you get started?",
        "How did you feel when it was complete?"
       
    };

    // constructor
    public ReflectionActivity(int duration, string description) : base(duration, description)
    {
        
    }
    
    

// a method to start the activity
    public override void StartActivity()
    {
        base.StartActivity();  // calling the base class method
        Console.WriteLine("Get ready to start reflecting");
        ShowSpinner(3000); // rotatiing spinner 3 sec
        
        Random random = new Random();  // create a random object so that we can use it later

        
        string prompt = prompts[random.Next(prompts.Length)];// randomly select the prompt
        Console.WriteLine(prompt);// show the prompt
        Thread.Sleep(1000);   // pause 1 sec

        foreach (string question in questions) // display each question in the question list
        {
            Console.WriteLine(question);  // show the question
            Thread.Sleep(1000); // Pause for 1 second before displaying the spinner
            ShowSpinner(5000);   // show rotating spinner for 5 sec
            Console.Write("\b \b"); // Erase the spinner
        }


        base.ShowEndingMessage();
    }
}

