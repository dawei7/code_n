class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        left = 0
        right = 1

        while reader.get(right) < target:
            left = right + 1
            right *= 2

        while left <= right:
            middle = (left + right) // 2
            value = reader.get(middle)
            if value == target:
                return middle
            if value < target:
                left = middle + 1
            else:
                right = middle - 1

        return -1
