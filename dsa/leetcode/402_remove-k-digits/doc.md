# Remove K Digits

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 402 |
| Difficulty | Medium |
| Topics | String, Stack, Greedy, Monotonic Stack |
| Official Link | [LeetCode](https://leetcode.com/problems/remove-k-digits/) |

## Problem Description
### Goal
Given the normalized decimal string `num` and an integer `k`, delete exactly `k` digit occurrences. The digits that remain must preserve their original relative order, so they form a subsequence rather than an arbitrary rearrangement.

Return the numerically smallest value obtainable, written as a normalized decimal string. Remove leading zeroes from the retained sequence, and return exactly `"0"` when all digits are deleted or only zeroes remain. A locally large earlier digit may need removal to expose a smaller prefix, while any unused deletion quota must still be applied from the remaining digits. Do not parse the full number into a fixed-width integer.

### Function Contract
**Inputs**

- `num`: the original decimal representation without a leading zero
- `k`: the exact number of digits to delete

**Return value**

- Return the smallest remaining value as a normalized decimal string: remove leading zeroes and return `"0"` if no nonzero digit remains.

### Examples
**Example 1**

- Input: `num = "1432219", k = 3`
- Output: `"1219"`

**Example 2**

- Input: `num = "10200", k = 1`
- Output: `"200"`

**Example 3**

- Input: `num = "10", k = 2`
- Output: `"0"`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Remove a larger prefix digit when a smaller one arrives**

Maintain the kept digits as a nondecreasing stack while deletions remain. Before pushing a new digit, pop from the stack while its top is larger. Replacing the earliest possible larger digit with the current smaller one improves the number at its most significant differing position.

**Keep equal and increasing digits in order**

If the stack top is no larger than the current digit, deleting it would not create a better prefix than retaining it. Push the new digit and continue, allowing later smaller digits to trigger the necessary removals.

**Delete from the end when no inversion remains**

If the scan finishes with unused deletions, the kept sequence is nondecreasing. Its largest and least significant digits are at the end, so remove the remaining count from the suffix. Any earlier deletion would worsen a more significant position.

**Why the greedy stack is globally minimal**

At each inversion, any result that keeps the larger earlier digit while retaining the smaller later digit is lexicographically larger than one that deletes the former. The stack performs that forced best exchange as early as possible. After all inversions are resolved, suffix deletion is optimal for the monotone remainder, so the final fixed-length subsequence is minimal.

#### Complexity detail

Each of the `n` digits is pushed once and popped at most once, giving $O(n)$ time. The stack stores at most `n` digits and uses $O(n)$ space.

#### Alternatives and edge cases

- **Repeatedly find and delete the first descent:** makes the same greedy choice but rescans and rebuilds the string up to `k` times, taking $O(nk)$.
- **Enumerate all retained subsequences:** is combinatorial and impractical.
- **Dynamic programming by position and deletions:** stores far more state than the forced greedy prefix decisions require.
- Removing every digit returns `"0"`.
- Leading zeroes created by deletion must be stripped.
- An already nondecreasing number loses digits from its suffix.
- Equal adjacent digits can remain in their original order.

</details>
