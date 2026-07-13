from collections import defaultdict
from heapq import heappop, heappush


def solve(nums: list[int], k: int, x: int) -> list[int]:
    freq = defaultdict(int)
    top = set()
    rest = set()
    top_min = []
    rest_max = []
    current_sum = 0

    def key(value: int) -> tuple[int, int]:
        return freq[value], value

    def push_top(value: int) -> None:
        heappush(top_min, key(value))

    def push_rest(value: int) -> None:
        f, v = key(value)
        heappush(rest_max, (-f, -v))

    def clean_top() -> None:
        while top_min:
            f, value = top_min[0]
            if value in top and freq[value] == f:
                return
            heappop(top_min)

    def clean_rest() -> None:
        while rest_max:
            nf, nv = rest_max[0]
            value = -nv
            if value in rest and freq[value] == -nf:
                return
            heappop(rest_max)

    def remove_current(value: int) -> None:
        nonlocal current_sum
        if value in top:
            top.remove(value)
            current_sum -= freq[value] * value
        elif value in rest:
            rest.remove(value)

    def move_rest_to_top() -> None:
        nonlocal current_sum
        clean_rest()
        nf, nv = heappop(rest_max)
        value = -nv
        rest.remove(value)
        top.add(value)
        current_sum += -nf * value
        push_top(value)

    def move_top_to_rest() -> None:
        nonlocal current_sum
        clean_top()
        f, value = heappop(top_min)
        top.remove(value)
        current_sum -= f * value
        rest.add(value)
        push_rest(value)

    def rebalance() -> None:
        while len(top) < x and rest:
            move_rest_to_top()
        while len(top) > x:
            move_top_to_rest()

        while top and rest:
            clean_top()
            clean_rest()
            top_key = top_min[0]
            rest_key = (-rest_max[0][0], -rest_max[0][1])
            if rest_key <= top_key:
                break
            move_top_to_rest()
            move_rest_to_top()

    def add(value: int) -> None:
        remove_current(value)
        freq[value] += 1
        rest.add(value)
        push_rest(value)
        rebalance()

    def remove(value: int) -> None:
        remove_current(value)
        freq[value] -= 1
        if freq[value] > 0:
            rest.add(value)
            push_rest(value)
        else:
            del freq[value]
        rebalance()

    result = []
    for i, value in enumerate(nums):
        add(value)
        if i >= k:
            remove(nums[i - k])
        if i >= k - 1:
            result.append(current_sum)

    return result
