MAX_AGE = 120


def solve(ages: list[int]) -> int:
    counts = [0] * (MAX_AGE + 1)
    for age in ages:
        counts[age] += 1

    prefix = counts[:]
    for age in range(1, MAX_AGE + 1):
        prefix[age] += prefix[age - 1]

    requests = 0
    for sender_age in range(15, MAX_AGE + 1):
        senders = counts[sender_age]
        if senders == 0:
            continue

        lower_cutoff = sender_age // 2 + 7
        eligible_people = prefix[sender_age] - prefix[lower_cutoff]
        requests += senders * (eligible_people - 1)

    return requests
