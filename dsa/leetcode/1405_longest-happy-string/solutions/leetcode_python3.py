from heapq import heapify, heappop, heappush


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = [(-count, letter) for count, letter in ((a, 'a'), (b, 'b'), (c, 'c')) if count]
        heapify(heap)
        result = []
        while heap:
            count, letter = heappop(heap)
            if len(result) >= 2 and result[-1] == result[-2] == letter:
                if not heap:
                    break
                fallback_count, fallback = heappop(heap)
                result.append(fallback)
                fallback_count += 1
                if fallback_count:
                    heappush(heap, (fallback_count, fallback))
                heappush(heap, (count, letter))
            else:
                result.append(letter)
                count += 1
                if count:
                    heappush(heap, (count, letter))
        return ''.join(result)
