from itertools import chain
import numpy as np
from scipy.sparse import coo_array
from scipy.sparse.csgraph import shortest_path, yen


class Day16ReindeerMaze:
    def solvePart1(self, input_value: list[str], stepCost=1, rotationCost=1000) -> int:
        return (lambda as_flat_coord, next_coordinate, symbol_at: (lambda graphRepr : int(min([shortest_path(coo_array((np.array(list(chain(*[[v[1] for v in graphRepr[key]] for key in graphRepr])), dtype=np.int32), (np.array(list(chain(*[[key]*len(graphRepr[key]) for key in graphRepr])), dtype=np.int32), np.array(list(chain(*[[v[0] for v in graphRepr[key]] for key in graphRepr])), dtype=np.int32)))), indices=as_flat_coord(*sum([[(ri, ci, 2) for ci in range(len(input_value[0])) if input_value[ri][ci] == "S"] for ri in range(len(input_value))], [])[0]))[as_flat_coord(*endIndex)] for endIndex in sum([[(ri, ci, di) for di in range(4) for ci in range(len(input_value[0])) if input_value[ri][ci] == "E"] for ri in range(len(input_value))], [])])))({as_flat_coord(ri, ci, di): (lambda row, column, direction: [(as_flat_coord(row, column, (direction + ddirection)%4), rotationCost) for ddirection in [-1, 1]] + ([(as_flat_coord(*next_coordinate(row, column, direction)), stepCost)] if next_coordinate(row, column, direction) and symbol_at(*next_coordinate(row, column, direction)) != "#" else []) if symbol_at(row, column, direction) != "#" else [])(ri, ci, di) for di in range(4) for ci in range(len(input_value[0])) for ri in range(len(input_value))}))(lambda row, column, direction: direction + column * 4 + row * 4 * len(input_value), (lambda di_to_deltas: (lambda row, column, direction: (row + di_to_deltas[direction][0], column + di_to_deltas[direction][1], direction) if 0 <= row + di_to_deltas[direction][0] < len(input_value) and 0 <= column + di_to_deltas[direction][1] < len(input_value[1]) else None))({0: (0, -1), 1: (-1, 0), 2: (0, 1), 3: (1, 0)}), lambda row, column, _: input_value[row][column])

    def solvePart2(self, input_value: list[str], stepCost=1, rotationCost=1000) -> int:
        return 0