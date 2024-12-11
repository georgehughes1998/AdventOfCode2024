

class Day11PlutonianPebbles:
    def solvePart1(self, input_value: list[str], count=25) -> int:
        return (blink := (lambda values, depth=count: len(values) if depth <= 0 else sum([cache[(v, depth)] if (v, depth) in cache else (lambda key, value: value if not cache.update({key: value}) else None)((v, depth), blink([1], depth-1)) if v == 0 else (lambda key, value: value if not cache.update({key: value}) else None)((v, depth), blink([int(str(v)[:len(str(v))//2]), int(str(v)[len(str(v))//2:])], depth-1)) if len(str(v)) % 2 == 0 else (lambda key, value: value if not cache.update({key: value}) else None)((v, depth), blink([v * 2024], depth-1)) for v in values])))(([int(v) for v in "".join(input_value).split()]) if not (cache := {}) else None)

    def solvePart2(self, input_value: list[str]) -> int:
        return self.solvePart1(input_value, count=75)
        