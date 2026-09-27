# Guided Example: Find Median Given Frequency of Numbers

`Numbers` is a run-length encoding of an integer sample: each row names one distinct value and how many times it occurs. Expanding those counts into a flat sorted sample is the obvious reading of the task and also the one that fails at scale, so this lesson stays inside the compressed representation. Four rows are ordered instead of twelve values, and the median falls out of two cumulative-mass ranks whose intersection isolates the run of positions straddling the sample's midpoint.

## 1. The Instance and the Required Outcome

| `num` | `frequency` |
|:---:|:---:|
| 0 | 7 |
| 1 | 1 |
| 2 | 3 |
| 3 | 1 |

Read as a multiset, the table describes the sample $[\,0,0,0,0,0,0,0,\;1,\;2,2,2,\;3\,]$, which holds $T = 7 + 1 + 3 + 1 = 12$ numbers. Because $T$ is even, the median is the mean of the 6th and 7th smallest entries, and both positions lie inside the run of seven zeros, so the median is $0$. The required result is one row:

| `median` |
|:---:|
| 0.0 |

Two details of the contract shape everything below. The comparison happens on the *expanded* sample, never on the distinct values, so the mean of the four stored values — $1.5$ — is not the answer. And the reported number is rounded to one decimal place, so an integer median must still print as $0.0$ rather than $0$.

## 2. Position Blocks in the Compressed Sample

Let $R$ be the row count and $T = \sum \text{frequency}$ the sample size. Materialising the sample costs $\Theta(T)$ storage, and the gap between $T$ and $R$ is the entire reason the input has this shape: two rows can describe a sample of a billion numbers. Instead of positions, the compressed view holds intervals. Index the rows $i = 1, \dots, R$ by ascending `num`, and let $f_i$ be the frequency of row $i$. Row $i$ covers the contiguous block

$$
L_i = 1 + \sum_{j<i} f_j, \qquad R_i = L_i + f_i - 1,
$$

and the blocks $[L_i, R_i]$ partition $\{1, \dots, T\}$ exactly.

| Row $i$ | `num` | $f_i$ | First position $L_i$ | Last position $R_i$ | Positions covered |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | 0 | 7 | 1 | 7 | 1–7 |
| 2 | 1 | 1 | 8 | 8 | 8 |
| 3 | 2 | 3 | 9 | 11 | 9–11 |
| 4 | 3 | 1 | 12 | 12 | 12 |

The central positions of this instance are 6 and 7, both inside row 1's block $[1,7]$. The task is to detect that containment without ever enumerating a position.

## 3. The Two Cumulative Mass Ranks

Define the forward and backward ranks of row $i$:

$$
rk_1(i) = \sum_{j \le i} f_j = R_i, \qquad rk_2(i) = \sum_{j \ge i} f_j = T - L_i + 1 .
$$

The forward rank is the running total of `frequency` in ascending `num` order; the backward rank is the same running total in descending order. Each is a single ordered pass over the compressed rows, so neither expands anything.

| Row $i$ | `num` | $f_i$ | $rk_1(i)$ | $rk_2(i)$ | Check: $rk_1 + rk_2 = T + f_i$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | 0 | 7 | 7 | 12 | $19 = 19$ |
| 2 | 1 | 1 | 8 | 5 | $13 = 13$ |
| 3 | 2 | 3 | 11 | 4 | $15 = 15$ |
| 4 | 3 | 1 | 12 | 1 | $13 = 13$ |

Row $i$ is counted by both ranks while every other row is counted by exactly one, which is why $rk_1(i) + rk_2(i) = T + f_i$. The identity confirms that the two ranks are two views of one total mass, and that no row can sit near the end of both orders unless it holds a large share of that mass.

## 4. The Half-Mass Intersection Criterion

For the even sample $T = 12$ the central positions are 6 and 7. Consider the candidate condition

$$
rk_1(i) \ge \frac{T}{2} \quad \text{and} \quad rk_2(i) \ge \frac{T}{2}.
$$

In terms of block boundaries, $rk_1(i) \ge T/2$ says $R_i \ge T/2$ and $rk_2(i) \ge T/2$ says $T - L_i + 1 \ge T/2$, that is $L_i \le T/2 + 1$. So the condition says exactly that $[L_i, R_i]$ meets the one- or two-position loop of central positions. For this instance that loop is $\{6, 7\}$ and the threshold is $6$:

| Row $i$ | `num` | $rk_1(i)$ | $rk_1 \ge 6$? | $rk_2(i)$ | $rk_2 \ge 6$? | Both hold? | Block meets $\{6,7\}$? |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | 0 | 7 | yes | 12 | yes | **yes** | yes, $[1,7]$ covers both |
| 2 | 1 | 8 | yes | 5 | no | no | no, $[8,8]$ starts after 7 |
| 3 | 2 | 11 | yes | 4 | no | no | no, $[9,11]$ starts after 7 |
| 4 | 3 | 12 | yes | 1 | no | no | no, $[12,12]$ starts after 7 |

Exactly one row survives, and the answer is the mean of the surviving `num` values:

$$
\mathrm{median} = \mathrm{round}\!\left(\frac{0}{1},\, 1\right) = 0.0 .
$$

No special case is needed for odd and even sample sizes. The criterion returns one surviving row when a single run covers the centre and two when the centre falls on a run boundary, where the mean of the two `num` values is by definition the mean of the two central order statistics.

> **Central-window invariant.** For any sample, the rows satisfying $rk_1 \ge T/2$ and $rk_2 \ge T/2$ are exactly the runs whose position block meets the loop of central positions, and there are either one or two of them.

## 5. Worked Trace of the Official Instance

| Step | Row inspected | Ascending running total | Descending running total | Threshold $\frac{12}{2}$ | Decision |
|:---:|:---:|:---:|:---:|:---:|:---|
| 1 | `num = 0`, `frequency = 7` | $0 + 7 = 7$ | $7 + 1 + 3 + 1 = 12$ | 6 | $7 \ge 6$ and $12 \ge 6$ — retain |
| 2 | `num = 1`, `frequency = 1` | $7 + 1 = 8$ | $1 + 3 + 1 = 5$ | 6 | $5 < 6$ — discard |
| 3 | `num = 2`, `frequency = 3` | $8 + 3 = 11$ | $3 + 1 = 4$ | 6 | $4 < 6$ — discard |
| 4 | `num = 3`, `frequency = 1` | $11 + 1 = 12$ | $1$ | 6 | $1 < 6$ — discard |
| 5 | surviving set | — | — | — | $\{0\}$, so $\mathrm{mean}\{0\} = 0$ rounded to $0.0$ |

## 6. Correctness of the Intersection Criterion

Let $\mathcal{M}$ be the loop of central positions: $\{T/2, T/2+1\}$ for even $T$ and $\{\lceil T/2 \rceil\}$ for odd $T$. The claim is that row $i$ satisfies both inequalities if and only if $[L_i, R_i] \cap \mathcal{M} \neq \emptyset$.

If both inequalities hold, then $R_i \ge T/2$ and $L_i \le T/2 + 1$, so the non-empty block starts no later than the position after the midpoint and ends no earlier than the midpoint; it must therefore contain a member of $\{T/2, T/2+1\}$, a superset of $\mathcal{M}$. Conversely, if the block meets $\mathcal{M}$, then $R_i \ge \min \mathcal{M} \ge T/2$, giving $rk_1(i) \ge T/2$, and $L_i \le \max \mathcal{M} \le T/2+1$, giving $rk_2(i) = T - L_i + 1 \ge T/2$.

Because the blocks partition all positions, at most two can meet a loop of at most two adjacent positions, which proves the cardinality claim. The median of an expanded sample is the mean of the values at its central positions, so averaging the surviving `num` values returns that quantity; a single survivor owns both central positions, so its value is simply repeated. Three authored checks confirm the criterion outside the official example:

| Instance | Expanded sample | $T$ | Central loop | Surviving rows | Median |
|:---|:---|:---:|:---:|:---|:---:|
| `num` 1 and 3, one each | $[1, 3]$ | 2 | $\{1, 2\}$ | both rows | $2$ |
| `num` 1 twice, `num` 5 twice | $[1,1,5,5]$ | 4 | $\{2, 3\}$ | both rows | $3$ |
| `num` 1, 2, 3, one each | $[1, 2, 3]$ | 3 | $\{2\}$ | `num = 2` only | $2$ |

## 7. Boundary Cases and Alternative Strategies

| Situation | Behaviour of the criterion | Consequence |
|:---|:---|:---|
| Odd $T$, one run covers the centre | exactly one row survives | the median is that `num` |
| Even $T$, centre on a run boundary | exactly two rows survive | their mean, for example $1.5$ |
| Even $T$, one run owns both central positions | exactly one row survives | its value, as in the official instance |
| `Numbers` holding a single row | $rk_1 = rk_2 = T \ge T/2$ | that row always survives, even at `frequency = 100` |
| Very large `frequency` | both ranks are integers of the same magnitude | cost is unchanged; nothing is expanded |
| Negative and positive `num` | ordering is numeric, not by appearance | `-5`, `0`, `10` are ordered before the ranks are built |

| Strategy | Relational shape | Cost | Assessment |
|:---|:---|:---|:---|
| Expand, sort, index the centre | one row per unit of frequency | $\Theta(T \log T)$ time, $\Theta(T)$ space | correct but unusable |
| Recursive row generation from `frequency` | iterative expansion by a counter | $\Theta(T)$ time, deep recursion | hits memory and recursion limits |
| Self-join on position containment | pair every row with its predecessors | $\Theta(R^2)$ | quadratic cost for information one pass already yields |
| Cumulative ranks plus the intersection test | two ordered running totals | $\Theta(R \log R)$ time, $\Theta(R)$ space | the method traced above |

Two near-misses are worth naming. Ordering the running totals by `frequency` instead of `num` breaks the block partition: the accumulating sequence would no longer follow sample order, and the surviving rows would have nothing to do with the centre. And comparing against a truncated $T/2$ shifts the boundary for odd samples, where the honest test is $rk_1 \ge \lceil T/2 \rceil$; the mean must also be taken over the surviving `num` values alone, since averaging every row happens to look plausible here only because the single survivor is $0$.

## 8. Complexity Derivation

Let $R$ be the number of rows in `Numbers`, which is the number of distinct sample values.

- **Time.** Each rank is a running total over an ordering of `num`, which costs $\Theta(R \log R)$ comparisons to produce and $\Theta(R)$ to accumulate. The intersection test is one comparison per row and the final mean touches only the survivors, so both are $\Theta(R)$. Total: $\Theta(R \log R)$, with no dependence on $T$.
- **Auxiliary space.** Two integers per row are materialised, so $\Theta(R)$ working memory, and the result is a single row. Nothing proportional to $T$ is ever allocated, which is precisely the advantage the compressed input was designed to give.

For the official instance $R = 4$: four items are ordered and eight rank integers are held, even though the sample they describe contains twelve values. A table whose frequencies sum to a billion costs the same.