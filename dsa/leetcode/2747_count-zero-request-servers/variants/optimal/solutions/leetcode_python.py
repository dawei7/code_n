class Solution:
    def countServers(
        self, n: int, logs: List[List[int]], x: int, queries: List[int]
    ) -> List[int]:
        logs.sort(key=lambda entry: entry[1])
        ordered_queries = sorted((time, index) for index, time in enumerate(queries))
        answer = [0] * len(queries)
        active_counts = {}
        left = 0
        right = 0

        for time, index in ordered_queries:
            while right < len(logs) and logs[right][1] <= time:
                server = logs[right][0]
                active_counts[server] = active_counts.get(server, 0) + 1
                right += 1

            start = time - x
            while left < right and logs[left][1] < start:
                server = logs[left][0]
                active_counts[server] -= 1
                if active_counts[server] == 0:
                    del active_counts[server]
                left += 1

            answer[index] = n - len(active_counts)

        return answer
