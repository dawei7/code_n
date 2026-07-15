# Odd Even Jump

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 975 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Stack, Sorting, Monotonic Stack, Ordered Set |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/odd-even-jump/) |

## Problem Description

### Goal

Given an integer array `arr`, consider a sequence of forward jumps from a chosen starting index. The first, third, fifth, and subsequent alternating jumps are odd-numbered jumps; the second, fourth, sixth, and remaining alternating jumps are even-numbered jumps. The parity describes the jump count, not an array index.

From index `i`, every destination `j` must satisfy $i<j$. On an odd-numbered jump, choose a destination whose value is at least `arr[i]`; among all legal values, its value must be the smallest, and a tie is resolved by choosing the smallest destination index. On an even-numbered jump, choose a value at most `arr[i]`; take the largest legal value, again breaking ties toward the smallest index. A required jump may have no legal destination.

A starting index is good when this forced sequence can reach the final index. Reaching it with zero jumps is allowed, so the final index is always good. Return the number of good starting indices.

### Function Contract

**Inputs**

- `arr`: a list of $N$ integers, where $1 \le N \le 2\cdot10^4$ and $0 \le \texttt{arr[i]} < 10^5$.

For each index $i$, let $H_i$ be its forced odd-jump destination and $L_i$ its forced even-jump destination, or let either be absent when no legal destination exists.

**Return value**

- The number of starting indices from which the prescribed alternating jumps can reach index $N-1$.

### Examples

**Example 1**

- Input: `arr = [10, 13, 12, 14, 15]`
- Output: `2`
- Explanation: indices `3` and `4` are the only good starts.

**Example 2**

- Input: `arr = [2, 3, 1, 1, 4]`
- Output: `3`
- Explanation: indices `1`, `3`, and `4` can reach the end. Equal values at indices `2` and `3` demonstrate the smallest-index tie rule.

**Example 3**

- Input: `arr = [5, 1, 3, 4, 2]`
- Output: `3`
- Explanation: the good starting indices are `1`, `2`, and `4`.

### Required Complexity

- **Time:** $O(N\log N)$
- **Space:** $O(N)$

<details>
<summary>Approach</summary>

#### General

**Separate jump selection from reachability:** Once $H_i$ and $L_i$ are known, no choices remain. Define `odd[i]` to mean that index `i` reaches the end when its next jump is odd, and define `even[i]` analogously. Then `odd[i] = even[H_i]` when $H_i$ exists, while `even[i] = odd[L_i]` when $L_i$ exists. Both states are true at the final index.

**Build next-higher destinations:** Sort indices by `(arr[i], i)`. Values then appear in ascending order and equal values in ascending index order. Scan this order with a stack of unresolved indices. Whenever the current index is larger than the stack top, it is the smallest legal forward index for that top among the smallest eligible values, so pop and record it. Repeating the pop resolves every index for which the current item is the required $H_i$.

**Reverse the value order for next-lower destinations:** Apply the identical stack procedure after sorting by `(-arr[i], i)`. Descending values make the first resolvable value the largest value not exceeding the source, and the ascending index tie key again selects the smallest legal destination. This constructs every $L_i$.

**Evaluate from right to left:** All jumps move to larger indices, so when processing `i` in reverse, the destination states have already been computed. The two recurrences therefore determine both states without recursion. Counting true entries in `odd` gives precisely the good starting indices because the first jump is odd.

#### Complexity detail

Sorting two index lists costs $O(N\log N)$ time. Each index is pushed and popped at most once in each monotonic-stack pass, and the dynamic program is linear. The destination arrays, stacks, sorted indices, and two state arrays use $O(N)$ space.

#### Alternatives and edge cases

- **Ordered map while scanning right to left:** Ceiling and floor queries can find $H_i$ and $L_i$ in $O(\log N)$ per index, also giving $O(N\log N)$ time, but Python has no built-in balanced search tree.
- **Scan every suffix:** Directly searching all later indices implements the tie rules transparently but requires $O(N^2)$ time.
- **Final index:** It is good without making any jump, which supplies both dynamic-programming base states.
- **Duplicate values:** Sorting equal values by ascending index is essential; a different tie order can select a later duplicate illegally.
- **Missing destination:** If the required odd or even destination does not exist, that state is false even if a jump of the opposite parity would have been possible.

</details>
