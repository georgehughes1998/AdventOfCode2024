from collections import namedtuple


class Day4CeresSearch:
    def solvePart1(self, input_value: list[str]) -> int:        
        return sum([rot for rot in (lambda x : [sum([s.count("XMAS") for s in a]) for a in x] + [sum(["".join(reversed(s)).count("XMAS") for s in a]) for a in x])([input_value, ["".join(list(row)) for row in zip(*input_value)], ["".join([input_value[coord.y][coord.x] for coord in row]) for row in [[namedtuple("c", ["x","y"])(o + i, len(input_value[0]) - 1 - i) for i in range(-max(len(input_value[0]),len(input_value)), max(len(input_value[0]),len(input_value))) if 0<=o+i<len(input_value[0]) and 0<=len(input_value)-1-i<len(input_value)  ] for o in range(-max(len(input_value[0]),len(input_value)), max(len(input_value[0]),len(input_value)))]], ["".join([input_value[coord.y][coord.x] for coord in row]) for row in [[namedtuple("c", ["x","y"])(len(input_value[0])+o+i,len(input_value[0]) + i) for i in range(-max(len(input_value[0]),len(input_value)), max(len(input_value[0]),len(input_value))) if 0<=len(input_value[0])+o+i<len(input_value[0]) and 0<=len(input_value[0])+i<len(input_value)  ] for o in range(-max(len(input_value[0]),len(input_value)), max(len(input_value[0]),len(input_value)))]]])])
    
    def solvePart2(self, input_value: list[str]) -> int:
        return sum([1 for c in sum([[namedtuple("c", ["x","y"])(x,y) for x in range(1,len(input_value[0])-1)] for y in range(1,len(input_value)-1)],[]) if input_value[c.y][c.x] == "A" and (lambda s : s in ["MMSS", "SSMM", "MSMS", "SMSM"] )(input_value[c.y-1][c.x-1] + input_value[c.y+1][c.x-1] + input_value[c.y-1][c.x+1] + input_value[c.y+1][c.x+1])])

