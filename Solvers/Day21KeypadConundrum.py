from collections import namedtuple
from itertools import product, combinations, permutations, accumulate


class Day21KeypadConundrum:
    def solvePart1(self, input_value: list[str]) -> int:
        # TODO: return all possibilities
        keys_drow = lambda drow: "v" * drow if drow > 0 else "^" * abs(drow)
        keys_dcol = lambda dcol: ">" * dcol if dcol > 0 else "<" * abs(dcol)

        convert_difference_to_keys_numeric = lambda drow, dcol: (keys_dcol(dcol) + keys_drow(drow) if drow > 0 else keys_drow(drow) + keys_dcol(dcol)) + "A"
        convert_difference_to_keys_directional = lambda drow, dcol: (keys_dcol(dcol) + keys_drow(drow) if drow < 0 else keys_drow(drow) + keys_dcol(dcol)) + "A"

        delta_to_symbol = lambda drow, dcol: ("v" if drow == 1 else "^" if drow == -1 else "") + (">" if dcol == 1 else "<" if dcol == -1 else "")
        convert_difference_to_keys = lambda startCoord, endCoord, keypad: \
            [ "".join([delta_to_symbol(*d) for d in stepPermutations]) + "A" for stepPermutations in
             set(permutations(([(1, 0)] * (endCoord[0] - startCoord[0]) if (endCoord[0] - startCoord[0]) > 0 else [(-1, 0)] * abs((endCoord[0] - startCoord[0]))) + ([(0, 1)] * (endCoord[1] - startCoord[1]) if (endCoord[1] - startCoord[1]) > 0 else [(0, -1)] * abs((endCoord[1] - startCoord[1])))))
             if all([keypad[testCoord[0]][testCoord[1]] != "#" for testCoord in accumulate(stepPermutations, func=lambda c1, c2: (c1[0] + c2[0], c1[1] + c2[1]), initial=startCoord)])
             ]

        numeric_keypad = ['789', '456', '123', '#0A']
        directional_keypad = ['#^A', '<v>']

        numeric_keypad_coords = [(row, column) for column in range(len(numeric_keypad[0])) for row in range(len(numeric_keypad)) if not numeric_keypad[row][column] == "#"]
        directional_keypad_coords = [(row, column) for column in range(len(directional_keypad[0])) for row in range(len(directional_keypad)) if not directional_keypad[row][column] == "#"]

        numeric_keypad_dict = {(numeric_keypad[row1][col1], numeric_keypad[row2][col2]): convert_difference_to_keys((row1, col1), (row2, col2), numeric_keypad) for ((row1, col1), (row2, col2)) in list(product(numeric_keypad_coords, repeat=2))}
        directional_keypad_dict = {(directional_keypad[row1][col1], directional_keypad[row2][col2]): convert_difference_to_keys((row1, col1), (row2, col2), directional_keypad) for ((row1, col1), (row2, col2)) in list(product(directional_keypad_coords, repeat=2))}

        print(directional_keypad_dict)



        Work = namedtuple("Work", ["Level", "Processed", "ToProcess"])

        stack: list[Work] = [Work(0, tuple("" for i in range(4)), (l, *("" for i in range(3)))) for l in input_value]
        finished: list[str] = []

        def processWork(stack: list[Work], finished: list[str]):
            while len(stack) > 0:
                work = stack.pop(0)
                print(work)

                if all(toProcess == "" for toProcess in work.ToProcess):
                    finished.insert(0, work.Processed)
                elif work.Level == 4:
                    continue
                elif work.ToProcess[work.Level] == "":
                    nextPosition = work.ToProcess[work.Level][0]
                    newProcessed = tuple(work.Processed[i] + nextPosition if i == work.Level - 1 else work.Processed[i] for i in range(len(work.Processed)))
                    newToProcess = tuple(work.ToProcess[i][1:] if i == work.Level - 1 else work.ToProcess[i] for i in range(len(work.ToProcess)))
                    stack.insert(0, Work(work.Level - 1, newProcessed, work.ToProcess))
                else:
                    keypad_dict = numeric_keypad_dict if work.Level == 0 else directional_keypad_dict

                    currentPosition = work.Processed[work.Level][-1] if len(work.Processed[work.Level]) > 0 else "A"
                    nextPosition = work.ToProcess[work.Level][0]
                    possible_movements = keypad_dict[(currentPosition, nextPosition)]

                    newProcessed = tuple(work.Processed[i] + nextPosition if i == work.Level else work.Processed[i] for i in range(len(work.Processed)))
                    for movement in possible_movements:
                        newToProcess = tuple(work.ToProcess[i] + movement if i == work.Level + 1 else work.ToProcess[i][1:] if i == work.Level else work.ToProcess[i] for i in range(len(work.ToProcess)))
                        stack.insert(0, Work(work.Level + 1, newProcessed, newToProcess))







        def get_next(target, robotStates=("A", "A", "A"), level=0):
            if level == 3:
                return target
            elif target == "":
                return robotStates, ""
            else:
                keypad_dict = numeric_keypad_dict if level == 0 else directional_keypad_dict

                possible_movements = keypad_dict[(robotStates[level], target[0])]

                movements_expanded = "".join([get_next(m, robotStates, level + 1) for m in movements])

                print(f"robotStates[{level}] {robotStates[level]} -> {target[0]} (movements : {movements_expanded})")
                robotStates[level] = target[0]

                return movements_expanded + get_next(target[1:], robotStates, level)

        processWork(stack, finished)
        return finished

    def solvePart2(self, input_value: list[str]) -> int:
        return 0
