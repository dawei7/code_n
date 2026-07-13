# Random Pick Index

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 398 |
| Difficulty | Medium |
| Topics | Hash Table, Math, Reservoir Sampling, Randomized |
| Official Link | [LeetCode](https://leetcode.com/problems/random-pick-index/) |

## Problem Description
### Goal
Construct a selector from an integer array that may contain duplicate values. For each `pick(target)` call, the target is guaranteed to occur, and the method must return one zero-based index whose stored value equals that target.

Choose uniformly among all matching positions, so every occurrence of the requested value has equal probability on each call. Repeated calls make fresh selections without consuming, rearranging, or modifying positions. Equal values at different indices remain distinct candidates. The app adapter supplies a sequence of targets and returns selected indices, while the native object exposes one stateful random call at a time.

### Function Contract
**Inputs**

- `nums`: the stored integer array
- `targets`: for the app adapter, the chronological target values passed to successive pick operations

**Return value**

- The app adapter returns one valid randomly selected index for each target. Native LeetCode calls `pick(target)` separately.

### Examples
**Example 1**

- Input: `nums = [1,2,3,3,3], targets = [3,1,3]`
- Output: one valid result is `[2,0,4]`

**Example 2**

- Input: `nums = [7], targets = [7,7]`
- Output: `[0,0]`

**Example 3**

- Input: `nums = [-1,4,-1], targets = [-1,4]`
- Output: one valid result is `[2,1]`

### Required Complexity

- **Time:** $O(n + q)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Index every occurrence during initialization**

Scan `nums` once and append each position to a list keyed by its value. Occurrences remain separate even when their values are equal, which is essential because the contract assigns probability to indices, not merely to distinct values.

**Choose uniformly within one target's index list**

For a pick, retrieve the target's stored positions and choose one list element uniformly at random. If there are `c` occurrences, every matching array index occupies exactly one of the `c` equally likely list positions and therefore has probability $1 / c$.

**Judge random output semantically**

A finite run cannot establish a distribution and should not require a predetermined random sequence. The package verifies that each returned integer is in bounds and that `nums[index]` equals its corresponding target. The uniform-list-choice implementation provides the probability guarantee.

**Why preprocessing fits repeated picks**

Construction pays for one complete scan, after which each query performs only a dictionary lookup and random choice. No prior random result changes the stored occurrence lists, so all picks remain independent and use the same correct candidate set.

#### Complexity detail

Let `n` be the array length and `q` the number of app-adapter picks. Building the map takes $O(n)$ time and stores exactly `n` indices. Each pick is $O(1)$, giving $O(n + q)$ total time and $O(n)$ space.

#### Alternatives and edge cases

- **Reservoir sampling per pick:** uses $O(1)$ extra storage and selects occurrences uniformly, but scans all `n` values for every query.
- **Collect matching indices per pick:** is simple but repeatedly allocates and scans, taking $O(n)$ time and space per call.
- **Choose a random array index until it matches:** can be arbitrarily slow when the target is rare.
- A target with one occurrence always returns its sole index.
- Duplicate values at different positions must all remain eligible.
- Negative and zero values work as ordinary dictionary keys.
- Repeated calls for the same target must not remove or favor previous choices.

</details>
