namespace AOC2021.Day6;

class LanternFishSimulator
{

    public LanternFishSimulator()
    {

    }

    public static LanternFishCounts SimulateFish(LanternFishCounts initialFish)
    {
        LanternFishCounts result = new LanternFishCounts();

        result.FishInTimer0 = initialFish.FishInTimer1;
        result.FishInTimer1 = initialFish.FishInTimer2;
        result.FishInTimer2 = initialFish.FishInTimer3;
        result.FishInTimer3 = initialFish.FishInTimer4;
        result.FishInTimer4 = initialFish.FishInTimer5;
        result.FishInTimer5 = initialFish.FishInTimer6;
        result.FishInTimer6 = initialFish.FishInTimer7 + initialFish.FishInTimer0;
        result.FishInTimer7 = initialFish.FishInTimer8;
        result.FishInTimer8 = initialFish.FishInTimer0;

        return result;
    }

    public static LanternFishCounts SimulateFish(LanternFishCounts initialFish, int rounds)
    {
        LanternFishCounts result = initialFish;

        for (int i = 0; i < rounds; i++)
        {
            result = LanternFishSimulator.SimulateFish(result);
        }

        return result;
    }
}