from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        read = 0
        write = 0
        while read < len(chars):
            end = read + 1
            while end < len(chars) and chars[end] == chars[read]:
                end += 1

            chars[write] = chars[read]
            write += 1
            run_length = end - read
            if run_length > 1:
                for digit in str(run_length):
                    chars[write] = digit
                    write += 1
            read = end
        return write
