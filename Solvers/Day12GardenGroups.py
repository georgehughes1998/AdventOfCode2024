from functools import reduce



class Day12GardenGroups:
    def solvePart1(self, input_value: list[str]) -> int:
        return (lambda coordinates, regions: sum([(lambda region: region["Area"] * (4 * region["Area"] - region["Neighbours"]))(regions[r]) for r in regions]) if [(get_neighbour := lambda id, coord, coordinates, regions, coordinates_immutable : (lambda v: [get_neighbour(id, coord2, coordinates, regions, coordinates_immutable) if coord2 in coordinates_immutable and coordinates_immutable[coord2] == v and not regions.update({id: {"Area": regions[id]["Area"], "Neighbours": regions[id]["Neighbours"] + 1}}) else None for coord2 in [(coord[0] + dr, coord[1] + dc) for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]]])(coordinates.pop(coord)) if coord in coordinates and regions.setdefault(id, {"Area": 0, "Neighbours": 0}) and not regions.update({id: {"Area": regions[id]["Area"] + 1, "Neighbours": regions[id]["Neighbours"]}}) else None)(id, coord, coordinates, regions, coordinates.copy()) for id, coord in enumerate(list(coordinates.keys()))] or True else None)(reduce(lambda d1, d2: d1 | d2, [{(ri, ci): input_value[ri][ci] for ci in range(len(input_value[ri]))} for ri in range(len(input_value))]), dict())

    def solvePart2(self, input_value: list[str]) -> int:
        return 0
