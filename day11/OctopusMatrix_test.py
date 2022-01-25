import unittest

import numpy as np

import OctopusMatrix as om
import OctopusMatrix_inputs as omi


class TestOctopusMatrix(unittest.TestCase):

    def test_scenario1_step1(self):
        octopus = om.OctopusMatrix(omi.input_test1_step0)
        octopus.simulate_steps(100)
        self.assertTrue(np.array_equal(
            omi.input_test1_step1, octopus.matrix_octopi))

    def test_scenario1_step2(self):
        octopus = om.OctopusMatrix(omi.input_test1_step0)
        octopus.simulate_steps(100)
        octopus.simulate_steps(100)
        self.assertTrue(np.array_equal(
            omi.input_test1_step2, octopus.matrix_octopi))

    def test_scenario2_step001(self):
        octopus = om.OctopusMatrix(omi.input_test2_step0)
        octopus.simulate_steps(100)
        self.assertTrue(np.array_equal(
            omi.input_test2_step1, octopus.matrix_octopi))

    def test_scenario2_step002(self):
        octopus = om.OctopusMatrix(omi.input_test2_step1)
        octopus.simulate_steps(100)
        self.assertTrue(np.array_equal(
            omi.input_test2_step2, octopus.matrix_octopi))

    def test_scenario2_step003(self):
        octopus = om.OctopusMatrix(omi.input_test2_step2)
        octopus.simulate_steps(100)
        self.assertTrue(np.array_equal(
            omi.input_test2_step3, octopus.matrix_octopi))

    def test_scenario2_step004(self):
        octopus = om.OctopusMatrix(omi.input_test2_step3)
        octopus.simulate_steps(100)
        self.assertTrue(np.array_equal(
            omi.input_test2_step4, octopus.matrix_octopi))

    def test_scenario2_step005(self):
        octopus = om.OctopusMatrix(omi.input_test2_step4)
        octopus.simulate_steps(100)
        self.assertTrue(np.array_equal(
            omi.input_test2_step5, octopus.matrix_octopi))

    def test_scenario2_step006(self):
        octopus = om.OctopusMatrix(omi.input_test2_step5)
        octopus.simulate_steps(100)
        self.assertTrue(np.array_equal(
            omi.input_test2_step6, octopus.matrix_octopi))

    def test_scenario2_step007(self):
        octopus = om.OctopusMatrix(omi.input_test2_step6)
        octopus.simulate_steps(100)
        self.assertTrue(np.array_equal(
            omi.input_test2_step7, octopus.matrix_octopi))

    def test_scenario2_step008(self):
        octopus = om.OctopusMatrix(omi.input_test2_step7)
        octopus.simulate_steps(100)
        self.assertTrue(np.array_equal(
            omi.input_test2_step8, octopus.matrix_octopi))

    def test_scenario2_step009(self):
        octopus = om.OctopusMatrix(omi.input_test2_step8)
        octopus.simulate_steps(100)
        self.assertTrue(np.array_equal(
            omi.input_test2_step9, octopus.matrix_octopi))

    def test_scenario2_step010(self):
        octopus = om.OctopusMatrix(omi.input_test2_step9)
        octopus.simulate_steps(100)

        octopus_loop = om.OctopusMatrix(omi.input_test2_step0)
        for i in range(10):
            octopus_loop.simulate_steps(100)

        self.assertTrue(np.array_equal(
            omi.input_test2_step10, octopus.matrix_octopi))
        self.assertTrue(np.array_equal(
            omi.input_test2_step10, octopus_loop.matrix_octopi))

    def test_scenario2_step020(self):
        octopus_loop = om.OctopusMatrix(omi.input_test2_step0)
        for i in range(20):
            octopus_loop.simulate_steps(100)
        self.assertTrue(np.array_equal(
            omi.input_test2_step20, octopus_loop.matrix_octopi))

    def test_scenario2_step030(self):
        octopus_loop = om.OctopusMatrix(omi.input_test2_step0)
        for i in range(30):
            octopus_loop.simulate_steps(100)
        self.assertTrue(np.array_equal(
            omi.input_test2_step30, octopus_loop.matrix_octopi))

    def test_scenario2_step040(self):
        octopus_loop = om.OctopusMatrix(omi.input_test2_step0)
        for i in range(40):
            octopus_loop.simulate_steps(100)
        self.assertTrue(np.array_equal(
            omi.input_test2_step40, octopus_loop.matrix_octopi))

    def test_scenario2_step050(self):
        octopus_loop = om.OctopusMatrix(omi.input_test2_step0)
        for i in range(50):
            octopus_loop.simulate_steps(100)
        self.assertTrue(np.array_equal(
            omi.input_test2_step50, octopus_loop.matrix_octopi))

    def test_scenario2_step060(self):
        octopus_loop = om.OctopusMatrix(omi.input_test2_step0)
        for i in range(60):
            octopus_loop.simulate_steps(100)
        self.assertTrue(np.array_equal(
            omi.input_test2_step60, octopus_loop.matrix_octopi))

    def test_scenario2_step070(self):
        octopus_loop = om.OctopusMatrix(omi.input_test2_step0)
        for i in range(70):
            octopus_loop.simulate_steps(100)
        self.assertTrue(np.array_equal(
            omi.input_test2_step70, octopus_loop.matrix_octopi))

    def test_scenario2_step080(self):
        octopus_loop = om.OctopusMatrix(omi.input_test2_step0)
        for i in range(80):
            octopus_loop.simulate_steps(100)
        self.assertTrue(np.array_equal(
            omi.input_test2_step80, octopus_loop.matrix_octopi))

    def test_scenario2_step090(self):
        octopus_loop = om.OctopusMatrix(omi.input_test2_step0)
        for i in range(90):
            octopus_loop.simulate_steps(100)
        self.assertTrue(np.array_equal(
            omi.input_test2_step90, octopus_loop.matrix_octopi))

    def test_scenario2_step100(self):
        octopus_loop = om.OctopusMatrix(omi.input_test2_step0)
        for i in range(100):
            octopus_loop.simulate_steps(100)
        self.assertTrue(np.array_equal(
            omi.input_test2_step100, octopus_loop.matrix_octopi))


if __name__ == '__main__':
    unittest.main()
