from functools import reduce
from itertools import chain


class Day23LANParty:
    def solvePart1(self, input_value: list[str]) -> int:
        return (lambda machines: (lambda links: len({truple for truple in (sum([sum([[frozenset((m, l, l2)) for l2 in links[l] if m in links[l2] and m != l2] for l in links[m]], []) for m in machines], [])) if any([mch.startswith("t") for mch in truple])}))({m: [A if m == B else B if m == A else None for A, B in [tuple(l.split("-")) for l in input_value] if m in (A, B)] for m in machines}))(set(chain(*[tuple(l.split("-")) for l in input_value])))

    def solvePart2(self, input_value: list[str]) -> str:
        return (lambda machines: (lambda links: ",".join(sorted(max({reduce(lambda s, m: s | {m} if all([m in links[m2] for m2 in s]) else s, machines - {m1}, frozenset({m1})) for m1 in machines}, key=lambda x: len(x)))))({m: [A if m == B else B if m == A else None for A, B in [tuple(l.split("-")) for l in input_value] if m in (A, B)] for m in machines}))(set(chain(*[tuple(l.split("-")) for l in input_value])))
