using System;

public class Program
{
    static void Main(string[] args)
    {
        Manager manager = new Manager();  // create manager object

        while (true)
        {
            ShowMenu();
            int choice = GetChoice();  // store the user input of choice

            switch (choice)
            {
                case 1:
                    manager.CreateNewGoal();
                    break;
                case 2:
                    manager.LoadGoalsFromFile(); // Load goals from file
                    manager.DisplayGoals(); // Display loaded goals 
                    break;
                case 3:
                    manager.SaveGoalsToFile();
                    break;
                case 4:
                    manager.DisplayScoreAndStatus();
                    break;
                case 5:
                    Console.WriteLine("what's the name of the goal that you want to record?");
                    string name = Console.ReadLine();
                    manager.RecordEvent(name);
                    break;
                case 6:
                    Console.WriteLine("Exiting program...");
                    return;
                default:
                    Console.WriteLine("Invalid choice. Please enter a number between 1 and 6.");
                    break;
            }
        }
    }
    

    // show the user the menu
    static void ShowMenu()
    {
        Console.WriteLine("Menu:");
        Console.WriteLine("1. Create New Goal");
        Console.WriteLine("2. List Goals");
        Console.WriteLine("3. Save Goals");
        Console.WriteLine("4. Load Goals");
        Console.WriteLine("5. Record Event");
        Console.WriteLine("6. Quit");
        Console.Write("Enter your choice: ");
    }
    
    // get user's choice
    static int GetChoice()
    {
        int choice;
        while (!int.TryParse(Console.ReadLine(), out choice))
        {
            Console.WriteLine("Invalid input. Please enter a number.");
            Console.Write("Enter your choice: ");
        }
        return choice;
    }
}


//--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

// base class
public abstract class Goal
{
    protected string _name;   // name of the goal
    protected int _value;    // how many points of the goal
    public virtual bool IsComplete { get; protected set; }  // a bool value and another way to do getter and setters

    // Constructor
    public Goal(string name, int value)
    {
        _name = name;
        _value = value;
    }

    // getters
    public int GetValue()
    {
        return _value;
    }

    public string GetName()
    {
        return _name;
    }

    public virtual string GetDescription()
    {
        return $"Name: {_name}, Value: {_value}";
    }

    // Abstract method to mark the goal as complete
    public abstract void MarkComplete();

    // Method to get the string representation of the goal
    public virtual string GetStringRepresentation()
    {
        return $"{GetType().Name}:{_name}:{_value}";
    }
    

    
}


//-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

// derived class
public class ChecklistGoal : Goal
{
    private int _targetCount;  // how many times in total
    private int _completedCount;   // completed times
    
    // constructor
    public ChecklistGoal(string name, int value, int targetCount, int completedCount) : base(name, value)
    {
        _targetCount = targetCount;
        _completedCount = completedCount;
    }
    
    // a method to mark the checklist goal is complete
    public override void MarkComplete()
    {
        _completedCount++;
        IsComplete = _completedCount >= _targetCount; // Update IsComplete based on completion status
        Console.WriteLine($"Goal '{_name}' completed {_completedCount}/{_targetCount} times! You gained {_value} points.");
        
        if (IsComplete)
        {
            Console.WriteLine($"Congratulations! You achieved the goal '{_name}' {_targetCount} times and received a bonus of {_value * 2} points.");
        }
    }

    public override string GetDescription()
    {
        return base.GetDescription() + $" - {_completedCount}/{_targetCount} ({(_completedCount >= _targetCount ? "Complete" : "Incomplete")})";
    }
}

//---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

using System;
using System.Collections.Generic;
using System.IO;

// a class to handle all the operations
public class Manager
{
    private List<Goal> goals = new List<Goal>();   // a list of goals
    private int totalScore = 0;   // initialize the score

    public void AddGoal(Goal goal)
    {
        goals.Add(goal);
    }


    public void DisplayGoals()
    {
        foreach (var goal in goals)
        {
            Console.WriteLine(goal.GetDescription());
        }
    }

    // when people choose load, show them the score and status of goals
    public void DisplayScoreAndStatus()
    {
        Console.WriteLine("Goal Status:");
        foreach (var goal in goals)
        {
            Console.WriteLine($"{goal.GetDescription()} - {(goal.IsComplete ? "Complete" : "Incomplete")}");
        }
        Console.WriteLine($"Total Score: {totalScore}");
    }

    public void SaveGoalsToFile()
    {
        using (StreamWriter writer = new StreamWriter("goals.txt"))
        {
            foreach (var goal in goals)
            {
                writer.WriteLine(goal.GetStringRepresentation());
            }
        }
    }

    public void LoadGoalsFromFile()
    {
        goals.Clear();

        if (File.Exists("goals.txt"))
        {
            string[] lines = File.ReadAllLines("goals.txt");

            foreach (string line in lines)
            {
                // Parse each line and create Goal objects
                string[] parts = line.Split(':');
                string type = parts[0];
                string name = parts[1];
                int value = int.Parse(parts[2]);

                Goal goal;

                if (type == "SimpleGoal")
                {
                    goal = new SimpleGoal(name, value);
                }
                else if (type == "EternalGoal")
                {
                    goal = new EternalGoal(name, value);
                }
                else // Assuming it's ChecklistGoal
                {
                    int targetCount = 0;
                    int completedCount = 0;

                    if (parts.Length > 3)
                    {
                        // Parse the target count
                        string[] counts = parts[3].Split('/');
                        targetCount = int.Parse(counts[0]);

                        // Parse the completed count
                        if (counts.Length > 1)
                        {
                            completedCount = int.Parse(counts[1]);
                        }
                    }

                    goal = new ChecklistGoal(name, value, targetCount, completedCount);
                }

                goals.Add(goal);
            }
        }
    }


    // a method to create different kinds of new goals
    public void CreateNewGoal()
    {
        Console.WriteLine("Select the type of goal:");
        Console.WriteLine("1. Simple Goal");
        Console.WriteLine("2. Eternal Goal");
        Console.WriteLine("3. Checklist Goal");
        int choice;
        while (!int.TryParse(Console.ReadLine(), out choice) || choice < 1 || choice > 3)
        {
            Console.WriteLine("Invalid input. Please enter a number between 1 and 3.");
        }

        string name;
        int value;
        int targetCount;
        int completedCount = 0; // Initialize completedCount
        
        // differentiate what type of goals the user is creating
        switch (choice)
        {
            case 1:
                Console.Write("Enter the name of the simple goal: ");
                name = Console.ReadLine();
                Console.Write("Enter the value of the simple goal: ");
                while (!int.TryParse(Console.ReadLine(), out value))
                {
                    Console.WriteLine("Invalid input. Please enter a valid integer value.");
                }
                AddGoal(new SimpleGoal(name, value));
                break;
            case 2:
                Console.Write("Enter the name of the eternal goal: ");
                name = Console.ReadLine();
                Console.Write("Enter the value of the eternal goal: ");
                while (!int.TryParse(Console.ReadLine(), out value))
                {
                    Console.WriteLine("Invalid input. Please enter a valid integer value.");
                }
                AddGoal(new EternalGoal(name, value));
                break;
            case 3:
                Console.Write("Enter the name of the checklist goal: ");
                name = Console.ReadLine();
                Console.Write("Enter the value of the checklist goal: ");
                while (!int.TryParse(Console.ReadLine(), out value))
                {
                    Console.WriteLine("Invalid input. Please enter a valid integer value.");
                }
                Console.Write("Enter the target count for the checklist goal: ");
                while (!int.TryParse(Console.ReadLine(), out targetCount) || targetCount < 1)
                {
                    Console.WriteLine("Invalid input. Please enter a positive integer value.");
                }
                // Initialize completedCount to 0 when creating a new checklist goal
                AddGoal(new ChecklistGoal(name, value, targetCount, completedCount));
                break;
        }
    }

    // when the user choose 5
    public void RecordEvent(string name)
    {
        Goal goal = goals.Find(g => g.GetName() == name);

        if (goal != null)
        {
            if (goal is ChecklistGoal checklistGoal) // Check if the goal is a ChecklistGoal
            {
                checklistGoal.MarkComplete(); // Call MarkComplete directly on ChecklistGoal
            }
            else
            {
                goal.MarkComplete(); // For other types of goals, call MarkComplete as usual
            }

            totalScore += goal.GetValue();
        }
        else
        {
            Console.WriteLine("Goal not found.");
        }
    }

    // a method to check the status of goals
    public void CheckGoalStatus()
    {
        foreach (var goal in goals)
        {
            if (!goal.IsComplete)
            {
                Console.WriteLine($"Goal '{goal.GetName()}' is incomplete.");
            }
        }
    }


}


//-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

// derived class
public class SimpleGoal : Goal
{   

    // constructor
    public SimpleGoal(string name, int value) : base(name, value)
    {
    }

    // Method to mark the simple goal as complete
    public override void MarkComplete()
    {
        Console.WriteLine($"Goal '{_name}' completed! You gained {_value} points.");
    }
}


//-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

// derived class
public class EternalGoal : Goal
{
    // constructor
    public EternalGoal(string name, int value) : base(name, value)
    {
    }

    // Method to mark the eternal goal as complete (simply rewards the user)
    public override void MarkComplete()
    {
        Console.WriteLine($"Goal '{_name}' completed! You gained {_value} points.");
    }
}
