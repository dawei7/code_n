## Description

You are given an integer array `arr`.

In one move, you can select a **palindromic** subarray $\text{arr}[i], arr[i + 1], ..., \text{arr}[j]$ where $i \le j$, and remove that subarray from the given array. Note that after removing a subarray, the elements on the left and on the right of that subarray move to fill the gap left by the removal.

Return *the minimum number of moves needed to remove all numbers from the array*.
### Function Contract

### Inputs

- `arr`: A nonempty list of integers.

A **subarray** is contiguous. A selected subarray is **palindromic** when its values read identically from left to right and from right to left. A one-element subarray therefore qualifies. Each removal changes which surviving values are adjacent before the next move.

### Return value

Return the smallest number of valid palindromic-subarray removals that leaves `arr` empty.

### Examples

#### Example 1

- **Input:** `arr = [1,2]`
- **Output:** `2`
#### Example 2

- **Input:** `arr = [1,3,4,1,5]`
- **Output:** `3`
- **Explanation:** Remove [4] then remove [1,3,1] then remove [5].
### Constraints

- $1 \le \text{arr.length} \le 100$

- $1 \le \text{arr}[i] \le 20$