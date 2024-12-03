import re
from Solvers.Solver import Solver


class Day3MullItOver(Solver):
    def solvePart1(self, input_value: list[str]) -> int:
        return sum([sum([int(r.group("First")) * int(r.group("Second")) for r in re.finditer(r"mul\((?P<First>\d{1,3}),(?P<Second>\d{1,3})\)", l)]) for l in input_value])

    def solvePart2(self, input_value: list[str]) -> int:
        return sum([sum([int(r.group("First")) * int(r.group("Second")) for r in re.finditer(r"mul\((?P<First>\d{1,3}),(?P<Second>\d{1,3})\)", j.split("don't()")[0])]) for j in "".join(input_value).split("do()")])
