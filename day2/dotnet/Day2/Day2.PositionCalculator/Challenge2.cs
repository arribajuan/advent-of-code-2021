using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.CompilerServices;
using System.Text;
using System.Threading.Tasks;

namespace Day2.PositionCalculator
{
    public class Challenge2
    {
        public static int Solution(List<SubmarineMovement> movements)
        {
            int result = 0;

            int aim = 0;
            int depth = 0;
            int movesForward = 0;

            foreach (SubmarineMovement movement in movements)
            {
                switch (movement.Direction)
                {
                    case SubmarineMovement.MovementDirectionEnum.Up:
                        aim -= movement.Magnitude;
                        break;
                    case SubmarineMovement.MovementDirectionEnum.Down:
                        aim += movement.Magnitude;
                        break;
                    case SubmarineMovement.MovementDirectionEnum.Forward:
                        movesForward += movement.Magnitude;
                        depth += (aim * movement.Magnitude);
                        break;
                }
            }

            result = depth * movesForward;

            return result;
        }
    }
}