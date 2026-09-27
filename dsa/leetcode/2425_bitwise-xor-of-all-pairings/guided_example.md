# Guided Example: Bitwise XOR of All Pairings

## 1. The instance and the product that must not be built

We trace

- `nums1 = [2, 1, 3]`, so $n = 3$;
- `nums2 = [10, 2, 5, 0]`, so $m = 4$.

The conceptual array `nums3` holds the value $a \oplus b$ for every ordered choice
of $a \in \texttt{nums1}$ and $b \in \texttt{nums2}$, so it has $nm = 12$ entries,
and the required answer is the XOR of all of them: `13`.

At the stated limits $n, m \le 10^{5}$, the product has up to $10^{10}$ entries.
Materialising it is not merely slow, it is impossible, so the lesson has to
explain how the answer can be computed without ever forming a single pair.

## 2. The three algebraic facts that do the work

XOR on non-negative integers, written $\oplus$, is a commutative and associative
operation with identity $0$:

$$
a \oplus b = b \oplus a, \qquad
(a \oplus b) \oplus c = a \oplus (b \oplus c), \qquad
a \oplus 0 = a .
$$

It is also self-inverse: $a \oplus a = 0$. Two consequences follow, and together
they are the entire algorithm.

- **Reordering is free.** Because $\oplus$ is associative and commutative, a long
  chain of XOR terms may be permuted and regrouped arbitrarily without changing
  the result. The nested sum $\bigoplus_{a} \bigoplus_{b} (a \oplus b)$ can
  therefore be expanded into $nm$ flat terms and sorted by origin.
- **Multiplicity is everything.** A fixed value $x$ contributes to a flat chain
  only through the parity of how many times it appears: an even count cancels
  pairwise down to $0$, and an odd count leaves exactly one copy of $x$. The
  numeric value of $x$ only matters for the final combination, never for the
  cancellation count.

## 3. Counting occurrences without enumerating them

Expand every pair term into its two source halves:

$$
\bigoplus_{a \in \texttt{nums1}} \ \bigoplus_{b \in \texttt{nums2}} (a \oplus b)
\;=\; \bigoplus_{a \in \texttt{nums1}} \ \bigoplus_{b \in \texttt{nums2}} a
\;\oplus\;
\bigoplus_{a \in \texttt{nums1}} \ \bigoplus_{b \in \texttt{nums2}} b .
$$

Now read each half separately:

- A fixed $a$ from `nums1` is paired with each of the $m$ values in `nums2`, so it
  appears **$m$ times** in the left half. It survives when $m$ is odd and cancels
  when $m$ is even.
- Symmetrically, a fixed $b$ from `nums2` appears **$n$ times** in the right half.
  It survives when $n$ is odd and cancels when $n$ is even.

This is the crux that beginners get backwards: an element of `nums1` repeats
according to the length of `nums2`, not its own array's length.

| Source array | Length | Multiplicity of each of its elements | Survives when |
|---|---|---|---|
| `nums1` | $n = 3$ | $m = 4$ | $m$ is odd |
| `nums2` | $m = 4$ | $n = 3$ | $n$ is odd |

## 4. The four parity cases

Combining the two independent groups gives a complete decision table. No case
needs a special branch beyond the parity test itself.

| $n$ parity | $m$ parity | Contributing values | Answer |
|---|---|---|---|
| even | even | none | `0` |
| even | odd | every element of `nums1` once | $\bigoplus_{a \in \texttt{nums1}} a$ |
| odd | even | every element of `nums2` once | $\bigoplus_{b \in \texttt{nums2}} b$ |
| odd | odd | both full arrays | $\bigl(\bigoplus_a a\bigr) \oplus \bigl(\bigoplus_b b\bigr)$ |

For the traced instance $n = 3$ is odd and $m = 4$ is even, which is the third
row: every element of `nums2` contributes exactly once, and both `2`, `1` and `3`
cancel completely.

| Element | Array | Multiplicity in the flat expansion | Parity | Contributes |
|---|---|---|---|---|
| `2` | `nums1` | 4 | even | no |
| `1` | `nums1` | 4 | even | no |
| `3` | `nums1` | 4 | even | no |
| `10` | `nums2` | 3 | odd | yes, once |
| `2` | `nums2` | 3 | odd | yes, once |
| `5` | `nums2` | 3 | odd | yes, once |
| `0` | `nums2` | 3 | odd | yes, once |

Note that the value `2` appears in both arrays. The table counts *positions*, not
distinct numerals: the `2` in `nums1` contributes nothing, while the independent
`2` in `nums2` contributes once. Values are never deduplicated.

## 5. Executing the instance, bit by bit

Only the four surviving values remain to be combined:

$$
10 \oplus 2 \oplus 5 \oplus 0 .
$$

Writing the operands in binary exposes the parity test at each bit position, since
XOR decides each bit independently of the others.

| Bit position | 3 | 2 | 1 | 0 |
|---|---|---|---|---|
| `10` | 1 | 0 | 1 | 0 |
| `2` | 0 | 0 | 1 | 0 |
| `5` | 0 | 1 | 0 | 1 |
| `0` | 0 | 0 | 0 | 0 |
| Count of ones | 1 | 1 | 2 | 1 |
| Count parity | odd | odd | even | odd |
| Result bit | 1 | 1 | 0 | 1 |

The result is `1101`, which is `13`, matching the required output. The bit at
position 1 shows the cancellation rule working inside a single column: two ones
annihilate and the bit becomes 0.

For contrast, the second official instance has `nums1 = [1, 2]` and
`nums2 = [3, 4]`, so $n$ and $m$ are both even. Every element repeats an even
number of times and the answer is `0` without reading a single value's bits. The
four generated pair values are `1 ^ 3 = 2`, `1 ^ 4 = 5`, `2 ^ 3 = 1`, `2 ^ 4 = 6`,
and indeed $2 \oplus 5 \oplus 1 \oplus 6 = 0$.

## 6. Why the reasoning is correct

**Claim.** The XOR of all $nm$ pair values equals
$\bigl(m \bmod 2\bigr) \cdot \bigoplus_{a \in \texttt{nums1}} a \;\oplus\;
\bigl(n \bmod 2\bigr) \cdot \bigoplus_{b \in \texttt{nums2}} b$,
where the multiplier 0 suppresses the whole group and the multiplier 1 keeps it.

*Proof.* The nested sum expands to a flat chain of $nm$ terms, each of which is an
element of `nums1` or an element of `nums2` (using the associative and
commutative laws, which permit any regrouping). Group the terms by source
position. A source position with value $x$ that occurs $t$ times contributes $x$
if $t$ is odd and $0$ if $t$ is even, because $x \oplus x = 0$ allows the copies
to be cancelled in pairs, leaving at most one. Each `nums1` position occurs
exactly $m$ times and each `nums2` position exactly $n$ times. Summing the
surviving positions of each group reproduces the two displayed XOR aggregates,
and the groups are then XORed together. $\square$

**Completeness.** The expansion above uses every one of the $nm$ pair terms
exactly once: no term is dropped and none is double-counted, since each pair
$(a, b)$ is generated by exactly one choice of indices. Hence the computed value
is the XOR of the whole of `nums3`, as the statement defines it.

**Bit-level cross-check.** The same conclusion follows one bit at a time. At any
bit position, the answer bit is the parity of the number of pair values with a 1
there; each bit of each $a$ is repeated $m$ times and each bit of each $b$ is
repeated $n$ times, so only the length parities decide which bits survive. This
view confirms that the argument never depends on the magnitudes of the numbers,
only on how often each position is counted.

## 7. Boundary conditions this instance family exposes

| Situation | Instance | Answer | Reason |
|---|---|---|---|
| Both lengths even | `nums1 = [2, 2]`, `nums2 = [10, 2, 5, 0]` | `0` | Every position has even multiplicity, regardless of the values. |
| Both lengths odd | `nums1 = [1, 2, 4]`, `nums2 = [8, 16, 32]` | `63` | $7 \oplus 56 = 63$; both aggregates survive and are combined. |
| Only the second length odd | `nums1 = [1, 2]`, `nums2 = [4, 5, 6]` | `3` | $n$ even cancels `nums2`; `nums1` survives with $1 \oplus 2 = 3$. |
| Only the first length odd | `nums1 = [7, 8, 9]`, `nums2 = [1, 2]` | `3` | `nums1` cancels; $1 \oplus 2 = 3$ from `nums2`. |
| Singleton on each side | `nums1 = [1]`, `nums2 = [2]` | `3` | Both lengths are odd, so the answer is simply $1 \oplus 2$. |
| Singleton against three values | `nums1 = [5]`, `nums2 = [1, 2, 3]` | `5` | The lone `5` repeats 3 times and survives; $1 \oplus 2 \oplus 3 = 0$ disappears. |
| Zero values | `nums1 = [0]`, `nums2 = [0]` | `0` | Zero has no set bits and cannot change an accumulator, but its multiplicities still count. |
| Duplicate values | `nums1 = [2, 2]`, `nums2 = [10, 2, 5, 0]` | `0` | Counting is positional; `nums1`'s even length removes everything. |
| Maximum magnitudes | values near $10^{9}$ | depends | Values need about 30 bits, so each XOR is a constant number of word operations. |

## 8. Alternative methods and their trade-offs

| Method | Time | Auxiliary space | Why it is not used here |
|---|---|---|---|
| Two nested loops over all pairs | $O(nm)$ | $O(1)$ if folded on the fly, $O(nm)$ if `nums3` is stored | Matches the definition literally, but $nm$ can reach $10^{10}$; the extra array cannot fit in memory. |
| Frequency dictionary of all source values | $O(n + m)$ | $O(n + m)$ | Correct — keep only odd multiplicities — but it hashes every value to rediscover a parity that the array lengths already determine. |
| XOR each array first, then gate on parity | $O(n + m)$ | $O(1)$ | Equally correct, but it always reads both arrays even when one group provably cancels. |
| Parity-gated accumulation | $O(n + m)$ worst case | $O(1)$ | Chosen. It reads an array only when the opposite length is odd, and folds values directly into a single running accumulator. |

## 9. Cost of the method: complexity derivation

Let $n = \lvert\texttt{nums1}\rvert$ and $m = \lvert\texttt{nums2}\rvert$.

*Time.* A single scan of `nums1` runs only when $m$ is odd, and a single scan of
`nums2` runs only when $n$ is odd. Each scan performs one XOR per element, so the
worst case — both lengths odd — costs $n + m$ XOR operations and the best case
costs none. The parity tests themselves are constant-time bit inspections, and
each value is at most $10^{9}$, so one XOR is a constant number of word
operations under the standard word-RAM model. Therefore

$$
T(n, m) = O(n + m).
$$

This is asymptotically optimal whenever an array genuinely contributes: if $m$ is
odd, changing any single element of `nums1` changes the answer, so no correct
algorithm can avoid reading the whole array. When both lengths are even the answer
is `0` without inspecting any value, because parity alone proves universal
cancellation.

*Auxiliary space.* The computation keeps one accumulator and a loop variable, and
never allocates a list of size $nm$ or of size $n + m$. Auxiliary memory is

$$
S(n, m) = O(1).
$$

The only quantity that grows is the arithmetic width: with $B$-bit inputs the
bit-level cost of a scan would be $O((n + m)B)$, but $B \le 30$ here, so the
word-level bound stands.