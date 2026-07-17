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

### Required Complexity
- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Store by one-based ID.** Allocate an array with positions 1 through $n$ and initialize them as missing. Maintain `pointer`, the smallest ID whose value has not yet been returned. It starts at 1.

**Release only from the pointer.** On insertion, store `value` at `idKey`. Starting at `pointer`, append consecutive present values to the response and advance the pointer past each one. Stop at the first missing slot or after position $n$. If the inserted ID is beyond an existing gap, the pointer cannot move and the response is empty.

**Why every value appears once and in order.** The pointer advances only after returning its current value and never moves backward. Consequently, returned IDs are globally increasing and no ID can be returned twice. When an insertion closes a gap, the scan continues through every already buffered successor, making the returned chunk maximal. After all IDs arrive, the pointer has crossed $n$, so every value has been released exactly once.

#### Complexity detail

An individual insertion may return many values, but each array position is visited by the advancing pointer only once across the entire operation sequence. The constructor plus all $n$ insertions therefore take $O(n)$ total time, or $O(1)$ amortized time per call excluding the returned chunk itself. The value array uses $O(n)$ space.

#### Alternatives and edge cases

- **Hash map plus pointer:** A dictionary of arrived IDs supports the same $O(n)$ total expected time and is useful when the ID range is not known in advance, but the fixed dense range makes an array simpler.
- **Rescan from ID 1 after every insertion:** Tracking released IDs keeps this correct, but repeatedly walking the emitted prefix costs $O(n^2)$ total time for increasing arrivals.
- **Sort all received pairs after every insertion:** This also finds order but costs unnecessary $O(n^2\log n)$ total work.
- Inserting an ID beyond the current gap returns an empty chunk.
- One insertion can close a gap and release several values that arrived earlier.
- Increasing ID order returns a one-value chunk on every call.
- Decreasing ID order returns empty chunks until ID 1 arrives, then releases the entire stream.
- A one-element stream releases its only value immediately.
- Values need not be distinct; ordering is determined solely by `idKey`.

</details>
