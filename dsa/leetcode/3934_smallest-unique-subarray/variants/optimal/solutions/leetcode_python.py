from typing import List


class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        transitions = [{}]
        suffix_link = [-1]
        maximum_length = [0]
        occurrences = [0]
        last = 0

        for value in nums:
            current = len(transitions)
            transitions.append({})
            suffix_link.append(0)
            maximum_length.append(maximum_length[last] + 1)
            occurrences.append(1)

            state = last
            while state != -1 and value not in transitions[state]:
                transitions[state][value] = current
                state = suffix_link[state]

            if state == -1:
                suffix_link[current] = 0
            else:
                target = transitions[state][value]
                if maximum_length[state] + 1 == maximum_length[target]:
                    suffix_link[current] = target
                else:
                    clone = len(transitions)
                    transitions.append(transitions[target].copy())
                    suffix_link.append(suffix_link[target])
                    maximum_length.append(maximum_length[state] + 1)
                    occurrences.append(0)

                    while state != -1 and transitions[state].get(value) == target:
                        transitions[state][value] = clone
                        state = suffix_link[state]

                    suffix_link[target] = clone
                    suffix_link[current] = clone

            last = current

        length_counts = [0] * (len(nums) + 1)
        for length in maximum_length:
            length_counts[length] += 1
        for length in range(1, len(length_counts)):
            length_counts[length] += length_counts[length - 1]

        order = [0] * len(transitions)
        for state in range(len(transitions) - 1, -1, -1):
            length = maximum_length[state]
            length_counts[length] -= 1
            order[length_counts[length]] = state

        for state in reversed(order[1:]):
            occurrences[suffix_link[state]] += occurrences[state]

        answer = len(nums)
        for state in range(1, len(transitions)):
            if occurrences[state] == 1:
                answer = min(
                    answer,
                    maximum_length[suffix_link[state]] + 1,
                )

        return answer
