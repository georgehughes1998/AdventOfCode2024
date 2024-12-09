from functools import reduce
import sys


class Day9DiskFragmenter:
    def solvePart1(self, input_value: list[str]) -> int:
        next_space = (lambda s: s.find("."))
        is_sorted = (lambda s: all([len(a) == 0 for a in s.split(".")[1:]]))
        checksum = (lambda s: sum([i*int(s[i]) for i in range(len(s)) if s[i] != "." ]))
        compact_step = (lambda s: "".join(["." if i == len(s) - 1 else s[-1] if i == next_space(s) else s[i] for i in range(len(s))])[:-1])
        initial_memory = (lambda l: "".join([str(i//2) * int(l[i]) if i%2 == 0 else "." * int(l[i]) for i in range(0, len(l))]))
        
        return sum([checksum(reduce(lambda memory, n: memory if is_sorted(memory) else compact_step(memory), range(len(initial_memory(l))), initial_memory(l))) for l in input_value])

    def solvePart2(self, input_value: list[str]) -> int:
        return 0
