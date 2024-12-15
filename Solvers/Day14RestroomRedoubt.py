import pathlib
import re
import numpy as np
from cv2 import imwrite
from itertools import groupby
from functools import reduce


class Day14RestroomRedoubt:
    def solvePart1(self, input_value: list[str], gridWidth=101, gridHeight=103, steps=100) -> int:
        return (lambda positions, keyFunc: reduce(lambda x, y: x * y, [(len(list(v))) for k, v in groupby(sorted(positions, key=keyFunc), key=keyFunc)]))([(x, y) for x,y in [((int(g.group('StartX')) + steps * int(g.group('VelocityX'))) % gridWidth, (int(g.group('StartY')) + steps * int(g.group('VelocityY'))) % gridHeight) for g in [re.search(r'p=(?P<StartX>\d+),(?P<StartY>\d+) v=(?P<VelocityX>-?\d+),(?P<VelocityY>-?\d+)', l) for l in input_value]] if x != gridWidth // 2 and y != gridHeight // 2], lambda c: (c[0] < gridWidth / 2, c[1] < gridHeight / 2))

    def solvePart2(self, input_value: list[str], gridWidth=101, gridHeight=103, minSteps=7847, maxSteps=7848) -> int:
        return 0 if not pathlib.Path("Output/Day14RestRoomRedoubt").mkdir(exist_ok=True) and [imwrite(f"Output/Day14RestRoomRedoubt/Day14RestRoomRedoubt-{steps}.png", (lambda coords: np.array([np.array([(0, 255, 0) if (x, y) in coords else (0, 0, 0) for x in range(gridWidth)]) for y in range(gridHeight)]))(([(x, y) for x,y in [((int(g.group('StartX')) + steps * int(g.group('VelocityX'))) % gridWidth, (int(g.group('StartY')) + steps * int(g.group('VelocityY'))) % gridHeight) for g in [re.search(r'p=(?P<StartX>\d+),(?P<StartY>\d+) v=(?P<VelocityX>-?\d+),(?P<VelocityY>-?\d+)', l) for l in input_value]]]))) for steps in range(minSteps, maxSteps, 101)] else None
