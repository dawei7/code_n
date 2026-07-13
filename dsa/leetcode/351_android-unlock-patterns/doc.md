# Android Unlock Patterns

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 351 |
| Difficulty | Medium |
| Topics | Dynamic Programming, Backtracking, Bit Manipulation, Bitmask |
| Official Link | [LeetCode](https://leetcode.com/problems/android-unlock-patterns/) |

## Problem Description
### Goal
On the $3 x 3$ Android keypad, form unlock patterns containing between `m` and `n` keys, inclusive. A pattern can start at any key and may use each of the nine keys at most once.

A move is valid when it goes directly to an unused key without passing through another keypad key, or when any key lying exactly between the endpoints has already appeared earlier in the pattern. Count every distinct ordered pattern satisfying these rules and permitted lengths. Do not count prefixes shorter than `m`, extensions longer than `n`, or paths that jump over an unvisited intermediate key.

### Function Contract
**Inputs**

- `m`: the minimum pattern length
- `n`: the maximum pattern length, with $1 \le m \le n \le 9$

**Return value**

- The number of valid patterns whose lengths lie in the inclusive range `[m, n]`.

### Examples
**Example 1**

- Input: `m = 1, n = 1`
- Output: `9`

**Example 2**

- Input: `m = 1, n = 2`
- Output: `65`

**Example 3**

- Input: `m = 2, n = 2`
- Output: `56`

### Required Complexity

- **Time:** $O(K^3 \cdot 2^K)$
- **Space:** $O(K^2 \cdot 2^K)$

<details>
<summary>Approach</summary>

#### General

**Encode only the moves that cross another key**

Number the keypad as

`1 2 3`

`4 5 6`

`7 8 9`.

Most moves between unused keys are immediately legal. The exceptional pairs cross a key exactly halfway between them: `1-3` crosses `2`, `1-7` crosses `4`, `3-9` crosses `6`, `7-9` crosses `8`, and `1-9`, `3-7`, `2-8`, and `4-6` cross `5`. The same restriction applies in both directions. Store these intermediate keys in a symmetric `skip` table; every other pair has intermediate value zero.

**Search legal continuations from a compact state**

A bitmask records visited keys. A state consists of the current key, the visited mask, and the number of additional keys still required. To extend it, try every unvisited destination. The move is legal when its `skip` entry is zero or the indicated intermediate key is already set in the mask. Mark the destination and recurse. When no additional key is required, the current prefix itself contributes one valid pattern.

**Exploit the keypad's three symmetry classes**

Memoizing this state avoids recounting identical suffix choices reached through different orders. For each requested total length, start once from a representative corner, edge, and center. Rotational/reflection symmetry makes keys `1, 3, 7, 9` equivalent and keys `2, 4, 6, 8` equivalent, while key `5` stands alone. Thus the count is

$4 \cdot \operatorname{count\_from}(1) + 4 \cdot \operatorname{count\_from}(2) + \operatorname{count\_from}(5)$.

**Why the search counts every legal pattern once**

The transition checks exactly the two validity rules: the destination is unused, and any crossed key has already been used. Therefore every generated sequence is legal. Conversely, the next key of any legal pattern satisfies those checks and is among the tried destinations, so induction on the remaining length shows that every legal pattern is counted. Distinct starting keys and destination choices describe distinct sequences, so none are counted twice.

#### Complexity detail

Let $K = 9$ keypad keys. There are at most `K` current keys, $2^{K}$ masks, and `K` remaining-length values. Each state tries up to `K` destinations, giving the conservative bound $O(K^3 \cdot 2^K)$ time and $O(K^2 \cdot 2^K)$ cached states plus recursion. Since `K` is fixed at nine, the real resource use is bounded by a small constant.

#### Alternatives and edge cases

- **Backtracking without memoization:** is correct but revisits equivalent suffix states and approaches permutation growth as the maximum length increases.
- **Generate permutations before validation:** performs still more wasted work because illegal jumps are not pruned when they first occur.
- The intermediate-key rule depends on history: `1 -> 3` is illegal initially but becomes legal after visiting key `2`.
- Adjacent and non-collinear moves do not require an intermediate key.
- Length one has exactly nine patterns, and no pattern can exceed nine because keys cannot repeat.

</details>
