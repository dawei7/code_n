# Reducing Dishes

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1402 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/reducing-dishes/) |

## Problem Description

### Goal

A chef has several dishes, and `satisfaction[i]` is the satisfaction value of one dish. The chef may discard any dishes and may arrange the selected dishes in any order before cooking them. Every selected dish takes one unit of time.

If a dish with satisfaction $s$ finishes at time $t$, it contributes $t \cdot s$ to the like-time coefficient. Cooking starts at time one for the first selected dish. Return the maximum total like-time coefficient possible; selecting no dishes is allowed and gives zero.

### Function Contract

**Inputs**

- `satisfaction`: an array of $n$ integers, where $1 \le n \le 500$ and $-1000 \le \texttt{satisfaction[i]} \le 1000$.

**Return value**

- The greatest sum of completion-time-weighted satisfaction over any chosen subset and ordering.

### Examples

**Example 1**

- Input: `satisfaction = [-1,-8,0,5,-9]`
- Output: `14`

**Example 2**

- Input: `satisfaction = [4,3,2]`
- Output: `20`

**Example 3**

- Input: `satisfaction = [-1,-4,-5]`
- Output: `0`

### Required Complexity

- **Time:** $O(n\log n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Fix the order before choosing the prefix.** For any selected set, placing lower satisfaction earlier and higher satisfaction later maximizes the weighted sum: swapping an inverted adjacent pair increases or preserves the total. Sort the values, then inspect them from greatest to least while deciding whether to prepend each one.

Let `suffix_sum` be the sum of dishes already selected from the high end. Prepending a new value delays every selected dish by one time unit and places the new dish at time one, so the total increases by `suffix_sum + value`. Accept the value exactly when this new cumulative sum is positive, then add it to the answer.

Once `suffix_sum + value` is nonpositive, every unexamined value is no greater. Prepending any of them cannot help, and including several makes their successive cumulative contributions no better. Therefore stopping at that point gives the optimal suffix of the sorted array. If the first cumulative sum is nonpositive, choosing nothing correctly yields zero.

#### Complexity detail

Sorting $n$ values takes $O(n\log n)$ time, and the reverse scan takes $O(n)$. Creating a sorted copy uses $O(n)$ space; an in-place sort can reduce auxiliary storage according to the language's sorting implementation.

#### Alternatives and edge cases

- **Dynamic programming by chosen count:** Track the best coefficient after each dish and count. It is correct but costs $O(n^2)$ time and $O(n)$ space.
- **Repeated maximum extraction:** Build descending order by repeatedly finding and removing the maximum. It preserves the greedy result but takes $O(n^2)$ time.
- **All negative:** Select no dishes and return zero.
- **All positive:** Select every dish in ascending satisfaction order.
- **Zero values:** A zero can still be useful when it delays a positive selected suffix.
- **Negative but useful:** A negative dish should be included when the current suffix sum is large enough to make its cumulative contribution positive.
- **Nonpositive cumulative sum:** Equality at zero gives no improvement, and smaller remaining values cannot create a later gain.

</details>
