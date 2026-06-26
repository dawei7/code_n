# Design Twitter

| Field | Value |
|---|---|
| Source | LeetCode |
| Local Source | `nc_116` |
| Frontend ID | 355 |
| Difficulty | Medium |
| Topics | Hash Table, Linked List, Design, Heap (Priority Queue) |
| Official Link | [design-twitter](https://leetcode.com/problems/design-twitter/) |

## Problem Description & Examples
### Goal
Design a simplified Twitter-like feed. `solve(operations)` processes:
- `["postTweet", userId, tweetId]`
- `["getNewsFeed", userId]`  returns 10 most recent tweet IDs
- `["follow", followerId, followeeId]`
- `["unfollow", followerId, followeeId]`

### Function Contract
**Inputs**

- `operations`: List[List] - Twitter operations

**Return value**

List[List[int]] - results of getNewsFeed operations

### Examples
**Example 1**

- Input: `[["postTweet", 1, 5], ["getNewsFeed", 1]]`
- Output: `[[5]]`

**Example 2**

- Input: `operations = [['follow', 2, 1], ['getNewsFeed', 3], ['follow', 2, 3], ['follow', 2, 1]]`
- Output: `[[]]`

**Example 3**

- Input: `operations = [['postTweet', 3, 1], ['postTweet', 2, 2], ['postTweet', 2, 3], ['follow', 2, 3]]`
- Output: `[]`

---

## Underlying Base Algorithm(s)
- [Kth largest with heap](heap_02_kth-largest-element.md)
- [Top-K frequent elements](heap_03_top-k-frequent-elements.md)
- [Median in a stream](heap_04_median-in-a-stream.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n log n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
