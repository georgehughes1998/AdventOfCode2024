import unittest

from Solvers.Day18RAMRun import Day18RAMRun
from Tests.SolverTestBase import SolverTestBase


class Day18RAMRunTest(SolverTestBase):
    solverClass = Day18RAMRun

    def test_Part1Examples(self):
        for s in self._readDataExample(1):
            with self.subTest(s=s):
                self.assertEqual(s.ExpectedResult, self.solver.solvePart1(s.Input, gridSize=7, numberToSimulate=12))

    def test_Part2Examples(self):
        for s in self._readDataExample(2):
            with self.subTest(s=s):
                self.assertEqual(s.ExpectedResult, self.solver.solvePart2(s.Input, gridSize=7, minNumberToSimulate=12))

if __name__ == '__main__':
    unittest.main()
