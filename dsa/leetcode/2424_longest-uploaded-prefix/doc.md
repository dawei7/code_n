# Longest Uploaded Prefix

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2424 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, Binary Search, Union-Find, Design, Binary Indexed Tree, Segment Tree, Heap (Priority Queue), Ordered Set |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Longest Uploaded Prefix](https://leetcode.com/problems/longest-uploaded-prefix/) |

## Problem Description

### Goal

A stream contains $n$ videos identified by the distinct integers from 1 through $n$. Videos are uploaded to a server in an arbitrary order. An integer $i$ is an uploaded prefix when every video numbered from 1 through $i$, inclusive, has already been uploaded.

Implement a data structure that records uploads and reports the greatest current uploaded prefix. Before video 1 arrives, the reported length is 0; gaps prevent the prefix from extending even when larger-numbered videos have already arrived.

### Function Contract

**Platform interface**

- `LUPrefix(n)` initializes a stream containing videos 1 through $n$.
- `upload(video)` records the specified video as uploaded and returns nothing.
- `longest()` returns the largest $i$ for which all videos from 1 through $i$ are uploaded.

The constraints are $1 \le n \le 10^5$ and $1 \le \texttt{video} \le n$. Every uploaded video number is distinct. Across one object, at most $2 \cdot 10^5$ calls are made to `upload` and `longest`, and `longest` is called at least once.

**App-local adapter**

Let $q$ be the number of entries in `operations`.

- `n`: The number of videos in the stream.
- `operations`: An ordered list of `[name, arguments]` calls using `"upload"` or `"longest"`.
- Return one output per operation: `null` for `upload` and the reported integer for `longest`.

### Examples

**Example 1**

- Input: `n = 4, operations = [["upload",[3]],["longest",[]],["upload",[1]],["longest",[]],["upload",[2]],["longest",[]]]`
- Output: `[null,0,null,1,null,3]`

Video 3 is initially separated from the prefix. Uploading 1 creates a prefix of length 1, and uploading 2 joins the already-uploaded video 3.

**Example 2**

- Input: `n = 5, operations = [["upload",[1]],["upload",[2]],["longest",[]],["upload",[4]],["longest",[]]]`
- Output: `[null,null,2,null,2]`

Uploading video 4 cannot extend the prefix while video 3 is missing.

**Example 3**

- Input: `n = 1, operations = [["longest",[]],["upload",[1]],["longest",[]]]`
- Output: `[0,null,1]`

The prefix is empty before the only video arrives and complete afterward.
