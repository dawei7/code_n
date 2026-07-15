# Maximum Equal Frequency

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1224 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-equal-frequency/) |

## Problem Description

### Goal

Given an array of positive integers `nums`, consider a prefix ending at any position. That prefix is valid when exactly one element can be removed so that every number still present in the prefix occurs the same number of times.

Return the length of the longest valid prefix. The removed element is one occurrence at one index, not every occurrence of its value; a prefix of length one is valid because removing its only element leaves no unequal frequencies.

### Function Contract

**Inputs**

- `nums`: An array of length $n$, where $1\le n\le10^5$ and $1\le\texttt{nums[i]}\le10^5$.

**Return value**

- The maximum prefix length for which removing exactly one element makes all remaining positive frequencies equal.

### Examples

**Example 1**

- Input: `nums = [2,2,1,1,5,3,3,5]`
- Output: `7`

In the first seven elements, removing `5` leaves `1`, `2`, and `3` with frequency two. The full length-eight prefix cannot be repaired by one removal.

**Example 2**

- Input: `nums = [1,1,1,2,2,2,3,3,3,4,4,4,5]`
- Output: `13`

Removing the single `5` leaves four values that each occur three times.

**Example 3**

- Input: `nums = [1,1,1,2,2,2]`
- Output: `5`

For the first five elements, removing one `1` leaves both values with frequency two.

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Maintain counts at two levels.** One hash map stores each value's current occurrence count. A second map stores how many distinct values currently have each frequency. When a new array element arrives, decrement the bucket for its old positive frequency, increment its value count, and increment the bucket for the new frequency. Also retain the maximum current frequency $M$.

**Recognize the only repairable frequency shapes.** Let the current prefix length be $\ell$, and let $F_r$ be the number of distinct values whose frequency is $r$. Exactly one removal succeeds only in one of three configurations:

- $M=1$, so every value is a singleton and any one may be removed.
- $M F_M=\ell-1$, so all but one occurrence belong to frequency-$M$ groups and the remaining value is a singleton to remove.
- $(M-1)(F_{M-1}+1)=\ell-1$, so exactly one value has frequency $M$ and removing one of its occurrences makes every group have frequency $M-1$.

Whenever one condition holds, record $\ell$ as the latest valid prefix.

**Why no other shape can work.** One removal changes only one value's frequency, and changes it by exactly one (or removes a singleton entirely). Therefore all untouched values must already share a frequency, while the changed value must be either a singleton or exactly one occurrence above that common frequency. The three tests enumerate those possibilities, so rejecting every other frequency distribution is sound.

#### Complexity detail

Each of the $n$ elements triggers a constant expected number of hash-map updates and condition checks, giving $O(n)$ expected time. The maps contain at most $n$ value or frequency entries, so space is $O(n)$.

#### Alternatives and edge cases

- **Recount every prefix:** Building frequencies from scratch for each endpoint is correct but takes $O(n^2)$ time.
- **Try every removal explicitly:** Recomputing the remaining frequency multiset for every index adds another unnecessary factor.
- **All singleton values:** Every prefix is valid because removing any element leaves all remaining frequencies equal to one.
- **One distinct value:** Every prefix is valid; remove one occurrence and the sole remaining positive frequency is still uniform.
- **One singleton among equal groups:** Remove the singleton itself rather than lowering one of the larger groups.
- **One overfull group:** Remove an occurrence from the unique group at frequency $M$.
- **Exactly one removal:** A prefix whose frequencies are already equal may still be valid only if one removal preserves equality, as covered by the stated shapes.

</details>
