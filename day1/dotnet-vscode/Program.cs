namespace AOC2021.Day1
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Advent of Code 2021 - Day 1 - Challenge 1");

            string filePath = "day1-input.txt";
            string[] inputLines = Utilities.LoadInput(filePath);

            int previousNumber = 0;
            int increaseCount = 0;
            foreach (string line in inputLines)
            {
                int currentNumber = Convert.ToInt32(line);

                if (currentNumber > previousNumber)
                {
                    increaseCount++;
                }

                previousNumber = currentNumber;
            }

            Console.WriteLine($"Total increases: {increaseCount}");
            Console.ReadKey(true);
        }
    }
}