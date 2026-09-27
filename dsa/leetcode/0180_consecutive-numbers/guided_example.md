# Guided Example: Consecutive Numbers

`Logs` records a value per row, and the row identifiers define the sequence in which those values were written. A number qualifies when it appears on at least three rows that follow one another in that sequence. The result is one row per qualifying number under the column `ConsecutiveNums`, in any order, and an empty result is the correct answer when nothing qualifies.

## 1. The Instance and the Meaning of "Consecutive"

The worked instance is the official seven-row log.

| `id` | `num` |
|:---:|:---:|
| 1 | 1 |
| 2 | 1 |
| 3 | 1 |
| 4 | 2 |
| 5 | 1 |
| 6 | 2 |
| 7 | 2 |

Two readings of "consecutive" are possible, and only one of them is correct here:

| Reading | Definition used | Status for this problem |
|:---|:---|:---|
| Sequence-adjacent | Position $i$ and position $i+1$ in `id` order carry the same value | This is the intended meaning. |
| Arithmetically adjacent | Identifiers differ by exactly 1, so rows $i$ and $i+1$ pair up | Equivalent only while the identifiers happen to be dense. |

The distinction matters because the identifiers are described as an autoincrementing primary key, but a sequence is defined by its order rather than by the literal gap between successive key values. Section 4 shows a concrete case where the two readings disagree.

## 2. Maximal Runs in `id` Order

A **run** of a value $v$ is a maximal block of consecutive positions in the `id`-ordered sequence whose `num` equals $v$. Maximising the block is what makes runs a clean model: every position belongs to exactly one run, and the runs partition the whole sequence.

| Run | Value | Positions (`id`) | Length | Length $\ge 3$? |
|:---:|:---:|:---|:---:|:---:|
| 1 | 1 | 1, 2, 3 | 3 | yes |
| 2 | 2 | 4 | 1 | no |
| 3 | 1 | 5 | 1 | no |
| 4 | 2 | 6, 7 | 2 | no |

The run lengths sum to $3 + 1 + 1 + 2 = 7 = \lvert \texttt{Logs} \rvert$, which confirms that the four runs partition the sequence.

Only run 1 reaches the threshold, so the qualifying value set is $\{1\}$. Notice that value $1$ appears on four rows in total yet still qualifies through one run of length 3; the recurrence at position 5 is a separate run of length 1 and neither extends nor rescues the earlier run. Likewise value $2$ appears three times overall, but split into runs of lengths 1 and 2, so it never qualifies — a total count of three is not the same as three consecutive occurrences.

| Value | Total occurrences | Maximal run length | Qualifies? | Why |
|:---:|:---:|:---:|:---:|:---|
| 1 | 4 | 3 | yes | One run of length 3 satisfies the threshold. |
| 2 | 3 | 2 | no | Occurrences are split across runs of lengths 1 and 2. |

## 3. Sliding Triple Lookahead Over the Sequence

A run of length at least 3 exists for a value exactly when some position $i$ satisfies

$$ \text{num}_i = \text{num}_{i+1} = \text{num}_{i+2}, $$

so a single ordered sweep that inspects each position together with its two successors detects every qualifying value. Writing $\text{next}_1(i) = \text{num}_{i+1}$ and $\text{next}_2(i) = \text{num}_{i+2}$, the sweep behaves as follows.

| `id` $i$ | `num`$_i$ | next$_1$ | next$_2$ | $\text{num}_i = \text{next}_1 = \text{next}_2$? | Verdict |
|:---:|:---:|:---:|:---:|:---:|:---|
| 1 | 1 | 1 | 1 | true | Run of length 3 anchored at positions 1–3 |
| 2 | 1 | 1 | 2 | false | Triple breaks at position 4 |
| 3 | 1 | 2 | 1 | false | Triple breaks immediately |
| 4 | 2 | 1 | 2 | false | Value changes at the next position |
| 5 | 1 | 2 | 2 | false | Value changes at the next position |
| 6 | 2 | 2 | past the end | unsatisfiable | Fewer than three positions remain |
| 7 | 2 | past the end | past the end | unsatisfiable | Fewer than three positions remain |

Every position that anchors a qualifying run produces a `true` in column five; here only position 1 does. The candidate values collected during the sweep are therefore $\{1\}$, and one projection step emits a single row:

| `ConsecutiveNums` |
|:---:|
| 1 |

The two trailing positions deserve a comment. There is no successor value for them, so the equality cannot be satisfied. This is a property of comparing against an absent value rather than a special case that needs its own branch: an absent value is never equal to a present one, so the anchor condition simply fails.

## 4. Fixed-Offset Triple Matching and Its Fragility

A three-way match over ordered positions can also be expressed by pairing each row with the row one step ahead and the row two steps ahead on the sequence. That formulation is conceptually identical to the lookahead sweep, but the two differ in how they obtain the successor positions.

| Aspect | Successor located by key arithmetic | Successor located by sequence order |
|:---|:---|:---|
| Depends on identifiers being dense | yes | no |
| Correct after rows were deleted | no | yes |
| Cost with a unique index | one probe per pairing, $O(N)$ total | one ordered pass, $O(N)$ total |
| Cost without a usable index | nested or hash pairing over all rows | an ordering step plus one pass |
| Behaviour at the end of the sequence | no partner row exists, so the pairing simply yields nothing | successor value is absent, so the comparison is unsatisfied |
| Duplicate suppression still required | yes | yes |

A concrete instance separates the two. Consider a table whose identifiers are $1, 3, 4$ and whose values are all $9$:

| `id` | `num` | Formal successor by order | Successor by key arithmetic |
|:---:|:---:|:---:|:---:|
| 1 | 9 | `id` 3 has value 9 | no row with `id` 2 exists |
| 3 | 9 | `id` 4 has value 9 | row with `id` 4 exists and carries 9 |
| 4 | 9 | no further row | no row with `id` 5 exists |

By sequence order the three rows form one run of a single value and it qualifies; by key arithmetic the identifiers are not dense and the run is invisible. The order-based reading is the one the contract describes, so the lookahead formulation is the robust choice.

## 5. Why the Reasoning Is Correct

**Invariant.** For a value $v$, the following three statements are equivalent: $v$ occurs on at least three consecutive positions; the maximal run of $v$ has length at least 3; and there exists a position $i$ with $\text{num}_i = \text{num}_{i+1} = \text{num}_{i+2} = v$.

*Soundness.* If the anchor condition holds at position $i$, then positions $i$, $i+1$ and $i+2$ are consecutive, carry the same value, and form a block of length at least 3, so $v$ genuinely occurs at least three times consecutively. The lookahead never reports a value that fails the requirement.

*Completeness.* Suppose the maximal run of $v$ has length $L \ge 3$ and starts at position $j$. Then positions $j$, $j+1$ and $j+2$ all carry $v$, so the anchor condition holds at $j$ and the sweep detects the run at its first position. Values whose maximal run is shorter than 3 have no position whose two successors still carry the same value, so they are never reported.

*Why duplicate suppression is mandatory.* One run of length $L \ge 3$ satisfies the anchor condition at $L - 2$ different positions, so without projection onto distinct values the same number would be emitted several times.

| Maximal run length $L$ | Anchoring positions, $\max(0, L-2)$ | Required emissions after deduplication |
|:---:|:---:|:---:|
| 2 | 0 | 0 |
| 3 | 1 | 1 |
| 4 | 2 | 1 |
| 5 | 3 | 1 |
| $L$ | $\max(0, L-2)$ | 1 when $L \ge 3$, otherwise 0 |

## 6. Boundary Conditions This Instance Exposes

| Scenario | Instance | Result | Reason |
|:---|:---|:---|:---|
| Exactly two consecutive occurrences | `id` 1 and 2 both carry value 5 | empty result | The maximal run has length 2, below the threshold. |
| Exactly three consecutive occurrences | `id` 1, 2, 3 all carry value 1 | one row, value 1 | The threshold is inclusive. |
| Four consecutive occurrences | `id` 1 to 4 all carry value 2 | one row, value 2 | Overlapping triples collapse under deduplication. |
| Two separate qualifying values | three consecutive 3s, then three consecutive 4s | rows for 3 and 4 | Each value qualifies through its own run. |
| Recurrence after a break | three consecutive 1s, then a single 1 later | one row, value 1 | The later occurrence is a separate run of length 1 and neither extends nor merges. |
| Fewer than three rows in the table | `id` 1 and 2 only | empty result | No position can anchor a triple. |
| Positions near the end | the last two `id` values | never reported | Their successors are absent, so the equality is unsatisfied. |
| Empty result is legal | nothing qualifies | zero rows | The contract asks for one row per qualifying value, so an empty relation is a correct answer, not a `null`. |
| Output order | any qualifying set | any order | The statement accepts any order, so no ordering step is required for correctness. |

## 7. Complexity Derivation

Let $N = \lvert \texttt{Logs} \rvert$ and let $K \le N$ be the number of distinct values in the relation.

| Stage | Work | Cost |
|:---|:---|:---|
| Obtain rows in sequence order | ordering by `id`, if the stored order is not already usable | $O(N \log N)$, or $O(N)$ when the primary-key order can be read directly |
| Sweep once, comparing each position with its two successors | two comparisons per position | $O(N)$ |
| Collect candidate values and project them onto distinct values | hashing the candidates, or ordering the at most $N$ candidates | $O(N)$ expected, $O(K \log K)$ if ordered |
| Total | ordering dominates | $O(N \log N)$ worst case; $O(N)$ when sequence order comes for free |

The sweep alone needs only the two successor values of the current position, so it is a streaming computation: it can decide each anchor as soon as the two following rows have been read. It cannot, however, decide the final answer before reading the whole relation, because the last rows of the table are precisely the ones whose successor values are absent.

**Auxiliary space.** Keeping only the current value and its two successors requires $O(1)$ state, while retaining the distinct qualifying values costs $O(K)$ memory for the output set. A windowed implementation that materialises the successors for every row at once uses $O(N)$ buffer space; the streaming variant trades that buffer for a constant amount of state without changing the time bound.