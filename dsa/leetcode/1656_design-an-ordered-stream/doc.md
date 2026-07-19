# Design an Ordered Stream

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1656 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, Design, Data Stream |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/design-an-ordered-stream/) |

## Problem Description
### Goal
A stream contains $n$ pairs `(idKey, value)` that arrive in arbitrary order. Each `idKey` is a unique integer from 1 through $n$. Design a structure whose insertion response releases values in increasing ID order.

After storing a pair, return the largest contiguous chunk beginning at the smallest ID not released by an earlier call. If that ID has not arrived, return an empty list. Concatenating every returned chunk over all insertions must equal the values ordered by IDs 1 through $n$.

### Function Contract
**Inputs**

- `OrderedStream(n)`: constructs an empty stream for IDs 1 through $n$, where $1 \le n \le 1000$.
- `insert(idKey, value)`: inserts a previously unseen ID in that range and its five-character lowercase value.
- Exactly $n$ `insert` calls occur, one for every ID.

**Return value**

Each `insert` returns the longest list of consecutive stored values starting at the current unreleased ID, or an empty list when that starting ID is absent.

### Examples
**Example 1**

- Input: `OrderedStream(5)`, followed by `(3,"ccccc")`, `(1,"aaaaa")`, `(2,"bbbbb")`, `(5,"eeeee")`, `(4,"ddddd")`
- Output chunks: `[]`, `["aaaaa"]`, `["bbbbb","ccccc"]`, `[]`, `["ddddd","eeeee"]`

The concatenated chunks are ordered by IDs 1 through 5.

**Example 2**

- Input: IDs 3, 2, then 1 in a stream of size 3
- Output chunks: `[]`, `[]`, then all three values in ID order

**Example 3**

- Input: `OrderedStream(1)`, then `(1,"aaaaa")`
- Output chunk: `["aaaaa"]`
