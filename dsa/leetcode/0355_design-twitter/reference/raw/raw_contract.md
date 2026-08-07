## Function Contract

**Inputs**

- `operations`: For the app adapter, a chronological list of `postTweet`, `getNewsFeed`, `follow`, and `unfollow` calls and their arguments. LeetCode invokes the corresponding native methods directly.

**Return value**

The app adapter returns the feed produced by each `getNewsFeed` operation, in query order. Each native call returns at most ten eligible tweet IDs from newest to oldest.
