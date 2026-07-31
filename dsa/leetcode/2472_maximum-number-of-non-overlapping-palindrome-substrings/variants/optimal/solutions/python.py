def solve(s, k):
    answer = 0
    available = 0

    def is_palindrome(left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    for right in range(k - 1, len(s)):
        for length in (k, k + 1):
            left = right - length + 1
            if left >= available and is_palindrome(left, right):
                answer += 1
                available = right + 1
                break

    return answer
