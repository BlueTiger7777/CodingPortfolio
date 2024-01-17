// Declare variables and then initialize to zero
int num1 = 0; int num2 = 0;

// Displat tital as the C# console calculator app
Console.WriteLine("Console Calculator in C#\r");
Console.WriteLine("------------------------\n");

// Loops through the code infefinetly
while (true)
{
    // Asks the user to type the first number
    Console.WriteLine("Type a number, and then press Enter");
    num1 = Convert.ToInt32(Console.ReadLine());

    // Asks the user to eype the second number
    Console.WriteLine("Type another number, and then press Enter");
    num2 = Convert.ToInt32(Console.ReadLine());

    // Ask the user to choose an option
    Console.WriteLine("Choose an option from the following list:");
    Console.WriteLine("\ta - Add");
    Console.WriteLine("\ts - Subtract");
    Console.WriteLine("\tm - Multiply");
    Console.WriteLine("\td - Divide");
    Console.Write("Your Option? ");

    // Use a switch statement to do the math
    switch (Console.ReadLine())
    {
        case "a":
            Console.WriteLine($"Your result: {num1} + {num2} = {num1 + num2}");
            break;
        case "s":
            Console.WriteLine($"Your result: {num1} - {num2} = {num1 - num2}");
            break;
        case "m":
            Console.WriteLine($"Your result: {num1} * {num2} = {num1 * num2}");
            break;
        case "d":
            Console.WriteLine($"Your result: {num1} / {num2} = {num1 / num2}");
            break;
    }
    // Wait for the user to respond before closing
    Console.Write("Press Enter to calculate a new pair of numbers\n");
    Console.ReadKey();
}