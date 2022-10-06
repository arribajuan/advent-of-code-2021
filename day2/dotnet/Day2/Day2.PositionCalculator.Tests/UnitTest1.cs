using Day2.PositionCalculator;

namespace Day2.PositionCalculator.Tests
{
    public class UnitTest1
    {
        [Fact]
        public void Challenge1Solution()
        {
            string filePath = "./Inputs/day2-input.txt";
            List<SubmarineMovement> movements = Utilities.LoadInput(filePath);

            int expectedResult = 1250395;
            int challengeSolution = Challenge1.Solution(movements);

            Assert.Equal(expectedResult, challengeSolution);
        }

        [Fact]
        public void Challenge2Solution()
        {
            string filePath = "./Inputs/day2-input.txt";
            List<SubmarineMovement> movements = Utilities.LoadInput(filePath);

            int expectedResult = 1451210346;
            int challengeSolution = Challenge2.Solution(movements);

            Assert.Equal(expectedResult, challengeSolution);
        }

    }
}