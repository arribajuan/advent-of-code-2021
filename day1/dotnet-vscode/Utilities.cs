namespace AOC2021.Day1
{
    using System.IO;

    class Utilities
    {
        public static string[] LoadInput(string filePath)
        {
            return File.ReadAllLines(filePath, System.Text.Encoding.Default);
        }
    }
}