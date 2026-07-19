def solve(numberOfUsers, events):
    ordered = sorted(events, key=lambda event: (int(event[1]), 0 if event[0] == "OFFLINE" else 1))
    mentions = [0] * numberOfUsers
    offline_until = [0] * numberOfUsers

    for event_type, timestamp_text, payload in ordered:
        timestamp = int(timestamp_text)
        if event_type == "OFFLINE":
            offline_until[int(payload)] = timestamp + 60
            continue

        if payload == "ALL":
            for user in range(numberOfUsers):
                mentions[user] += 1
        elif payload == "HERE":
            for user in range(numberOfUsers):
                if offline_until[user] <= timestamp:
                    mentions[user] += 1
        else:
            for token in payload.split():
                mentions[int(token[2:])] += 1

    return mentions
