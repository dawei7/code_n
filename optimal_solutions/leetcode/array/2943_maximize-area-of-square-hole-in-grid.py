def solve(n: int, m: int, hBars: list[int], vBars: list[int]) -> int:
    def get_max_consecutive(bars: list[int]) -> int:
        if not bars:
            return 1
        bars.sort()
        max_seq = 1
        current_seq = 1
        for i in range(1, len(bars)):
            if bars[i] == bars[i - 1] + 1:
                current_seq += 1
            else:
                current_seq = 1
            max_seq = max(max_seq, current_seq)
        return max_seq + 1

    max_h = get_max_consecutive(hBars)
    max_v = get_max_consecutive(vBars)
    
    side = min(max_h, max_v)
    return side * side
