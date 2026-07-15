# RLE Iterator

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 900 |
| Difficulty | Medium |
| Topics | Array, Design, Counting, Iterator |
| Official Link | [LeetCode](https://leetcode.com/problems/rle-iterator/) |

## Problem Description
### Goal
Run-length encoding represents an integer sequence with an even-length, 0-indexed array `encoding`. At every even index `i`, `encoding[i]` is the number of consecutive copies of the non-negative value `encoding[i + 1]`. A count may be zero, and adjacent runs may contain the same value, so one decoded sequence can have several valid encodings.

Design an iterator over the represented sequence without requiring it to be expanded.

Construct `RLEIterator` from `encoding`. Each call `next(n)` exhausts the next `n` decoded elements and returns the last element exhausted. If fewer than `n` elements remain, exhaust everything that is left and return `-1`.

### Function Contract
Let $m$ be the number of encoded runs and $q$ be the number of `next` calls.

**Operations**

- `RLEIterator(encoding)`: initialize the iterator from $m$ count-value pairs.
- `next(n)`: consume the next $n$ represented elements, where $1 \leq n \leq 10^9$, and return the final consumed value or `-1` if the request passes the end.
- `encoding` has even length between `2` and `1000`, and every entry is between `0` and $10^9$.
- At most `1000` calls are made to `next`.

**App-local input**

- `encoding`: the alternating count-value array.
- `operations`: calls encoded as `["next", n]`.

**Return value**

Return the integer result of each `next` call in order.

### Examples
**Example 1**

- Input: `encoding = [3,8,0,9,2,5], operations = [["next",2],["next",1],["next",1],["next",2]]`
- Output: `[8,8,5,-1]`

The encoding represents `[8,8,8,5,5]`. The final request asks for two elements when only one remains, so it returns `-1`.

**Example 2**

- Input: `encoding = [1,4], operations = [["next",1]]`
- Output: `[4]`

**Example 3**

- Input: `encoding = [0,7,2,3], operations = [["next",1],["next",1]]`
- Output: `[3,3]`

### Required Complexity
- **Time:** $O(m+q)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Keep one run pointer and one remaining count**

Store the index of the current count-value pair and how many copies remain in that run. For `next(n)`, if the request is larger than the current remainder, subtract the entire remainder from `n` and advance to the next pair. Zero-count runs are skipped by the same rule.

When the current run contains at least `n` elements, subtract `n` from its remainder and return that run's value. If the pointer reaches the end first, every remaining element has been exhausted and the answer is `-1`.

**Why the compressed scan is enough**

Before each loop iteration, all runs before the pointer are fully exhausted, and `remaining` is exactly the unused prefix length of the current run. Consuming a whole run preserves this statement at the next pair. Consuming only part of a run leaves the requested last element equal to that run's value and updates `remaining` exactly. If no pair remains, the request necessarily extended beyond the decoded sequence. Therefore every call returns the required final exhausted value without materializing individual elements.

#### Complexity detail

Across all calls, the run pointer advances through each of the $m$ pairs at most once. Besides that traversal, every call performs constant work, so the complete operation trace takes $O(m+q)$ time, equivalent to amortized $O(1)$ per call after initialization. The iterator stores only an index and a remaining count beyond the input array, using $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Fully decompress the sequence:** Indexing an expanded list is simple, but time and space depend on the sum of counts, which can be enormous even when `encoding` is short.
- **Prefix sums plus binary search:** Cumulative run endpoints allow each call to locate its final position in $O(\log m)$ time, but require $O(m)$ preprocessing space.
- **Mutate counts in place:** Subtracting directly from `encoding` also achieves the same bounds, but a separate remainder avoids modifying the caller's array.
- **Zero-count run:** Skip it without returning its associated value.
- **Exact run exhaustion:** When `n` equals the remaining count, return that run's value and leave zero copies for the next call to skip.
- **Request beyond the end:** Consume all remaining runs and return `-1`; later calls also return `-1`.
- **Adjacent equal values:** Treat them as separate runs; the returned value remains correct as the pointer crosses their boundary.
- **Large counts and requests:** Arithmetic on counts handles values up to $10^9$ without expanding the represented sequence.

</details>
