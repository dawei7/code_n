# Design Twitter

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 355 |
| Difficulty | Medium |
| Topics | Hash Table, Linked List, Design, Heap (Priority Queue) |
| Official Link | [LeetCode](https://leetcode.com/problems/design-twitter/) |

## Problem Description
### Goal
Design a miniature Twitter service with persistent users, follow relationships, and timestamped tweet publications. `postTweet(userId, tweetId)` records a new globally later tweet with a unique tweet ID, while `follow` and `unfollow` update which other users contribute to a follower's feed.

`getNewsFeed(userId)` returns at most the ten most recent tweet IDs posted by that user or by users currently followed, ordered newest first. A user's own tweets are always eligible without requiring a self-follow. Unfollowing affects later feeds but does not delete tweets. Process operations in order, avoid duplicate feed entries from self-follow behavior, and return results only for feed queries.

### Function Contract
**Inputs**

- `operations`: for the app adapter, operations `postTweet`, `getNewsFeed`, `follow`, and `unfollow` with their integer arguments. Native LeetCode calls the corresponding `Twitter` methods directly.

**Return value**

- The app adapter returns one feed list for each `getNewsFeed` operation, in query order. Each feed is newest first and contains at most ten tweet IDs.

### Examples
**Example 1**

- Input: `operations = [["postTweet",1,5],["getNewsFeed",1]]`
- Output: `[[5]]`

**Example 2**

- Input: `operations = [["postTweet",1,5],["follow",1,2],["postTweet",2,6],["getNewsFeed",1],["unfollow",1,2],["getNewsFeed",1]]`
- Output: `[[6,5],[5]]`

**Example 3**

- Input: `operations = [["getNewsFeed",7]]`
- Output: `[[]]`
