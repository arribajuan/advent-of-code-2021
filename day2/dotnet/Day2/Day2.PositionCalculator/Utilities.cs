namespace Day2.PositionCalculator
{
    public class Utilities
    {
        public static List<int> LoadInput(string filePath)
        {
            List<int> result = new List<int>();

            string[] fileLines = File.ReadAllLines(filePath, System.Text.Encoding.Default);

            foreach (string line in fileLines)
            {
                Console.WriteLine(line);
            }

            //char[] spearator = { ',' };
            //String[] strlist = fileLines[0].Split(spearator, StringSplitOptions.TrimEntries);       // Unsafe assumption that we have at least one line of texts

            //foreach (String s in strlist)
            //{
            //    result.Add(Convert.ToInt32(s));
            //}

            return result;
        }
    }
}