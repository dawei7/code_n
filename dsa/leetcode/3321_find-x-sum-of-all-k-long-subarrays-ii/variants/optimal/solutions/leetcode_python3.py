from collections import defaultdict
from heapq import heappop, heappush
from typing import List


class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        frequency = defaultdict(int)
        side = {}
        version = defaultdict(int)
        top_min = []
        rest_max = []
        top_count = 0
        top_sum = 0

        def place_in_rest(value):
            version[value] += 1
            side[value] = False
            heappush(rest_max, (-frequency[value], -value, version[value]))

        def place_in_top(value):
            nonlocal top_count, top_sum
            version[value] += 1
            side[value] = True
            top_count += 1
            top_sum += frequency[value] * value
            heappush(top_min, (frequency[value], value, version[value]))

        def discard(value):
            nonlocal top_count, top_sum
            if value not in side:
                return
            if side[value]:
                top_count -= 1
                top_sum -= frequency[value] * value
            del side[value]
            version[value] += 1

        def clean_top():
            while top_min:
                f, value, stamp = top_min[0]
                if (
                    side.get(value) is True
                    and version[value] == stamp
                    and frequency[value] == f
                ):
                    return
                heappop(top_min)

        def clean_rest():
            while rest_max:
                negative_f, negative_value, stamp = rest_max[0]
                value = -negative_value
                if (
                    side.get(value) is False
                    and version[value] == stamp
                    and frequency[value] == -negative_f
                ):
                    return
                heappop(rest_max)

        def move_rest_to_top():
            clean_rest()
            _, negative_value, _ = heappop(rest_max)
            value = -negative_value
            discard(value)
            place_in_top(value)

        def move_top_to_rest():
            clean_top()
            _, value, _ = heappop(top_min)
            discard(value)
            place_in_rest(value)

        def rebalance():
            desired = min(x, len(side))
            while top_count < desired:
                move_rest_to_top()
            while top_count > desired:
                move_top_to_rest()

            while top_count and top_count < len(side):
                clean_top()
                clean_rest()
                smallest_top = top_min[0][:2]
                largest_rest = (-rest_max[0][0], -rest_max[0][1])
                if largest_rest <= smallest_top:
                    break
                move_top_to_rest()
                move_rest_to_top()

        def change(value, delta):
            discard(value)
            frequency[value] += delta
            if frequency[value]:
                place_in_rest(value)
            else:
                del frequency[value]
            rebalance()

        answer = []
        for index, value in enumerate(nums):
            change(value, 1)
            if index >= k:
                change(nums[index - k], -1)
            if index >= k - 1:
                answer.append(top_sum)

        return answer
