from functools import reduce
from itertools import accumulate, pairwise
from more_itertools import windowed

from math import floor


class Day22MonkeyMarket:
    def solvePart1(self, input_value: list[str]) -> int:
        return sum([reduce(lambda secret, _: (((secret ^ (secret * 64)) % 16777216 ^ floor((secret ^ (secret * 64)) % 16777216 / 32)) % 16777216 ^ (((secret ^ (secret * 64)) % 16777216 ^ floor((secret ^ (secret * 64)) % 16777216 / 32)) % 16777216 * 2048)) % 16777216, range(2000), int(l)) for l in input_value])

    def solvePart2(self, input_value: list[str]) -> int:
        return max((lambda price_diff_dicts: [sum(d[k] for d in price_diff_dicts if k in d) for k in set(k for d in price_diff_dicts for k in d)])([(lambda price_diff_tuples: {diff: next((price for price, diff2 in price_diff_tuples if diff == diff2), 0) for diff in {diff_unique for _, diff_unique in price_diff_tuples}})(list(map(lambda x: (x[4], tuple(map(lambda xpair: xpair[1] - xpair[0], pairwise(x)))), windowed(map(lambda x: x % 10, accumulate(range(2000), func = lambda secret, _: ((((secret ^ (secret * 64)) % 16777216 ^ floor((secret ^ (secret * 64)) % 16777216 / 32)) % 16777216 ^ (((secret ^ (secret * 64)) % 16777216 ^ floor((secret ^ (secret * 64)) % 16777216 / 32)) % 16777216 * 2048)) % 16777216), initial=int(l))), n=5)))) for l in input_value]))
