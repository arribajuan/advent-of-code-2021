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

        private static void Challenge2(string[] inputLines)
        {
            Console.WriteLine(" - Challenge 2");

            int increaseCount = 0;
            for (int i = 0; i < inputLines.Length - 4; i++)
            {
                int num1 = Convert.ToInt32(inputLines[i]);
                int num2 = Convert.ToInt32(inputLines[i + 1]);
                int num3 = Convert.ToInt32(inputLines[i + 2]);
                int num4 = Convert.ToInt32(inputLines[i + 3]);

                int sum1 = num1 + num2 + num3;
                int sum2 = num2 + num3 + num4;

                if (sum2 > sum1)
                {
                    increaseCount++;
                }
            }

            Console.WriteLine($" - Total increases: {increaseCount}");
        }

        static void Main(string[] args)
        {
            Console.WriteLine("Advent of Code 2021 - Day 1");

            string filePath = "day1-input.txt";
            string[] inputLines = Utilities.LoadInput(filePath);

            Challenge1(inputLines);
            Challenge2(inputLines);

            Console.ReadKey(true);
        }
    }
}
