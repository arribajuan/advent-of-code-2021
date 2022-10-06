using Day2.PositionCalculator;

namespace Day2.CLI
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Advent of Code 2021 - Day 2");

            string filePath = "./Inputs/day2-input.txt";
            List<SubmarineMovement> movements = Utilities.LoadInput(filePath);
            Console.WriteLine(" - Input loaded");

            int result1 = Challenge1.Solution(movements);
            Console.WriteLine($" - Challenge 1: {result1}");

            int result2 = Challenge2.Solution(movements);
            Console.WriteLine($" - Challenge 2: {result2}");
        }
    }
}