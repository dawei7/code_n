from bisect import bisect_right


class TopVotedCandidate:
    def __init__(self, persons: list[int], times: list[int]):
        self.times = times
        self.leaders = []
        counts = {}
        leader = -1
        leader_count = 0

        for person in persons:
            counts[person] = counts.get(person, 0) + 1
            if counts[person] >= leader_count:
                leader = person
                leader_count = counts[person]
            self.leaders.append(leader)

    def q(self, t: int) -> int:
        vote_index = bisect_right(self.times, t) - 1
        return self.leaders[vote_index]


def solve(persons: list[int], times: list[int], queries: list[int]) -> list[int]:
    election = TopVotedCandidate(persons, times)
    return [election.q(time) for time in queries]
