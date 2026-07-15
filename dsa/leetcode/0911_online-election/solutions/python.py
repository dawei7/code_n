"""Optimal app-local solution for LeetCode 911."""

from bisect import bisect_right


def solve(persons, times, queries):
    counts = {}
    leaders = []
    leader = -1
    leader_count = 0

    for person in persons:
        counts[person] = counts.get(person, 0) + 1
        if counts[person] >= leader_count:
            leader = person
            leader_count = counts[person]
        leaders.append(leader)

    return [leaders[bisect_right(times, time) - 1] for time in queries]
