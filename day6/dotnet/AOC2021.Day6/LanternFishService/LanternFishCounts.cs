namespace AOC2021.Day6.LanternFishService;

public class LanternFishCounts
{
    public long FishInTimer0 = 0;
    public long FishInTimer1 = 0;
    public long FishInTimer2 = 0;
    public long FishInTimer3 = 0;
    public long FishInTimer4 = 0;
    public long FishInTimer5 = 0;
    public long FishInTimer6 = 0;
    public long FishInTimer7 = 0;
    public long FishInTimer8 = 0;

    public LanternFishCounts()
    {
        this.FishInTimer0 = 0;
        this.FishInTimer1 = 0;
        this.FishInTimer2 = 0;
        this.FishInTimer3 = 0;
        this.FishInTimer4 = 0;
        this.FishInTimer5 = 0;
        this.FishInTimer6 = 0;
        this.FishInTimer7 = 0;
        this.FishInTimer8 = 0;
    }

    public long TotalFish
    {
        get { return this.FishInTimer0 + this.FishInTimer1 + this.FishInTimer2 + this.FishInTimer3 + this.FishInTimer4 + this.FishInTimer5 + this.FishInTimer6 + this.FishInTimer7 + this.FishInTimer8; }
    }
}