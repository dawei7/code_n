## Description

Design a simplified Twitter service. Users must be able to publish tweets, follow or unfollow other users, and view the ten most recent tweets available in their news feed.

Implement the `Twitter` class:

- `Twitter()` initializes the service object.
- `void postTweet(int userId, int tweetId)` publishes a tweet with ID `tweetId` from `userId`. Every invocation receives a globally unique `tweetId`.
- `List<Integer> getNewsFeed(int userId)` returns up to ten tweet IDs posted by `userId` or by users whom `userId` follows. Order them from most recent to least recent.
- `void follow(int followerId, int followeeId)` makes `followerId` follow `followeeId`.
- `void unfollow(int followerId, int followeeId)` makes `followerId` stop following `followeeId`.
