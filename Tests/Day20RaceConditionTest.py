import unittest

from Solvers.Day20RaceCondition import Day20RaceCondition
from Tests.SolverTestBase import SolverTestBase


class Day20RaceConditionTest(SolverTestBase):
    solverClass = Day20RaceCondition

    def test_Part1Examples(self):
        for s in self._readDataExample(1):
            with self.subTest(s=s):
                self.assertEqual(s.ExpectedResult, self.solver.solvePart1(s.Input, atLeast=40))

    def test_Part2Examples(self):
        for s in self._readDataExample(2):
            with self.subTest(s=s):
                self.assertEqual(s.ExpectedResult, self.solver.solvePart2(s.Input, atLeast=50))

if __name__ == '__main__':
    unittest.main()
