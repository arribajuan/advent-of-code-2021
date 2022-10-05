using Day2.PositionCalculator;

namespace Day2.CLI
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello, World!");


            //string filePath1 = "/Inputs/day6-input1.txt";
            string filePath = "D:\\code\\repos\\advent-of-code-2021\\advent-of-code-2021\\day2\\dotnet\\Day2\\Day2\\Inputs\\day2-input.txt";

            List<int> result = Utilities.LoadInput(filePath);

            // This points to the correct path, but the files are not eing copied ... troubleshoot this
            //string filePath1 = System.AppContext.BaseDirectory + "Inputs\\day6-input1.txt";



        }


    }
}