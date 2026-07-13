# Shuffle an Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 384 |
| Difficulty | Medium |
| Topics | Array, Math, Design, Randomized |
| Official Link | [LeetCode](https://leetcode.com/problems/shuffle-an-array/) |

## Problem Description
### Goal
Construct an object from an integer array whose elements are unique, and preserve an immutable copy of its original order. `shuffle()` returns a random permutation of all positions, with every possible permutation equally likely.

`reset()` restores and returns the original ordering exactly as supplied at construction. Repeated shuffle and reset calls operate on the same object without corrupting that baseline, and returned arrays must contain the complete original multiset. Use an unbiased shuffling process rather than repeatedly choosing positions in a way that gives some permutations greater probability.

### Function Contract
**Inputs**

- `nums`: the initial integer array
- `operations`: for the app adapter, a chronological list containing `"shuffle"` and `"reset"`

**Return value**

- The app adapter returns one array for each operation. A reset returns the initial order; a shuffle returns a uniformly random permutation. Native LeetCode invokes the corresponding methods directly.

### Examples
**Example 1**

- Input: `nums = [1,2,3], operations = ["shuffle","reset"]`
- Output: one valid result is `[[2,3,1],[1,2,3]]`

**Example 2**

- Input: `nums = [5], operations = ["shuffle","reset","shuffle"]`
- Output: `[[5],[5],[5]]`

**Example 3**

- Input: `nums = [1,1,2], operations = ["shuffle"]`
- Output: one valid result is `[[1,2,1]]`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Preserve the initial configuration**

Store a private copy of `nums` at construction. A reset returns a new copy of this snapshot, so neither a caller's later mutation nor a previous shuffle can alter the required original order.

**Commit one position at a time**

To shuffle, copy the original array and process positions from left to right. At position $i$, choose an index uniformly from the still-uncommitted range $[i,n-1]$ and swap its value into position $i$. This is the Fisher-Yates shuffle.

**Why every permutation has equal probability**

Any target permutation requires one particular choice among `n` candidates for position zero, then one among $n - 1$ for position one, continuing to the final forced choice. Its probability is therefore $1 / n \cdot 1 / (n - 1) \cdot \ldots \cdot 1 = 1 / n!$. Every permutation follows exactly one such choice sequence, so none is favored.

**Validate structure without prescribing randomness**

A shuffle is allowed to return the original order, especially for short arrays. The package checks that each shuffle preserves all values and multiplicities and that each reset exactly restores the snapshot; the Fisher-Yates selection rule supplies the uniformity guarantee.

#### Complexity detail

For an array of length `n`, either public operation copies `n` values. Shuffle also performs $n - 1$ constant-time random choices and swaps, so both operations take $O(n)$ time and return $O(n)$ output space. The object retains an additional $O(n)$ snapshot.

#### Alternatives and edge cases

- **Built-in shuffle on a fresh copy:** is concise and normally implements an equivalent linear-time algorithm, but hides the uniformity argument.
- **Repeatedly choose and remove from a shrinking list:** can be uniform, but middle removals make it $O(n^2)$.
- **Random-key sorting:** costs $O(n \log n)$ and can introduce bias when random keys collide.
- A one-element array has exactly one permutation.
- Duplicate values must preserve their full multiplicities even though several position permutations look identical.
- A shuffle may legally equal the original array.
- Reset must return the original order after any number of shuffles and should not expose mutable internal storage.

</details>
