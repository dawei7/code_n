from math import gcd


def solve(nums, k):
    states = {}
    answer = 0

    for value in nums:
        if k % value != 0:
            states = {}
            continue

        next_states = {value: 1}
        for previous, count in states.items():
            combined = previous // gcd(previous, value) * value
            if k % combined == 0:
                next_states[combined] = next_states.get(combined, 0) + count

        states = next_states
        answer += states.get(k, 0)

    return answer
