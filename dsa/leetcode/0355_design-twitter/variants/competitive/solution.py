import heapq
from collections import defaultdict
from typing import List


class Twitter:
    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        posts = self.tweets[userId]
        posts.append((self.time, tweetId))
        if len(posts) > 10:
            del posts[0]

    def getNewsFeed(self, userId: int) -> List[int]:
        sources = set(self.following[userId])
        sources.add(userId)
        heap = []
        for source in sources:
            posts = self.tweets[source]
            if posts:
                index = len(posts) - 1
                timestamp, tweet_id = posts[index]
                heap.append((-timestamp, tweet_id, source, index))
        heapq.heapify(heap)

        feed = []
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
