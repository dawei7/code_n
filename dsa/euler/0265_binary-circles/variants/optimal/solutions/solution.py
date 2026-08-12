def solve(n: int = 5) -> int:
    """Find S(5), the sum of all unique numeric representations of De Bruijn binary circles of order 5.
    
    Time Complexity: O(2^(2^N)) with bitmask DFS pruning
    Space Complexity: O(2^N)
    """
    length = 1 << n
    mask = (1 << n) - 1
    total_sum = 0

    def dfs(seq_bits, visited_mask, current_subseq):
        nonlocal total_sum
        bits_count = len(seq_bits)

        if bits_count == length:
            v_mask = visited_mask
            valid = True
            for k in range(1, n):
                sub = 0
                for idx in range(length - n + k, length):
                    sub = (sub << 1) | seq_bits[idx]
                sub <<= k
                if (v_mask & (1 << sub)) != 0:
                    valid = False
                    break
                v_mask |= 1 << sub

            if valid and v_mask == (1 << length) - 1:
                num = 0
                for b in seq_bits:
                    num = (num << 1) | b
                total_sum += num
            return

        for bit in (0, 1):
            next_subseq = ((current_subseq << 1) & mask) | bit
            if (visited_mask & (1 << next_subseq)) == 0:
                seq_bits.append(bit)
                dfs(seq_bits, visited_mask | (1 << next_subseq), next_subseq)
                seq_bits.pop()

    dfs([0] * n, 1 << 0, 0)
    return total_sum
