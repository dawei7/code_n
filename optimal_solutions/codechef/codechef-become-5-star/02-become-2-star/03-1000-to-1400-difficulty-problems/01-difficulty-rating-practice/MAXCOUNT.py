from collections import Counter


def solve():
    def mostFrequent(N: int, A: list) -> list:
        counts = Counter(A)
        max_freq = max(counts.values())

        # Filter all elements that have the maximum frequency, then find the minimum
        best_elem = min(num for num, count in counts.items() if count == max_freq)

        return [best_elem, max_freq]


if __name__ == "__main__":
    solve()
