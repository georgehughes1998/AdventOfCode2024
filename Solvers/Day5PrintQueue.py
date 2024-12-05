import re

class Day5PrintQueue:
    def solvePart1(self, input_value: list[str]) -> int:
        return sum([(lambda rules, pages : int(pages[len(pages)//2]) if all([all([rule(index, pages) for rule in rules]) for index in range(len(pages))]) else 0 )([lambda index, pages, r=r : all([ (pages[index] == r.group("After")) and (pages[index2] == r.group("Before")) for index2 in range(index) if pages[index] in r.groups() and pages[index2] in r.groups() ]) and all([  (pages[index] == r.group("Before")) and (pages[index2] == r.group("After")) for index2 in range(index + 1, len(pages)) if pages[index] in r.groups() and pages[index2] in r.groups() ]) for r in [re.search(r"(?P<Before>\d{1,2})\|(?P<After>\d{1,2})", l) for l in input_value] if r], pages) for pages in [l.split(",") for l in input_value if re.search(r"(?P<Pages>(\d{1,2},)+\d{1,2})", l)]])

    def solvePart2(self, input_value: list[str]) -> int:
        return 0
