def solve(s: str, numOps: int) -> int:
    if not s:
        return 0

    # Identify lengths of contiguous blocks of identical characters
    blocks = []
    if not s:
        return 0

    curr_len = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            curr_len += 1
        else:
            blocks.append(curr_len)
            curr_len = 1
    blocks.append(curr_len)

    def can_achieve(max_len: int) -> bool:
        if max_len == 1:
            start_zero = sum(char != ("0" if index % 2 == 0 else "1") for index, char in enumerate(s))
            start_one = len(s) - start_zero
            return min(start_zero, start_one) <= numOps
        if max_len == 0:
            return False
        ops_needed = 0
        for length in blocks:
            if length > max_len:
                # To break a block of size 'length' into pieces of size 'max_len',
                # we need floor(length / (max_len + 1)) operations.
                ops_needed += length // (max_len + 1)
        return ops_needed <= numOps

    # Binary search for the minimum possible maximum length
    low = 1
    high = len(s)
    ans = len(s)

    while low <= high:
        mid = (low + high) // 2
        if can_achieve(mid):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans
