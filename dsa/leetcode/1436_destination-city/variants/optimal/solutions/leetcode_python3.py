from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        starting_cities = {source for source, _ in paths}
        for _, destination in paths:
            if destination not in starting_cities:
                return destination
        raise ValueError("valid paths must contain a destination city")
