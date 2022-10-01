using System.IO;

namespace AOC2021.Day1
{
    internal class Utilities
    {
        public static string[] LoadInput(string filePath)
        {
            return File.ReadAllLines(filePath, System.Text.Encoding.Default);
        }
    }
}