# Iterator for Combination

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1286 |
| Difficulty | Medium |
| Topics | String, Backtracking, Design, Iterator |
| Official Link | [LeetCode](https://leetcode.com/problems/iterator-for-combination/) |

## Problem Description
### Goal
Design a `CombinationIterator` initialized with `characters`, a string of sorted distinct lowercase English letters, and an integer `combinationLength`. The iterator represents every subsequence of exactly that length, ordered lexicographically.

Calling `next()` must return the next represented combination in lexicographical order. Calling `hasNext()` must return `true` exactly while another combination remains. Every call to `next()` is guaranteed to occur when such a combination exists.

### Function Contract
**Inputs**

- `characters`: a sorted string of $n$ distinct lowercase English letters, where $1 \le n \le 15$.
- `combinationLength`: the required combination length $k$, where $1 \le k \le n$.
- `operations`: an app-local sequence of `next` and `hasNext` calls; at most $10^4$ calls occur.
- Let $q$ be the number of `next` calls.

**Return value**

For the app-local adapter, a list containing each operation's result in order. The native `next()` method returns a length-$k$ string, and `hasNext()` returns a Boolean.

### Examples
**Example 1**

- Input: `characters = "abc"`, `combinationLength = 2`, operations `next, hasNext, next, hasNext, next, hasNext`
- Output: `["ab",true,"ac",true,"bc",false]`

**Example 2**

- Input: `characters = "abcd"`, `combinationLength = 3`, operations `next, next`
- Output: `["abc","abd"]`

**Example 3**

- Input: `characters = "xy"`, `combinationLength = 2`, operations `hasNext, next, hasNext`
- Output: `[true,"xy",false]`

### Required Complexity
- **Time:** $O(qk)$
- **Space:** $O(k)$

<details>
<summary>Approach</summary>

#### General

**Represent the current combination by indices.** Store the increasing index vector $[0,1,\ldots,k-1]$. Joining the corresponding characters produces the first lexicographical combination. A Boolean records whether this current vector is still available.

**Advance to the lexicographical successor.** After returning the current string, scan indices from right to left for the last position $p$ that can increase. Position $p$ may be at most $n-k+p$ so that enough characters remain for its suffix. Increment that index, then reset every later index to one more than its predecessor. This is exactly the smallest index vector greater than the previous one: positions before $p$ stay fixed, $p$ increases by the minimum amount, and the suffix becomes as small as possible. If no position can increase, the returned combination was the final one and the availability flag becomes false.

Because `hasNext()` reads only the flag, it does not change iterator state. The index vectors remain strictly increasing, so every returned string uses distinct characters in source order; successor construction returns every valid vector once and in lexicographical order.

#### Complexity detail

Constructing the initial $k$ indices takes $O(k)$ time and space. Each `next()` call builds a $k$-character result and may scan and reset up to $k$ indices, so $q$ such calls take $O(qk)$ time. `hasNext()` is $O(1)$. The iterator stores $k$ indices and fixed-size metadata, for $O(k)$ auxiliary space; returned strings belong to the output.

#### Alternatives and edge cases

- **Precompute every combination:** Backtracking or `itertools.combinations` makes later calls simple but stores $\binom{n}{k}$ strings and uses $O(k\binom{n}{k})$ space.
- **Restart enumeration on every call:** Selecting the next result by rescanning from the first combination is correct but takes quadratic total work across successive calls.
- **Full-length combination:** When $k=n$, exactly one string exists and `hasNext()` becomes false after its return.
- **Length one:** Successor generation advances a single index through the sorted characters.
- **Repeated `hasNext()`:** These calls must be observational and return the same value until `next()` advances the state.

</details>
