from array import array


class Solution:
    def numberOfCombinations(self, num: str) -> int:
        if num[0] == "0":
            return 0

        modulus = 1_000_000_007
        length = len(num)
        lcp = [array("H", [0]) * (length + 1) for _ in range(length + 1)]

        for left in range(length - 2, -1, -1):
            left_row = lcp[left]
            next_row = lcp[left + 1]
            for right in range(left + 1, length):
                if num[left] == num[right]:
                    left_row[right] = next_row[right + 1] + 1

        prefix = [array("I", [0]) * (length + 1) for _ in range(length + 1)]

        for end in range(1, length + 1):
            row = prefix[end]
            for current_length in range(1, end + 1):
                start = end - current_length
                ways = 0

                if num[start] != "0":
                    if start == 0:
                        ways = 1
                    else:
                        ways = prefix[start][min(current_length - 1, start)]
                        if start >= current_length:
                            previous_start = start - current_length
                            common = lcp[previous_start][start]
                            if (
                                common >= current_length
                                or num[previous_start + common] <= num[start + common]
                            ):
                                ways += (
                                    prefix[start][current_length]
                                    - prefix[start][current_length - 1]
                                ) % modulus

                row[current_length] = (row[current_length - 1] + ways) % modulus

        return prefix[length][length]
