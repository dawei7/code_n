# XOR Queries of a Subarray

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1310 |
| Difficulty | Medium |
| Topics | Array, Bit Manipulation, Prefix Sum |
| Official Link | [LeetCode](https://leetcode.com/problems/xor-queries-of-a-subarray/) |

## Problem Description
### Goal
A positive-integer array `arr` is accompanied by a list of inclusive index ranges. For each query `[left, right]`, compute the bitwise XOR of every array element in the subarray from `arr[left]` through `arr[right]`.

Return one value per query in the same order as the queries were given. Queries may overlap, repeat, cover one element, or span the entire array; each answer is based on the unchanged original array.

### Function Contract
**Inputs**

- `arr`: an array of $n$ positive integers, where $1\le n\le3\cdot10^4$ and $1\le\texttt{arr[i]}\le10^9$.
- `queries`: an array of $q$ pairs, where $1\le q\le3\cdot10^4$.
- Every query satisfies $0\le\texttt{left}\le\texttt{right}<n$.

**Return value**

An array `answer` of length $q$ such that

$$
\texttt{answer[i]}
=
\texttt{arr[left]}\mathbin{\mathtt{XOR}}\cdots\mathbin{\mathtt{XOR}}\texttt{arr[right]}
$$

for the inclusive range in `queries[i]`.

### Examples
**Example 1**

- Input: `arr = [1,3,4,8]`, `queries = [[0,1],[1,2],[0,3],[3,3]]`
- Output: `[2,7,14,8]`

**Example 2**

- Input: `arr = [4,8,2,10]`, `queries = [[2,3],[1,3],[0,0],[0,3]]`
- Output: `[8,0,4,4]`

**Example 3**

- Input: `arr = [5]`, `queries = [[0,0],[0,0]]`
- Output: `[5,5]`

### Required Complexity
- **Time:** $O(n+q)$
- **Space:** $O(n+q)$

<details>
<summary>Approach</summary>

#### General

**Store XOR prefixes**

Build `prefix` with one extra leading zero, where `prefix[k]` is the XOR of `arr[0]` through `arr[k - 1]`. The update `prefix.append(prefix[-1] ^ value)` constructs all $n+1$ prefix values in one pass.

For a query `[left, right]`, `prefix[right + 1]` contains the desired subarray together with the elements before `left`. XORing it with `prefix[left]` cancels that common earlier prefix because $x\mathbin{\mathtt{XOR}}x=0$ and $0\mathbin{\mathtt{XOR}}y=y$. Thus `prefix[right + 1] ^ prefix[left]` contains exactly the inclusive queried range.

Answering each query with this identity preserves query order and takes constant time after preprocessing. It also handles `left = 0` through the stored zero prefix and a one-element query because every other contribution cancels.

#### Complexity detail

Constructing the prefix array takes $O(n)$ time, and answering all $q$ queries takes $O(q)$ time, for $O(n+q)$ total. The prefix array uses $O(n)$ space and the required answer uses $O(q)$ space, giving $O(n+q)$ including output.

#### Alternatives and edge cases

- **Direct range scan:** XORing each queried subarray independently uses constant auxiliary space but can take $O(nq)$ time when many ranges are long.
- **Segment tree:** Range XOR queries can be answered in $O(\log n)$ after $O(n)$ construction and support updates, but the array is immutable here, so prefix XOR is simpler and faster.
- **Single-element range:** The answer is that element because the two surrounding prefixes cancel.
- **Full-array range:** Use `prefix[n] ^ prefix[0]`, which is the XOR of the whole array.
- **Repeated or overlapping queries:** Each constant-time prefix lookup is independent; no query mutates shared state.
- **XOR cancellation:** Equal values may cancel within a range, so zero is a valid answer even though every input value is positive.

</details>
