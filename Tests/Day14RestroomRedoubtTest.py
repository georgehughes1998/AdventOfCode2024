import unittest

from Solvers.Day14RestroomRedoubt import Day14RestroomRedoubt
from Tests.SolverTestBase import SolverTestBase


class Day14RestroomRedoubtTest(SolverTestBase):
    solverClass = Day14RestroomRedoubt

    def test_Part1Examples(self):
        for s in self._readDataExample(1):
            with self.subTest(s=s):
                self.assertEqual(s.ExpectedResult, self.solver.solvePart1(s.Input, gridWidth=11, gridHeight=7))

    def test_Part2Examples(self):
        for s in self._readDataExample(2):
            with self.subTest(s=s):
                self.assertEqual(s.ExpectedResult, self.solver.solvePart2(s.Input))

if __name__ == '__main__':
    unittest.main()
