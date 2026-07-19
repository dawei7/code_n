"""App-local reference solution for LeetCode 1912."""

import heapq
from collections import defaultdict


class MovieRentingSystem:
    def __init__(self, n: int, entries: list[list[int]]):
        self.price: dict[tuple[int, int], int] = {}
        self.version: dict[tuple[int, int], int] = {}
        self.rented: set[tuple[int, int]] = set()
        self.available: dict[int, list[tuple[int, int, int]]] = defaultdict(list)
        self.rented_heap: list[tuple[int, int, int, int]] = []

        for shop, movie, price in entries:
            key = (shop, movie)
            self.price[key] = price
            self.version[key] = 0
            heapq.heappush(self.available[movie], (price, shop, 0))

    def search(self, movie: int) -> list[int]:
        heap = self.available[movie]
        selected: list[tuple[int, int, int]] = []
        while heap and len(selected) < 5:
            price, shop, version = heapq.heappop(heap)
            key = (shop, movie)
            if key not in self.rented and self.version[key] == version:
                selected.append((price, shop, version))

        for entry in selected:
            heapq.heappush(heap, entry)
        return [shop for _, shop, _ in selected]

    def rent(self, shop: int, movie: int) -> None:
        key = (shop, movie)
        self.version[key] += 1
        self.rented.add(key)
        heapq.heappush(
            self.rented_heap,
            (self.price[key], shop, movie, self.version[key]),
        )

    def drop(self, shop: int, movie: int) -> None:
        key = (shop, movie)
        self.version[key] += 1
        self.rented.remove(key)
        heapq.heappush(
            self.available[movie],
            (self.price[key], shop, self.version[key]),
        )

    def report(self) -> list[list[int]]:
        selected: list[tuple[int, int, int, int]] = []
        while self.rented_heap and len(selected) < 5:
            price, shop, movie, version = heapq.heappop(self.rented_heap)
            key = (shop, movie)
            if key in self.rented and self.version[key] == version:
                selected.append((price, shop, movie, version))

        for entry in selected:
            heapq.heappush(self.rented_heap, entry)
        return [[shop, movie] for _, shop, movie, _ in selected]


def solve(operations: list[str], arguments: list[list[object]]) -> list[object]:
    system: MovieRentingSystem | None = None
    output: list[object] = []

    for operation, args in zip(operations, arguments):
        if operation == "MovieRentingSystem":
            system = MovieRentingSystem(args[0], args[1])
            output.append(None)
        elif operation == "search":
            assert system is not None
            output.append(system.search(args[0]))
        elif operation == "rent":
            assert system is not None
            system.rent(args[0], args[1])
            output.append(None)
        elif operation == "drop":
            assert system is not None
            system.drop(args[0], args[1])
            output.append(None)
        elif operation == "report":
            assert system is not None
            output.append(system.report())
        else:
            raise ValueError(f"unknown operation: {operation}")

    return output
