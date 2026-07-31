from collections import defaultdict, deque
from typing import List


class Solution:
    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        maximum = max(nums)
        is_prime = bytearray(b"\x01") * (maximum + 1)
        if maximum >= 0:
            is_prime[0] = 0
        if maximum >= 1:
            is_prime[1] = 0
        limit = int(maximum**0.5)
        for prime in range(2, limit + 1):
            if is_prime[prime]:
                start = prime * prime
                count = (maximum - start) // prime + 1
                is_prime[start : maximum + 1 : prime] = b"\x00" * count

        indices_by_value = defaultdict(list)
        for index, value in enumerate(nums):
            indices_by_value[value].append(index)

        distance = [-1] * n
        distance[0] = 0
        queue = deque([0])
        used_primes = set()

        while queue:
            index = queue.popleft()
            next_distance = distance[index] + 1

            for neighbor in (index - 1, index + 1):
                if 0 <= neighbor < n and distance[neighbor] == -1:
                    if neighbor == n - 1:
                        return next_distance
                    distance[neighbor] = next_distance
                    queue.append(neighbor)

            prime = nums[index]
            if is_prime[prime] and prime not in used_primes:
                used_primes.add(prime)
                for multiple in range(prime, maximum + 1, prime):
                    for neighbor in indices_by_value.get(multiple, ()):
                        if distance[neighbor] == -1:
                            if neighbor == n - 1:
                                return next_distance
                            distance[neighbor] = next_distance
                            queue.append(neighbor)

        return distance[-1]
