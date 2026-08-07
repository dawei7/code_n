class Solution:
    def minimumValueSum(self, nums: List[int], andValues: List[int]) -> int:
        infinity = 10**30
        states = {(0, -1): 0}

        for value in nums:
            next_states = {}
            for (segment, current_and), cost in states.items():
                if segment == len(andValues):
                    continue

                current_and &= value
                target = andValues[segment]
                if current_and & target != target:
                    continue

                state = (segment, current_and)
                next_states[state] = min(
                    next_states.get(state, infinity),
                    cost,
                )

                if current_and == target:
                    state = (segment + 1, -1)
                    next_states[state] = min(
                        next_states.get(state, infinity),
                        cost + value,
                    )

            states = next_states

        return states.get((len(andValues), -1), -1)
