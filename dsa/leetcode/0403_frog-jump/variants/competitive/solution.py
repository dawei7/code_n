class Solution:
    def canCross(self, stones: List[int]) -> bool:
        reachable = {position: set() for position in stones}
        reachable[0].add(0)

        for position in stones:
            for last_jump in reachable[position]:
                for next_jump in (last_jump - 1, last_jump, last_jump + 1):
                    next_position = position + next_jump
                    if next_jump > 0 and next_position in reachable:
                        reachable[next_position].add(next_jump)

        return bool(reachable[stones[-1]])
