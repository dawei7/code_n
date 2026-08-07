class Solution:
    def maxCoins(self, lane1: List[int], lane2: List[int]) -> int:
        unreachable = -(10**30)
        no_switch = unreachable
        one_switch = unreachable
        two_switches = unreachable
        answer = unreachable

        for first, second in zip(lane1, lane2):
            next_no_switch = max(
                first,
                no_switch + first,
            )
            next_one_switch = max(
                second,
                one_switch + second,
                no_switch + second,
            )
            next_two_switches = max(
                two_switches + first,
                one_switch + first,
            )

            no_switch = next_no_switch
            one_switch = next_one_switch
            two_switches = next_two_switches
            answer = max(
                answer,
                no_switch,
                one_switch,
                two_switches,
            )

        return answer
