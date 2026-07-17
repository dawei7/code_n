# Decode XORed Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1720 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/decode-xored-array/) |

## Problem Description

### Goal

A hidden array `arr` contains $n$ non-negative integers. It was transformed into an array `encoded` of length $n-1$ by setting `encoded[i] = arr[i] XOR arr[i + 1]` for every adjacent pair. You are given this encoded data together with `first`, the known value of `arr[0]`.

Reconstruct and return the entire original array. The supplied values always describe one valid answer, and knowing the first element makes that answer unique.

### Function Contract

**Inputs**

- `encoded`: an integer array of length $n-1$, where $2 \le n \le 10^4$ and $0 \le \texttt{encoded[i]} \le 10^5$.
- `first`: the first original element, where $0 \le \texttt{first} \le 10^5$.

**Return value**

- Return the unique original array `arr` of length $n$.

### Examples

**Example 1**

- Input: `encoded = [1,2,3], first = 1`
- Output: `[1,0,2,1]`
- Explanation: The adjacent XOR values are `1 XOR 0 = 1`, `0 XOR 2 = 2`, and `2 XOR 1 = 3`.

**Example 2**

- Input: `encoded = [6,2,7,3], first = 4`
- Output: `[4,2,0,7,4]`
- Explanation: Each next element is recovered from the previous decoded value and the corresponding encoded value.

**Example 3**

- Input: `encoded = [0], first = 100000`
- Output: `[100000,100000]`
- Explanation: Two equal values have XOR zero.

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Invert one adjacent XOR at a time**

XOR is its own inverse: if `encoded[i] = arr[i] XOR arr[i + 1]`, XORing both sides with `arr[i]` cancels that known value and gives `arr[i + 1] = arr[i] XOR encoded[i]`. Begin the decoded array with `first`, which supplies the recurrence's initial value.

**Extend the unique decoded prefix**

Scan `encoded` from left to right. At each step, the last decoded value is `arr[i]`, so append `decoded[-1] XOR encoded[i]`. By induction, every appended value is the only value that can satisfy the current adjacent equation. Once every encoded entry has been consumed, the result contains all $n$ original elements and recreates every supplied XOR.

#### Complexity detail

The algorithm performs one constant-time XOR and one append for each of the $n-1$ encoded values, so it takes $O(n)$ time. The returned decoded array contains $n$ integers and therefore uses $O(n)$ space; beyond that required output, the algorithm uses $O(1)$ auxiliary state.

#### Alternatives and edge cases

- **Recompute each prefix:** Deriving `arr[i]` by XORing `first` with `encoded[0:i]` independently is correct but repeats work and takes $O(n^2)$ time.
- **In-place reuse of `encoded`:** The input storage can be overwritten with decoded suffix values, but a separate returned array preserves the caller's input and makes the leading `first` explicit.
- **Zero encoded value:** An encoded zero means the two adjacent original values are equal.
- **Zero first value:** The recurrence is unchanged; XOR has no special failure case at zero.
- **Maximum values:** XOR may produce values beyond either individual operand's decimal pattern, but ordinary non-negative integer XOR remains exact.

</details>
