# Guided Example: Find Xor-Beauty of Array

## 1. The definition, and why it must collapse

For a 0-indexed array `nums` of length $n$, the *effective value* attached to an ordered triple of indices $(i, j, k)$ with $0 \le i, j, k < n$ is

$$
E(i,j,k) = \bigl(\text{nums}[i] \lor \text{nums}[j]\bigr) \land \text{nums}[k],
$$

where $\lor$ is bitwise OR and $\land$ is bitwise AND. The xor-beauty is the XOR of $E(i,j,k)$ over all $n^3$ ordered triples. Evaluating $n^3$ values is hopeless at the stated limit $n \le 10^{5}$, since $n^3 = 10^{15}$; the lesson below shows that the whole expression collapses to a single pass over the array.

The traced instance is `nums = [1, 4]`, for which $n = 2$ and there are only $n^3 = 8$ triples — small enough to enumerate completely, and rich enough that the two values share no set bit, so every intermediate value is easy to read in binary.

| Index | `nums[index]` | Binary (3 bits) |
|:---:|:---:|:---:|
| 0 | 1 | `001` |
| 1 | 4 | `100` |

## 2. Complete enumeration of the instance

Because $n = 2$, every ordered triple can be listed. The two source indices are OR-ed first, then the result is AND-ed with the third value; both operations act independently on each bit position, so the numbers can be read directly in binary.

| Triple $(i,j,k)$ | `nums[i]` | `nums[j]` | `nums[k]` | Bitwise OR of the first two | Effective value |
|:---:|:---:|:---:|:---:|:---:|:---:|
| (0,0,0) | 1 | 1 | 1 | 1 | 1 |
| (0,0,1) | 1 | 1 | 4 | 1 | 0 |
| (0,1,0) | 1 | 4 | 1 | 5 | 1 |
| (0,1,1) | 1 | 4 | 4 | 5 | 4 |
| (1,0,0) | 4 | 1 | 1 | 5 | 1 |
| (1,0,1) | 4 | 1 | 4 | 5 | 4 |
| (1,1,0) | 4 | 4 | 1 | 4 | 0 |
| (1,1,1) | 4 | 4 | 4 | 4 | 4 |

Chaining the eight effective values with XOR gives

$$
1 \oplus 0 \oplus 1 \oplus 4 \oplus 1 \oplus 4 \oplus 0 \oplus 4 = 5,
$$

so the required answer is 5. The enumeration also exposes the structure that will be exploited: the four triples with $k$ pointing at 4 contribute 0, 4, 4, 4, and the four with $k$ pointing at 1 contribute 1, 0, 1, 0. The answer therefore looks like a parity phenomenon rather than a magnitude phenomenon.

## 3. Bit independence: one independent problem per bit position

OR, AND, and XOR are all applied bit by bit with no interaction between positions, and XOR in particular never carries. That gives the first invariant of the method:

> Bit $b$ of the final answer depends only on bit $b$ of the array elements. No bit position can influence another.

Formally, if the answer's bit $b$ is written $\text{ans}_b$, then

$$
\text{ans}_b = \Bigl( \sum_{i=0}^{n-1}\sum_{j=0}^{n-1}\sum_{k=0}^{n-1} E_b(i,j,k) \Bigr) \bmod 2,
$$

where $E_b(i,j,k) \in \{0,1\}$ is bit $b$ of the effective value of that triple. The sum counts how many triples produce a 1 in that position, and XOR keeps exactly the parity of that count. So the task reduces to: for each bit position, count triples with odd parity.

Within one bit position, the arithmetic of section 1 becomes plain Boolean algebra:

$$
E_b(i,j,k) = \bigl(x_i \lor x_j\bigr) \land x_k,
\qquad x_m = \text{bit } b \text{ of } \text{nums}[m].
$$

## 4. Counting triples per bit position

Fix a bit position $b$ and let

$$
c = \lvert \{\, m : x_m = 1 \,\} \rvert
$$

be the number of array entries whose bit $b$ is set, so that $n - c$ entries have it clear.

| Quantity | Formula | Derivation |
|:---|:---|:---|
| ordered pairs $(i,j)$ with $x_i \lor x_j = 1$ | $n^2 - (n-c)^2 = 2nc - c^2$ | start from all $n^2$ ordered pairs and remove the $(n-c)^2$ pairs in which both entries have bit $b$ clear |
| triples with $E_b = 1$ | $T = c\,(2nc - c^2) = 2nc^2 - c^3$ | the third index $k$ must itself have bit $b$ set, giving $c$ choices for each qualifying pair |

The parity of $T$ is all that survives into the answer:

$$
T = 2nc^2 - c^3 \;\equiv\; -c^3 \;\equiv\; c^3 \;\equiv\; c \pmod 2,
$$

because $2nc^2$ is even and $c^3 \equiv c \pmod 2$ for every non-negative integer $c$. Reading the same fact case by case:

| $c \bmod 2$ | $c^2 \bmod 2$ | $(2n - c) \bmod 2$ | $T \bmod 2$ | Bit $b$ of the answer |
|:---:|:---:|:---:|:---:|:---:|
| 0 (even count) | 0 | 0 | 0 | 0 |
| 1 (odd count) | 1 | 1 | 1 | 1 |

So bit $b$ of the xor-beauty is exactly the parity of the number of array entries with bit $b$ set — which is precisely bit $b$ of the XOR of the whole array. Therefore

$$
\text{xor-beauty}(\text{nums}) = \text{nums}[0] \oplus \text{nums}[1] \oplus \dots \oplus \text{nums}[n-1].
$$

The $n^3$ enumeration and the single accumulator compute the same number.

## 5. Reading the instance bit by bit

For `nums = [1, 4]` we have $n = 2$, and bits above position 2 are clear in both entries. Each row below is one bit position, and the last column must reproduce the binary form of the enumerated answer $5 = 101_2$.

| Bit $b$ | Weight $2^b$ | Entries with the bit set | $c$ | Pairs with OR bit set, $2nc - c^2$ | $T = 2nc^2 - c^3$ | $T \bmod 2$ | Answer bit |
|:---:|:---:|:---|:---:|:---:|:---:|:---:|:---:|
| 0 | 1 | `nums[0] = 1` | 1 | $4 - 1 = 3$ | 3 | 1 | 1 |
| 1 | 2 | none | 0 | 0 | 0 | 0 | 0 |
| 2 | 4 | `nums[1] = 4` | 1 | $4 - 1 = 3$ | 3 | 1 | 1 |
| 3 and above | — | none | 0 | 0 | 0 | 0 | 0 |

Assembling the surviving bits gives $4 + 1 = 5$, matching section 2 exactly. The bit-level view explains *why* the answer is 5 without ever enumerating a triple: at bit 0 there are three triples with the bit set (an odd count, so the bit survives), and at bit 2 there are likewise three.

## 6. Why the enumeration is correct, and where a naive count goes wrong

The derivation rests on three claims, each checkable independently.

1. **Bit decomposition is lossless.** OR, AND, and XOR are bitwise, and XOR is addition in $\mathbb{Z}_2$ per position with no carry, so the XOR of a multiset of integers is determined by the parity of the count of 1s in each position. Nothing is lost when the integer-level statement is replaced by one Boolean statement per bit.
2. **The pair count is exact.** Among the $n^2$ ordered pairs $(i,j)$, exactly $(n-c)^2$ have both entries with bit $b$ clear, because the two choices are independent; every other pair has $x_i \lor x_j = 1$. Ordered pairs are counted with multiplicity, which is what the triple definition requires: $(i,j)$ and $(j,i)$ are different triples even when they contribute the same value.
3. **The parity reduction is exact.** $c^3 \equiv c \pmod 2$ holds for both possible residues, so the $2n$ factor and the square can be discarded. The final criterion depends only on $c \bmod 2$.

The subtle part is step 3 combined with the structure of the formula: the count $T$ grows cubically and is *never* small, yet only its parity matters. An author who tries to compute the xor-beauty by combining counts rather than parities will accumulate large numbers and still have to reduce them modulo 2 — the collapse to one XOR pass is what makes the method linear.

| Claim | What would break without it | Instance that exposes it |
|:---|:---|:---|
| bit positions are independent | a carry-style interaction would make the answer depend on magnitudes | `nums = [1, 2, 3]`, whose answer 0 is invisible in any single-element view |
| the OR pair count is $n^2 - (n-c)^2$ | counting only $\binom{c}{2}$ unordered matching pairs would miss triples where exactly one source holds the bit | triples $(0,1,1)$ and $(1,0,1)$ in the traced instance, where only one source has bit 2 |
| only parity survives | treating a count of 3 as "contributes 3" rather than "contributes 1" would produce the wrong bit at positions 0 and 2 | the traced instance, where both surviving bits have $T = 3$ |
| the third index must hold the bit | ignoring $\text{nums}[k]$ would make every triple with a set source contribute | `nums = [1, 1]`, where OR bit 0 is set for all four pairs but only two triples have $k$ set |

## 7. Boundary instances and their lessons

Each row of this table is an authored case of this package with its required answer, chosen to isolate one edge of the derivation.

| `nums` | Required answer | The edge it isolates |
|:---|:---:|:---|
| `[7]` | 7 | $n = 1$: the only triple is $(0,0,0)$ and its effective value is the single element, so the answer must equal it |
| `[5, 5]` | 0 | a duplicated value cancels: $c$ is even for every set bit, so every bit of the answer is 0 |
| `[1, 2, 3]` | 0 | three distinct values whose XOR is 0; the answer is not obtained from any partial combination of the inputs |
| `[42, 42, 42]` | 42 | odd multiplicity leaves exactly one copy, matching the parity rule |
| `[1, 4]` | 5 | the traced instance: disjoint set bits, and each surviving bit comes from a count of 3 |
| `[1000000000, 1000000000, 999999999]` | 999999999 | at the upper value bound the duplicate cancels and the remaining value survives unchanged |
| `[15, 45, 20, 2, 34, 35, 5, 44, 32, 30]` | 34 | ten mixed values with heavily overlapping bits; the per-bit parities still reproduce one integer |

The pattern across the rows is that the answer is insensitive to the *order* of the array and to the multiplicity of any value beyond its parity: only which values appear, an odd or even number of times, matters.

## 8. Alternative methods considered and rejected

| Method | Cost | Why it is not used |
|:---|:---|:---|
| enumerate all $n^3$ triples and XOR the effective values | $\Theta(n^3)$ time | at $n = 10^{5}$ this is $10^{15}$ evaluations; the definition is a specification, not an algorithm |
| enumerate all $n^2$ ordered pairs, form the OR, then fold in every $k$ | $\Theta(n^3)$ or $\Theta(n^2)$ with large constants | still quadratic at best, and it computes the same per-bit parities that the counting formula gives in $\Theta(1)$ per bit |
| count, per bit, the triples with the bit set and reduce modulo 2 | $\Theta(n \log \max \text{nums})$ time | correct and already linear in practice, but it inspects each element once per bit position instead of once in total |
| restricting the three indices to be pairwise distinct | correct-looking and cheaper on small $n$, but wrong | the definition runs over every ordered triple and includes repetitions such as $i = j = k$; this variant would return 0 instead of 5 on the traced instance, where no triple of pairwise distinct indices exists |
| XOR the whole array once | $\Theta(n)$ time, $\Theta(1)$ space | this is the derived method: the per-bit counting argument proves it equals the definition |
| sort or hash the values to detect duplicates | $\Theta(n \log n)$ time, $\Theta(n)$ space | unnecessary: XOR handles multiplicity parity without ordering or extra storage |

The final row is the method, and the rows above it are the reasons the definition looks much harder than the computation turns out to be.

## 9. Time and auxiliary space

**Time.** The derived method performs one XOR per element: the accumulator starts at 0, each element is folded in once, and the accumulator is returned. That is

$$
\Theta(n)
$$

elementary operations, and it is optimal up to a constant factor, since every element must be read at least once. The bit-level counting argument costs nothing extra: it proves the identity once and for all, independently of the particular array. Contrast this with the literal definition, which needs $\Theta(n^3)$ effective-value computations and is infeasible for $n = 10^{5}$.

**Auxiliary space.** Only one integer accumulator is maintained, together with the loop position over the array. Nothing is copied, hashed, or sorted, and the accumulator stays within the bit width of the inputs ($\text{nums}[i] \le 10^{9} < 2^{30}$, and XOR never sets a bit that is clear in every input). Hence the auxiliary space is

$$
\Theta(1),
$$

independent of $n$. The streaming form of the method means the array does not even need to be held in memory as a whole.
