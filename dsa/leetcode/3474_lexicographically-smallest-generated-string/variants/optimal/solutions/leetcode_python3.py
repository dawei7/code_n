class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        condition_length = len(str1)
        pattern_length = len(str2)
        total_length = condition_length + pattern_length - 1

        fixed = [""] * total_length
        for start, condition in enumerate(str1):
            if condition != "T":
                continue
            for offset, character in enumerate(str2):
                position = start + offset
                if fixed[position] and fixed[position] != character:
                    return ""
                fixed[position] = character

        prefix_function = [0] * pattern_length
        for index in range(1, pattern_length):
            matched = prefix_function[index - 1]
            while matched and str2[index] != str2[matched]:
                matched = prefix_function[matched - 1]
            if str2[index] == str2[matched]:
                matched += 1
            prefix_function[index] = matched

        transitions = [[0] * 26 for _ in range(pattern_length)]
        pattern_first = ord(str2[0]) - ord("a")
        transitions[0][pattern_first] = 1
        for state in range(1, pattern_length):
            transitions[state] = transitions[prefix_function[state - 1]].copy()
            character_index = ord(str2[state]) - ord("a")
            transitions[state][character_index] = state + 1

        feasible = [bytearray(pattern_length) for _ in range(total_length + 1)]
        feasible[total_length] = bytearray([1]) * pattern_length
        fallback = prefix_function[-1]

        for position in range(total_length - 1, -1, -1):
            candidates = (fixed[position],) if fixed[position] else ("a", "b")
            row = feasible[position]
            next_row = feasible[position + 1]
            window_start = position - pattern_length + 1

            for state in range(pattern_length):
                for character in candidates:
                    next_state = transitions[state][ord(character) - ord("a")]
                    if next_state == pattern_length:
                        if window_start >= 0 and str1[window_start] == "F":
                            continue
                        next_state = fallback
                    if next_row[next_state]:
                        row[state] = 1
                        break

        if not feasible[0][0]:
            return ""

        answer = []
        state = 0
        for position in range(total_length):
            candidates = (fixed[position],) if fixed[position] else ("a", "b")
            window_start = position - pattern_length + 1

            for character in candidates:
                next_state = transitions[state][ord(character) - ord("a")]
                if next_state == pattern_length:
                    if window_start >= 0 and str1[window_start] == "F":
                        continue
                    next_state = fallback
                if feasible[position + 1][next_state]:
                    answer.append(character)
                    state = next_state
                    break

        return "".join(answer)
