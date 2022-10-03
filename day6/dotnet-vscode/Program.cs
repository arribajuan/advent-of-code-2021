namespace AOC2021.Day6
{
    internal class Program
    {
        private static void Main(string[] args)
        {
            Console.WriteLine("Advent of Code 2021 - Day 6");

            #region Test data

            string filePath1 = "day6-input1.txt";
            List<int> inputNumbers1 = Utilities.LoadInput(filePath1);
            LanternFishCounts initialFish1 = Utilities.LoadBucketsFromInput(inputNumbers1);

            Console.WriteLine("");
            Console.WriteLine("Test data");
            Console.WriteLine($" - Total initial fish: {initialFish1.TotalFish}");

            LanternFishCounts sim1_18 = LanternFishSimulator.SimulateFish(initialFish1, 18);
            Console.WriteLine($" - Total initial fish after 18 days: {sim1_18.TotalFish}");     // Expect 26

            LanternFishCounts sim1_80 = LanternFishSimulator.SimulateFish(initialFish1, 80);
            Console.WriteLine($" - Total initial fish after 80 days: {sim1_80.TotalFish}");     // Expect 5934

            LanternFishCounts sim1_256 = LanternFishSimulator.SimulateFish(initialFish1, 256);
            Console.WriteLine($" - Total initial fish after 256 days: {sim1_256.TotalFish}");   // Expect 26984457539

            #endregion

            #region Puzzle data

            string filePath2 = "day6-input2.txt";
            List<int> inputNumbers2 = Utilities.LoadInput(filePath2);
            LanternFishCounts initialFish2 = Utilities.LoadBucketsFromInput(inputNumbers2);

            Console.WriteLine("");
            Console.WriteLine("Puzzle data");
            Console.WriteLine($" - Total initial fish: {initialFish2.TotalFish}");

            LanternFishCounts sim2_80 = LanternFishSimulator.SimulateFish(initialFish2, 80);
            Console.WriteLine($" - Total initial fish after 80 days: {sim2_80.TotalFish}");     // Answer 350917

            LanternFishCounts sim2_256 = LanternFishSimulator.SimulateFish(initialFish2, 256);
            Console.WriteLine($" - Total initial fish after 256 days: {sim2_256.TotalFish}");   // Answer 1592918715629 

            #endregion

            Console.ReadKey(true);
        }
    }
}