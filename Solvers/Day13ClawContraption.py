import re
from numpy.linalg import solve
from numpy import allclose, dot, array, int64, int64, round

class Day13ClawContraption:
    def solvePart1(self, input_value: list[str], prizeOffset=0) -> int:
        return int(sum([(3*a+b) for a,b in [round(solve((a,b), c), 4) for ((a,b), c) in [(array([[(r.group("AX")), (r.group("BX"))], [(r.group("AY")), (r.group("BY"))]], int64), array([int64(r.group("PrizeX")) + prizeOffset, int64(r.group("PrizeY")) + prizeOffset], int64)) for r in re.finditer(r"Button (A): X\+(?P<AX>\d+), Y\+(?P<AY>\d+)\nButton (B): X\+(?P<BX>\d+), Y\+(?P<BY>\d+)\nPrize: X=(?P<PrizeX>\d+), Y=(?P<PrizeY>\d+)", "\n".join(input_value))]] if int64(a) == a and int64(b) == b]))

    def solvePart2(self, input_value: list[str]) -> int:
        return self.solvePart1(input_value, prizeOffset=10000000000000)

