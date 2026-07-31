def solve(nums: list[int], k: int) -> int:
    limit = max(nums)
    prime_scores = [0] * (limit + 1)

    for prime in range(2, limit + 1):
        if prime_scores[prime] == 0:
            for multiple in range(prime, limit + 1, prime):
                prime_scores[multiple] += 1

    scores = [prime_scores[value] for value in nums]
    length = len(nums)
    left = [-1] * length
    right = [length] * length
    stack: list[int] = []

    for index, score in enumerate(scores):
        while stack and scores[stack[-1]] < score:
            right[stack.pop()] = index
        if stack:
            left[index] = stack[-1]
        stack.append(index)

    answer = 1
    modulus = 1_000_000_007

    for index in sorted(range(length), key=lambda i: nums[i], reverse=True):
        choices = (index - left[index]) * (right[index] - index)
        uses = min(k, choices)
        answer = answer * pow(nums[index], uses, modulus) % modulus
        k -= uses
        if k == 0:
            break

    return answer
