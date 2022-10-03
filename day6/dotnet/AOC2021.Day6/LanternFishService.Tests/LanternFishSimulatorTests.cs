using Xunit;
using AOC2021.Day6.LanternFishService;

namespace AOC2021.Day6.LanternFishService.Tests;

public class UnitTLanternFishSimulatorTests
{
    #region Basic unit tests

    [Fact]
    public void NoInitialFish()
    {
        #region test setup

        LanternFishCounts initialFish = new LanternFishCounts();
        initialFish.FishInTimer0 = 0;
        initialFish.FishInTimer1 = 0;
        initialFish.FishInTimer2 = 0;
        initialFish.FishInTimer3 = 0;
        initialFish.FishInTimer4 = 0;
        initialFish.FishInTimer5 = 0;
        initialFish.FishInTimer6 = 0;
        initialFish.FishInTimer7 = 0;
        initialFish.FishInTimer8 = 0;

        LanternFishCounts expected = new LanternFishCounts();
        expected.FishInTimer0 = 0;
        expected.FishInTimer1 = 0;
        expected.FishInTimer2 = 0;
        expected.FishInTimer3 = 0;
        expected.FishInTimer4 = 0;
        expected.FishInTimer5 = 0;
        expected.FishInTimer6 = 0;
        expected.FishInTimer7 = 0;
        expected.FishInTimer8 = 0;

        #endregion

        LanternFishCounts simulatedFish = LanternFishSimulator.SimulateFish(initialFish);
        bool result = Utilities.CompareLanterFishCounts(expected, simulatedFish);

        Assert.True(result, "No initial fish, no simulated fish ... ");
    }

    [Fact]
    public void FishInTimer0()
    {
        #region test setup

        LanternFishCounts initialFish = new LanternFishCounts();
        initialFish.FishInTimer0 = 1;
        initialFish.FishInTimer1 = 0;
        initialFish.FishInTimer2 = 0;
        initialFish.FishInTimer3 = 0;
        initialFish.FishInTimer4 = 0;
        initialFish.FishInTimer5 = 0;
        initialFish.FishInTimer6 = 0;
        initialFish.FishInTimer7 = 0;
        initialFish.FishInTimer8 = 0;

        LanternFishCounts expected = new LanternFishCounts();
        expected.FishInTimer0 = 0;
        expected.FishInTimer1 = 0;
        expected.FishInTimer2 = 0;
        expected.FishInTimer3 = 0;
        expected.FishInTimer4 = 0;
        expected.FishInTimer5 = 0;
        expected.FishInTimer6 = 1;
        expected.FishInTimer7 = 0;
        expected.FishInTimer8 = 1;

        #endregion

        LanternFishCounts simulatedFish = LanternFishSimulator.SimulateFish(initialFish);
        bool result = Utilities.CompareLanterFishCounts(expected, simulatedFish);

        Assert.True(result, "Generates fish in timer 6 and 8");
    }

    [Fact]
    public void FishInTimer1()
    {
        #region test setup

        LanternFishCounts initialFish = new LanternFishCounts();
        initialFish.FishInTimer0 = 0;
        initialFish.FishInTimer1 = 1;
        initialFish.FishInTimer2 = 0;
        initialFish.FishInTimer3 = 0;
        initialFish.FishInTimer4 = 0;
        initialFish.FishInTimer5 = 0;
        initialFish.FishInTimer6 = 0;
        initialFish.FishInTimer7 = 0;
        initialFish.FishInTimer8 = 0;

        LanternFishCounts expected = new LanternFishCounts();
        expected.FishInTimer0 = 1;
        expected.FishInTimer1 = 0;
        expected.FishInTimer2 = 0;
        expected.FishInTimer3 = 0;
        expected.FishInTimer4 = 0;
        expected.FishInTimer5 = 0;
        expected.FishInTimer6 = 0;
        expected.FishInTimer7 = 0;
        expected.FishInTimer8 = 0;

        #endregion

        LanternFishCounts simulatedFish = LanternFishSimulator.SimulateFish(initialFish);
        bool result = Utilities.CompareLanterFishCounts(expected, simulatedFish);

        Assert.True(result, "Generates fish in timer 0");
    }

    [Fact]
    public void FishInTimer2()
    {
        #region test setup

        LanternFishCounts initialFish = new LanternFishCounts();
        initialFish.FishInTimer0 = 0;
        initialFish.FishInTimer1 = 0;
        initialFish.FishInTimer2 = 1;
        initialFish.FishInTimer3 = 0;
        initialFish.FishInTimer4 = 0;
        initialFish.FishInTimer5 = 0;
        initialFish.FishInTimer6 = 0;
        initialFish.FishInTimer7 = 0;
        initialFish.FishInTimer8 = 0;

        LanternFishCounts expected = new LanternFishCounts();
        expected.FishInTimer0 = 0;
        expected.FishInTimer1 = 1;
        expected.FishInTimer2 = 0;
        expected.FishInTimer3 = 0;
        expected.FishInTimer4 = 0;
        expected.FishInTimer5 = 0;
        expected.FishInTimer6 = 0;
        expected.FishInTimer7 = 0;
        expected.FishInTimer8 = 0;

        #endregion

        LanternFishCounts simulatedFish = LanternFishSimulator.SimulateFish(initialFish);
        bool result = Utilities.CompareLanterFishCounts(expected, simulatedFish);

        Assert.True(result, "Generates fish in timer 1");
    }

    [Fact]
    public void FishInTimer3()
    {
        #region test setup

        LanternFishCounts initialFish = new LanternFishCounts();
        initialFish.FishInTimer0 = 0;
        initialFish.FishInTimer1 = 0;
        initialFish.FishInTimer2 = 0;
        initialFish.FishInTimer3 = 1;
        initialFish.FishInTimer4 = 0;
        initialFish.FishInTimer5 = 0;
        initialFish.FishInTimer6 = 0;
        initialFish.FishInTimer7 = 0;
        initialFish.FishInTimer8 = 0;

        LanternFishCounts expected = new LanternFishCounts();
        expected.FishInTimer0 = 0;
        expected.FishInTimer1 = 0;
        expected.FishInTimer2 = 1;
        expected.FishInTimer3 = 0;
        expected.FishInTimer4 = 0;
        expected.FishInTimer5 = 0;
        expected.FishInTimer6 = 0;
        expected.FishInTimer7 = 0;
        expected.FishInTimer8 = 0;

        #endregion

        LanternFishCounts simulatedFish = LanternFishSimulator.SimulateFish(initialFish);
        bool result = Utilities.CompareLanterFishCounts(expected, simulatedFish);

        Assert.True(result, "Generates fish in timer 2");
    }

    [Fact]
    public void FishInTimer4()
    {
        #region test setup

        LanternFishCounts initialFish = new LanternFishCounts();
        initialFish.FishInTimer0 = 0;
        initialFish.FishInTimer1 = 0;
        initialFish.FishInTimer2 = 0;
        initialFish.FishInTimer3 = 0;
        initialFish.FishInTimer4 = 1;
        initialFish.FishInTimer5 = 0;
        initialFish.FishInTimer6 = 0;
        initialFish.FishInTimer7 = 0;
        initialFish.FishInTimer8 = 0;

        LanternFishCounts expected = new LanternFishCounts();
        expected.FishInTimer0 = 0;
        expected.FishInTimer1 = 0;
        expected.FishInTimer2 = 0;
        expected.FishInTimer3 = 1;
        expected.FishInTimer4 = 0;
        expected.FishInTimer5 = 0;
        expected.FishInTimer6 = 0;
        expected.FishInTimer7 = 0;
        expected.FishInTimer8 = 0;

        #endregion

        LanternFishCounts simulatedFish = LanternFishSimulator.SimulateFish(initialFish);
        bool result = Utilities.CompareLanterFishCounts(expected, simulatedFish);

        Assert.True(result, "Generates fish in timer 3");
    }

    [Fact]
    public void FishInTimer5()
    {
        #region test setup

        LanternFishCounts initialFish = new LanternFishCounts();
        initialFish.FishInTimer0 = 0;
        initialFish.FishInTimer1 = 0;
        initialFish.FishInTimer2 = 0;
        initialFish.FishInTimer3 = 0;
        initialFish.FishInTimer4 = 0;
        initialFish.FishInTimer5 = 1;
        initialFish.FishInTimer6 = 0;
        initialFish.FishInTimer7 = 0;
        initialFish.FishInTimer8 = 0;

        LanternFishCounts expected = new LanternFishCounts();
        expected.FishInTimer0 = 0;
        expected.FishInTimer1 = 0;
        expected.FishInTimer2 = 0;
        expected.FishInTimer3 = 0;
        expected.FishInTimer4 = 1;
        expected.FishInTimer5 = 0;
        expected.FishInTimer6 = 0;
        expected.FishInTimer7 = 0;
        expected.FishInTimer8 = 0;

        #endregion

        LanternFishCounts simulatedFish = LanternFishSimulator.SimulateFish(initialFish);
        bool result = Utilities.CompareLanterFishCounts(expected, simulatedFish);

        Assert.True(result, "Generates fish in timer 4");
    }

    [Fact]
    public void FishInTimer6()
    {
        #region test setup

        LanternFishCounts initialFish = new LanternFishCounts();
        initialFish.FishInTimer0 = 0;
        initialFish.FishInTimer1 = 0;
        initialFish.FishInTimer2 = 0;
        initialFish.FishInTimer3 = 0;
        initialFish.FishInTimer4 = 0;
        initialFish.FishInTimer5 = 0;
        initialFish.FishInTimer6 = 1;
        initialFish.FishInTimer7 = 0;
        initialFish.FishInTimer8 = 0;

        LanternFishCounts expected = new LanternFishCounts();
        expected.FishInTimer0 = 0;
        expected.FishInTimer1 = 0;
        expected.FishInTimer2 = 0;
        expected.FishInTimer3 = 0;
        expected.FishInTimer4 = 0;
        expected.FishInTimer5 = 1;
        expected.FishInTimer6 = 0;
        expected.FishInTimer7 = 0;
        expected.FishInTimer8 = 0;

        #endregion

        LanternFishCounts simulatedFish = LanternFishSimulator.SimulateFish(initialFish);
        bool result = Utilities.CompareLanterFishCounts(expected, simulatedFish);

        Assert.True(result, "Generates fish in timer 5");
    }

    [Fact]
    public void FishInTimer7()
    {
        #region test setup

        LanternFishCounts initialFish = new LanternFishCounts();
        initialFish.FishInTimer0 = 0;
        initialFish.FishInTimer1 = 0;
        initialFish.FishInTimer2 = 0;
        initialFish.FishInTimer3 = 0;
        initialFish.FishInTimer4 = 0;
        initialFish.FishInTimer5 = 0;
        initialFish.FishInTimer6 = 0;
        initialFish.FishInTimer7 = 1;
        initialFish.FishInTimer8 = 0;

        LanternFishCounts expected = new LanternFishCounts();
        expected.FishInTimer0 = 0;
        expected.FishInTimer1 = 0;
        expected.FishInTimer2 = 0;
        expected.FishInTimer3 = 0;
        expected.FishInTimer4 = 0;
        expected.FishInTimer5 = 0;
        expected.FishInTimer6 = 1;
        expected.FishInTimer7 = 0;
        expected.FishInTimer8 = 0;

        #endregion

        LanternFishCounts simulatedFish = LanternFishSimulator.SimulateFish(initialFish);
        bool result = Utilities.CompareLanterFishCounts(expected, simulatedFish);

        Assert.True(result, "Generates fish in timer 6");
    }

    [Fact]
    public void FishInTimer8()
    {
        #region test setup

        LanternFishCounts initialFish = new LanternFishCounts();
        initialFish.FishInTimer0 = 0;
        initialFish.FishInTimer1 = 0;
        initialFish.FishInTimer2 = 0;
        initialFish.FishInTimer3 = 0;
        initialFish.FishInTimer4 = 0;
        initialFish.FishInTimer5 = 0;
        initialFish.FishInTimer6 = 0;
        initialFish.FishInTimer7 = 0;
        initialFish.FishInTimer8 = 1;

        LanternFishCounts expected = new LanternFishCounts();
        expected.FishInTimer0 = 0;
        expected.FishInTimer1 = 0;
        expected.FishInTimer2 = 0;
        expected.FishInTimer3 = 0;
        expected.FishInTimer4 = 0;
        expected.FishInTimer5 = 0;
        expected.FishInTimer6 = 0;
        expected.FishInTimer7 = 1;
        expected.FishInTimer8 = 0;

        #endregion

        LanternFishCounts simulatedFish = LanternFishSimulator.SimulateFish(initialFish);
        bool result = Utilities.CompareLanterFishCounts(expected, simulatedFish);

        Assert.True(result, "Generates fish in timer 7");
    }

    #endregion

    #region Sample input tests

    [Fact]
    public void FishCountInput1Turn0()
    {
        string filePath = "./Inputs/day6-input1.txt";
        List<int> inputNumbers = Utilities.LoadInput(filePath);
        LanternFishCounts initialFish = Utilities.LoadBucketsFromInput(inputNumbers);

        long expectedFishCount = 5;
        bool result = initialFish.TotalFish == expectedFishCount;

        Assert.True(result, "Should be 5");
    }

    [Fact]
    public void FishCountInput1Turn18()
    {
        string filePath = "./Inputs/day6-input1.txt";
        List<int> inputNumbers = Utilities.LoadInput(filePath);
        LanternFishCounts initialFish = Utilities.LoadBucketsFromInput(inputNumbers);

        long expectedFishCount = 26;
        LanternFishCounts simulatedFish = LanternFishSimulator.SimulateFish(initialFish, 18);
        bool result = simulatedFish.TotalFish == expectedFishCount;

        Assert.True(result, "Should be 26");
    }

    [Fact]
    public void FishCountInput1Turn80()
    {
        string filePath = "./Inputs/day6-input1.txt";
        List<int> inputNumbers = Utilities.LoadInput(filePath);
        LanternFishCounts initialFish = Utilities.LoadBucketsFromInput(inputNumbers);

        long expectedFishCount = 5934;
        LanternFishCounts simulatedFish = LanternFishSimulator.SimulateFish(initialFish, 80);
        bool result = simulatedFish.TotalFish == expectedFishCount;

        Assert.True(result, "Should be 5934");
    }

    [Fact]
    public void FishCountInput1Turn256()
    {
        string filePath = "./Inputs/day6-input1.txt";
        List<int> inputNumbers = Utilities.LoadInput(filePath);
        LanternFishCounts initialFish = Utilities.LoadBucketsFromInput(inputNumbers);

        long expectedFishCount = 26984457539;
        LanternFishCounts simulatedFish = LanternFishSimulator.SimulateFish(initialFish, 256);
        bool result = simulatedFish.TotalFish == expectedFishCount;

        Assert.True(result, "Should be 26984457539");
    }

    #endregion
}
