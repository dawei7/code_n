# Guided Example: Find The Original Array of Prefix Xor

## 1. The Instance and the Question Being Asked

The input is an integer array `pref`, and it is presented as the running XOR of some hidden
array `arr` of the same length:

$$
\text{pref}[i] = \text{arr}[0] \oplus \text{arr}[1] \oplus \dots \oplus \text{arr}[i],
\qquad i = 0, 1, \dots, n-1 .
$$

The task is to recover `arr`. For this lesson we trace

$$
\texttt{pref} = [5, 2, 0, 3, 1],
$$

whose authored reconstruction is `[5, 7, 2, 3, 2]`. The instance is chosen because it
contains a prefix value of `0` at index $2$, a value that a naive "read the magnitudes back
off" attempt cannot explain, and because the hidden array is not monotone, not sorted, and
not related to the prefix values by any simple arithmetic difference.

| Index $i$ | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| `pref[i]` | 5 | 2 | 0 | 3 | 1 |
| Binary (3 bits) | `101` | `010` | `000` | `011` | `001` |

The promise that the answer is unique means we do not have to search: there is exactly one
array consistent with the prefix XORs, and the method below constructs it directly.

## 2. Prefix XOR Is an Invertible Operator

Two algebraic facts carry the whole solution.

**XOR is its own inverse.** For every integer $a$, $\;a \oplus a = 0$. This is what makes
information recoverable: a value that has been XORed into an accumulator can be removed
again by XORing it a second time.

**XOR is associative and commutative.** Grouping and reordering the terms of a chain of XOR
operations never changes the result. The set of $k$-bit vectors under this operation forms
the abelian group $(\mathbb{Z}/2)^{k}$, in which every element has order two, so the
operation is a perfect involution on every bit independently.

Together these facts mean the map that sends the hidden array to its prefix-XOR array is a
bijection. Write $P_i = \text{pref}[i]$ and introduce the virtual predecessor
$P_{-1} = 0$. Then by definition

$$
P_i = P_{i-1} \oplus \text{arr}[i],
\qquad\text{so}\qquad
P_{i-1} \oplus P_i = P_{i-1} \oplus P_{i-1} \oplus \text{arr}[i] = \text{arr}[i].
$$

The accumulator cancels against itself and exposes the hidden term. This is the only
algebraic step in the algorithm; everything else is bookkeeping.

| Quantity | Definition | Role in the reconstruction |
|---|---|---|
| $P_{-1}$ | $0$ | virtual prefix XOR before the array begins, so index $0$ needs no special algebra |
| $P_i$ | `pref[i]` | the accumulated XOR of the first $i+1$ hidden values |
| $\text{arr}[i]$ | $P_{i-1} \oplus P_i$ | the single value that must have been introduced between the two prefixes |

## 3. The Difference Rule

Reading the identity above as a construction rule gives the whole method:

$$
\text{arr}[0] = \text{pref}[0], \qquad
\text{arr}[i] = \text{pref}[i-1] \oplus \text{pref}[i] \quad \text{for } i \ge 1 .
$$

The first entry has no predecessor to cancel, so the virtual value $P_{-1} = 0$ makes the
rule $\text{arr}[0] = 0 \oplus \text{pref}[0] = \text{pref}[0]$ uniform with the rest.

The name "difference rule" is deliberate but must not be confused with subtraction. XOR is
not arithmetic difference: `pref[i] - pref[i-1]` gives a different number in general. What
the rule really says is that `arr[i]` is the *odd one out* between two consecutive
accumulated states, recovered by cancelling their common part.

## 4. Step-by-Step Reconstruction

Each row takes the two adjacent prefix values, XORs them, and records the hidden value. Bit
columns are shown because XOR acts per bit, with no carries between positions.

| Step $i$ | $\text{pref}[i-1]$ | $\text{pref}[i]$ | Operation | $\text{arr}[i]$ | Binary of $\text{arr}[i]$ |
|---|---|---|---|---|---|
| 0 | $0$ (virtual) | 5 | `0 ^ 5` | 5 | `101` |
| 1 | 5 | 2 | `5 ^ 2` | 7 | `111` |
| 2 | 2 | 0 | `2 ^ 0` | 2 | `010` |
| 3 | 0 | 3 | `0 ^ 3` | 3 | `011` |
| 4 | 3 | 1 | `3 ^ 1` | 2 | `010` |

Assembling the results in order gives

$$
\texttt{arr} = [5, 7, 2, 3, 2],
$$

which matches the authored expectation for `pref = [5, 2, 0, 3, 1]`.

## 5. Bit-Level View of Each Step

Writing the operands in binary makes the cancellation explicit and shows why a prefix value
of `0` is ordinary rather than degenerate.

| Step $i$ | $\text{pref}[i-1]$ (binary) | $\text{pref}[i]$ (binary) | Per-bit XOR | Result (binary) | Result (decimal) |
|---|---|---|---|---|---|
| 1 | `101` | `010` | `1^0, 0^1, 1^0` | `111` | 7 |
| 2 | `010` | `000` | `0^0, 1^0, 0^0` | `010` | 2 |
| 3 | `000` | `011` | `0^0, 0^1, 0^1` | `011` | 3 |
| 4 | `011` | `001` | `0^0, 1^0, 1^1` | `010` | 2 |

Step 2 shows the case that defeats magnitude-based reasoning: `pref` falls from `2` to `0`,
which looks like an arithmetic decrease of `2`, and the hidden value is indeed `2` here.
Step 4 shows why that coincidence proves nothing: `pref` falls from `3` to `1`, again a
decrease of `2`, yet the hidden value is also `2`. The relationship is bitwise, not
arithmetic, and the two cases agree only by accident.

## 6. Verification by Re-accumulation

Recomputing the prefix XORs of the reconstructed array is the natural audit, and it must
reproduce the input exactly at every index.

| Index $i$ | Partial XOR chain | Accumulated value | Expected `pref[i]` | Match |
|---|---|---|---|---|
| 0 | `5` | 5 | 5 | yes |
| 1 | `5 ^ 7` | 2 | 2 | yes |
| 2 | `5 ^ 7 ^ 2` | 0 | 0 | yes |
| 3 | `5 ^ 7 ^ 2 ^ 3` | 3 | 3 | yes |
| 4 | `5 ^ 7 ^ 2 ^ 3 ^ 2` | 1 | 1 | yes |

The last row is the strongest check available on this instance: the two final hidden values
`3` and `2` XOR to `1`, and the accumulated `0` at index $2$ contributed nothing to any
later prefix. A wrong value anywhere earlier would have propagated into every later row.

## 7. Why the Method Is Correct and the Answer Unique

**Soundness.** Define `arr` by the difference rule. For $i = 0$, the running XOR of the
first one entries is $\text{pref}[0]$ by construction. For $i \ge 1$, induction gives

$$
\text{arr}[0] \oplus \dots \oplus \text{arr}[i]
= \bigl(\text{arr}[0] \oplus \dots \oplus \text{arr}[i-1]\bigr) \oplus \text{arr}[i]
= \text{pref}[i-1] \oplus \bigl(\text{pref}[i-1] \oplus \text{pref}[i]\bigr)
= \text{pref}[i],
$$

where the outer two terms cancel because every element of the group is its own inverse. The
constructed array therefore satisfies the required prefix identity at every index.

**Completeness and uniqueness.** Suppose two arrays `arr` and `arr'` both produce the prefix
array `pref`. Their prefixes agree at every index. At index $0$,
`arr[0] = pref[0] = arr'[0]`. If the two arrays agree through index $i-1$, then applying the
difference rule at index $i$ gives
$\text{arr}[i] = \text{pref}[i-1] \oplus \text{pref}[i] = \text{arr}'[i]$, so they agree
through index $i$ as well. Induction over the whole array shows the arrays are identical, so
the answer is unique — exactly the uniqueness the problem promises.

**Invariant of the construction.** After step $i$ has been processed, the values written at
positions $0$ through $i$ are precisely the hidden values of the unique array whose running
XOR is `pref` through index $i$. No backtracking, verification pass, or repair step is ever
needed.

## 8. Boundary and Degenerate Instances

| Situation | Input | Behaviour of the rule | Output |
|---|---|---|---|
| Single element | `pref = [13]` | `arr[0]` equals `pref[0]` because the virtual predecessor is $0$ | `[13]` |
| Two elements | `pref = [5, 2]` | `arr[1] = 5 ^ 2 = 7` | `[5, 7]` |
| All prefix values equal | `pref = [7, 7, 7]` | equal neighbours cancel, so every later hidden value is $0$ | `[7, 0, 0]` |
| Original begins with zero | `pref = [0, 1, 1]` | `arr[0] = 0`, then `0 ^ 1 = 1`, then `1 ^ 1 = 0` | `[0, 1, 0]` |
| Prefix XOR returns to zero | `pref = [1, 0, 3]` | `arr[1] = 0 ^ 1 = 1` and `arr[2] = 3 ^ 0 = 3`; a zero prefix is an ordinary state | `[1, 1, 3]` |
| Alternating zeros | `pref = [0, 9, 0, 9, 0]` | neighbours alternate between equal and different | `[0, 9, 9, 9, 9]` |
| Maximum legal values | `pref = [1000000, 0, 1000000]` | every XOR of two values at most $10^{6}$ stays below $2^{20}$ | `[1000000, 1000000, 1000000]` |

Three traps live here. A hidden value may legitimately be `0`, so no step may assume the
answer is nonzero. The hidden array need not be monotone, sorted, or positive-looking: the
prefix map is a bijection of the whole value space and does not preserve order. And holding
the accumulator for $P_{i-1}$ is essential — dropping it and XORing the raw inputs would
reconstruct a different array.

## 9. Alternative Methods and Their Costs

| Alternative | Idea | Trade-off |
|---|---|---|
| Brute-force search per position | For each index, try candidate values until one turns the running XOR into `pref[i]` | Up to $2^{20}$ tests per position under the stated bounds, giving $O(n \cdot 2^{20})$, when the algebra pins the value down immediately |
| Back-substitution over GF(2) | Treat the prefix relations as a unit lower-triangular linear system and solve it | Correct and yields exactly the difference rule, but the general machinery of elimination is unnecessary for a triangular system whose diagonal is all ones |
| Recompute every prefix from scratch | For each $i$, XOR `arr[0]` through `arr[i-1]` to test a guess | $O(n^2)$ time; a valid verification strategy, not a construction strategy |
| Arithmetic difference | Use `pref[i] - pref[i-1]` | Wrong: XOR is not subtraction. For `pref = [5, 2]` it gives $2 - 5 = -3$ instead of $7$ |
| Sort or match by magnitude | Infer the hidden values from how the prefix values grow | Invalid: the map is not order-preserving. A prefix can drop from `3` to `1` while the hidden value is `2`, as in section 5 |
| Hash-map over cumulative values | Exploit `arr[i] = pref[i] ^ pref[i-1]` by storing prefixes in a table | Identical arithmetic with extra memory; the table is only useful for range-XOR queries, which this problem never asks |

## 10. Complexity Derivation

Let $n = \texttt{pref.length}$.

**Time.** Each of the $n$ output positions requires exactly one XOR of two input values and
one store. Under the stated bounds `pref[i]` $\le 10^{6} < 2^{20}$, every value fits in a
single machine word, so each XOR is $O(1)$ and the total is

$$
\Theta(n).
$$

The bound is tight in both directions: every hidden value must be produced, and producing it
requires examining the two adjacent prefix values that determine it. Nothing is searched,
sorted, or compared, so no logarithmic factor appears.

**Auxiliary space.** Only the two adjacent prefix values are needed simultaneously, and the
output array is written in place as it is produced. Auxiliary space beyond the returned
array is therefore

$$
O(1).
$$

The returned array itself occupies $O(n)$ output space, which is unavoidable since the
answer consists of $n$ integers. An implementation that reuses the input buffer, or that
writes the result into a fresh array, has the same auxiliary cost either way; the difference
is only in the output space that the contract already requires.