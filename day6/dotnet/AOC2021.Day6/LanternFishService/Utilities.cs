namespace AOC2021.Day6.LanternFishService;

public class Utilities
{
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
