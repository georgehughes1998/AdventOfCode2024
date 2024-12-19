import numpy as np
from itertools import chain
from scipy.sparse import coo_array
from scipy.sparse.csgraph import shortest_path


class Day18RAMRun:
    def solvePart1(self, input_value: list[str], gridSize=71, numberToSimulate=1024) -> int:
        return (lambda x: -9999 if np.isinf(x) else int(x))(shortest_path((lambda graphi, graphj: coo_array((np.ones_like(graphi), (graphi, graphj))))(*(lambda blocked, as_flat_coord, as_3d_coord: (lambda get_traversible: (np.array(list(chain(*[[yx]*len(get_traversible(*as_3d_coord(yx), blocked)) for yx in range(gridSize ** 2)])), dtype=np.int32), np.array(list(chain(*[get_traversible(*as_3d_coord(yx), blocked) for yx in range(gridSize ** 2)])), dtype=np.int32)))(lambda y, x, blocked: [as_flat_coord(y + yd, x + xd) for yd, xd in [(0, -1), (-1, 0), (0, 1), (1, 0)] if 0 <= y + yd < gridSize and 0 <= x + xd < gridSize and not (y, x) in blocked and not (y + yd, x + xd) in blocked]))([tuple(map(int, l.split(","))) for l in input_value[:numberToSimulate]], lambda y, x: y * gridSize + x, lambda flatcoord: (flatcoord // gridSize, flatcoord % gridSize))), indices=0)[gridSize*gridSize - 1])
        
    def solvePart2(self, input_value: list[str], gridSize=71, minNumberToSimulate=1024) -> str:
        return next(input_value[i-1] for i in range(minNumberToSimulate, len(input_value)) if not print(f"Checking {i} / {len(input_value)} ({round(i/len(input_value),2)*100}%)") and self.solvePart1(input_value, gridSize=gridSize, numberToSimulate=i) == -9999)
