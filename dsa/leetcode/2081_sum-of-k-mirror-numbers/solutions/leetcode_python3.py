class Solution:
    def kMirror(self, k: int, n: int) -> int:
        def is_base_k_palindrome(number: int) -> bool:
            digits = []
            while number:
                digits.append(number % k)
                number //= k
            return digits == digits[::-1]

        total = 0
        found = 0
        length = 1

        while found < n:
            half_length = (length + 1) // 2
            start = 10 ** (half_length - 1)
            stop = 10**half_length

            for half in range(start, stop):
                text = str(half)
                if length % 2 == 0:
                    palindrome = int(text + text[::-1])
                else:
                    palindrome = int(text + text[-2::-1])

                if is_base_k_palindrome(palindrome):
                    total += palindrome
                    found += 1
                    if found == n:
                        return total

            length += 1

        return total
