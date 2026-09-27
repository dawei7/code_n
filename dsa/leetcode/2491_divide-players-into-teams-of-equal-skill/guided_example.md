# Guided Example: Divide Players Into Teams of Equal Skill

## 1. What a Valid Partition Actually Constrains

An even number $n$ of players, each with a positive skill, must be split into $n/2$ teams of
exactly two. Every team must have the **same** total skill, and the quantity to report is the sum of
the per-team products — the "chemistry" — or `-1` when no such partition exists.

Write the sorted skills as

$$
a_1 \le a_2 \le \dots \le a_n
$$

and suppose a valid partition exists. Let the common team total be $S$. Two facts are immediate but
easy to under-use:

- Every player belongs to exactly one team, so the number of teams and the pairing are both
  complete coverings of the index set.
- Summing all team totals gives $S \cdot \frac{n}{2} = \sum_i a_i$, so $S$ is determined by the
  input: $S = \frac{2}{n}\sum_i a_i$. In particular $S$ is unique if it exists at all.

The second fact is necessary but far from sufficient, and it is also not something the method below
needs to compute. What pins the structure down is the extremal argument in the next section.

## 2. The Extremes Lemma: Smallest Must Pair With Largest

**Claim.** In every valid partition, the smallest skill $a_1$ is teamed with the largest skill
$a_n$, and the common team total is $S = a_1 + a_n$.

**Proof.** Let $a_1$ be teamed with some partner $a_x$, and let $a_n$ be teamed with some partner
$a_y$, where $x \neq 1$ and $y \neq n$ (the two teams may coincide only when $n = 2$, handled
separately below). Both teams must total $S$, so

$$
a_1 + a_x = S, \qquad a_y + a_n = S.
$$

Because $a_x \ge a_1$ we get $S = a_1 + a_x \ge 2a_1$, and because $a_y \le a_n$ we get
$S = a_y + a_n \le 2a_n$. More directly, substitute the second equation into the first:

$$
a_1 + a_x = a_y + a_n
\quad\Longrightarrow\quad
a_x - a_y = a_n - a_1 \ge 0 .
$$

Now $a_x \le a_n$ and $a_y \ge a_1$. The equality $a_x - a_y = a_n - a_1$ can hold only when both
sides are tight, that is $a_x = a_n$ and $a_y = a_1$. Since the sorted order forces $a_x \le a_n$
and $a_y \ge a_1$, any slack on either side makes the left side strictly smaller than the right.
Hence $a_1$'s partner is $a_n$, $a_n$'s partner is $a_1$, and both are the same team with total
$S = a_1 + a_n$. $\square$

The consequence is a complete algorithm. Remove the forced team $\{a_1, a_n\}$; the remaining
$n - 2$ players must satisfy the identical condition, so the smallest and largest of the remainder
are forced together as well. Induction gives a single candidate partition:

$$
\bigl(a_1, a_n\bigr),\; \bigl(a_2, a_{n-1}\bigr),\; \bigl(a_3, a_{n-2}\bigr),\; \dots
$$

Every team must have total $S = a_1 + a_n$. If any of these forced pairs fails to reach that total,
no valid partition exists at all, and the answer is `-1`.

## 3. Worked Trace on the Official Instance

`skill = [3,2,5,1,3,4]`, expected `22`. Sorting is the first move, because the extremes lemma is a
statement about the sorted order:

| $i$ | 1 | 2 | 3 | 4 | 5 | 6 |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| $a_i$ | 1 | 2 | 3 | 3 | 4 | 5 |

The extreme sum is fixed by the first and last entries: $S = a_1 + a_6 = 1 + 5 = 6$.

Two indices walk inward from the ends. The left index rises, the right index falls, and they meet in
the middle.

| Step | Left index $i$ | Right index $j$ | Pair $(a_i, a_j)$ | Sum | Equals $S = 6$? | Product | Running chemistry |
|:---:|:---:|:---:|:---|:---:|:---:|:---:|:---:|
| 1 | 1 | 6 | $(1, 5)$ | 6 | yes | 5 | 5 |
| 2 | 2 | 5 | $(2, 4)$ | 6 | yes | 8 | 13 |
| 3 | 3 | 4 | $(3, 3)$ | 6 | yes | 9 | 22 |

After the third step the indices cross, the scan stops, and the accumulated value `22` is returned.
This matches the official partition $(1,5), (2,4), (3,3)$ and its chemistry $5 + 8 + 9 = 22$.

Note that the duplicate skill `3` is not a complication: the two `3` entries are adjacent in sorted
order and are consumed by the same middle pair. Duplicates only matter when they break the forced
pairing, which is exactly what the next trace shows.

## 4. A Trace That Must Fail

`skill = [1,1,2,3]`, expected `-1`. Sorted, the array is already $[1,1,2,3]$, and the extreme sum is
$S = a_1 + a_4 = 1 + 3 = 4$.

| Step | Left index $i$ | Right index $j$ | Pair $(a_i, a_j)$ | Sum | Equals $S = 4$? | Outcome |
|:---:|:---:|:---:|:---|:---:|:---:|:---|
| 1 | 1 | 4 | $(1, 3)$ | 4 | yes | Continue inward. |
| 2 | 2 | 3 | $(1, 2)$ | 3 | no | Return `-1` immediately. |

The failure is structural, not accidental. The forced team $\{1, 3\}$ consumes the only `3`, leaving
$\{1, 2\}$ as the only possible second team with total $3 \neq 4$. No rearrangement can fix this:
the extremes lemma already proved that the first pair was not a choice but a consequence of $S$.
The remaining alternative partitions of $[1,1,2,3]$ are $(1,1) + (2,3)$ with totals $2$ and $5$, and
$(1,2) + (1,3)$ with totals $3$ and $4$ — neither has equal totals, so `-1` is correct.

A second failure shape appears in `skill = [1,1,1,4,5,6]`, sorted to itself with $S = 1 + 6 = 7$.
The first pair $(1,6)$ totals $7$ exactly, but the second pair $(1,5)$ totals $6$, so the scan stops
with `-1`. Here the total sum $18$ divides evenly into three teams of $6$, so a divisibility check
alone would have wrongly suggested feasibility. The per-pair check is what catches it.

## 5. Invariant and Correctness

**Invariant.** Before iteration $k$, the pairs
$(a_1, a_n), (a_2, a_{n-1}), \dots, (a_k, a_{n-k+1})$ have each been verified to total
$S = a_1 + a_n$, and the accumulated chemistry is the sum of their products.

**Preservation.** Iteration $k + 1$ examines $a_{k+1}$ and $a_{n-k}$, the smallest and largest
entries of the still-unpaired subarray. If their sum is not $S$, the method halts with `-1`, which
the extremes lemma justifies: that pair is forced, and a forced pair with the wrong sum means no
valid partition exists. If the sum is $S$, the pair is committed and the invariant advances.

**Soundness.** If the scan completes without failing, the pairs it formed are a partition of all
$n$ players, and each has total exactly $S$; so the partition is valid and the accumulated sum of
products is a genuine achievable chemistry.

**Completeness and uniqueness.** The extremes lemma shows that *every* valid partition must contain
$\{a_1, a_n\}$ as a team. Applying the lemma inductively to the remaining elements shows that every
valid partition must be the extremes pairing, so there is at most one valid partition. When the scan
completes, that unique partition was found and the reported chemistry is the answer; when the scan
fails on a forced pair, no valid partition exists and `-1` is required. The method is therefore
exact in both directions, and no case analysis over alternative pairings is needed.

**The two-player base case.** For $n = 2$ the indices are $i = 1$, $j = 2$, and the single pair
$(a_1, a_2)$ trivially totals $S$, so the answer is $a_1 a_2$; this is the official second example
where `[3,4]` yields $12$. A one-element input leaves the two indices coincident, the loop body never
executes, and the accumulated chemistry is $0$ — the empty sum over zero teams.

## 6. Boundary Analysis

Each row is an authored case, and each verdict follows from the forced-pairing rule.

| Instance | `skill` (sorted) | $S = a_1 + a_n$ | Forced pairs | Expected | Why it is a boundary |
|:---|:---|:---:|:---|:---:|:---|
| Three teams | `[1,2,3,3,4,5]` | 6 | all three total 6 | 22 | Duplicates sit in the middle and pair with each other. |
| Single team | `[3,4]` | 7 | one pair | 12 | The smallest legal even length; base case of the induction. |
| Impossible | `[1,1,2,3]` | 4 | second pair totals 3 | $-1$ | The only available complement for `1` is used up by the first pair. |
| All equal | `[5,5,5,5]` | 10 | two pairs of equals | 50 | Every forced pair is automatically valid; chemistry $25 + 25$. |
| Repeated complements | `[1,1,4,4]` | 5 | two identical pairs | 8 | Duplicated values pair symmetrically, not within their own group. |
| Sum divides evenly, pairing fails | `[1,2,2,2]` | 3 | second pair totals 4 | $-1$ | Total $7$ would not divide, but the pair check fails first. |
| Complement shortage | `[1,1,1,4,5,6]` | 7 | second pair totals 6 | $-1$ | Total sum divides evenly into three teams of 6; divisibility is not sufficient. |
| Maximum skills | `[1,2,999,1000]` | 1001 | both pairs total 1001 | 2998 | Exercises the upper value bound and a large product sum. |
| One element | `[3]` | undefined | none | 0 | No team exists; the empty chemistry sum is 0. |
| Two identical | `[3,3]` | 6 | one pair | 9 | Smallest case with a duplicated value. |

The `[1,1,1,4,5,6]` row is the most instructive because it defeats the most tempting shortcut.
Checking that $\sum_i a_i$ is divisible by $n/2$ is a necessary condition and would pass here, yet
the instance is infeasible. The reason is that equal team totals are a much stronger requirement
than an average that happens to be an integer.

## 7. Alternatives and Their Cost

| Approach | Idea | Verdict |
|:---|:---|:---|
| Sort, then pair extremes with two pointers | Verify each forced pair against $S = a_1 + a_n$. | Chosen method: one sort plus one linear scan, and it certifies uniqueness. |
| Try all perfect matchings | Enumerate every way to pair the players. | Correct but has $(n-1)!!$ candidates; hopeless beyond tiny $n$. |
| Frequency table of complements | Count each skill and match value $v$ with $S - v$. | Correct and $O(n)$ when the pair sum is known in advance; needs the same extremes insight to obtain $S$, and adds counting bookkeeping. |
| Divisibility check on the total | Compute $\sum_i a_i$, divide by $n/2$, and accept. | Wrong: necessary but not sufficient, as `[1,1,1,4,5,6]` shows. |
| Greedy smallest with nearest complement | Pair each smallest value with the closest available value summing to $S$. | Unnecessary complexity; the extremes lemma already names the partner exactly. |

The frequency-table row is the strongest alternative and is asymptotically faster on paper, but it
still needs $S$, which comes from the extremes argument, and its behaviour with duplicates requires
careful counting in both directions. Two pointers on a sorted array make the duplicate handling
implicit, because the pairs are read off the sorted order rather than reconstructed from counts.

## 8. Complexity Derivation

Let $n = \lvert \text{skill} \rvert$, with $n$ even and $n \le 10^{5}$.

**Time.** Sorting dominates. Comparison sorting costs $O(n \log n)$, which for $n = 10^{5}$ is on the
order of $1.7 \times 10^{6}$ comparisons. The two-pointer verification then performs exactly $n/2$
iterations, each doing one integer addition, one comparison, and one multiplication-accumulation —
$O(n)$ in total. Reading the extreme sum $S = a_1 + a_n$ is $O(1)$ after sorting. The overall time
is therefore $O(n \log n)$, and no step after sorting is superlinear. An early failure can only
reduce the constant factor, never the asymptotic class.

**Auxiliary space.** The scan uses two integer indices, the target sum $S$, and the accumulator — a
constant number of scalars, $O(1)$. Sorting is the only source of extra storage: an in-place
comparison sort needs $O(\log n)$ stack space or none, while a copy-then-sort strategy uses $O(n)$
for the copy. The reported bound is $O(n)$ auxiliary space on the assumption that the sorted array
is materialized, which is the conservative and portable description. The products and their running
sum are single integers.

**Accumulator range.** Each product is at most $1000 \times 1000 = 10^{6}$, and there are at most
$5 \times 10^{4}$ teams, so the chemistry sum is at most $5 \times 10^{10}$. That exceeds 32-bit
range, so the accumulator must be a 64-bit (or arbitrary-precision) integer. This does not change
the asymptotic bounds but it is a genuine correctness trap for fixed-width implementations, and it
is the reason the maximum-value case `[1,2,999,1000]` is worth including in a test set.

**Verdict cost.** Deciding `-1` costs no more than deciding a valid instance: the same single scan
over the sorted array is performed, and a failure simply terminates it early.