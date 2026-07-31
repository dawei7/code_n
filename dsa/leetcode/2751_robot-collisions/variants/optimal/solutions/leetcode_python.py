class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        order = sorted(range(len(positions)), key=positions.__getitem__)
        right_movers = []

        for robot in order:
            if directions[robot] == "R":
                right_movers.append(robot)
                continue

            while right_movers and healths[robot] > 0:
                opponent = right_movers[-1]
                if healths[opponent] < healths[robot]:
                    healths[opponent] = 0
                    healths[robot] -= 1
                    right_movers.pop()
                elif healths[opponent] == healths[robot]:
                    healths[opponent] = 0
                    healths[robot] = 0
                    right_movers.pop()
                else:
                    healths[opponent] -= 1
                    healths[robot] = 0

        return [health for health in healths if health > 0]
