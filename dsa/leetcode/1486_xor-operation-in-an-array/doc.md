# XOR Operation in an Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1486 |
| Difficulty | Easy |
| Topics | Math, Bit Manipulation |
| Official Link | [LeetCode](https://leetcode.com/problems/xor-operation-in-an-array/) |

## Problem Description
### Goal

Given integers `n` and `start`, define a zero-indexed array `nums` of length `n` by

$$
\texttt{nums[i]} = \texttt{start} + 2i
$$

for every $0 \le i < n$. Return the bitwise XOR of all generated elements. The array is conceptual; it does not have to be stored.

The first term is `start`, and every later term is exactly two larger than the preceding term. Include all `n` positions once, combine them with bitwise XOR rather than addition or exponentiation, and return the resulting integer. Because only the aggregate is requested, an implementation may derive it without materializing `nums`.

### Function Contract
**Inputs**

- `n`: the number of generated values, with $1 \le n \le 1000$.
- `start`: the first generated value, with $0 \le \texttt{start} \le 1000$.

**Return value**

Return

$$
\bigoplus_{i=0}^{n-1}(\texttt{start}+2i),
$$

where $\oplus$ denotes bitwise XOR.

### Examples
**Example 1**

- Input: `n = 5, start = 0`
- Generated values: `[0,2,4,6,8]`
- Output: `8`

**Example 2**

- Input: `n = 4, start = 3`
- Generated values: `[3,5,7,9]`
- Output: `8`

### Required Complexity
- **Time:** $O(1)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Separating the shared least-significant bit**

Every term differs from the next by two, so all generated numbers have the same least-significant bit as `start`. Write

$$
\texttt{start}+2i
=
2\left(\left\lfloor\frac{\texttt{start}}{2}\right\rfloor+i\right)
+
(\texttt{start}\bmod 2).
$$

XOR acts independently on each bit. The common low bit survives only when it is XORed an odd number of times. Therefore `low_bit = start & 1` when `n` is odd, and `low_bit = 0` when `n` is even.

**Reducing the higher bits to a consecutive range**

After removing the common low bit and shifting right once, the remaining values are consecutive integers beginning at

$$
a=\left\lfloor\frac{\texttt{start}}{2}\right\rfloor
$$

and ending at $a+n-1$. Let $F(x)$ be the XOR of every integer from zero through $x$, with $F(-1)=0$. The XOR of the desired consecutive range is

$$
F(a-1)\oplus F(a+n-1).
$$

This works because every value below $a$ appears in both prefixes and cancels through $x \oplus x = 0$.

**Using the four-value prefix-XOR cycle**

The prefix XOR has a repeating form determined by $x \bmod 4$:

$$
F(x)=
\begin{cases}
x, & x\bmod 4=0,\\
1, & x\bmod 4=1,\\
x+1, & x\bmod 4=2,\\
0, & x\bmod 4=3.
\end{cases}
$$

Each block of four consecutive integers contributes zero after the bit patterns cancel, which makes these four cases repeat. Consequently, each prefix result is computed with constant arithmetic and one remainder lookup.

**Reassembling the original bit positions**

The consecutive-range XOR represents every bit above the common least-significant bit, so shift it left once. Combine it with `low_bit` using bitwise OR:

```text
(high_bits << 1) | low_bit
```

The shifted portion has zero in bit zero, so OR and XOR would be equivalent at this final combination. The result contains exactly the XOR contribution of every bit of every generated term.

**Why the formula is complete**

The decomposition maps each generated number bijectively into one shared low bit plus one consecutive higher-bit value. Prefix cancellation computes the XOR of all higher parts, and parity computes the XOR of all low parts. Since no bit is omitted or counted twice, recombining the two independent portions gives the requested array XOR.

#### Complexity detail

The algorithm evaluates two constant-case prefix formulas and a fixed number of bitwise operations, independent of `n`. It therefore takes $O(1)$ time and uses $O(1)$ space. No generated array is allocated.

#### Alternatives and edge cases

- **Direct accumulation:** Initialize `result = 0` and XOR `start + 2 * i` for every index. This is simple and correct in $O(n)$ time and $O(1)$ space, but it does not exploit the progression's bit structure.
- **Materialize then reduce:** Build all `n` values and reduce them with XOR. It adds unnecessary $O(n)$ storage to the linear scan.
- **Arithmetic sum:** Addition cannot replace XOR because carries change higher bits; the requested operator is bitwise.
- **One element:** For `n = 1`, both the prefix range and low-bit rule reconstruct `start`.
- **Even number of terms:** The shared least-significant bit cancels completely.
- **Odd number of terms:** The output retains the parity bit of `start`.
- **Even start:** Every generated value is even, so the result's least-significant bit is zero.
- **Odd start:** Every term is odd, but the output is odd only when `n` is odd.
- **Prefix below zero:** Define $F(-1)=0$ so ranges beginning at zero require no special subtraction logic.
- **Operator notation:** In executable code, use the language's bitwise XOR operator, not exponentiation.

</details>
