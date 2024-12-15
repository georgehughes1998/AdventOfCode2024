import re
from itertools import groupby
from functools import reduce

class Day14RestroomRedoubt:
    def solvePart1(self, input_value: list[str], gridWidth=101, gridHeight=103, steps=100) -> int:
        return (lambda positions, keyFunc: reduce(lambda x, y: x * y, [(len(list(v))) for k, v in groupby(sorted(positions, key=keyFunc), key=keyFunc)]))([(x, y) for x,y in [((int(g.group('StartX')) + steps * int(g.group('VelocityX'))) % gridWidth, (int(g.group('StartY')) + steps * int(g.group('VelocityY'))) % gridHeight) for g in [re.search(r'p=(?P<StartX>\d+),(?P<StartY>\d+) v=(?P<VelocityX>-?\d+),(?P<VelocityY>-?\d+)', l) for l in input_value]] if x != gridWidth // 2 and y != gridHeight // 2], lambda c: (c[0] < gridWidth / 2, c[1] < gridHeight / 2))

    def solvePart2(self, input_value: list[str]) -> int:
        return 0


