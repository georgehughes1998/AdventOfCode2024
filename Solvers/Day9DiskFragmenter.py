from functools import reduce
import sys

sys.setrecursionlimit(40000)


class Day9DiskFragmenter:
    def solvePart1(self, input_value: list[str]) -> int:
        subtract_from_list_ix = (lambda l, n: next(-1-i for i in range(len(l)) if sum(l[:-2-i:-1])-n >= 0))
        subtract_from_list_diff = (lambda l, n: next(sum(l[:-2-i:-1])-n for i in range(len(l)) if sum(l[:-2-i:-1])-n >= 0))

        #12345
        #0..111....22222

        #0 111 22222
        #.. ....
        values = ([int(v) for v in "".join(input_value)])

        initial_memory = "".join([str(i // 2) * int(values[i]) if i % 2 == 0 else "." * int(values[i]) for i in range(0, len(values))])
        def consume(to_process: str, processed: str = ""):
            if to_process == "":
                return processed
            else:
                return consume(to_process[to_process.find("."):-1], processed + to_process[:to_process.find(".")-1] + to_process[-1])

        return consume(initial_memory)
        #return (compact := lambda files, spaces, index=0: str(index) * files[index] + str(len(files) - 1) * (spaces[index] if print("compact()", index+1) or index < len(spaces) else 0) + compact(files[:subtract_from_list_ix(files, spaces[0])], spaces, index + 1) if len(spaces) > 0 and len(files) > index else "")(*(lambda values: [[values[i] for i in range(n, len(values), 2)] for n in [0, 1]])([int(v) for v in "".join(input_value)]))


        # next_space = (lambda s: s.find("."))
        # is_sorted = (lambda s: all([len(a) == 0 for a in s.split(".")[1:]]))
        # checksum = (lambda s: sum([i*int(s[i]) for i in range(len(s)) if s[i] != "." ]))
        # compact_step = (lambda s: "".join(["." if i == len(s) - 1 else s[-1] if i == next_space(s) else s[i] for i in range(len(s))])[:-1])
        # initial_memory = (lambda l: "".join([str(i//2) * int(l[i]) if i%2 == 0 else "." * int(l[i]) for i in range(0, len(l))]))
        
        # return sum([checksum(reduce(lambda memory, n: memory if is_sorted(memory) else compact_step(memory), range(len(initial_memory(l))), initial_memory(l))) for l in input_value])

    def solvePart2(self, input_value: list[str]) -> int:
        return 0
