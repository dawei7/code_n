from heapq import heappop, heappush
from typing import List


class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        events.sort(key=lambda event: (int(event[1]), event[0] == "MESSAGE"))

        direct = [0] * numberOfUsers
        here_mentions = [0] * numberOfUsers
        online_since = [0] * numberOfUsers
        returns: list[tuple[int, int]] = []
        all_messages = 0
        here_messages = 0

        for event_type, timestamp_text, payload in events:
            timestamp = int(timestamp_text)
            while returns and returns[0][0] <= timestamp:
                _, user = heappop(returns)
                online_since[user] = here_messages

            if event_type == "OFFLINE":
                user = int(payload)
                here_mentions[user] += here_messages - online_since[user]
                online_since[user] = -1
                heappush(returns, (timestamp + 60, user))
            elif payload == "ALL":
                all_messages += 1
            elif payload == "HERE":
                here_messages += 1
            else:
                for token in payload.split():
                    direct[int(token[2:])] += 1

        for user in range(numberOfUsers):
            if online_since[user] != -1:
                here_mentions[user] += here_messages - online_since[user]
            direct[user] += all_messages + here_mentions[user]
        return direct
