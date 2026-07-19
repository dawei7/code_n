def solve(s: str) -> int:
    length = len(s)
    limit = 1 << length
    is_palindrome = [False] * limit
    is_palindrome[0] = True
    palindrome_length = [0] * limit

    for mask in range(1, limit):
        lowest_bit = mask & -mask
        left = lowest_bit.bit_length() - 1
        right = mask.bit_length() - 1
        if left == right:
            is_palindrome[mask] = True
            palindrome_length[mask] = 1
            continue

        inner_mask = mask ^ lowest_bit ^ (1 << right)
        if s[left] == s[right] and is_palindrome[inner_mask]:
            is_palindrome[mask] = True
            palindrome_length[mask] = mask.bit_count()

    best_submask = palindrome_length.copy()
    for bit in (1 << index for index in range(length)):
        block_size = bit << 1
        for start in range(0, limit, block_size):
            middle = start + bit
            stop = middle + bit
            best_submask[middle:stop] = list(
                map(max, zip(best_submask[middle:stop], best_submask[start:middle]))
            )

    full_mask = limit - 1
    return max(
        palindrome_length[mask] * best_submask[full_mask ^ mask]
        for mask in range(limit)
    )
