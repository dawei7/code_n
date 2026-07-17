# Decode XORed Permutation

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1734 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/decode-xored-permutation/) |

## Problem Description

### Goal

An integer array `perm` is a permutation of the first $n$ positive integers, and $n$ is odd. The permutation was replaced by a length-$(n-1)$ array `encoded`, where each entry is the bitwise XOR of one adjacent pair:

`encoded[i] = perm[i] ^ perm[i + 1]`.

Recover and return the original permutation. The input guarantees $3 \le n < 10^5$, and guarantees that exactly one valid original permutation exists.

### Function Contract

**Inputs**

- `encoded`: a length-$(n-1)$ integer list produced from adjacent entries of a permutation of $1$ through $n$, where $n$ is odd.

**Return value**

- Return the unique original length-$n$ permutation.

### Examples

**Example 1**

- Input: `encoded = [3,1]`
- Output: `[1,2,3]`
- Explanation: The adjacent XOR values are `1 ^ 2 = 3` and `2 ^ 3 = 1`.

**Example 2**

- Input: `encoded = [6,5,4,6]`
- Output: `[2,4,1,5,3]`
- Explanation: XORing every adjacent pair of the returned permutation recreates `encoded`.

**Example 3**

- Input: `encoded = [4,3,1,7]`
- Output: `[5,1,2,3,4]`
- Explanation: The odd length and permutation range determine the otherwise missing first value.

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Recover the XOR of the complete permutation**

Because `perm` contains every integer from $1$ through $n$ exactly once, XORing that entire range gives the XOR of every unknown permutation entry. The order is irrelevant because XOR is associative and commutative.

**Cancel every value except the first**

XOR the encoded entries at odd zero-based indices: `encoded[1] ^ encoded[3] ^ ...`. These entries expand to

$$
(\texttt{perm[1]} \mathbin{\oplus} \texttt{perm[2]})
\mathbin{\oplus} \cdots \mathbin{\oplus}
(\texttt{perm[n-2]} \mathbin{\oplus} \texttt{perm[n-1]}),
$$

so they contain every permutation value except `perm[0]` exactly once. XORing this result with the XOR of $1$ through $n$ cancels all those shared values and leaves `perm[0]`. Odd $n$ is essential: it makes the remaining $n-1$ positions pair up in this pattern.

**Decode every following value**

Once the first value is known, invert the encoding relation from left to right with `perm[i + 1] = perm[i] ^ encoded[i]`. Each recovered value supplies the next one, so one pass reconstructs the unique permutation.

#### Complexity detail

The range XOR, odd-index XOR, and forward reconstruction each perform linear total work, giving $O(n)$ time. The returned permutation contains $n$ integers and therefore uses $O(n)$ space; aside from that required output, the algorithm keeps only constant-size XOR accumulators.

#### Alternatives and edge cases

- **Try every possible first value:** Decoding and validating a permutation for each candidate can take $O(n^2)$ time.
- **Gaussian elimination over bits:** The adjacent XOR equations are linear, but generic elimination ignores the permutation and odd-length structure and is unnecessarily expensive.
- **Smallest legal length:** For $n=3$, the single odd-index encoded entry still identifies the first value correctly.
- **Unordered permutation:** No assumption is made about increasing, decreasing, or random order.
- **Repeated encoded values:** Adjacent XOR results need not be unique even though permutation values are unique.
- **Large integer boundary:** Values up to $n$ participate directly in bitwise XOR without arithmetic overflow in Python.

</details>
