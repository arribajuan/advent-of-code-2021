namespace AOC2021.Day6.LanternFishService;

public class Utilities
{
    public static List<int> LoadInput(string filePath)
    {
        List<int> result = new List<int>();

        string[] fileLines = File.ReadAllLines(filePath, System.Text.Encoding.Default);

        char[] spearator = { ',' };
        String[] strlist = fileLines[0].Split(spearator, StringSplitOptions.TrimEntries);       // Unsafe assumption that we have at least one line of texts

        foreach (String s in strlist)
        {
            result.Add(Convert.ToInt32(s));
        }

        return result;
    }

    public static LanternFishCounts LoadBucketsFromInput(List<int> inputNumbers)
    {
        LanternFishCounts result = new LanternFishCounts();

        foreach (int number in inputNumbers)
        {
            if (number == 0) { result.FishInTimer0++; }
            if (number == 1) { result.FishInTimer1++; }
            if (number == 2) { result.FishInTimer2++; }
            if (number == 3) { result.FishInTimer3++; }
            if (number == 4) { result.FishInTimer4++; }
            if (number == 5) { result.FishInTimer5++; }
            if (number == 6) { result.FishInTimer6++; }
            if (number == 7) { result.FishInTimer7++; }
            if (number == 8) { result.FishInTimer8++; }
        }

        return result;
    }

    public static bool CompareLanterFishCounts(LanternFishCounts fish1, LanternFishCounts fish2)
    {
        bool result = false;
        if (fish1.FishInTimer0 == fish2.FishInTimer0
            && fish1.FishInTimer1 == fish2.FishInTimer1
            && fish1.FishInTimer2 == fish2.FishInTimer2
            && fish1.FishInTimer3 == fish2.FishInTimer3
            && fish1.FishInTimer4 == fish2.FishInTimer4
            && fish1.FishInTimer5 == fish2.FishInTimer5
            && fish1.FishInTimer6 == fish2.FishInTimer6
            && fish1.FishInTimer7 == fish2.FishInTimer7
            && fish1.FishInTimer8 == fish2.FishInTimer8)
        {
            result = true;
        }

        return result;
    }
}
