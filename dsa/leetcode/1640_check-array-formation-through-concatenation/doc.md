# Check Array Formation Through Concatenation

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1640 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/check-array-formation-through-concatenation/) |

## Problem Description
### Goal
You are given an array `arr` of distinct integers and a collection `pieces` of non-empty integer arrays. All values across the flattened pieces are distinct, and the pieces contain the same total number of values as `arr`.

Determine whether the pieces can be placed in some order and concatenated to equal `arr`. The pieces themselves may be reordered, but the order of values within any individual piece must remain unchanged.

### Function Contract
**Inputs**

- `arr`: an array of $n$ distinct integers, where $1 \le n \le 100$ and $1 \le \texttt{arr[i]} \le 100$.
- `pieces`: between 1 and $n$ non-empty integer arrays whose total length is $n$.
- Every flattened value in `pieces` is distinct and lies between 1 and 100.

**Return value**

Return `true` exactly when some ordering of all arrays in `pieces`, without reordering any piece internally, concatenates to `arr`; otherwise return `false`.

### Examples
**Example 1**

- Input: `arr = [15,88], pieces = [[88],[15]]`
- Output: `true`

Placing `[15]` before `[88]` forms the target.

**Example 2**

- Input: `arr = [49,18,16], pieces = [[16,18,49]]`
- Output: `false`

The values match as a set, but the sole piece's internal order cannot be changed.

**Example 3**

- Input: `arr = [91,4,64,78], pieces = [[78],[4,64],[91]]`
- Output: `true`

The ordering `[91]`, `[4,64]`, `[78]` reproduces `arr`.

### Required Complexity
- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**The next target value identifies at most one piece.** Because all flattened piece values are distinct, no two pieces can begin with the same integer. Build a map from each piece's first value to the complete piece. This converts choosing the next piece from a search into a direct lookup.

**Consume the target from left to right.** At target index `i`, `arr[i]` must be the first value of whichever piece appears next in a valid concatenation. Look up that piece and compare it with the target slice beginning at `i`. If no piece starts there or any internal value disagrees, no alternative piece can repair the mismatch, so return `false`. Otherwise advance by the entire piece length and repeat.

Reaching the end proves that the encountered pieces concatenate to `arr`. Since both sides contain $n$ distinct values in total, the successful scan cannot silently omit or reuse a piece: every target value is consumed once, and each matched piece is uniquely identified by its first value.

#### Complexity detail

Building the first-value map visits each piece once. Across the scan, slice comparisons examine each of the $n$ target positions once because matched pieces do not overlap. Total time is $O(n)$, and the piece map uses $O(n)$ space in the maximum case of singleton pieces.

#### Alternatives and edge cases

- **Search every remaining piece:** At each target boundary, scanning the full collection for a matching first value is correct but can take $O(n^2)$ time when many pieces are singletons.
- **Sort pieces by target positions:** A target-value-to-index map can order pieces by their first values, after which flattening and comparison works in $O(n\log n)$ time; sorting is unnecessary.
- **Try all piece permutations:** Permutation search ignores the distinct first-value property and grows factorially.
- A single piece succeeds only when its complete internal order equals `arr`.
- Singleton pieces may appear in any collection order because their concatenation order is chosen freely.
- Matching the first value is insufficient; every later value in that piece must match the consecutive target segment.
- The equal total lengths mean a successful complete scan uses all supplied values; no optional piece may be discarded.
- Distinctness is global across all flattened pieces, so first-value lookups are unambiguous.

</details>
