# Guided Example: Largest Positive Integer That Exists With Its Negative

## 1. The Instance and the Question It Poses

The array `nums` holds no zeros. The task is to find the largest positive integer $k$ for which the array also carries $-k$, and to answer with the sentinel `-1` when no such magnitude exists anywhere in the input.

**Representative input.** `nums = [-1, 10, 6, 7, -7, 1]`

**Required output.** `7`

This instance is worth tracing because it separates three ideas that a single-pair example keeps hidden:

- Two magnitudes compete, $1$ and $7$, so the method must compare candidates instead of stopping at the first pair it meets.
- The two largest array values, `10` and `6`, are decoys whose negatives never appear, so "the biggest number in the array" is the wrong instinct.
- The positive and negative members of the winning pair live in different regions of the array, so position and reading order are irrelevant to the answer.

Stated formally, the requested value is

$$
k^{*} = \max\{\, k > 0 \;:\; k \in \texttt{nums} \ \wedge\ -k \in \texttt{nums} \,\},
$$

with $k^{*} = -1$ when that set is empty. Everything that follows is a way of evaluating this maximum without ever enumerating pairs.

## 2. Collapsing the Array into a Membership Set

Every clause of the definition is a question of **existence**, never of position or multiplicity. Whether `-7` occurs once or four times, and whether it sits before or after `7`, cannot change $k^{*}$. The first modelling step therefore discards order and repetition, replacing the sequence with its distinct-value set $S$.

| Index `i` | `nums[i]` | Sign | Partner this value would need: `-nums[i]` | Partner present in $S$? |
|:---:|:---:|:---:|:---:|:---:|
| 0 | `-1` | negative | `1` | yes |
| 1 | `10` | positive | `-10` | no |
| 2 | `6` | positive | `-6` | no |
| 3 | `7` | positive | `-7` | yes |
| 4 | `-7` | negative | `7` | yes |
| 5 | `1` | positive | `-1` | yes |

For this input,

$$
S = \{-7,\,-1,\,1,\,6,\,7,\,10\}, \qquad \lvert S \rvert = 6 = n.
$$

The collapse is lossy in exactly one direction and harmless in the other: $S$ can no longer answer "where did this value appear?", but the contract never asks that. Every fact the contract does ask about — does $k$ occur, does $-k$ occur — survives the collapse intact. Notice that row 4 confirms the pair from the negative side while row 3 confirms the same pair from the positive side; the two rows are two views of one candidate, which is the seed of the invariant in the next section.

## 3. The Symmetry Invariant Behind a Single Maximum Scan

Write $q(v)$ for the predicate "$-v$ belongs to $S$".

**Invariant (negation symmetry).** $q(v)$ holds if and only if $q(-v)$ holds, because the partner required by $-v$ is $-(-v) = v$. Consequently $q(v) \wedge q(-v)$ is equivalent to the single statement $\{v, -v\} \subseteq S$.

This has two immediate consequences that carry the whole method.

1. The qualifying values inside $S$ form a union of **complete opposite pairs** $\{-k, k\}$. A magnitude can never be half-present in the qualifying family; either both signs qualify or neither does.
2. For every $k > 0$ we have $-k < k$, so inside each pair the positive member is strictly the larger. Therefore

$$
\max\{\, v \in S \;:\; q(v) \,\} = \max\{\, k > 0 \;:\; \{k, -k\} \subseteq S \,\} = k^{*}
$$

whenever at least one pair exists. A plain maximum over the qualifying values already *is* the positive answer, which is why no separate positivity test is needed: the negative twin of any admissible magnitude is always beaten by its positive twin before the scan finishes.

The running invariant of the scan is equally simple. After examining any collection $T \subseteq S$ of values, the accumulator holds $\max\{v \in T : q(v)\}$, or the sentinel when no examined value qualifies. Adding one more value either raises the accumulator to that value (when it qualifies and exceeds the current best) or leaves it untouched. The maximum is associative and commutative, so the traversal order of $S$ never affects the final accumulator.

**Why the exclusion of zero is load-bearing.** If $0$ were permitted, then $-0 = 0$, so $q(0)$ would be satisfied by the value $0$ alone — a value paired with itself. An input containing zero and no genuine opposite pair would then return `0` instead of the required `-1`. The guarantee `nums[i] != 0` is what makes the symmetric test exactly equivalent to the contract, and it is a correctness condition rather than a performance footnote.

## 4. Step-by-Step Trace on the Chosen Instance

The first table follows the scan in a concrete order over the six distinct values, showing how the accumulator changes and why. Any other order reaches the same final state.

| Step | Value `v` examined | Partner `-v` required | `-v` in $S$? | Accumulator after the step | Reason for the change |
|:---:|:---:|:---:|:---:|:---:|---|
| 0 | — | — | — | no candidate yet | nothing has been examined |
| 1 | `-7` | `7` | yes | `-7` | first qualifying value becomes the best |
| 2 | `-1` | `1` | yes | `-1` | `-1 > -7`, so the best improves |
| 3 | `1` | `-1` | yes | `1` | `1 > -1`; the best crosses into the positives |
| 4 | `6` | `-6` | no | `1` | decoy rejected, accumulator untouched |
| 5 | `7` | `-7` | yes | `7` | `7 > 1`, a new best |
| 6 | `10` | `-10` | no | `7` | decoy rejected, accumulator untouched |

The final accumulator is `7`, matching the required output for this input. The same information can be read magnitude by magnitude, which makes the decoys explicit rather than merely implied by rejected lookups.

| Magnitude $k$ | $k \in S$ | $-k \in S$ | Admissible? | Role in this instance |
|:---:|:---:|:---:|:---:|---|
| 1 | yes | yes | yes | smaller competing candidate, discarded by the maximum |
| 6 | yes | no | no | decoy: a large positive with no negative counterpart |
| 7 | yes | yes | yes | winning candidate, $k^{*} = 7$ |
| 10 | yes | no | no | the largest value in the array, still inadmissible |

Two readings of the trace deserve emphasis. First, step 3 shows the accumulator reaching a positive value before the scan has seen the winning magnitude; intermediate accumulator values are not answers, only the final one is. Second, the magnitude table shows that `10`, the maximum of the input, plays no role at all — it fails $q$ and is never a candidate.

## 5. Correctness: Why the Scan Neither Misses nor Overshoots

**Soundness.** Suppose the scan finishes with some value $v \neq -1$ in the accumulator. Then $v$ was examined and $q(v)$ held, so $-v \in S$. Because $S$ was built from `nums`, both $v$ and $-v$ occur in the original array. Under the no-zero guarantee, $v$ has a qualifying opposite that is strictly larger if $v < 0$, so the accumulator — being a maximum over qualifying values — can only settle on a non-negative, hence positive, magnitude. That magnitude is therefore a legitimate witness for the contract.

**Completeness.** Let $k$ be any admissible magnitude, so $\{k, -k\} \subseteq S$. Negation symmetry puts $k$ among the qualifying values, hence $k$ is examined during the scan and is available to the accumulator. By iteration 3 of the invariant, the final accumulator is at least $k$. Since $k$ was arbitrary, the accumulator is at least every admissible magnitude, and combined with soundness it is exactly $k^{*}$.

**Sentinel path.** If no value satisfies $q$, the qualifying family is empty, no admissible magnitude exists by the definition of $q$, and `-1` is the value the contract demands. The sentinel is also unreachable by accident: admissible magnitudes are positive, so they can never equal `-1`.

The argument never inspects a pair of positions, which is the point — completeness is inherited from the fact that the family of qualifying *values* is exactly the family of admissible *magnitudes*, and a maximum over a finite non-empty family always exists.

## 6. Boundary and Trap Analysis

| Boundary situation | Instance | Result | Why the rule handles it |
|:---|:---|:---:|:---|
| Sentinel path | `nums = [-10, 8, 6, 7, -2, -3]` | `-1` | no value has its opposite in $S$, so nothing qualifies and the sentinel stands |
| All values negative | `nums = [-1, -2, -3]` | `-1` | a candidate pair needs both signs; the positive member is absent from the array |
| Duplicates on both sides | `nums = [-5, -5, 5, 5, 2]` | `5` | multiplicity is erased by $S$; one surviving copy of each sign is enough |
| Order inversion | `nums = [42, 7, -42, -3]` | `42` | the positive twin appears before its negative twin; existence is order-free |
| Largest allowed magnitude | `nums = [999, -999, -1000, 1000]` | `1000` | both extremes of the permitted domain form a pair, and the maximum of the two admissible magnitudes wins |
| Zero present (excluded by the constraints) | `nums = [0, 2]` | would be `0`; the contract wants `-1` | $-0 = 0$ makes zero a self-paired value, so the symmetric test alone would be wrong |
| Minimum length | `nums = [7]` | `-1` | the only element cannot supply a distinct opposite, and zero is excluded |
| Two equal admissible magnitudes | `nums = [-3, 3, 3, -3]` | `3` | the pair collapses to one magnitude; the maximum is unaffected by how often it was confirmed |

The trap that this instance punishes hardest is treating the array maximum as a starting point. `10` is the largest value present, yet it is worthless because `-10` is missing; a method that seeds its accumulator with the array maximum and then validates downward would still be correct but would waste effort, whereas seeding with the sentinel and scanning the distinct values costs nothing extra.

## 7. Alternatives That Lose on This Problem

| Method | Expected time | Auxiliary space | Verdict |
|:---|:---:|:---:|:---|
| Membership set plus one maximum scan | $O(n)$ | $O(n)$ | the method derived above |
| Same set with an explicit positivity filter | $O(n)$ | $O(n)$ | identical cost and identical result, since zero is excluded; it states intent more loudly |
| Sort the array, then walk two pointers inward | $O(n \log n)$ | $O(n)$ for the sorted copy | correct, but it buys an ordering that the contract never uses |
| All-pairs search for a zero sum | $O(n^2)$ | $O(1)$ | easiest to state and verify, quadratically slower |
| Direct-address presence array over $[-1000, 1000]$ | $O(n + U)$, $U = 2001$ | $O(U)$ | deterministic constant-time membership, but the cost is governed by the constraint domain rather than by $n$ |

The two linear methods agree exactly because the symmetry invariant makes the positivity filter redundant. The sorted method is interesting only as a demonstration that the problem is not about order; the pairwise method is the honest brute force whose quadratic factor the set removes.

## 8. Time and Auxiliary-Space Complexity Derivation

Let $n = \lvert \texttt{nums} \rvert$ and let $\lvert S \rvert \le n$ be the number of distinct values.

| Phase | Work performed | Cost |
|:---|:---|:---|
| Build $S$ | one insertion per array element; repeated values collapse automatically | expected $O(n)$ |
| Scan | at most $\lvert S \rvert$ values, one membership lookup and one comparison each | expected $O(n)$ |
| Select | keep a single current best across the scan | $O(\lvert S \rvert)$ |
| **Time** | sum of the phases | **expected $O(n)$** |
| **Auxiliary space** | the set holds at most $n$ integers; the accumulator is one scalar and one lookup result | **$O(n)$** |

Hash-set operations are expected constant time under a well-distributed hash, so the whole bound is expected rather than worst case; an adversarial collision pattern could in principle degrade individual lookups to linear time. That risk is not mitigated by the input, because the constraint domain is small and dense: the alternative row above shows that a fixed presence table over the $2001$ permitted values turns the same scan into a deterministic $O(n + U)$ procedure with $O(U)$ storage. Neither variant allocates anything proportional to the number of pairs, and no candidate list is ever materialised — the accumulator keeps only the current best, so the auxiliary space is dominated entirely by the membership structure.
