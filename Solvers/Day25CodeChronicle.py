from itertools import groupby, takewhile, product


class Day25CodeChronicle:
    def solvePart1(self, input_value: list[str]) -> int:
        return sum([all([v1 + v2 <= 5 for v1, v2 in zip(x, y)]) for x,y in product(*[(lambda lockskeys: [[(lambda s: len([x for x in takewhile(lambda c: c == s[0], s[1:])]))("".join((lambda l: reversed(l) if l[0] == "." else l)([lock[i][j] for i in range(len(lock))]))) for j in range(len(lock[0]))] for lock in lockskeys])(lockskeys) for lockskeys in (lambda lockskeys: [[l for l in lockskeys if all(c == c0 for c in l[0])] for c0 in "#."])([l for l in filter(lambda x: x != [""], [list(g) for _, g in groupby(input_value, key=lambda x: x == "")])])])])

    def solvePart2(self, input_value: list[str]) -> int:
        return 0
