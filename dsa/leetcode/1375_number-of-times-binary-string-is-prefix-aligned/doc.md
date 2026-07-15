# Number of Times Binary String Is Prefix-Aligned

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1375 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/number-of-times-binary-string-is-prefix-aligned/) |

## Problem Description

### Goal

A binary string of length `n` initially contains only zeroes. The array `flips` is a permutation of the positions from $1$ through $n$. At step `i`, the bit at position `flips[i]` changes permanently from `0` to `1`.

The string is prefix-aligned after a step when every bit from position $1$ through the number of completed steps is `1`; because exactly that many bits have been changed, all later positions are then still `0`. Count how many steps leave the string prefix-aligned.

### Function Contract

**Inputs**

- `flips`: a permutation of $1, 2, \ldots, n$ describing the order in which the `n` bits are turned on.

**Return value**

- The number of steps after which the bits equal a prefix of `1` values followed by only `0` values.

### Examples

**Example 1**

- Input: `flips = [3,2,4,1,5]`
- Output: `2`

**Example 2**

- Input: `flips = [4,1,2,3]`
- Output: `1`

**Example 3**

- Input: `flips = [1,2,3]`
- Output: `3`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Replace the bit string with one boundary.** After `i` steps, exactly `i` distinct positions are on. Those positions are exactly $1, 2, \ldots, i$ if and only if none lies to the right of `i`. Track the largest position encountered so far as `rightmost`.

At step `i`, every seen position is at most `i` exactly when `rightmost == i`. Since there are `i` distinct seen positions drawn from the `i` available positions in that prefix, they must fill the entire prefix. Conversely, a prefix-aligned state cannot contain an on bit beyond `i`, so its maximum is necessarily `i`. Count each step satisfying this equality.

#### Complexity detail

The scan processes each of the `n` flips once and performs constant work per entry, so time is $O(n)$. The running maximum and answer counter use $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Materialize and rescan the bits:** Mark each flipped position and test the current prefix after every step. This is correct but can take $O(n^2)$ time.
- **Track a set of missing positions:** Removing each flip and checking whether the prefix is complete works, but requires $O(n)$ additional space.
- **First position delayed:** No alignment occurs until every earlier gap is filled, even if many positions to its right are already on.
- **Already ordered flips:** For `[1,2,...,n]`, every step is prefix-aligned.
- **Reverse order:** Only the final step is aligned when positions are flipped from `n` down to `1`.
- **Final step:** It always counts because all `n` positions are on and the running maximum equals `n`.

</details>
