using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Day2.PositionCalculator
{
    public class SubmarineMovement
    {
        public MovementDirectionEnum Direction = MovementDirectionEnum.Unknown;
        public int Magnitude = 0;

        public SubmarineMovement()
        {
            Direction = MovementDirectionEnum.Unknown;
            Magnitude = 0;
        }

        public SubmarineMovement(MovementDirectionEnum direction, int magnitude)
        {
            Direction = direction;
            Magnitude = magnitude;
        }

        public enum MovementDirectionEnum
        {
            Up,
            Down,
            Forward,
            Unknown
        }

    }

}
