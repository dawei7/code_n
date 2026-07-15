# Create Target Array in the Given Order

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1389 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/create-target-array-in-the-given-order/) |

## Problem Description

### Goal

Two arrays, `nums` and `index`, have the same length. Start with an empty target array and process their entries from left to right. At step `i`, insert `nums[i]` at position `index[i]` in the target as it exists at that moment.

The supplied position is always valid for the current target, so $0 \le \texttt{index[i]} \le i$. Inserting before an existing position shifts that element and every later element one place to the right. Return the target after every insertion has been performed.

### Function Contract

**Inputs**

- `nums`: an integer array of length $n$, with $1 \le n \le 100$.
- `index`: an array of $n$ insertion positions, where `index[i]` is valid after the first `i` operations.

**Return value**

- The final array produced by applying the insertions in input order.

### Examples

**Example 1**

- Input: `nums = [0,1,2,3,4], index = [0,1,2,2,1]`
- Output: `[0,4,1,3,2]`

**Example 2**

- Input: `nums = [1,2,3,4,0], index = [0,1,2,3,0]`
- Output: `[0,1,2,3,4]`

**Example 3**

- Input: `nums = [1], index = [0]`
- Output: `[1]`

### Required Complexity

- **Time:** $O(n^2)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Simulate the evolving array.** Initialize an empty list. For each paired value and position, call the list insertion operation at that position. The list implementation shifts the existing suffix right and places the new value in the opened slot.

After step `i`, the maintained list is exactly the target defined by the first `i + 1` operations: the induction base inserts the first value at position zero, and each later operation applies the specified insertion to the already-correct prefix result. Therefore the final list has the required order.

The positions refer to the current partial target, not to fixed locations in the final array. Processing operations sequentially is what preserves that distinction.

#### Complexity detail

One insertion can shift $O(n)$ existing elements. Across $n$ insertions, worst-case time is $O(n^2)$. The target list contains $n$ values and uses $O(n)$ space.

#### Alternatives and edge cases

- **Manual suffix shifting:** Append one slot and move elements right explicitly. It has the same $O(n^2)$ bound but more indexing logic.
- **Repeated rebuilding during shifts:** Rescan or copy the whole partial array for every moved element. It remains correct but can take $O(n^3)$ time.
- **Insert at zero:** Every existing element shifts right.
- **Insert at current length:** The operation is an append and shifts nothing.
- **Repeated positions:** Each position is interpreted against the newly updated target.
- **Repeated values:** Values need not be distinct; insertion order still determines occurrence positions.
- **Single value:** Its only valid insertion position is zero.

</details>
