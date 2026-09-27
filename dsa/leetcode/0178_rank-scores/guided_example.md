# Guided Example: Rank Scores

A `Scores` relation stores one game score per row, and equal scores may appear on several rows. The task is to attach a competition rank to every row: larger scores receive smaller rank numbers, equal scores share one rank, and the next different score receives the next consecutive integer, so no holes ever appear between ranks. Every input row survives, and the result is presented with scores from largest to smallest.

## 1. The Instance and the Ranking Contract

| `id` | `score` |
|:---:|:---:|
| 1 | 3.50 |
| 2 | 3.65 |
| 3 | 4.00 |
| 4 | 3.85 |
| 5 | 4.00 |
| 6 | 3.65 |

The four contract rules, stated as properties the output must satisfy:

| Rule | Requirement | Consequence for this instance |
|:---:|:---|:---|
| 1 | Rank scores from highest to lowest | $4.00$ gets the smallest rank number |
| 2 | Tied scores share one rank | Both $4.00$ rows receive the same rank |
| 3 | Next different score gets the next consecutive integer | $3.85$ must receive rank 2, not rank 3 |
| 4 | Return the result ordered by score descending | No row may be dropped or reordered arbitrarily |

The required result therefore has six rows, exactly as many as the input:

| `score` | `rank` |
|:---:|:---:|
| 4.00 | 1 |
| 4.00 | 1 |
| 3.85 | 2 |
| 3.65 | 3 |
| 3.65 | 3 |
| 3.50 | 4 |

## 2. Peer Groups in the Descending Order

Group the rows by equal score. Each such group is a **peer group**: a maximal set of rows that must all receive the same rank. Ordering the groups from largest score to smallest turns the problem into a positional one.

| Rank | Distinct score of the group | Rows in this peer group | Group size |
|:---:|:---:|:---|:---:|
| 1 | 4.00 | `id` 3, `id` 5 | 2 |
| 2 | 3.85 | `id` 4 | 1 |
| 3 | 3.65 | `id` 2, `id` 6 | 2 |
| 4 | 3.50 | `id` 1 | 1 |

Because rule 3 forbids holes, the rank of a peer group is exactly its one-based position in this descending list of groups. That yields the closed form used to check the assignment:

$$ \operatorname{rank}(v) = 1 + \lvert\{\, u \in D : u > v \,\}\rvert, \qquad D = \text{the set of distinct scores}. $$

| Distinct score $v$ | Distinct scores greater than $v$ | Count | $\operatorname{rank}(v)$ |
|:---:|:---|:---:|:---:|
| 4.00 | none | 0 | 1 |
| 3.85 | 4.00 | 1 | 2 |
| 3.65 | 4.00, 3.85 | 2 | 3 |
| 3.50 | 4.00, 3.85, 3.65 | 3 | 4 |

This counting definition and the peer-group position definition agree by construction, and the agreement is worth noticing: it means correctness can be argued either positionally (walk the sorted groups) or arithmetically (count strictly greater distinct values) without changing the answer.

## 3. Step-by-Step Assignment Over the Ordered Rows

Order the six rows by score from largest to smallest, then sweep once, comparing each row with its predecessor.

| Position | `id` | `score` | Peer group | Predecessor score | Same peer group? | Assigned `rank` |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | 3 | 4.00 | 1 | — | no predecessor; a new group starts | 1 |
| 2 | 5 | 4.00 | 1 | 4.00 | yes | 1 |
| 3 | 4 | 3.85 | 2 | 4.00 | no | 2 |
| 4 | 2 | 3.65 | 3 | 3.85 | no | 3 |
| 5 | 6 | 3.65 | 3 | 3.65 | yes | 3 |
| 6 | 1 | 3.50 | 4 | 3.65 | no | 4 |

The sweep only ever increments the rank counter when the score actually changes, which is exactly what rule 3 demands. Positions 2 and 5 show the tie behaviour: no increment happens inside a peer group.

One presentation detail is easy to conflate with the ranking rule itself, so it is worth separating explicitly.

| Concern | What it determines | What it does *not* determine |
|:---|:---|:---|
| Ranking order | Which direction the scores are compared for rank computation | The order in which the result rows are returned |
| Presentation order | The order of rows in the emitted relation | The rank values themselves |

Rule 4 is a separate requirement from rules 1–3: an ordering used to compute ranks is not by itself a guarantee about the order in which the result is presented, so the presentation ordering must be stated as part of the contract rather than assumed.

## 4. Why Sparse Ranking and Row Numbering Fail

Three closely related tie policies are easy to confuse. Only one satisfies all four rules on this instance.

| Policy | Ranks produced for $[4.00, 4.00, 3.85, 3.65, 3.65, 3.50]$ | Satisfies the contract? | Failure mode |
|:---|:---|:---:|:---|
| Row numbering | $1, 2, 3, 4, 5, 6$ | no | Ties are broken arbitrarily, violating rule 2. |
| Sparse ranking | $1, 1, 3, 4, 4, 6$ | no | Ranks jump after a tie, violating rule 3: $3.85$ receives 3 instead of 2. |
| Dense ranking | $1, 1, 2, 3, 3, 4$ | yes | — |
| Grouping with collapse | one row per distinct score, four rows in total | no | Aggregation removes rows, violating the requirement that all six input rows appear. |

The two workable conceptual formulations differ in cost and in how directly they express the rule:

| Formulation | Idea | Ordering-gap behaviour | Cost |
|:---|:---|:---|:---|
| Dense rank over a descending ordering | Rank equals the position of the peer group | No holes by definition | $O(N \log N)$ for the ordering, $O(N)$ for the sweep |
| Count of distinct scores at least as large | Rank equals $1$ plus the count of strictly greater distinct scores | No holes, since distinct values are counted once | $O(N \log N)$ or better with sorting; a per-row scan without an index degrades to $O(N^2)$ |

## 5. Why the Reasoning Is Correct

**Invariant.** Let $D = \{v_1 > v_2 > \dots > v_d\}$ be the distinct scores ordered from largest to smallest. Every row whose score is $v_k$ receives rank $k$, so equal scores receive equal ranks and consecutive distinct values receive consecutive integers.

*Soundness.* Any row is a member of exactly one peer group, because equality partitions the rows. Sweeping the groups in descending order and incrementing the counter only on a change of value assigns $k$ to the group at position $k$. Since $\operatorname{rank}(v_k) = 1 + \lvert\{u \in D : u > v_k\}\rvert = k$, the sweep and the counting definition agree, so the assignment satisfies rules 1 and 2.

*Completeness and dense-ness.* Distinct values $v_k$ and $v_{k+1}$ are adjacent in the ordered list, so their ranks differ by exactly 1; no integer between two used ranks can be skipped. Rule 3 therefore holds for every adjacent pair, and by transitivity for the whole sequence. Since the assignment is defined on all rows and removes none, all six rows of the instance appear in the output.

*Uniqueness.* The three rules force the assignment completely: rule 1 fixes which end receives rank 1, rule 2 forces equal scores to coincide, and rule 3 forces each subsequent distinct value to take the next integer. Hence dense ranking is not merely one acceptable policy; it is the only one the contract permits.

## 6. Boundary Conditions This Instance Exposes

| Scenario | Instance | Result | Reason |
|:---|:---|:---|:---|
| Single row | `[(1, 8)]` | `[(8, 1)]` | One peer group at position 1. |
| All scores tied | `[(1,5),(2,5),(3,5)]` | ranks $1, 1, 1$ | A single peer group, so only rank 1 is used. |
| Negative scores | `[(1,-2),(2,0),(3,-2),(4,-1)]` | $0 \to 1$, $-1 \to 2$, $-2 \to 3$ for both tied rows | Ordering is on the numeric domain, so signs are irrelevant. |
| Tie at the maximum | the worked instance | both $4.00$ rows rank 1, then $3.85$ ranks 2 | The dense policy resumes at the next integer after a tie. |
| Tie in the middle | the worked instance | both $3.65$ rows rank 3, then $3.50$ ranks 4 | No hole is introduced between groups. |
| Rank column identity | any instance | the rank column must carry the exact required name | An engine may treat the word `rank` as reserved, so the emitted identifier must be produced exactly as specified. |

## 7. Complexity Derivation

Let $N$ be the number of rows in `Scores` and $d \le N$ the number of distinct scores.

| Stage | Work | Cost |
|:---|:---|:---|
| Order the rows by score from largest to smallest | comparison sort of $N$ values | $O(N \log N)$, or $O(N)$ when an index on `score` already delivers the order |
| Sweep the ordered rows, comparing each with its predecessor | one comparison and at most one counter increment per row | $O(N)$ |
| Emit all $N$ rows with their rank | one projection per row | $O(N)$ |
| Total | ordering dominates | $O(N \log N)$ worst case; $O(N)$ when the ordering is free |

The ordering step cannot be avoided in general: distinguishing the peer groups requires knowing the relative order of the distinct values, and comparison-based ordering of $d$ distinct values has an $\Omega(d \log d)$ lower bound. Reading the relation contributes the separate $\Omega(N)$ lower bound, which the sweep already meets.

**Auxiliary space.** The sweep needs one buffer for the ordered rows and a constant number of state variables, so the auxiliary cost is $O(N)$ for the ordered copy and $O(1)$ beyond it. If the ordering is supplied by an index, only the constant state remains. The $N$ emitted rows are the required output and are not counted as auxiliary space.