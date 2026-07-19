import heapq
from typing import List


class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        available = [0] + [index & -index for index in range(1, k + 1)]

        def add(server: int, delta: int) -> None:
            index = server + 1
            while index <= k:
                available[index] += delta
                index += index & -index

        def prefix(count: int) -> int:
            total = 0
            while count:
                total += available[count]
                count -= count & -count
            return total

        def server_with_order(order: int) -> int:
            index = 0
            step = 1 << (k.bit_length() - 1)
            while step:
                candidate = index + step
                if candidate <= k and available[candidate] < order:
                    index = candidate
                    order -= available[candidate]
                step >>= 1
            return index

        busy = []
        handled = [0] * k
        for request, (start_time, duration) in enumerate(zip(arrival, load)):
            while busy and busy[0][0] <= start_time:
                _, server = heapq.heappop(busy)
                add(server, 1)

            total_available = prefix(k)
            if total_available == 0:
                continue

            preferred = request % k
            before_preferred = prefix(preferred)
            if total_available > before_preferred:
                order = before_preferred + 1
            else:
                order = 1
            server = server_with_order(order)
            add(server, -1)
            handled[server] += 1
            heapq.heappush(busy, (start_time + duration, server))

        busiest_count = max(handled)
        return [server for server, count in enumerate(handled) if count == busiest_count]
