from Solvers.Solver import Solver


class Day2RedNosedReports(Solver):
    def solvePart1(self, input_value: list[str]) -> int:
        return sum([(lambda x: (not False in [1 <= abs(v) <= 3 for v in x]) and (not False in [(x[0] > 0) == (v > 0) for v in x]))([int(l.split()[i]) - int(l.split()[i+1]) for i in range(len(l.split())-1)]) for l in input_value])

    def solvePart2(self, input_value: list[str]) -> int:
        return sum(([(lambda b: True if b[0] else True in b)([(lambda x: (not False in [1 <= abs(v) <= 3 for v in x]) and (not False in [(x[0] > 0) == (v > 0) for v in x]))((lambda x: [x[i] - x[i+1] for i in range(len(x) - 1)])(y)) for y in [[int(a) for a in l.split()]] + [([int(n) for n in l.split()[:x] + l.split()[x + 1:]]) for x in range(len(l.split()))]]) for l in input_value]))
