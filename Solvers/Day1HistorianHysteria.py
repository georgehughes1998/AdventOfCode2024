from Solvers.Solver import Solver


class Day1HistorianHysteria(Solver):
    def solvePart1(self, input_value: list[str]) -> int:
        return sum([abs(int(x) - int(y)) for (x,y) in zip(sorted([l.split()[0] for l in input_value]), sorted([l.split()[1] for l in input_value]))])

    def solvePart2(self, input_value: list[str]) -> int:
        return sum([int(x) * sum([1 for i in [l.split()[1] for l in input_value] if x == i]) for x in [l.split()[0] for l in input_value]])
