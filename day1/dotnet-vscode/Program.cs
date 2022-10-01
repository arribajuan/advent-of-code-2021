namespace AOC2021.Day1
{
    class Program
    {
        private static void Challenge1(string[] inputLines)
        {
            Console.WriteLine(" - Challenge 1");

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

            Console.WriteLine($" - Total increases: {increaseCount}");
        }

        static void Main(string[] args)
        {
            Console.WriteLine("Advent of Code 2021 - Day 1");

            string filePath = "day1-input.txt";
            string[] inputLines = Utilities.LoadInput(filePath);

            Challenge1(inputLines);

            Console.ReadKey(true);
        }
    }
}