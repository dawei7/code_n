# Shortest Impossible Sequence of Rolls

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2350 |
| Difficulty | Hard |
| Topics | Array, Hash Table, Greedy |
| Official Link | [shortest-impossible-sequence-of-rolls](https://leetcode.com/problems/shortest-impossible-sequence-of-rolls/) |

## Problem Description & Examples
### Goal
Given an array of integer `rolls` representing outcomes of a dice, and an integer `k` representing the maximum possible value for a single roll (i.e., rolls are between 1 and `k`), determine the length of the shortest positive integer sequence that cannot be formed as a subsequence of the given `rolls`. A sequence `[s_1, s_2, ..., s_L]` is considered formed if there exist indices `i_1 < i_2 < ... < i_L` in the `rolls` array such that `rolls[i_j] = s_j` for all `j` from 1 to `L`.

### Function Contract
**Inputs**

- `rolls`: `List[int]` - An array of integers, where each `rolls[i]` is between 1 and `k`.
- `k`: `int` - An integer representing the maximum possible value for a roll.

**Return value**

- `int` - The length of the shortest positive integer sequence (composed of values from 1 to `k`) that cannot be formed as a subsequence of `rolls`.

### Examples
**Example 1**

- Input: `rolls = [4,2,1,2,3,3,2,4,1]`, `k = 4`
- Output: `3`
- Explanation:
    - We initialize `current_sequence_length = 0` and `seen_in_current_block = set()`.
    - Iterate through `rolls`:
        - `roll = 4`: `seen_in_current_block` becomes `{4}`.
        - `roll = 2`: `seen_in_current_block` becomes `{4, 2}`.
        - `roll = 1`: `seen_in_current_block` becomes `{4, 2, 1}`.
        - `roll = 2`: (already in `seen_in_current_block`).
        - `roll = 3`: `seen_in_current_block` becomes `{4, 2, 1, 3}`. Since `len(seen_in_current_block) == k` (i.e., 4), we increment `current_sequence_length` to `1` and clear `seen_in_current_block`.
        - `roll = 3`: `seen_in_current_block` becomes `{3}`.
        - `roll = 2`: `seen_in_current_block` becomes `{3, 2}`.
        - `roll = 4`: `seen_in_current_block` becomes `{3, 2, 4}`.
        - `roll = 1`: `seen_in_current_block` becomes `{3, 2, 4, 1}`. Since `len(seen_in_current_block) == k`, we increment `current_sequence_length` to `2` and clear `seen_in_current_block`.
    - After processing all rolls, `current_sequence_length` is `2`.
    - The shortest impossible sequence has length `current_sequence_length + 1 = 2 + 1 = 3`. This means all sequences of length 2 can be formed, but at least one sequence of length 3 cannot.

**Example 2**

- Input: `rolls = [1,1,2,2]`, `k = 2`
- Output: `2`
- Explanation:
    - We initialize `current_sequence_length = 0` and `seen_in_current_block = set()`.
    - Iterate through `rolls`:
        - `roll = 1`: `seen_in_current_block` becomes `{1}`.
        - `roll = 1`: (already in `seen_in_current_block`).
        - `roll = 2`: `seen_in_current_block` becomes `{1, 2}`. Since `len(seen_in_current_block) == k` (i.e., 2), we increment `current_sequence_length` to `1` and clear `seen_in_current_block`.
        - `roll = 2`: `seen_in_current_block` becomes `{2}`.
    - After processing all rolls, `current_sequence_length` is `1`.
    - The shortest impossible sequence has length `current_sequence_length + 1 = 1 + 1 = 2`.
    - For instance, the sequence `[2,1]` is impossible to form. To form `[2,1]`, we need to find a `2` at index `i_1` and a `1` at index `i_2` such that `i_1 < i_2`. In `rolls = [1,1,2,2]`, all `1`s appear at indices `0, 1` and all `2`s appear at indices `2, 3`. Thus, any `2` will always appear after any `1`, making `[2,1]` impossible.

**Example 3**

- Input: `rolls = [1,2,3,4,5,6]`, `k = 6`
- Output: `2`
- Explanation:
    - We initialize `current_sequence_length = 0` and `seen_in_current_block = set()`.
    - Iterate through `rolls`:
        - `roll = 1`: `seen_in_current_block` becomes `{1}`.
        - `roll = 2`: `seen_in_current_block` becomes `{1, 2}`.
        - `roll = 3`: `seen_in_current_block` becomes `{1, 2, 3}`.
        - `roll = 4`: `seen_in_current_block` becomes `{1, 2, 3, 4}`.
        - `roll = 5`: `seen_in_current_block` becomes `{1, 2, 3, 4, 5}`.
        - `roll = 6`: `seen_in_current_block` becomes `{1, 2, 3, 4, 5, 6}`. Since `len(seen_in_current_block) == k` (i.e., 6), we increment `current_sequence_length` to `1` and clear `seen_in_current_block`.
    - After processing all rolls, `current_sequence_length` is `1`.
    - The shortest impossible sequence has length `current_sequence_length + 1 = 1 + 1 = 2`. For example, `[1,1]` is impossible as there is only one `1` in the `rolls` array.

---

## Underlying Base Algorithm(s)
The problem can be solved using a **Greedy Algorithm** combined with a **Hash Set** (or `set` in Python) for efficient tracking of seen elements.

The core idea is to determine how many "full sets" of distinct numbers from `1` to `k` can be formed sequentially from the `rolls` array. A "full set" is achieved when all `k` distinct numbers (`1, 2, ..., k`) have been encountered in a segment of the `rolls` array, using rolls that appear after the previous "full set" was completed.

If we can form `m` such "full sets" (let's call them `S_1, S_2, ..., S_m`), where each `S_j` is a subsequence of `rolls` that contains all numbers from `1` to `k`, and `S_j` appears entirely before `S_{j+1}` in `rolls`, then we can construct *any* sequence of length `m`. This is because for any target sequence `[x_1, x_2, ..., x_m]`, we can pick `x_1` from `S_1`, `x_2` from `S_2`, and so on, ensuring increasing indices.

If we can form `m` full sets, but cannot complete an `(m+1)`-th full set (either because we run out of rolls or don't see all `k` distinct values in the remaining rolls), then there must be at least one value `y \in \{1, ..., k\}` that is missing from the rolls available for the `(m+1)`-th set. In this scenario, any sequence of length `m+1` that ends with `y` (e.g., `[1, 1, ..., 1, y]` where `1` appears `m` times) cannot be formed. Thus, the length of the shortest impossible sequence is `m + 1`.

The greedy strategy works by iterating through `rolls`, adding distinct values (within `1` to `k`) to a hash set. Once the hash set contains `k` distinct values, it signifies the completion of one "full set". We then increment a counter for `current_sequence_length` and clear the hash set to start collecting for the next full set.

---

## Complexity Analysis
- **Time Complexity**: `O(N)` where `N` is the length of the `rolls` array. We iterate through the `rolls` array exactly once. Each operation on the hash set (insertion, checking size, clearing) takes `O(1)` on average.
- **Space Complexity**: `O(k)` in the worst case. The `seen_in_current_block` hash set stores at most `k` distinct integer values.
