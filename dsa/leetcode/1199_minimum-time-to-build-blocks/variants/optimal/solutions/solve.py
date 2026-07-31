from heapq import heapify, heappop, heappush


def solve(blocks: list[int], split: int) -> int:
    heapify(blocks)
    while len(blocks) > 1:
        heappop(blocks)
        larger = heappop(blocks)
        heappush(blocks, larger + split)
    return blocks[0]
