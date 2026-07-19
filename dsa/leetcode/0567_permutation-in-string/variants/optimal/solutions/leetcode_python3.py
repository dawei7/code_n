class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target_length = len(s1)
        if target_length > len(s2):
            return False

        target = [0] * 26
        window = [0] * 26

        for index in range(target_length):
            target[ord(s1[index]) - ord("a")] += 1
            window[ord(s2[index]) - ord("a")] += 1

        matches = sum(
            target[index] == window[index]
            for index in range(26)
        )
        if matches == 26:
            return True

        def adjust(letter_index: int, change: int) -> None:
            nonlocal matches
            if window[letter_index] == target[letter_index]:
                matches -= 1
            window[letter_index] += change
            if window[letter_index] == target[letter_index]:
                matches += 1

        for right in range(target_length, len(s2)):
            adjust(ord(s2[right]) - ord("a"), 1)
            adjust(
                ord(s2[right - target_length]) - ord("a"),
                -1,
            )
            if matches == 26:
                return True

        return False

