def solve(queries):
    def count_bits_upto(n):
        """Counts total bits in binary representations of 1 to n."""
        if n <= 0:
            return 0
        count = 0
        for i in range(n.bit_length()):
            full_blocks = (n + 1) // (1 << (i + 1))
            count += full_blocks * (1 << i)
            remainder = (n + 1) % (1 << (i + 1))
            count += max(0, remainder - (1 << i))
        return count

    def get_bit_counts(n):
        """Returns a list where index i stores count of bit i in 1 to n."""
        counts = [0] * 60
        if n <= 0:
            return counts
        for i in range(n.bit_length()):
            full_blocks = (n + 1) // (1 << (i + 1))
            counts[i] += full_blocks * (1 << i)
            remainder = (n + 1) % (1 << (i + 1))
            counts[i] += max(0, remainder - (1 << i))
        return counts

    def find_n(k):
        low, high = 1, max(1, k + 1)
        ans = high
        while low <= high:
            mid = (low + high) // 2
            if count_bits_upto(mid) >= k + 1:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans

    results = []
    for start, end, mod in queries:
        n_start = find_n(start)
        n_end = find_n(end)

        counts_end = get_bit_counts(n_end)
        counts_start = get_bit_counts(n_start - 1)

        # Bits in range [start, end]
        # We need to adjust for the partial n_start and n_end
        def get_bits_in_n(n):
            bits = []
            for i in range(60):
                if (n >> i) & 1:
                    bits.append(i)
            return bits

        # Total counts in [1, n_end] - [1, n_start-1]
        # Then subtract/add bits from the partial numbers n_start and n_end
        total_counts = [(counts_end[i] - counts_start[i]) for i in range(60)]

        # Remove bits of n_start that are before 'start'
        bits_n_start = get_bits_in_n(n_start)
        bits_before_start = count_bits_upto(n_start - 1)
        for i in range(len(bits_n_start)):
            if bits_before_start + i < start:
                total_counts[bits_n_start[i]] -= 1

        # Add bits of n_end that are after 'end'
        bits_n_end = get_bits_in_n(n_end)
        bits_before_end = count_bits_upto(n_end - 1)
        for i in range(len(bits_n_end)):
            if bits_before_end + i > end:
                total_counts[bits_n_end[i]] -= 1

        res = 1
        for i in range(60):
            if total_counts[i] > 0:
                res = (res * pow(1 << i, total_counts[i], mod)) % mod
        results.append(res)

    return results
