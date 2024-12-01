import os
import re
import unittest

from Solution import Solution
from Solver import Solver


def _readInputFile(filepath) -> list[str]:
    try:
        with open(filepath) as inputFile:
            lines = [l.strip("\n") for l in inputFile.readlines()]
    except FileNotFoundError:
        lines = []
    return lines


def _readSolutionFile(filepath) -> int:
    try:
        with open(filepath) as inputFile:
            expected = inputFile.read()
    except FileNotFoundError:
        expected = ""
    return int(expected)


class SolverTestBase(unittest.TestCase):
    solverClass = Solver

    def _readDataExample(self, part: int) -> list[Solution]:
        examples_dir = "InputData/Examples/"
        files = os.listdir(examples_dir)

        inputFilenamePattern = re.compile(rf"{self.solverClass.__name__}Part{part}Example(?P<Number>\d+).txt")
        solutionFilenamePattern = re.compile(rf"{self.solverClass.__name__}Part{part}Example(?P<Number>\d+)Solution.txt")

        inputsFiles = [f for f in files if inputFilenamePattern.search(f)]
        solutionsFiles = [f for f in files if solutionFilenamePattern.search(f)]

        inputsDict = {inputFilenamePattern.search(f).group("Number") : _readInputFile(examples_dir + f) for f in inputsFiles}
        solutionsDict = {solutionFilenamePattern.search(f).group("Number"): _readSolutionFile(examples_dir + f) for f in solutionsFiles}

        return [Solution(Input=inputsDict[i], ExpectedResult=solutionsDict[i]) for i in inputsDict]

    def _readDataReal(self) -> list[str]:
        filepath = f"InputData/Real/{self.solverClass.__name__}Real.txt"
        return _readInputFile(filepath)

    def setUp(self):
        self.solver:Solver = self.solverClass()
        self.puzzleInputPart1Examples: list[Solution] = self._readDataExample(1)
        self.puzzleInputReal: list[str] = self._readDataReal()
        self.puzzleInputPart2Examples: list[Solution] = self._readDataExample(2)

    def test_Part1Examples(self):
        for s in self.puzzleInputPart1Examples:
            self.assertEqual(s.ExpectedResult ,self.solver.solvePart1(s.Input))

    def test_Part1Real(self):
        print(self.solverClass.__name__, "Part 1", self.solver.solvePart1(self.puzzleInputReal))

    def test_Part2Examples(self):
        for s in self.puzzleInputPart2Examples:
            self.assertEqual(s.ExpectedResult ,self.solver.solvePart2(s.Input))

    def test_Part2Real(self):
        print(self.solverClass.__name__, "Part 2", self.solver.solvePart2(self.puzzleInputReal))
