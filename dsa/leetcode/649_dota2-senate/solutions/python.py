from collections import deque


def solve(senate: str) -> str:
    size = len(senate)
    radiant = deque(index for index, party in enumerate(senate) if party == "R")
    dire = deque(index for index, party in enumerate(senate) if party == "D")

    while radiant and dire:
        radiant_index = radiant.popleft()
        dire_index = dire.popleft()
        if radiant_index < dire_index:
            radiant.append(radiant_index + size)
        else:
            dire.append(dire_index + size)
    return "Radiant" if radiant else "Dire"
