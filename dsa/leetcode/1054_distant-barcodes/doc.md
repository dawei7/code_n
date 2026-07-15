# Distant Barcodes

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1054 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Greedy, Sorting, Heap (Priority Queue), Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/distant-barcodes/) |

## Problem Description

### Goal

A warehouse stores a row of barcode values, where `barcodes[i]` is the barcode at position `i`. Values may occur more than once.

Rearrange the entire array so that no two adjacent positions contain equal barcode values. Every input occurrence must appear exactly once in the result. Return any arrangement satisfying that condition; the input is guaranteed to admit at least one valid answer.

### Function Contract

**Inputs**

- `barcodes`: $N$ barcode values, where $1 \le N \le 10^4$ and $1 \le \texttt{barcodes[i]} \le 10^4$; let $U$ be the number of distinct values.

**Return value**

- Any permutation of all input values in which adjacent barcodes are always different.

### Examples

**Example 1**

- Input: `barcodes = [1,1,1,2,2,2]`
- Output: `[2,1,2,1,2,1]`
- Explanation: The counts are preserved and the two values alternate.

**Example 2**

- Input: `barcodes = [1,1,1,1,2,2,3,3]`
- Output: `[1,3,1,3,1,2,1,2]`

### Required Complexity

- **Time:** $O(N log U)$
- **Space:** $O(U)$

<details>
<summary>Approach</summary>

#### General

**Count remaining occurrences:** Build a frequency map and place pairs of negative count and barcode value into a heap. Negative counts make the most frequent remaining value the next heap entry.

**Hold back the previous value:** Remove the current most frequent available value, append it, and decrement its remaining count. Do not immediately return it to the heap. Instead, first reinsert the value used on the preceding step if it still has occurrences. The just-appended value is therefore unavailable for the next position.

**Keep the difficult value schedulable:** Choosing the most frequent allowed value uses scarce separating positions before less frequent values. The guarantee that a solution exists ensures the heap never becomes empty while the held-back value still needs placement.

Every output step removes one occurrence from the input multiset, so the result preserves all counts. The previous barcode is excluded from the heap during the next choice, proving adjacent outputs differ. The loop emits exactly $N$ values, and the greedy frequency priority prevents a high-count value from being postponed until it can no longer be separated.

#### Complexity detail

Counting takes $O(N)$ time. Each of the $N$ placements performs a constant number of heap operations on at most $U$ entries, giving $O(N log U)$ time. The frequency map and heap use $O(U)$ space; the returned array is output storage.

#### Alternatives and edge cases

- **Scan all remaining values:** At each position, linearly search the $U$ counts for the most frequent value unequal to the previous one. It remains correct but takes $O(NU)$ time.
- **Even-then-odd placement:** Sort values by frequency and fill even indices before odd indices. It can achieve $O(N+U log U)$ time with careful count handling.
- **Backtracking:** Try every currently legal value and undo failures. This explores an exponential search tree unnecessarily.
- **Single barcode:** The one-element array is already valid.
- **Two values:** When counts permit, they alternate until the less frequent value is exhausted.
- **All distinct:** Any order is valid because no equal values can become adjacent.
- **Dominant value:** It must occupy separated positions, which is why frequency priority matters.
- **Non-unique output:** Different valid permutations are accepted; only multiplicities and adjacency constraints matter.

</details>
