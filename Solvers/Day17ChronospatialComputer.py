from itertools import combinations, takewhile
from math import floor
import re


class Day17ChronospatialComputer:
    def solvePart1(self, input_value: list[str], initialA = None, cutoff = False) -> str:
        return (lambda combo: (lambda process_instruction : ",".join([str(v) for v in process_instruction(*(lambda s: (lambda state: (state[0], initialA if initialA != None else state[1], *state[2:]))((0, *[int(re.search(rf"Register {reg}: (?P<Value>\d+)", s).group("Value")) for reg in "ABC"], tuple([int(v) for v in re.search(r"Program: (?P<Program>(\d+,?)+)", s).group("Program").split(",")]))))("\n".join(input_value)))]))((process_instruction := lambda pointer, A, B, C, program, output=tuple() : (process_instruction(pointer + 2, floor(A / (2 ** combo(pointer, A, B, C, program))), B, C, program, output) if program[pointer] == 0 else process_instruction(pointer + 2, A, B ^ program[pointer + 1], C, program, output) if program[pointer] == 1 else process_instruction(pointer + 2, A, combo(pointer, A, B, C, program) % 8, C, program, output) if program[pointer] == 2 else (process_instruction(program[pointer + 1], A, B, C, program, output) if A != 0 else process_instruction(pointer + 2, A, B, C, program, output)) if program[pointer] == 3 else process_instruction(pointer + 2, A, B ^ C, C, program, output) if program[pointer] == 4 else process_instruction(pointer + 2, A, B, C, program, output + (combo(pointer, A, B, C, program) % 8,)) if program[pointer] == 5 else process_instruction(pointer + 2, A, floor(A / (2 ** combo(pointer, A, B, C, program))), C, program, output) if program[pointer] == 6 else process_instruction(pointer + 2, A, B, floor(A / (2 ** combo(pointer, A, B, C, program))), program, output) if program[pointer] == 7 else None) if pointer < len(program) - 1 and (not cutoff or program[:len(output)] == output) else output)))((lambda pointer, A, B, C, program: program[pointer + 1] if program[pointer + 1] in [0, 1, 2, 3] else A if program[pointer + 1] == 4 else B if program[pointer + 1] == 5 else C if program[pointer + 1] == 6 else None))

    def solvePart2(self, input_value: list[str], testRange=4096) -> int:
        expected = re.search(r"Program: (?P<Program>(\d+,?)+)", "\n".join(input_value)).group("Program")
        generator = (-320 + 512 * x for x in range(1, 100000))
        generator = range(testRange)
        n = 2
        return [(count, self.solvePart1(input_value, initialA=count)) for count in range(0, 8**(n+1)+1) if self.solvePart1(input_value, initialA=count)[0:n+1] == expected[0:n+1]]
        return list( (count for count in generator if self.solvePart1(input_value, initialA=count, cutoff=True)[0:3] == expected[0:3]) )
