from typing import List


class Solution:
    def countKConstraintSubstrings(
        self,
        s: str,
        k: int,
        queries: List[List[int]],
    ) -> List[int]:
        length = len(s)
        rightmost_valid = [length - 1] * length
        valid_suffix_prefix = [0] * (length + 1)

        counts = [0, 0]
        left = 0
        for right, bit in enumerate(s):
            counts[int(bit)] += 1
            while counts[0] > k and counts[1] > k:
                rightmost_valid[left] = right - 1
                counts[int(s[left])] -= 1
                left += 1
            valid_suffix_prefix[right + 1] = valid_suffix_prefix[right] + right - left + 1

        answer = []
        for query_left, query_right in queries:
            prefix_end = min(query_right, rightmost_valid[query_left])
            prefix_length = prefix_end - query_left + 1
            prefix_count = prefix_length * (prefix_length + 1) // 2
            tail_count = valid_suffix_prefix[query_right + 1] - valid_suffix_prefix[prefix_end + 1]
            answer.append(prefix_count + tail_count)

        return answer
