class Solution:
    def countDistinct(self, s: str) -> int:
        transitions = [{}]
        suffix_link = [-1]
        longest = [0]
        last = 0

        for character in s:
            current = len(transitions)
            transitions.append({})
            suffix_link.append(0)
            longest.append(longest[last] + 1)

            state = last
            while state != -1 and character not in transitions[state]:
                transitions[state][character] = current
                state = suffix_link[state]

            if state == -1:
                suffix_link[current] = 0
            else:
                target = transitions[state][character]
                if longest[state] + 1 == longest[target]:
                    suffix_link[current] = target
                else:
                    clone = len(transitions)
                    transitions.append(transitions[target].copy())
                    suffix_link.append(suffix_link[target])
                    longest.append(longest[state] + 1)
                    while (
                        state != -1
                        and transitions[state].get(character) == target
                    ):
                        transitions[state][character] = clone
                        state = suffix_link[state]
                    suffix_link[target] = clone
                    suffix_link[current] = clone

            last = current

        return sum(
            longest[state] - longest[suffix_link[state]]
            for state in range(1, len(transitions))
        )
