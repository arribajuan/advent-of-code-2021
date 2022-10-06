using static Day2.PositionCalculator.SubmarineMovement;

namespace Day2.PositionCalculator
{
    public class Utilities
    {
        public static List<SubmarineMovement> LoadInput(string filePath)
        {
            List<SubmarineMovement> result = new List<SubmarineMovement>();

            string[] fileLines = File.ReadAllLines(filePath, System.Text.Encoding.Default);

            foreach (string line in fileLines)
            {
                SubmarineMovement movement = new SubmarineMovement();

                char[] spearator = { ' ' };
                String[] strlist = line.Split(spearator, StringSplitOptions.TrimEntries);

                switch (strlist[0])
                {
                    case "up":
                        movement.Direction = MovementDirectionEnum.Up;
                        break;
                    case "down":
                        movement.Direction = MovementDirectionEnum.Down;
                        break;
                    case "forward":
                        movement.Direction = MovementDirectionEnum.Forward;
                        break;
                    default:
                        movement.Direction = MovementDirectionEnum.Unknown;
                        break;
                }
                movement.Magnitude = Convert.ToInt32(strlist[1]);

                result.Add(movement);
            }

            return result;
        }
    }
}