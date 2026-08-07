from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        blocked = {int(state) for state in deadends}
        start = 0
        goal = int(target)
        if start in blocked or goal in blocked:
            return -1
        if start == goal:
            return 0

        front = {start}
        back = {goal}
        seen_front = {start}
        seen_back = {goal}
        distance = 0
        place_values = (1, 10, 100, 1000)

        while front and back:
            if len(front) > len(back):
                front, back = back, front
                seen_front, seen_back = seen_back, seen_front

            next_front = set()
            for state in front:
                for place_value in place_values:
                    digit = (state // place_value) % 10
                    higher = state + place_value if digit < 9 else state - 9 * place_value
                    lower = state - place_value if digit > 0 else state + 9 * place_value

                    for neighbor in (higher, lower):
                        if neighbor in blocked:
                            continue
                        if neighbor in seen_back:
                            return distance + 1
                        if neighbor not in seen_front:
                            seen_front.add(neighbor)
                            next_front.add(neighbor)

            front = next_front
            distance += 1

        return -1
