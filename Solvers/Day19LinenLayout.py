

class Day19LinenLayout:
    def solvePart1(self, input_value: list[str]) -> int:
        return (lambda allowed_patterns, desired_designs, impossible=set(): len([1 for desired_design in desired_designs if (check_substring := lambda patterns, design, impossible, soFar="": True if design == "" else False if design in impossible else (lambda result: result if result else bool(impossible.add(design)))(next((nextPattern for nextPattern in [pattern for pattern in patterns if design.startswith(pattern)] if check_substring(patterns, design[len(nextPattern):], impossible, soFar + nextPattern)), False)))(allowed_patterns, desired_design, impossible)]))(sorted(input_value[0].split(", "), key=len, reverse=True), input_value[2:])

    def solvePart2(self, input_value: list[str]) -> int:
        return (lambda allowed_patterns, desired_designs, cache=dict(): sum([(check_substring := lambda patterns, design, cache, soFar="": cache[design] if design in cache else 1 if design == "" else cache.setdefault(design, sum([check_substring(patterns, design[len(nextPattern):], cache, soFar + nextPattern) for nextPattern in [pattern for pattern in patterns if design.startswith(pattern)]])))(allowed_patterns, desired_design, cache) for desired_design in desired_designs]))(sorted(input_value[0].split(", "), key=len, reverse=True), input_value[2:])
