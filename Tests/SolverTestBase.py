import os
import re
import unittest
import unittest.util

from Solution import Solution
from Solvers.Solver import Solver

unittest.util._MAX_LENGTH = 2000


def _readInputFile(filepath) -> list[str]:
    try:
        with open(filepath) as inputFile:
            lines = [l.strip("\n") for l in inputFile.readlines()]
    except FileNotFoundError:
        print(f"File not found : {filepath}")
        lines = []
    return lines


def _readSolutionFile(filepath) -> int:
    try:
        with open(filepath) as inputFile:
            expected = inputFile.read()
    except FileNotFoundError:
        print(f"File not found : {filepath}")
        expected = 0
    return int(expected)


class SolverTestBase(unittest.TestCase):
    solverClass = Solver

    def _readDataExample(self, part: int) -> list[Solution]:
        examples_dir = f"InputData/Examples/{self.solverClass.__name__}/"
        files = os.listdir(examples_dir)

        inputFilenamePattern = re.compile(rf"Part{part}-(?P<Number>\d+).txt")
        solutionFilenamePattern = re.compile(rf"Part{part}-(?P<Number>\d+)A.txt")

        inputsFiles = [f for f in files if inputFilenamePattern.search(f)]
        solutionsFiles = [f for f in files if solutionFilenamePattern.search(f)]

        if not inputsFiles:
            raise FileNotFoundError(f"No examples found for {self.solverClass.__name__}")

        if len(inputsFiles) != len(solutionsFiles):
            raise FileNotFoundError(f"Examples and solutions don't match")

        inputsDict = {inputFilenamePattern.search(f).group("Number") : _readInputFile(examples_dir + f) for f in inputsFiles}
        solutionsDict = {solutionFilenamePattern.search(f).group("Number"): _readSolutionFile(examples_dir + f) for f in solutionsFiles}

        return [Solution(Input=inputsDict[i], ExpectedResult=solutionsDict[i]) for i in inputsDict]

    def _readDataReal(self) -> list[str]:
        filepath = f"InputData/Real/{self.solverClass.__name__}.txt"
        return _readInputFile(filepath)

    def setUp(self):
        if self.solverClass.__name__ == "Solver":
            self.skipTest("Skipping base class")

        self.solver:Solver = self.solverClass()

    def test_Part1Examples(self):
        for s in self._readDataExample(1):
            self.assertEqual(s.ExpectedResult ,self.solver.solvePart1(s.Input))

    def test_Part1Real(self):
        print(self.solverClass.__name__, "Part 1", self.solver.solvePart1(self._readDataReal()))

    def test_Part2Examples(self):
        for s in self._readDataExample(2):
            self.assertEqual(s.ExpectedResult ,self.solver.solvePart2(s.Input))

    def test_Part2Real(self):
        print(self.solverClass.__name__, "Part 2", self.solver.solvePart2(self._readDataReal()))
