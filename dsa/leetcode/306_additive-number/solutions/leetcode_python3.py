def _is_additive(num: str) -> bool:
    length = len(num)
    for first_end in range(1, length - 1):
        if num[0] == "0" and first_end > 1:
            break
        first = int(num[:first_end])
        for second_end in range(first_end + 1, length):
            if num[first_end] == "0" and second_end - first_end > 1:
                break
            second = int(num[first_end:second_end])
            index = second_end
            terms = 2
            left = first
            right = second
            while index < length:
                next_text = str(left + right)
                if not num.startswith(next_text, index):
                    break
                index += len(next_text)
                left, right = right, left + right
                terms += 1
            if index == length and terms >= 3:
                return True
    return False


class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        return _is_additive(num)
