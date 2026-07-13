from collections import Counter, deque


def solve(watched_videos, friends, id, level):
    queue = deque([id])
    seen = {id}
    for _ in range(level):
        for _ in range(len(queue)):
            person = queue.popleft()
            for friend in friends[person]:
                if friend not in seen:
                    seen.add(friend)
                    queue.append(friend)
    counts = Counter()
    for person in queue:
        counts.update(watched_videos[person])
    return sorted(counts, key=lambda video: (counts[video], video))
