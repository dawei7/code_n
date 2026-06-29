


def solve():
    def sort_by_frequency(s: str) -> str:
        # Count frequency of each character
        freq = Counter(s)

        # Sort by frequency descending, then ASCII ascending
        sorted_chars = sorted(freq.items(), key=lambda x: (-x[1], ord(x[0])))

        # Build result string
        result = ''.join(ch * count for ch, count in sorted_chars)
        return result


if __name__ == "__main__":
    solve()
