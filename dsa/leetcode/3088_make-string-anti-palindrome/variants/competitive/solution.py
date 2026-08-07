class Solution:
    def makeAntiPalindrome(self, s: str) -> str:
        n = len(s)
        half = n // 2
        counts = [0] * 26
        for ch in s:
            counts[ord(ch) - ord("a")] += 1

        if max(counts) > half:
            return "-1"

        remaining = counts[:]
        first = []
        needed = half
        for letter in range(26):
            take = min(remaining[letter], needed)
            first.extend(chr(ord("a") + letter) for _ in range(take))
            remaining[letter] -= take
            needed -= take

        forbidden_counts = [0] * 26
        for ch in first:
            forbidden_counts[ord(ch) - ord("a")] += 1

        second = []
        slots = half
        for forbidden_ch in reversed(first):
            forbidden = ord(forbidden_ch) - ord("a")
            forbidden_counts[forbidden] -= 1
            slots -= 1

            pick = -1
            for letter in range(26):
                if remaining[letter] > slots - forbidden_counts[letter]:
                    pick = letter
                    break

            if pick == -1:
                for letter in range(26):
                    if remaining[letter] and letter != forbidden:
                        pick = letter
                        break

            remaining[pick] -= 1
            second.append(chr(ord("a") + pick))

        return "".join(first + second)
