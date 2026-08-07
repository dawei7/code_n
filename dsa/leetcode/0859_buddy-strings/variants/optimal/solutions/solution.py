class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        seen = [False] * 26
        has_duplicate = False
        mismatches = []

        for index, (source_letter, goal_letter) in enumerate(zip(s, goal)):
            letter_index = ord(source_letter) - ord("a")
            if seen[letter_index]:
                has_duplicate = True
            seen[letter_index] = True

            if source_letter != goal_letter:
                mismatches.append(index)
                if len(mismatches) > 2:
                    return False

        if not mismatches:
            return has_duplicate
        if len(mismatches) != 2:
            return False

        first, second = mismatches
        return s[first] == goal[second] and s[second] == goal[first]
