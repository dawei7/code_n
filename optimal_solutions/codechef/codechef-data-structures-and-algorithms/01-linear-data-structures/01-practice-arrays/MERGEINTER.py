


def solve():
    def merge(intervals):
        if not intervals:
            return []

        # Sort intervals based on the start time
        intervals.sort(key=lambda x: x[0])

        merged = [intervals[0]]

        for current in intervals[1:]:
            # If current interval overlaps with the last merged interval
            if current[0] <= merged[-1][1]:
                # Merge them by updating the end time
                merged[-1][1] = max(merged[-1][1], current[1])
            else:
                # No overlap, just add the interval
                merged.append(current)

        return merged


if __name__ == "__main__":
    solve()
