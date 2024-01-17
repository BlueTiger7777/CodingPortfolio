// Wait for the user to respond to change the seed
using System.Runtime.InteropServices;
using System.Security.Cryptography;
using System.Xml;

Console.Write("Press Enter to generate a modual\n");
Console.ReadKey();

// Setup
Random rand = new Random();
int modual = rand.Next(1, 2);
var indicator = new List<string> { "SND", "CLR", "CAR", "IND", "FRQ", "SIG", "NSA", "MSA", "TRN", "BOB", "FRK" };
var battery = new List<string> { "AA", "D" };
var port = new List<string> { "DVI-D", "Parallel", "PS/2", "RJ-45", "Serial", "Stereo RCA" };
var serialLetters = new List<string> { "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Z" };
var serialNumbers = new List<string> { "1", "2", "3", "4", "5", "6", "7", "8", "9", "0" };

// Serial Number Generation
var serial = "";
int serialIndex = 0;
int letNum = 0;
var serialLetPos = rand.Next(1, 6);
for (int i = 0; i < 5; i++)
{
    if (i == serialLetPos)
    {
        serialIndex = rand.Next(serialLetters.Count);
        serial += serialLetters[serialIndex];
    }
    else
    {
        letNum = rand.Next(1, 3);
        if (letNum == 1)
        {
            serialIndex = rand.Next(serialLetters.Count);
            serial += serialLetters[serialIndex];
        }
        else
        {
            serialIndex = rand.Next(serialNumbers.Count);
            serial += serialNumbers[serialIndex];
        }
    }
}
serialIndex = rand.Next(serialNumbers.Count);
serial += serialNumbers[serialIndex];
Console.WriteLine(serial);

switch (modual)
{
    case 1:
        Console.Write("Wires\n");
        int wireNum = rand.Next(3, 7);
        var wireColours = new List<string> { "Yellow", "Red", "Blue", "Black", "White" };
        var wires = new List<string> { };
        switch (wireNum)
        {
            case 3:
                Console.Write("Three Wires\n");
                break;
            case 4:
                Console.Write("Four Wires\n");
                break;
            case 5:
                Console.Write("Five Wires\n");
                break;
            case 6:
                Console.Write("Six Wires\n");
                break;
        }
        break;
    case 2:
        Console.Write("Button\n");
        break;
    case 3:
        Console.Write("Keypads\n");
        break;
    case 4:
        Console.Write("Simon Says\n");
        break;
    case 5:
        Console.Write("Who's on First\n");
        break;
    case 6:
        Console.Write("Memory\n");
        break;
    case 7:
        Console.Write("Morse Code\n");
        break;
    case 8:
        Console.Write("Complicated Wires\n");
        break;
    case 9:
        Console.Write("Wire Sequences\n");
        break;
    case 10:
        Console.Write("Mazes\n");
        break;
    case 11:
        Console.Write("Passwords\n");
        break;
}