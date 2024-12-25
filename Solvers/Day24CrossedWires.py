import re


class Day24CrossedWires:
    def solvePart1(self, input_value: list[str]) -> int:
        return (lambda operations: sum([operations[r.string](operations) << int(r.group("Shift")) for r in [re.search(r"z(?P<Shift>\d{2})", z) for z in operations] if r]))({r.group("Result"): (lambda d, r=r: dict(AND=lambda x, y: x & y, OR=lambda x, y: x | y, XOR=lambda x, y: x ^ y)[r.group("Operation")](d[r.group("First")](d), d[r.group("Second")](d))) for r in [re.search(r"(?P<First>\w{3}) (?P<Operation>(XOR|OR|AND)) (?P<Second>\w{3}) -> (?P<Result>\w{3})", l) for l in input_value] if r} | {r.group("Input"): (lambda d, r=r : int(r.group("Value"))) for r in [re.search(r"(?P<Input>([xy])\d+): (?P<Value>\d)", l) for l in input_value] if r})

    def solvePart2(self, input_value: list[str]) -> int:
        return 0
