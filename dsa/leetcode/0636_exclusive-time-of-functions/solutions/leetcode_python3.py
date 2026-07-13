from typing import List


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        exclusive = [0] * n
        stack = []
        previous = 0

        for log in logs:
            identifier_text, event, timestamp_text = log.split(":")
            identifier = int(identifier_text)
            timestamp = int(timestamp_text)

            if event == "start":
                if stack:
                    exclusive[stack[-1]] += timestamp - previous
                stack.append(identifier)
                previous = timestamp
            else:
                exclusive[stack.pop()] += timestamp - previous + 1
                previous = timestamp + 1

        return exclusive
