# Distribute Candies

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 575 |
| Difficulty | Easy |
| Topics | Array, Hash Table |
| Official Link | [LeetCode](https://leetcode.com/problems/distribute-candies/) |

## Problem Description
### Goal
Alice has `n` candies, where `candyType[i]` identifies the type of the `i`th candy and `n` is even. Following her doctor's advice, she may eat only $n / 2$ of the candies, but she may choose which individual candies make up that allowance.

Return the maximum number of different types of candies Alice can eat while still respecting the $n / 2$ limit. Multiple candies of one type occupy multiple positions in her allowance but increase the number of different types only once.

### Function Contract
**Inputs**

- `candyType: list[int]`: an even-length list where equal integers represent candies of the same type

**Return value**

- An integer giving the maximum possible number of distinct types among exactly `len(candyType) / 2` chosen candies

### Examples
**Example 1**

- Input: `candyType = [1, 1, 2, 2, 3, 3]`
- Output: `3`

**Example 2**

- Input: `candyType = [1, 1, 2, 3]`
- Output: `2`

**Example 3**

- Input: `candyType = [6, 6, 6, 6]`
- Output: `1`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Two independent limits determine the answer**

Let `d` be the number of distinct values in `candyType`. The sibling cannot receive more than `d` distinct types because no other types exist. She also receives exactly $n / 2$ candies, so she cannot represent more than $n / 2$ types.

**Both limits can be attained**

If $d \le n / 2$, choose one candy of every type and fill the remaining positions with arbitrary duplicates; all `d` types are represented. If $d > n / 2$, choose one candy from any $n / 2$ different types. Thus the maximum is exactly $\min(d, n / 2)$.

**Count types with a set**

Insert every candy value into a set, then return the smaller of the set size and half the list length. No arrangement or simulation of the other sibling's share is needed.

#### Complexity detail

For `n` candies, building the hash set takes $O(n)$ expected time and stores at most `n` distinct values, so the extra space is $O(n)$.

#### Alternatives and edge cases

- **Sort then count changes:** also finds the number of types but costs $O(n \log n)$ time and may mutate the input.
- **Linear list of discovered types:** is correct, but membership checks can take $O(n)$ apiece and make the full scan $O(n^2)$.
- **Frequency map:** works in $O(n)$ expected time, but the counts themselves are unnecessary.
- **All candies distinct:** the half-share capacity is the binding limit.
- **All candies identical:** exactly one type can be represented.
- **Many duplicates but enough capacity:** one candy of each existing type can be selected before filling the remaining share.
- **Negative type identifiers:** are ordinary hashable values and require no special handling.

</details>
