# Remove Element

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 27 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Two Pointers |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/remove-element/) |

## Problem Description
### Goal
Given an integer array `nums` and a value `val`, remove every occurrence of that value in place. The array's physical length need not shrink; instead, place all retained values in a prefix and treat positions beyond that prefix as irrelevant.

The native method returns the number `k` of retained elements, and its first `k` entries may appear in any order. The app-friendly contract uses a stable compaction and returns the retained prefix itself for direct checking. An empty array or an array containing only `val` therefore produces an empty retained result.

### Function Contract
**Inputs**

- `nums`: `List[int]`
- `val`: `int`

**Return value**

A `List[int]` containing all values unequal to `val` in original order. The platform artifact writes this prefix into `nums` and returns its length.

### Examples
**Example 1**

- Input: `nums = [3, 2, 2, 3], val = 3`
- Output: `[2, 2]`

**Example 2**

- Input: `nums = [0, 1, 2, 2, 3, 0, 4, 2], val = 2`
- Output: `[0, 1, 3, 0, 4]`

**Example 3**

- Input: `nums = [], val = 1`
- Output: `[]`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Write only values that survive the filter**

Set `write = 0` and scan every value. When a value differs from `val`, assign it to `nums[write]` and increment `write`. Matching values cause no write. The app returns `nums[:write]`; the official method returns `write` after the identical in-place compaction.

**The prefix is a stable filter of everything already read**

Before each read step, `nums[:write]` contains exactly the non-target values from the processed original prefix, in their original order. Writing the next retained value extends this prefix; skipping a target leaves it unchanged. Since `write` never exceeds the read index, an in-place assignment cannot overwrite an element that has not yet been inspected.

**Trace a case where reading moves ahead of writing**

For `[3, 2, 2, 3]` with target 3, skip the first value, write the two 2s into positions 0 and 1, then skip the final 3. The retained prefix is `[2, 2]` and its official length is 2.

**The write pointer counts retained values**

Each read position is classified exactly once. A target value leaves the write pointer unchanged; a non-target is copied to that boundary and advances it. Thus the prefix before `write` contains all and only retained values seen so far, in their original order.

When the read scan ends, every source value has been classified. No target can appear in the prefix and no non-target can be missing, so `write` is both the correct new length and the boundary of the required retained multiset.

#### Complexity detail

Every array element is read once and every retained value is written at most once, so time is $O(n)$. The two-pointer compaction uses $O(1)$ auxiliary space. The app returns the retained prefix for direct testing; the native LeetCode method instead returns its length.

#### Alternatives and edge cases

- **Swap targets with the end:** also uses linear time and constant space and can reduce writes when targets are rare, but does not preserve order.
- **Delete matching array elements:** repeated shifts can require $O(n^2)$ time.
- **Build a separate filtered list:** is simple but uses $O(n)$ auxiliary space; repeated concatenation may also become quadratic.
- An empty array and an array containing only `val` both produce retained count zero. If `val` is absent, every element remains in its original position.
- The official judge permits arbitrary retained order, but stable compaction gives deterministic app output with no complexity penalty.

</details>
