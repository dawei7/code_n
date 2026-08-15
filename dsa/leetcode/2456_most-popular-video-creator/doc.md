# Most Popular Video Creator

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2456 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, String, Sorting, Heap (Priority Queue) |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/most-popular-video-creator/) |

## Problem Description

### Goal

Three arrays `creators`, `ids`, and `views` describe $n$ videos. At index $i$, `creators[i]` names the video's creator, `ids[i]` is its identifier, and `views[i]` is its view count. A creator's popularity is the sum of the views of all videos attributed to that creator.

Find every creator whose popularity is maximal. For each such creator, pair the creator's name with the identifier of that creator's most-viewed video. If several of their videos share the largest individual view count, choose the lexicographically smallest identifier among them.

Identifiers are not guaranteed to be unique: two entries with the same identifier still describe distinct videos and both contribute their own views. Return the requested creator-and-identifier pairs in any order.

### Function Contract

**Inputs**

- `creators`: A list of lowercase creator names.
- `ids`: A list of lowercase video identifiers.
- `views`: A list of non-negative video view counts.

All three arrays have the same length $n$, where $1\le n\le 10^5$. Each creator name and identifier has length between $1$ and $5$, inclusive, and every view count is between $0$ and $10^5$, inclusive.

**Return value**

- A list containing `[creator, id]` for every creator tied for maximum total popularity. The pairs may appear in any order.

### Examples

#### Example 1

- **Input:** `creators = ["alice", "bob", "alice", "chris"]`, `ids = ["one", "two", "three", "four"]`, `views = [5, 10, 5, 4]`
- **Output:** `[["alice", "one"], ["bob", "two"]]`
- **Explanation:** Alice and Bob each total `10` views. Alice's two videos tie at `5`, so the smaller identifier `"one"` is selected.

#### Example 2

- **Input:** `creators = ["alice", "alice", "alice"]`, `ids = ["a", "b", "c"]`, `views = [1, 2, 2]`
- **Output:** `[["alice", "b"]]`
- **Explanation:** The videos `"b"` and `"c"` tie for Alice's largest view count, and `"b"` is lexicographically smaller.
