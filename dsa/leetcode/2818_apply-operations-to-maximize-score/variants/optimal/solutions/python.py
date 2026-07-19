def solve(nums: list[int], k: int) -> int:
    MOD = 10**9 + 7
    max_val = max(nums)

    # Precompute prime scores only as far as this input needs.
    prime_scores = [0] * (max_val + 1)
    for i in range(2, max_val + 1):
        if prime_scores[i] == 0:
            for j in range(i, max_val + 1, i):
                prime_scores[j] += 1

    n = len(nums)
    scores = [prime_scores[x] for x in nums]

    # Monotonic stack to find how many subarrays have nums[i] as the max prime score
    # We use >= to handle duplicates consistently
    left = [-1] * n
    right = [n] * n
    stack = []
    for i in range(n):
        while stack and scores[stack[-1]] < scores[i]:
            stack.pop()
        if stack:
            left[i] = stack[-1]
        stack.append(i)

    stack = []
    for i in range(n - 1, -1, -1):
        while stack and scores[stack[-1]] <= scores[i]:
            stack.pop()
        if stack:
            right[i] = stack[-1]
        stack.append(i)

    # Calculate contribution of each index
    elements = []
    for i in range(n):
        count = (i - left[i]) * (right[i] - i)
        elements.append((nums[i], count))

    # Sort by value descending to pick the largest elements greedily
    elements.sort(key=lambda x: x[0], reverse=True)

    ans = 1
    remaining_k = k
    for val, count in elements:
        take = min(remaining_k, count)
        ans = (ans * pow(val, take, MOD)) % MOD
        remaining_k -= take
        if remaining_k == 0:
            break

    return ans
