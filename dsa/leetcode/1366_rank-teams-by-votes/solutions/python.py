"""Reference solution for LeetCode 1366."""


def solve(votes):
    team_count = len(votes[0])
    ranks = {team: [0] * team_count for team in votes[0]}
    for vote in votes:
        for position, team in enumerate(vote):
            ranks[team][position] -= 1
    return "".join(sorted(ranks, key=lambda team: (ranks[team], team)))
