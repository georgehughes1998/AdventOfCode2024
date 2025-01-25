import re
from functools import reduce
from itertools import takewhile


class Day15WarehouseWoes:
    def solvePart1(self, input_value: list[str]) -> int:
        return (lambda finalMap: sum([sum([(100 * ri +  ci) for ci in range(len(finalMap)) if finalMap[ri][ci] == "O"]) for ri in range(len(finalMap[0]))]))(reduce((lambda carte, move: ((lambda position, carte, positionsToUpdate: [[positionsToUpdate[(ri, ci)] if (ri, ci) in positionsToUpdate else (lambda carte, coord: carte[coord[0]][coord[1]])(carte, (ri, ci)) for ci in range(len(carte[0]))] for ri in range(len(carte))])((lambda carte: sum([[(ri, ci) for ci in range(len(carte)) if carte[ri][ci] == "@"] for ri in range(len(carte))], [])[0])(carte), carte, (lambda position, carte, moveDelta: (lambda positions: {positions[p]: (lambda carte, coord: carte[coord[0]][coord[1]])(carte, positions[(p - 1) % len(positions)]) for p in range(len(positions))})([(position[0] + moveDelta[0] * i, position[1] + moveDelta[1] * i) for i in range((lambda position, carte, moveDelta: ((lambda facing: 1 if len(facing) > 0 and (lambda carte, coord: carte[coord[0]][coord[1]])(carte, facing[0]) == "." else "".join([(lambda carte, coord: carte[coord[0]][coord[1]])(carte, f) for f in facing]).find(".") + 1 )(list(takewhile(lambda v: (lambda carte, coord: carte[coord[0]][coord[1]])(carte, v) in list(".O"),((position[0] + moveDelta[0] * i, position[1] + moveDelta[1] * i) for i in range(1, max(len(carte), len(carte[0]))) if 0 <= position[0] + moveDelta[0] * i < len(carte) and 0 <= position[1] + moveDelta[1] * i < len(carte[0])))))))(position, carte, moveDelta) + 1 if (lambda position, carte, moveDelta: ((lambda facing: 1 if len(facing) > 0 and (lambda carte, coord: carte[coord[0]][coord[1]])(carte, facing[0]) == "." else "".join([(lambda carte, coord: carte[coord[0]][coord[1]])(carte, f) for f in facing]).find(".") + 1 )(list(takewhile(lambda v: (lambda carte, coord: carte[coord[0]][coord[1]])(carte, v) in list(".O"),((position[0] + moveDelta[0] * i, position[1] + moveDelta[1] * i) for i in range(1, max(len(carte), len(carte[0]))) if 0 <= position[0] + moveDelta[0] * i < len(carte) and 0 <= position[1] + moveDelta[1] * i < len(carte[0])))))))(position, carte, moveDelta) > 0 else 0) if 0 <= position[0] + moveDelta[0] * i < len(carte) and 0 <= position[1] + moveDelta[1] * i < len(carte[0])]))((lambda carte: sum([[(ri, ci) for ci in range(len(carte)) if carte[ri][ci] == "@"] for ri in range(len(carte))], [])[0])(carte), carte, {"<": (0, -1), "^": (-1, 0), ">": (0, 1), "v": (1, 0)}[move])))), list("".join([l for l in input_value if re.match(r"[<^>v]+", l)])), [list(l) for l in input_value if re.match(r"#[#.O@]+#", l)]))

    def solvePart2(self, input_value: list[str]) -> int:

        carte = [list(l.replace("#", "##").replace("O", "[]").replace(".","..").replace("@", "@.")) for l in input_value if re.match(r"#[#.O@]+#", l)]
        moves = list("".join([l for l in input_value if re.match(r"[<^>v]+", l)]))


        ([print("".join(l)) for l in carte])


        mapWidth, mapHeight = len(carte), len(carte[0])
        getPosition = lambda carte: sum([[(ri, ci) for ci in range(len(carte)) if carte[ri][ci] == "@"] for ri in range(len(carte))], [])[0]


        moveSymbolToDeltas = {"<": (0, -1), "^": (-1, 0), ">": (0, 1), "v": (1, 0)}
        symbolAtCoord = lambda carte, coord: carte[coord[0]][coord[1]]
        getNumToMove = lambda position, carte, moveDelta: (
            (lambda facing: 1 if len(facing) > 0 and symbolAtCoord(carte, facing[0]) == "." else "".join([symbolAtCoord(carte, f) for f in facing]).find(".") + 1 )(list(takewhile(lambda v: symbolAtCoord(carte, v) in list(".O"),
                      ((position[0] + moveDelta[0] * i, position[1] + moveDelta[1] * i)
                       for i in range(1, max(mapWidth, mapHeight)) if 0 <= position[0] + moveDelta[0] * i < mapWidth and 0 <= position[1] + moveDelta[1] * i < mapHeight)))))
        getPositionsToUpdate = lambda position, carte, moveDelta: (lambda positions: {positions[p]: symbolAtCoord(carte, positions[(p - 1) % len(positions)]) for p in range(len(positions))})([(position[0] + moveDelta[0] * i, position[1] + moveDelta[1] * i)
                       for i in range(getNumToMove(position, carte, moveDelta) + 1 if getNumToMove(position, carte, moveDelta) > 0 else 0) if 0 <= position[0] + moveDelta[0] * i < mapWidth and 0 <= position[1] + moveDelta[1] * i < mapHeight])


        getUpdatedMap = lambda position, carte, positionsToUpdate: [[positionsToUpdate[(ri, ci)] if (ri, ci) in positionsToUpdate else symbolAtCoord(carte, (ri, ci)) for ci in range(len(carte[0]))] for ri in range(len(carte))]
        getNextStep = lambda carte, move: (getUpdatedMap(getPosition(carte), carte, getPositionsToUpdate(getPosition(carte), carte, moveSymbolToDeltas[move])))



        #return (lambda finalMap: sum([sum([(100 * ri +  ci) for ci in range(mapWidth) if finalMap[ri][ci] == "O"]) for ri in range(mapHeight)]))(reduce(getNextStep, moves, carte))

