class Solution:
    def longestBalanced(self, s: str) -> int:
        best = 1

        run = 0
        previous = ""
        for char in s:
            if char == previous:
                run += 1
            else:
                previous = char
                run = 1
            best = max(best, run)

        alphabet = "abc"
        for excluded in alphabet:
            allowed = [char for char in alphabet if char != excluded]
            difference = 0
            earliest = {0: -1}

            for index, char in enumerate(s):
                if char == excluded:
                    difference = 0
                    earliest = {0: index}
                    continue

                difference += 1 if char == allowed[0] else -1
                if difference in earliest:
                    best = max(best, index - earliest[difference])
                else:
                    earliest[difference] = index

        counts = [0, 0, 0]
        earliest_state = {(0, 0): -1}

        for index, char in enumerate(s):
            counts[ord(char) - ord("a")] += 1
            state = (counts[0] - counts[1], counts[0] - counts[2])
            if state in earliest_state:
                best = max(best, index - earliest_state[state])
            else:
                earliest_state[state] = index

        return best
