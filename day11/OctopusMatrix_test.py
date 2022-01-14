import unittest

import numpy as np

import OctopusMatrix as om
import OctopusMatrix_inputs as omi


class TestOctopusMatrix(unittest.TestCase):

    def test_scenario1_step1(self):
        octopus = om.OctopusMatrix(omi.input_test1_step0)
        octopus.simulate_steps(10)
        self.assert_(np.array_equal(omi.input_test1_step1, octopus.matrix_octopi))

    def test_scenario1_step2(self):
        octopus = om.OctopusMatrix(omi.input_test1_step0)
        octopus.simulate_steps(10)
        octopus.simulate_steps(10)
        self.assert_(np.array_equal(omi.input_test1_step2, octopus.matrix_octopi))


if __name__ == '__main__':
    unittest.main()
