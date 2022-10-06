using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Day2.PositionCalculator
{
    public class Challenge1
    {
        public static int Solution(List<SubmarineMovement> movements)
        {
            int result = 0;

            int movesUp = 0;
            int movesDown = 0;
            int movesForward = 0;

            foreach (SubmarineMovement movement in movements)
            {
                switch (movement.Direction)
                {
                    case SubmarineMovement.MovementDirectionEnum.Up:
                        movesUp += movement.Magnitude;
                        break;
                    case SubmarineMovement.MovementDirectionEnum.Down:
                        movesDown += movement.Magnitude;
                        break;
                    case SubmarineMovement.MovementDirectionEnum.Forward:
                        movesForward += movement.Magnitude;
                        break;
                }
            }

            int depth = movesDown - movesUp;
            result = depth * movesForward;

            return result;
        }

    }
}
