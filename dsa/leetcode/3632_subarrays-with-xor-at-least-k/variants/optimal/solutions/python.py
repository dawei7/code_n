from array import array


def solve(nums: list[int], k: int) -> int:
    zero = array("i", [-1])
    one = array("i", [-1])
    count = array("I", [0])

    def insert(value: int) -> None:
        node = 0
        count[node] += 1
        for bit in range(29, -1, -1):
            direction = (value >> bit) & 1
            child = one[node] if direction else zero[node]
            if child == -1:
                child = len(count)
                zero.append(-1)
                one.append(-1)
                count.append(0)
                if direction:
                    one[node] = child
                else:
                    zero[node] = child
            node = child
            count[node] += 1

    def count_less(value: int) -> int:
        node = 0
        result = 0
        for bit in range(29, -1, -1):
            if node == -1:
                break
            value_bit = (value >> bit) & 1
            if (k >> bit) & 1:
                same = one[node] if value_bit else zero[node]
                if same != -1:
                    result += count[same]
                node = zero[node] if value_bit else one[node]
            else:
                node = one[node] if value_bit else zero[node]
        return result

    insert(0)
    answer = 0
    prefix = 0
    seen = 1
    for value in nums:
        prefix ^= value
        answer += seen - count_less(prefix)
        insert(prefix)
        seen += 1

    return answer

