import heapq
from collections import defaultdict


class Twitter:
    def __init__(self) -> None:
        self.time = 0
        self.tweets: dict[int, list[tuple[int, int]]] = defaultdict(list)
        self.following: dict[int, set[int]] = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        posts = self.tweets[userId]
        posts.append((self.time, tweetId))
        if len(posts) > 10:
            del posts[0]

    def getNewsFeed(self, userId: int) -> list[int]:
        sources = set(self.following[userId])
        sources.add(userId)
        heap: list[tuple[int, int, int, int]] = []
        for source in sources:
            posts = self.tweets[source]
            if posts:
                index = len(posts) - 1
                timestamp, tweet_id = posts[index]
                heap.append((-timestamp, tweet_id, source, index))
        heapq.heapify(heap)

        feed: list[int] = []
        while heap and len(feed) < 10:
            _, tweet_id, source, index = heapq.heappop(heap)
            feed.append(tweet_id)
            if index > 0:
                index -= 1
                timestamp, older_id = self.tweets[source][index]
                heapq.heappush(heap, (-timestamp, older_id, source, index))
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)


def solve(operations: list[list]) -> list[list[int]]:
    twitter = Twitter()
    feeds: list[list[int]] = []
    for operation in operations:
        name = operation[0]
        if name == "postTweet":
            twitter.postTweet(operation[1], operation[2])
        elif name == "getNewsFeed":
            feeds.append(twitter.getNewsFeed(operation[1]))
        elif name == "follow":
            twitter.follow(operation[1], operation[2])
        else:
            twitter.unfollow(operation[1], operation[2])
    return feeds
