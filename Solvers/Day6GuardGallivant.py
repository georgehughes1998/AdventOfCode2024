class Day6GuardGallivant:
    def solvePart1(self, input_value: list[str]) -> int:
        position = [(ri, input_value[ri].index("^")) for ri in range(len(input_value)) if "^" in input_value[ri]][0]
        puzzle_map = [[col for col in row] for row in input_value]
        within_map = (lambda position, rotation, puzzle_map: -1 < position[0] + rotation[0] < len(puzzle_map) and -1 < position[1] + rotation[1] < len(puzzle_map[0]))
        count_visited = (lambda puzzle_map: sum([sum([1 for col in row if col == "X"]) for row in puzzle_map]))
        updated_puzzle_map = (lambda position, rotation, puzzle_map, between_coords: [["X" if (ri, ci) in between_coords else puzzle_map[ri][ci] for ci in range(len(puzzle_map[ri]))] for ri in range(len(puzzle_map))])

        get_between_coords = (lambda position, rotation, puzzle_map, next_position: (sum([[(ri, ci) for ci in range(position[1], next_position[1] + (1 if rotation[1] > 0 else -1), 1 if rotation[1] > 0 else -1)] for ri in (range(position[0], next_position[0]+ (1 if rotation[0] > 0 else -1) , 1 if rotation[0] > 0 else -1))], start=[])))
        step_size = (lambda position, rotation, puzzle_map: len("".join([(puzzle_map[position[0]+rotation[0]*i][position[1]+rotation[1]*i]) for i in range(max(len(puzzle_map), len(puzzle_map[0]))) if 0 <= position[0]+rotation[0]*i < len(puzzle_map) and 0 <= position[1]+rotation[1]*i < len(puzzle_map[0])]).split("#")[0]) - 1)
        get_next_position = (lambda position, rotation, puzzle_map: tuple([position[i] + rotation[i] * step_size(position, rotation, puzzle_map) for i in [0, 1]]))
        rotate = (lambda rotation : {(-1, 0): (0, 1), (0, 1): (1, 0), (1, 0): (0, -1), (0, -1): (-1, 0)}[rotation])
        #return 0
        return (move := lambda position, rotation, puzzle_map:
            move(get_next_position(position, rotation, puzzle_map), rotate(rotation), updated_puzzle_map(position, rotation, puzzle_map, get_between_coords(position, rotation, puzzle_map, get_next_position(position, rotation, puzzle_map))))
            if within_map(position, rotate(rotate(rotate(rotation))), puzzle_map)
            else count_visited(puzzle_map))(position, (-1, 0), puzzle_map)

    def solvePart2(self, input_value: list[str]) -> int:
        position = [(ri, input_value[ri].index("^")) for ri in range(len(input_value)) if "^" in input_value[ri]][0]
        puzzle_map = [[col for col in row] for row in input_value]
        within_map = (lambda position, rotation, puzzle_map: -1 < position[0] + rotation[0] < len(puzzle_map) and -1 < position[1] + rotation[1] < len(puzzle_map[0]))
        count_visited = (lambda puzzle_map: sum([sum([1 for col in row if col == "X"]) for row in puzzle_map]))
        updated_puzzle_map = (lambda position, rotation, puzzle_map, between_coords: [["X" if (ri, ci) in between_coords else puzzle_map[ri][ci] for ci in range(len(puzzle_map[ri]))] for ri in range(len(puzzle_map))])


        get_between_coords = (lambda position, rotation, puzzle_map, next_position: (sum([[(ri, ci) for ci in range(position[1], next_position[1] + (1 if rotation[1] > 0 else -1), 1 if rotation[1] > 0 else -1)] for ri in (range(position[0], next_position[0]+ (1 if rotation[0] > 0 else -1) , 1 if rotation[0] > 0 else -1))], start=[])))
        step_size = (lambda position, rotation, puzzle_map: len("".join([(puzzle_map[position[0]+rotation[0]*i][position[1]+rotation[1]*i]) for i in range(max(len(puzzle_map), len(puzzle_map[0]))) if 0 <= position[0]+rotation[0]*i < len(puzzle_map) and 0 <= position[1]+rotation[1]*i < len(puzzle_map[0])]).split("#")[0]) - 1)
        get_next_position = (lambda position, rotation, puzzle_map: tuple([position[i] + rotation[i] * step_size(position, rotation, puzzle_map) for i in [0, 1]]))
        rotate = (lambda rotation : {(-1, 0): (0, 1), (0, 1): (1, 0), (1, 0): (0, -1), (0, -1): (-1, 0)}[rotation])

        add_obstacle = (lambda coords, puzzle_map: [["#" if (ri, ci) == coords else puzzle_map[ri][ci] for ci in range(len(puzzle_map[0]))] for ri in range(len(puzzle_map))])
        obstacle_combinations = (lambda puzzle_map, position: sum([[add_obstacle((ri, ci), puzzle_map) for ci in range(len(puzzle_map[0])) if (ri, ci) != position and puzzle_map[ri][ci] != "#"] for ri in range(len(puzzle_map))], start=[]))
        #print([new_puzzle_map for new_puzzle_map in obstacle_combinations(puzzle_map, position)])


        #print([len(m[0]) for m in obstacle_combinations(puzzle_map, position)])
        #return obstacle_combinations(puzzle_map)
        new_puzzle_maps = obstacle_combinations(puzzle_map, position)
        
        (move := lambda position, rotation, puzzle_map, previous_count, turns_without_increase:
            move(get_next_position(position, rotation, puzzle_map), rotate(rotation), updated_puzzle_map(position, rotation, puzzle_map, get_between_coords(position, rotation, puzzle_map, get_next_position(position, rotation, puzzle_map))), count_visited(puzzle_map), turns_without_increase + (count_visited(puzzle_map) == previous_count))
            if within_map(position, rotate(rotate(rotate(rotation))), puzzle_map) and turns_without_increase < 4 else
            within_map(position, rotate(rotate(rotate(rotation))), puzzle_map))

        return sum([1 for i in range(len(new_puzzle_maps)) if print(f"Progress: {i+1}/{len(new_puzzle_maps)} ({round(i/(len(new_puzzle_maps)-1),4)*100}%)") or move(position, (-1, 0), new_puzzle_maps[i], 0, 0)])
