from itertools import chain, product
import numpy as np
from scipy.sparse import coo_array
from scipy.sparse.csgraph import shortest_path

class Day20RaceCondition:
    def solvePart1(self, input_value: list[str], atLeast=100) -> int:
        return (lambda i_to_coord: (lambda coord_to_i, startPosition: (lambda cheatPositions, neighbours: (lambda graphi, graphj: (lambda shortestpaths: len([(shortestpaths[coord_to_i[startPosition], cheatPositionA] - shortestpaths[coord_to_i[startPosition], cheatPositionB] - 2) for cheatPositionA, cheatPositionB in cheatPositions if shortestpaths[coord_to_i[startPosition], cheatPositionA] - shortestpaths[coord_to_i[startPosition], cheatPositionB] - 2 >= atLeast]))(shortest_path(coo_array((np.ones_like(graphi, dtype=np.int32), (graphi, graphj))))))(np.array(list(chain(*[[k]*len(neighbours[k]) for k in neighbours])), dtype=np.int32), np.array(list(chain(*neighbours.values())), dtype=np.int32)))(sum([sum([sum([[[coord_to_i[(row + drow, column + dcol)], coord_to_i[(row - drow, column - dcol)]], [coord_to_i[(row - drow, column - dcol)], coord_to_i[(row + drow, column + dcol)]]] for drow, dcol in [(1,0), (0, 1)] if (row + drow, column + dcol) in coord_to_i and (row - drow, column - dcol) in coord_to_i],[]) for column in range(len(input_value[row])) if input_value[row][column] == "#"],[]) for row in range(len(input_value))],[]),{i:[coord_to_i[(i_to_coord[i][0] + drow, i_to_coord[i][1] + dcol)] for drow, dcol in [(0, -1), (-1, 0), (0, 1), (1, 0)] if (i_to_coord[i][0] + drow, i_to_coord[i][1] + dcol) in coord_to_i] for i in i_to_coord}))({i_to_coord[k]: k for k in i_to_coord}, sum([[(row, column) for column in range(len(input_value[row])) if input_value[row][column] == "S"] for row in range(len(input_value))],[])[0]))(i_to_coord = dict(enumerate(sum([[(row, column) for column in range(len(input_value[row])) if input_value[row][column] != "#"] for row in range(len(input_value))],[]))))
    
    def solvePart2(self, input_value: list[str], atLeast=100, cheatDistance=20) -> int:
        return (lambda i_to_coord: (lambda coord_to_i, startPosition: (lambda cheatPositions, neighbours: (lambda graphi, graphj: (lambda shortestpaths: sum([len([1 for cheatPositionB in cheatPositions[cheatPositionA] if shortestpaths[coord_to_i[startPosition], cheatPositionA] - shortestpaths[coord_to_i[startPosition], cheatPositionB] - (lambda c1, c2: abs(c1[0] - c2[0]) + abs(c1[1] - c2[1]))(i_to_coord[cheatPositionA], i_to_coord[cheatPositionB]) >= atLeast]) for cheatPositionA in cheatPositions ]))(shortest_path(coo_array((np.ones_like(graphi, dtype=np.int32), (graphi, graphj))))))(np.array(list(chain(*[[k]*len(neighbours[k]) for k in neighbours])), dtype=np.int32), np.array(list(chain(*neighbours.values())), dtype=np.int32)))({coord_to_i[(row, column)]: [coord_to_i[(row + drow, column + dcol)] for drow, dcol in ((x,y) for x,y in product(range(-cheatDistance, cheatDistance+1), repeat=2) if abs(x)+abs(y) <= cheatDistance) if (row + drow, column + dcol) in coord_to_i] for row, column in coord_to_i}, {i:[coord_to_i[(i_to_coord[i][0] + drow, i_to_coord[i][1] + dcol)] for drow, dcol in [(0, -1), (-1, 0), (0, 1), (1, 0)] if (i_to_coord[i][0] + drow, i_to_coord[i][1] + dcol) in coord_to_i] for i in i_to_coord}))({i_to_coord[k]: k for k in i_to_coord}, sum([[(row, column) for column in range(len(input_value[row])) if input_value[row][column] == "S"] for row in range(len(input_value))],[])[0]))(dict(enumerate(sum([[(row, column) for column in range(len(input_value[row])) if input_value[row][column] != "#"] for row in range(len(input_value))],[]))))