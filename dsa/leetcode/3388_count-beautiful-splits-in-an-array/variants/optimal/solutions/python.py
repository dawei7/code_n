def solve(nums: list[int]) -> int:
    n = len(nums)
    if n < 3:
        return 0

    mod1 = 1_000_000_007
    mod2 = 1_000_000_009
    base = 911_382_323

    pow1 = [1] * (n + 1)
    pow2 = [1] * (n + 1)
    pref1 = [0] * (n + 1)
    pref2 = [0] * (n + 1)

    for i, value in enumerate(nums):
        encoded = value + 1
        pow1[i + 1] = (pow1[i] * base) % mod1
        pow2[i + 1] = (pow2[i] * base) % mod2
        pref1[i + 1] = (pref1[i] * base + encoded) % mod1
        pref2[i + 1] = (pref2[i] * base + encoded) % mod2

    def same(left: int, right: int, length: int) -> bool:
        left_hash1 = (pref1[left + length] - pref1[left] * pow1[length]) % mod1
        right_hash1 = (pref1[right + length] - pref1[right] * pow1[length]) % mod1
        if left_hash1 != right_hash1:
            return False

        left_hash2 = (pref2[left + length] - pref2[left] * pow2[length]) % mod2
        right_hash2 = (pref2[right + length] - pref2[right] * pow2[length]) % mod2
        return left_hash2 == right_hash2

    count = 0

    for first_end in range(1, n - 1):
        first_prefixes_second = 2 * first_end <= n and same(0, first_end, first_end)

        if first_prefixes_second and 2 * first_end < n:
            count += n - 2 * first_end

        max_second_end = (n + first_end) // 2
        for second_end in range(first_end + 1, max_second_end + 1):
            if first_prefixes_second and second_end >= 2 * first_end:
                continue
            second_length = second_end - first_end
            if same(first_end, second_end, second_length):
                count += 1

    return count
