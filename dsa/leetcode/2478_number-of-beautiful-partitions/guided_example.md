# Guided Example: Number of Beautiful Partitions

## 1. Unpacking the definition of a beautiful partition

We are given a string `s` whose characters are the digits `'1'` through `'9'`, a
part count `k`, and a minimum part length `minLength`. A partition is beautiful
when it splits `s` into `k` contiguous, non-intersecting substrings that together
cover `s`, each of length at least `minLength`, each starting with a **prime**
digit and ending with a **non-prime** digit, where the prime digits are exactly
`'2'`, `'3'`, `'5'`, and `'7'`.

Describe a partition by the prefix lengths at which its parts end. If the parts
end at positions $\ell_1 < \ell_2 < \dots < \ell_k = n$, where $n$ is the length
of `s`, then part $j$ occupies the half-open range of indices
$[\ell_{j-1}, \ell_j)$ with $\ell_0 = 0$. The rules become local statements about
those positions:

- part $j$ starts at index $\ell_{j-1}$, so `s[ℓ_{j-1}]` must be prime;
- part $j$ ends at index $\ell_j - 1$, so `s[ℓ_j - 1]` must be non-prime;
- $\ell_j - \ell_{j-1} \ge \text{minLength}$.

The ends $\ell_1, \dots, \ell_{k-1}$ are the *internal cut positions*; the final
end is always the full length $n$. The decisive observation is that the value
condition constrains each cut position by itself, while the length condition
constrains the gaps between consecutive cut positions. Those two kinds of
constraint can be separated, and the instance below shows the separation paying
off.

## 2. Two global preconditions that reject a whole string

Two requirements involve the boundaries of `s` alone and cannot be repaired by any
choice of cuts:

- The first part starts at index `0`, so `s[0]` must be a prime digit. If it is
  not, no partition can be beautiful.
- The last part ends at index $n - 1$, so the final digit must be non-prime.

These give an immediate rejection test that is worth stating before any counting
begins.

| Instance | Boundary that fails | Why no partition exists | Result |
|:---|:---|:---|:---:|
| `s = "1234"`, `k = 1` | first digit `'1'` is non-prime | the single part would start with a non-prime digit | 0 |
| `s = "2357"`, `k = 1` | last digit `'7'` is prime | the single part would end with a prime digit | 0 |
| `s = "23542185131"` | none | `'2'` is prime, `'1'` is non-prime | proceed |
| `s = "3312958"` | none | `'3'` is prime, `'8'` is non-prime | proceed |

For the official instance of this lesson the preconditions hold, so the lesson
continues with `s = "23542185131"`, $n = 11$, $k = 3$, and
$\text{minLength} = 2$, whose required answer is `3`.

## 3. The admissible cut positions

A prefix length $\ell$ can end a part only if it satisfies the value rules on both
sides of the cut. Let $P = \{\texttt{'2'},\texttt{'3'},\texttt{'5'},\texttt{'7'}\}$.
Call $\ell$ **admissible** when

$$
\ell \ge 1, \qquad \texttt{s}[\ell - 1] \notin P, \qquad
\text{and} \quad \bigl(\ell = n \ \text{or}\ \texttt{s}[\ell] \in P\bigr).
$$

The three clauses say: the character just before the cut is non-prime (the
preceding part ends legally), and if a part follows, its first character is prime
(the next part starts legally). The final length $n$ is admissible whenever the
last digit is non-prime, which the precondition already checked.

| prefix length $\ell$ | `s[ℓ-1]` | `s[ℓ]` | non-prime end? | prime restart? | admissible |
|:---:|:---:|:---:|:---|:---|:---|
| 1 | `'2'` | `'3'` | no | yes | no |
| 2 | `'3'` | `'5'` | no | yes | no |
| 3 | `'5'` | `'4'` | no | no | no |
| 4 | `'4'` | `'2'` | yes | yes | **yes** |
| 5 | `'2'` | `'1'` | no | no | no |
| 6 | `'1'` | `'8'` | yes | no | no |
| 7 | `'8'` | `'5'` | yes | yes | **yes** |
| 8 | `'5'` | `'1'` | no | no | no |
| 9 | `'1'` | `'3'` | yes | yes | **yes** |
| 10 | `'3'` | `'1'` | no | no | no |
| 11 | `'1'` | — (end of string) | yes | not required | **yes** |

So the admissible set is $\{4, 7, 9, 11\}$. Two rows are worth studying. Prefix
length `6` ends on non-prime `'1'` but is followed by `'8'`, another non-prime
digit, so a cut there would create a part starting with `'8'`: rejected by the
restart clause. Prefix length `10` would end on the prime digit `'3'`: rejected by
the end clause. The digit `'5'` at index 7 is prime and never ends a part; it can
only begin one.

## 4. Beautiful partitions become boundary selections with spacing

Only the internal cuts matter for counting, and a beautiful partition into $k$
parts is exactly a choice of $k - 1$ internal cut positions

$$
\ell_1 < \ell_2 < \dots < \ell_{k-1}
\quad\text{from}\quad
B \setminus \{n\}, \qquad B = \{4, 7, 9, 11\},
$$

subject to the spacing constraints

$$
\ell_1 \ge \text{minLength}, \qquad
\ell_{j+1} - \ell_j \ge \text{minLength}, \qquad
n - \ell_{k-1} \ge \text{minLength}.
$$

Every such selection is automatically beautiful: the first part starts at the
prime first digit, every later part starts at an admissible position and therefore
at a prime digit, and every internal end is admissible and therefore non-prime,
with the final end checked by the precondition. Conversely every beautiful
partition yields such a selection. Counting beautiful partitions and counting
these selections are the same problem.

For $k = 3$ we choose two internal cuts out of $\{4, 7, 9\}$, so there are only
three candidates to test.

| internal cuts $(\ell_1, \ell_2)$ | part lengths | $\ell_1 \ge 2$ | $\ell_2 - \ell_1 \ge 2$ | $11 - \ell_2 \ge 2$ | beautiful? |
|:---|:---|:---:|:---:|:---:|:---|
| (4, 7) | 4, 3, 4 | yes | yes | yes | yes |
| (4, 9) | 4, 5, 2 | yes | yes | yes | yes |
| (7, 9) | 7, 2, 2 | yes | yes | yes | yes |

All three survive, and each reproduces one of the three partitions listed in the
official statement:

| internal cuts | the partition they spell | listed officially |
|:---|:---|:---|
| (4, 7) | `"2354"` + `"218"` + `"5131"` | yes |
| (4, 9) | `"2354"` + `"21851"` + `"31"` | yes |
| (7, 9) | `"2354218"` + `"51"` + `"31"` | yes |

The same enumeration explains the second official instance immediately. Raising
`minLength` to `3` keeps only $(4, 7)$, because $(4, 9)$ leaves a final part of
length `2` and $(7, 9)$ leaves a first internal gap of length `2`; the count
drops from `3` to `1`. The length condition alone, not the digit condition, is
what the tighter instance exercises.

## 5. Counting the selections with a prefix-sum dynamic program

Enumerating sets of cut positions costs $\binom{n}{k-1}$ in the worst case, so the
lesson now counts them instead. Fix a part count $j \ge 1$ and let

$$
f[i][j] = \text{number of ways to build } j \text{ parts covering } \texttt{s}[0..i-1]
\text{ with the } j\text{-th part ending exactly at } i,
$$

and let

$$
g[i][j] = \sum_{i' \le i} f[i'][j]
$$

be the running prefix total of $f$ over end positions. The arrays are defined only
for admissible $i$ — combined with the precondition, that means $g[i][j]$ reads as
"ways whose $j$-th part ends at or before $i$".

The transition follows from the spacing constraint. To end part $j$ at $i$, part
$j$ must have length at least `minLength`, so the $(j-1)$-th part must end at some
admissible $i' \le i - \text{minLength}$; each such $i'$ contributes one way.
Summing those ways is exactly the prefix total:

$$
f[i][j] = g\!\left[i - \text{minLength}\right][j - 1]
\quad\text{for admissible } i \ge \text{minLength},
\qquad f[i][j] = 0 \ \text{otherwise},
$$

with the basis $f[0][0] = 1$ and $g[0][0] = 1$ — the empty prefix, zero parts.
Because $g$ accumulates as $g[i][j] = g[i-1][j] + f[i][j]$, the whole lookback is
$O(1)$ per cell instead of a scan. The answer is $f[n][k]$.

The complete trace for `s = "23542185131"` with `minLength = 2` and $k = 3$ is
below; blank $f$ entries are zero, and $g$ columns are carried forward on every
step.

| $i$ | `s[i-1]` | admissible | $f[i][1]$ | $f[i][2]$ | $f[i][3]$ | $g[i][1]$ | $g[i][2]$ | $g[i][3]$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | — | basis | 0 | 0 | 0 | 0 | 0 | 0 |
| 1 | `'2'` | no | 0 | 0 | 0 | 0 | 0 | 0 |
| 2 | `'3'` | no | 0 | 0 | 0 | 0 | 0 | 0 |
| 3 | `'5'` | no | 0 | 0 | 0 | 0 | 0 | 0 |
| 4 | `'4'` | yes | $g[2][0] = 1$ | $g[2][1] = 0$ | $g[2][2] = 0$ | 1 | 0 | 0 |
| 5 | `'2'` | no | 0 | 0 | 0 | 1 | 0 | 0 |
| 6 | `'1'` | no | 0 | 0 | 0 | 1 | 0 | 0 |
| 7 | `'8'` | yes | $g[5][0] = 1$ | $g[5][1] = 1$ | $g[5][2] = 0$ | 2 | 1 | 0 |
| 8 | `'5'` | no | 0 | 0 | 0 | 2 | 1 | 0 |
| 9 | `'1'` | yes | $g[7][0] = 1$ | $g[7][1] = 2$ | $g[7][2] = 1$ | 3 | 3 | 1 |
| 10 | `'3'` | no | 0 | 0 | 0 | 3 | 3 | 1 |
| 11 | `'1'` | yes | $g[9][0] = 1$ | $g[9][1] = 3$ | $g[9][2] = 3$ | 4 | 6 | 4 |

The answer is $f[11][3] = 3$. The table also shows *where* the three ways come
from, because the transition cell is a sum over earlier end positions:

| target cell | decomposition through $g$ | boundary selections produced |
|:---|:---|:---|
| $f[7][2] = g[5][1] = 1$ | $f[4][1]$ | (4, 7) |
| $f[9][2] = g[7][1] = 2$ | $f[4][1] + f[7][1]$ | (4, 9), (7, 9) |
| $f[9][3] = g[7][2] = 1$ | $f[7][2]$ | (4, 7, 9) — not a full partition, since end `9` is not $n$ |
| $f[11][3] = g[9][2] = 3$ | $f[7][2] + f[9][2]$ | (4, 7, 11), (4, 9, 11), (7, 9, 11) |

Intersecting the last row with the final end $n = 11$ recovers exactly the three
official partitions of section 4. As a consistency check, $g[11][3] = 4$ counts
every way to place three parts ending at or before `11`, namely the three
partitions covering the whole string plus the single way that ends at `9`.

## 6. The invariant and why the recurrence is correct

The dynamic program rests on a bijection and an accumulation invariant.

*The bijection.* Section 4 established that beautiful partitions correspond
exactly to selections of internal cuts from $B \setminus \{n\}$ satisfying three
gap inequalities. No information about digits is needed afterwards, because
admissibility already encodes both digit rules and the precondition encodes the
outer two.

*The invariant.* After the tables have been filled up to prefix length $i$, the
cell $f[i'][j]$ equals the number of valid selections of $j - 1$ internal cuts
with the $j$-th part ending at $i'$, and $g[i][j]$ equals the number of such
selections whose $j$-th part ends at or before $i$. This holds at the basis:
$f[0][0] = 1$ counts the empty selection for the empty prefix, and $g[i][0] = 1$
for every $i \ge 0$ because the empty prefix is the only object with zero parts.

*Preservation.* Suppose the invariant holds up to $i - 1$. If $i$ is not
admissible, no part can end at $i$, so $f[i][j] = 0$ and the accumulation
$g[i][j] = g[i-1][j]$ leaves the invariant true. If $i$ is admissible and
$j \ge 1$, every selection ending its $j$-th part at $i$ is obtained by taking a
selection counted in $f[i'][j-1]$ for some admissible
$i' \le i - \text{minLength}$ and appending a part of length $i - i'$; that part
begins at the prime digit `s[i']` and ends at the non-prime digit `s[i-1]`, so it
is legal, and the spacing constraint for the appended part is exactly the
inequality $i - i' \ge \text{minLength}$. The map is one-to-one because a
selection determines its last end $i'$ uniquely. Hence the count is
$\sum_{i' \le i-\text{minLength}} f[i'][j-1] = g[i - \text{minLength}][j-1]$,
which is the stated transition, and the accumulated $g$ row preserves the
invariant for $g$.

Induction over $i$ from the basis therefore gives the invariant at $i = n$, where
$f[n][k]$ counts exactly the selections whose $k$-th (final) part ends at $n$ —
the beautiful partitions. The basis case $j = 1$ deserves a note: it reads
$f[i][1] = g[i - \text{minLength}][0] = 1$ for every admissible
$i \ge \text{minLength}$, which says a single part covering `s[0..i-1]` is legal
in exactly one way. That is right: one part, one choice of nothing.

## 7. Boundary conditions the authored trials expose

| Instance | Situation | What the method computes | Result |
|:---|:---|:---|:---:|
| `s = "214"`, $k = 1$, minLength $= 3$ | the whole string is one part, $n \in B$ | $f[3][1] = g[0][0] = 1$ | 1 |
| `s = "212121"`, $k = 2$, minLength $= 2$ | admissible set $\{2, 4, 6\}$, one internal cut | cuts `2` and `4` both leave gaps of at least `2` | 2 |
| `s = "212121"`, $k = 2$, minLength $= 4$ | length budget $\ge 2 \cdot 4$ exceeds $n = 6$ | neither cut leaves two parts of length `4` | 0 |
| `s = "2211"`, $k = 2$, minLength $= 2$ | length fits but no admissible internal cut | $B = \{4\}$ and the only cut allowed is the final end | 0 |
| `s = "3312958"`, $k = 3$, minLength $= 1$ | $B = \{3, 5, 7\}$ | only the cut pair (3, 5) fits, spelling `"331"`, `"29"`, `"58"` | 1 |
| `s = "1234"`, $k = 1$ | non-prime first digit | precondition rejects before counting | 0 |
| `s = "2357"`, $k = 1$ | prime last digit | precondition rejects before counting | 0 |

The pair of `"212121"` instances is the sharpest pair in the set: the same string
and the same part count give `2` or `0` depending only on the length budget. That
is the signature of a method whose value test and length test are genuinely
independent. The `"2211"` instance is the mirror image: the length budget is
plentiful, but prefix length `2` ends on the prime digit `'2'` and prefix length
`3` would start a part on the non-prime digit `'1'`, so no internal cut is ever
admissible and the answer collapses to `0` for a purely digit-theoretic reason.

## 8. Alternative formulations

| Formulation | How it counts | Cost | Where it breaks down |
|:---|:---|:---|:---|
| Enumerate every choice of $k-1$ cuts | test the value rules and the three gap inequalities for each candidate set | $\binom{n-1}{k-1}$ candidate sets | hopeless as soon as $k$ is large; the digit rules are re-tested for every set |
| Recursive search with memoisation on (index, parts used, last length) | recurse on the next admissible cut | close to $O(n \cdot k)$ states | the extra length coordinate is unnecessary because the spacing is already enforced by the admissible lookback |
| Dynamic program without prefix sums | recompute the sum over earlier end positions at every cell | $O(n^2 k)$ | correct but repeats work the prefix total already stored |
| Dynamic program with prefix totals (used here) | $f[i][j] = g[i - \text{minLength}][j - 1]$ with $g$ accumulated over $i$ | $O(n k)$ time, $O(n k)$ space | none for these constraints; the only subtlety is that the lookback index is $i - \text{minLength}$, not $i - 1$ |

The prefix-sum variant is the memoised recursion with the last coordinate
eliminated: because the transition only ever asks for the sum of $f[i'][j-1]$
over a prefix of end positions, the prefix total $g$ removes the inner loop
entirely, and its lookback is a single subtraction.

## 9. Complexity of the method

Let $n$ be the length of `s` and $k$ the required number of parts.

- **Time:** admissibility is a per-position test costing $\Theta(n)$ once.
  Filling the tables visits every pair $(i, j)$ with $1 \le i \le n$ and
  $1 \le j \le k$, and each cell is computed from a constant number of table
  reads, so the work is $\Theta(nk)$. With $n \le 1000$ that is at most about one
  million constant-cost cells, and the modulo reduction keeps every stored value
  small. Enumerating cut sets, by contrast, can produce
  $\binom{n-1}{k-1}$ candidates.
- **Auxiliary space:** two tables of $(n+1)(k+1)$ counters — the end-position
  counts and their prefix totals — give $O(nk)$ auxiliary space, plus a constant
  number of scalar temporaries. Only the accumulated row for $j-1$ is ever read
  while filling column $j$, so the space could be reduced to two rows of length
  $n+1$, i.e. $O(n)$, at the cost of losing the full trace that this lesson
  displays.

The growth reading is that the cost is linear in the string length for each part
count, so a longer string with the same part count costs proportionally more,
while doubling the part count roughly doubles the work again. The candidate
enumeration, whose count grows combinatorially in $k$, is what this recurrence
avoids.