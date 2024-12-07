import re
from functools import reduce


class Day7BridgeRepair:
    def solvePart1(self, input_value: list[str]) -> int:
        return sum([(lambda result, values: result if result in [reduce(lambda v1, fv2: fv2[0](v1, fv2[1]), zip([lambda v1, v2: v1 + v2] + [(lambda v1, v2: v1 + v2) if (operator//(2**v))%2 else (lambda v1, v2: v1 * v2) for v in range(len(values)-1)], values), 0) for operator in range(2**(len(values)-1))] else 0)(*(lambda match: (int(match.group("Result")), [int(v) for v in match.group("Values").split()]))(re.search(r"(?P<Result>\d+): (?P<Values>(\d+ ?)+)", l))) for l in input_value])

    def solvePart2(self, input_value: list[str]) -> int:
        return sum([(lambda result, values: result if result in [reduce(lambda v1, fv2: fv2[0](v1, fv2[1]), zip([lambda v1, v2: v1 + v2] + [[lambda v1, v2: v1 + v2, lambda v1, v2: v1 * v2, lambda v1, v2: int(f"{v1}{v2}")][(operator//(3**v))%3] for v in range(len(values)-1)], values), 0) for operator in range(3**(len(values)-1))] else 0)(*(lambda match: (int(match.group("Result")), [int(v) for v in match.group("Values").split()]))(re.search(r"(?P<Result>\d+): (?P<Values>(\d+ ?)+)", l))) for l in input_value])
