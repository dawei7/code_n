# Guided Example: Gray Code

We trace the step-by-step bitwise Gray code generation using both direct arithmetic ($G(i) = i \oplus (i \gg 1)$) and iterative reflected doubling:

- **Input:** $n = 2 \implies [0, 1, 3, 2]$
- **Input Extension:** $n = 3 \implies [0, 1, 3, 2, 6, 7, 5, 4]$

This instance demonstrates generating an $n$-bit Gray code sequence where adjacent values differ by exactly one binary bit (Hamming distance 1), cyclic wraparound verification, the XOR half-shift formula ($i \oplus (i \gg 1)$), and iterative mirrored prefix doubling in $O(2^n)$ time.

---

## 1. Instance & Teaching Goal

An $n$-bit Gray code sequence is a sequence of $2^n$ integers where:
1. The first integer is $0$.
2. Every integer appears **at most once** in the sequence.
3. The binary representation of every pair of adjacent integers differs by **exactly one bit** (Hamming distance $= 1$).
4. The binary representation of the first and last integers also differs by exactly one bit (forming a closed Hamiltonian cycle on the $n$-dimensional hypercube).

For $n = 2$, $2^2 = 4$ integers are required:
$$
[0, 1, 3, 2] \implies [00_2, \, 01_2, \, 11_2, \, 10_2]
$$
Differences between adjacent elements:
- $00_2 \to 01_2$: bit 0 flips.
- $01_2 \to 11_2$: bit 1 flips.
- $11_2 \to 10_2$: bit 0 flips.
- $10_2 \to 00_2$ (cyclic wrap): bit 1 flips.

Two elegant paradigms produce this sequence in $O(2^n)$ time:
1. **Direct Formula:** $G(i) = i \oplus (i \gg 1)$ for $i \in [0, 2^n - 1]$.
2. **Reflected Binary Construction:** Generate $n$-bit codes by taking the $(n-1)$-bit sequence and prefixing its reverse with a leading 1 bit.

---

## 2. Conceptual Foundation & Invariants

### Method 1: The Direct Bitwise Formula
For each integer $i \in [0, 2^n - 1]$:
$$
G(i) = i \oplus \lfloor i / 2 \rfloor = i \oplus (i \gg 1)
$$

#### Mathematical Proof of 1-Bit Difference
Let $X = i \oplus (i + 1)$. When adding 1 to binary integer $i$, a trailing run of $t$ consecutive `1`s flips to `0`, and the preceding `0` flips to `1`. Thus, $X$ is a contiguous block of $t + 1$ ones at the low-order bits:
$$
X = \underbrace{00\dots 0}_{\text{prefix}} \, \underbrace{11\dots 1}_{t+1 \text{ bits}}
$$
Computing the XOR difference between consecutive Gray values:
$$
G(i) \oplus G(i+1) = [i \oplus (i \gg 1)] \oplus [(i+1) \oplus ((i+1) \gg 1)] = X \oplus (X \gg 1)
$$
Because shifting $X$ right by 1 shifts the block of ones, XORing $X$ with $(X \gg 1)$ cancels all lower $t$ ones, leaving **strictly one set bit** (at position $t$).
Hence, $G(i)$ and $G(i+1)$ differ at exactly one bit position!

### Method 2: Reflected Doubling
- Start with sequence for $n = 0$: `[0]`.
- For each bit level $k = 0 \dots n - 1$:
  - Take the existing list of length $2^k$.
  - Read the list in reverse order, add $2^k$ (set bit $k$), and append to the list.
  - The list size doubles to $2^{k+1}$.

> **Invariant.** At each step, every consecutive pair and the cyclic end-to-start pair share Hamming distance exactly 1.

### Comparing the Two Paradigms

The two constructions exploit different structure, so their honest comparison is not about speed but about what each one has to prove and what each one can avoid materialising:

| Strategy | Mechanism | Time | Space beyond the returned sequence | Tradeoff |
|:---|:---|:---|:---|:---|
| Direct XOR formula | Evaluates $G(i) = i \oplus (i \gg 1)$ independently for every index $i$ | $O(2^n)$ | $O(1)$ | Values can be produced lazily and in any order, but the one-bit property must be proved algebraically rather than observed. |
| Reflected doubling | At level $k$, appends the reverse of the current prefix with bit $k$ set | $O(2^n)$ | $O(1)$ when the prefix is read backwards by index | The one-bit property is structural and needs only one seam check per level, but the whole sequence must be materialised before the next level begins. |
| Exhaustive Hamiltonian search | Walks vertex-to-vertex moves on the $n$-cube until a closed tour over all $2^n$ vertices is found | Factorial in $2^n$ in the worst case | $O(2^n)$ for the visited set and the partial tour | Correct in principle and usable only for tiny $n$; it also needs an explicit wraparound check on the final vertex. |

---

## 3. Step-by-Step Worked Execution

### Method 1: Direct Bitwise Evaluation for $n = 3$ ($i = 0 \dots 7$)

- **$i = 0$ (`000`):** $0 \oplus (0 \gg 1) = 0 \oplus 0 = 0$ (`000`).
- **$i = 1$ (`001`):** $1 \oplus (1 \gg 1) = 1 \oplus 0 = 1$ (`001`).
- **$i = 2$ (`010`):** $2 \oplus (2 \gg 1) = 2 \oplus 1 = 3$ (`011`).
- **$i = 3$ (`011`):** $3 \oplus (3 \gg 1) = 3 \oplus 1 = 2$ (`010`).
- **$i = 4$ (`100`):** $4 \oplus (4 \gg 1) = 4 \oplus 2 = 6$ (`110`).
- **$i = 5$ (`101`):** $5 \oplus (5 \gg 1) = 5 \oplus 2 = 7$ (`111`).
- **$i = 6$ (`110`):** $6 \oplus (6 \gg 1) = 6 \oplus 3 = 5$ (`101`).
- **$i = 7$ (`111`):** $7 \oplus (7 \gg 1) = 7 \oplus 3 = 4$ (`100`).

Output list: $[0, 1, 3, 2, 6, 7, 5, 4]$.

---

### Method 2: Reflected Construction Trace ($n = 1 \to 2$)
- Level $k = 0$ ($n = 1$, add $2^0 = 1$):
  - Base: `[0]`.
  - Reverse: `[0]`. Add $1 \implies [1]$.
  - Result: `[0, 1]`.
- Level $k = 1$ ($n = 2$, add $2^1 = 2$):
  - Existing: `[0, 1]`.
  - Reverse: `[1, 0]`. Add $2 \implies [1+2, 0+2] = [3, 2]$.
  - Concatenate: `[0, 1] + [3, 2] = [0, 1, 3, 2]`.

Doubling the construction once more at each level reproduces exactly the sequence the direct formula produced, and the table records the one adjacency the doubling creates from scratch:

| Level $k$ | Sequence before doubling $S_k$ | Reverse of $S_k$ | Offset added $2^k$ | Appended half | New sequence $S_{k+1}$ | Seam pair and differing bit |
|:---:|---|---|:---:|---|---|---|
| 0 | `[0]` | `[0]` | 1 | `[1]` | `[0, 1]` | `0` vs `1` — bit 0 |
| 1 | `[0, 1]` | `[1, 0]` | 2 | `[3, 2]` | `[0, 1, 3, 2]` | `01` vs `11` — bit 1 |
| 2 | `[0, 1, 3, 2]` | `[2, 3, 1, 0]` | 4 | `[6, 7, 5, 4]` | `[0, 1, 3, 2, 6, 7, 5, 4]` | `010` vs `110` — bit 2 |
| 3 | `[0, 1, 3, 2, 6, 7, 5, 4]` | `[4, 5, 7, 6, 2, 3, 1, 0]` | 8 | `[12, 13, 15, 14, 10, 11, 9, 8]` | `[0, 1, 3, 2, 6, 7, 5, 4, 12, 13, 15, 14, 10, 11, 9, 8]` | `0100` vs `1100` — bit 3 |

The **seam pair** is the junction where the reversed, offset copy meets the original prefix. It is the only adjacency the doubling introduces that was not already present in $S_k$: adjacencies strictly inside the first half are inherited unchanged, and adjacencies strictly inside the second half are inherited from the reverse of $S_k$. One seam check per level therefore accounts for the entire new sequence.

---

## 4. Complete Execution Trace

| Index $i$ | Binary $i$ | Half Shift $i \gg 1$ | XOR Calculation | Result $G(i)$ | Binary $G(i)$ | Bit Flipped from Prior |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | `000` | `000` | $0 \oplus 0$ | **0** | `000` | Start |
| 1 | `001` | `000` | $1 \oplus 0$ | **1** | `001` | Bit 0 |
| 2 | `010` | `001` | $2 \oplus 1$ | **3** | `011` | Bit 1 |
| 3 | `011` | `001` | $3 \oplus 1$ | **2** | `010` | Bit 0 |
| 4 | `100` | `010` | $4 \oplus 2$ | **6** | `110` | Bit 2 |
| 5 | `101` | `010` | $5 \oplus 2$ | **7** | `111` | Bit 0 |
| 6 | `110` | `011` | $6 \oplus 3$ | **5** | `101` | Bit 1 |
| 7 | `111` | `011` | $7 \oplus 3$ | **4** | `100` | Bit 0 |
| Wrap ($7 \to 0$) | - | - | $4 \oplus 0 = 4$ | - | `100` vs `000` | Bit 2 (Cycle Valid) |

---

## 5. Algorithmic Correctness

**Soundness.** The transformation $G(i) = i \oplus (i \gg 1)$ is an invertible bijection on the integers $[0, 2^n - 1]$. The difference between any two consecutive values $G(i) \oplus G(i+1) = X \oplus (X \gg 1)$ evaluates to a single power of 2, guaranteeing that every consecutive pair has Hamming distance 1.

**Completeness.** There are $2^n$ distinct index inputs $i \in [0, 2^n - 1]$. Because the mapping is bijective, it produces exactly $2^n$ distinct integers spanning the entire range $[0, 2^n - 1]$ without repetition.

---

## 6. Traps This Instance Exposes

The boundaries below decide whether a construction is accepted, and each one is checked against the instance values traced above:

| Boundary | Instance | Concrete outcome | Why it stays correct |
|:---|:---|:---|:---|
| Smallest legal width | $n = 1$ | `[0, 1]` | The forward step and the wraparound step are the same pair: `0` and `1` differ only in bit 0, so the two-vertex cycle closes. |
| Wraparound closure | $n = 3$, last versus first | `4` versus `0`, that is `100` versus `000` | $G(7) \oplus G(0) = 4 \oplus 0 = 4 = 2^2$, a single set bit at position 2. |
| Largest legal width | $n = 16$ | $2^{16} = 65{,}536$ distinct values covering $[0, 65{,}535]$ | The last index $i = 65{,}535$ gives $65{,}535 \oplus 32{,}767 = 32{,}768$, which differs from `0` only in bit 15, so the cycle still closes at the ceiling. |
| Numeric order is not the invariant | $n = 3$, $i = 3$ | Value `2` follows value `3` | The sequence decreases numerically at that step; adjacency is defined by Hamming distance, so any scan that looks for the next larger value is invalid. |
| No repeats permitted | $n = 2$ | `[0, 1, 3, 2]` | The map $i \mapsto i \oplus (i \gg 1)$ is invertible on $[0, 2^n - 1]$, so the $2^n$ indices yield $2^n$ distinct values and none repeats. |
| Valid sequences are not unique | $n = 2$ | `[0, 1, 3, 2]` and `[0, 2, 3, 1]` | Both trace Hamiltonian cycles of the four-vertex hypercube, `00`–`01`–`11`–`10` and `00`–`10`–`11`–`01`; the judge accepts either, so a fixed expected list must not be assumed. |

- **Bitwise Precedence in Python:** Writing `i ^ i >> 1` evaluates `>>` before `^`, so `i ^ (i >> 1)` is correct. Writing explicit parentheses prevents operator precedence bugs.
- **Multiple Valid Gray Codes:** Gray codes are not unique; any Hamiltonian cycle on the hypercube is valid. Both the direct formula and reflected doubling produce valid sequences accepted by LeetCode.
- **Memory Scaling:** For $n = 16$, the sequence contains $2^{16} = 65{,}536$ elements. The direct list comprehension `[i ^ (i >> 1) for i in range(1 << n)]` constructs the sequence in linear time without stack recursion.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(2^n)$. Generating each of the $2^n$ integers takes $O(1)$ bitwise operations.
- **Auxiliary Space Complexity:** $O(1)$ beyond the returned output list of size $2^n$.
