import heapq
from collections import defaultdict
from typing import List


class MovieRentingSystem:
    def __init__(self, n: int, entries: List[List[int]]):
        self.price = {}
        self.version = {}
        self.rented = set()
        self.available = defaultdict(list)
        self.rented_heap = []

        for shop, movie, price in entries:
            key = (shop, movie)
            self.price[key] = price
            self.version[key] = 0
            heapq.heappush(self.available[movie], (price, shop, 0))

    def search(self, movie: int) -> List[int]:
        heap = self.available[movie]
        selected = []
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

    def report(self) -> List[List[int]]:
        selected = []
        while self.rented_heap and len(selected) < 5:
            price, shop, movie, version = heapq.heappop(self.rented_heap)
            key = (shop, movie)
            if key in self.rented and self.version[key] == version:
                selected.append((price, shop, movie, version))

        for entry in selected:
            heapq.heappush(self.rented_heap, entry)
        return [[shop, movie] for _, shop, movie, _ in selected]
