def solve(nums: list[int], k: int, dist: int) -> int:
    values = sorted(set(nums))
    index = {value: i + 1 for i, value in enumerate(values)}

    class Fenwick:
        def __init__(self, size: int):
            self.bit = [0] * (size + 1)

        def add(self, pos: int, delta: int) -> None:
            while pos < len(self.bit):
                self.bit[pos] += delta
                pos += pos & -pos

        def prefix_sum(self, pos: int) -> int:
            total = 0
            while pos > 0:
                total += self.bit[pos]
                pos -= pos & -pos
            return total

        def lower_bound(self, target: int) -> int:
            pos = 0
            bit_mask = 1 << (len(self.bit).bit_length() - 1)
            while bit_mask:
                nxt = pos + bit_mask
                if nxt < len(self.bit) and self.bit[nxt] < target:
                    target -= self.bit[nxt]
                    pos = nxt
                bit_mask >>= 1
            return pos + 1

    counts = Fenwick(len(values))
    sums = Fenwick(len(values))

    def add_value(value: int, delta: int) -> None:
        pos = index[value]
        counts.add(pos, delta)
        sums.add(pos, delta * value)

    def smallest_sum(amount: int) -> int:
        if amount <= 0:
            return 0
        pos = counts.lower_bound(amount)
        before_count = counts.prefix_sum(pos - 1)
        before_sum = sums.prefix_sum(pos - 1)
        return before_sum + (amount - before_count) * values[pos - 1]

    choose = k - 1
    for i in range(1, dist + 2):
        add_value(nums[i], 1)

    ans = nums[0] + smallest_sum(choose)
    for right in range(dist + 2, len(nums)):
        add_value(nums[right - dist - 1], -1)
        add_value(nums[right], 1)
        ans = min(ans, nums[0] + smallest_sum(choose))

    return ans
