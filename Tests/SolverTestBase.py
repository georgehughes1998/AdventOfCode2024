import json
import os
import pathlib
import re
import unittest.util
from json import JSONDecodeError

from Solution import Solution
from Solvers.Solver import Solver

unittest.util._MAX_LENGTH = 60000


def _readInputFile(filepath) -> list[str]:
    with open(filepath) as inputFile:
        lines = [l.strip("\n") for l in inputFile.readlines()]
    return lines

def _readSolutionFile(filepath) -> int:
    with open(filepath) as inputFile:
        expected = inputFile.read()
    return int(expected)


class SolverTestBase(unittest.TestCase):
    solverClass = Solver

    def _readDataExample(self, part: int) -> list[Solution]:
        examples_json_path = "InputData/Examples/Tests.json"
        with open(examples_json_path) as f:
            examples_json = json.loads(f.read())
        
        return [Solution(Input=_readInputFile(example["filename"]), ExpectedResult=example["answer"]) 
         for example in examples_json[self.solverClass.__name__][f"Part{part}"]]

    def _readDataReal(self) -> list[str]:
        filepath = f"InputData/Real/{self.solverClass.__name__}.txt"
        return _readInputFile(filepath)

    def _writeOutputData(self, resultPart1: int, resultPart2: int):
        output_path = "Output/output.json"
        pathlib.Path(os.path.split(output_path)[0]).mkdir(exist_ok=True)

        if not os.path.exists(output_path):
            with open(output_path, "w") as output_file:
                output_file.write("{}")

        with open(output_path, "r") as output_file:
            try:
                structure = json.loads(output_file.read())
            except JSONDecodeError:
                structure = dict()
        structure |= {self.solverClass.__name__: {"1": resultPart1, "2": resultPart2}}
        with open(output_path, "w") as output_file:
            output_file.write(json.dumps(structure, indent=2))

    def setUp(self):
        if self.solverClass.__name__ == "Solver":
            self.skipTest("Skipping base class")

        self.solver:Solver = self.solverClass()

    def test_Part1Examples(self):
        for s in self._readDataExample(1):
            with self.subTest(s=s):
                self.assertEqual(s.ExpectedResult, self.solver.solvePart1(s.Input))

    def test_Part2Examples(self):
        for s in self._readDataExample(2):
            with self.subTest(s=s):
                self.assertEqual(s.ExpectedResult, self.solver.solvePart2(s.Input))

    def test_Real(self):
        self._writeOutputData(self.solver.solvePart1(self._readDataReal()),
                              self.solver.solvePart2(self._readDataReal()))
