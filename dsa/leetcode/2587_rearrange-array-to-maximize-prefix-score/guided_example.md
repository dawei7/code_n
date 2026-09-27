# Guided Example: Rearrange Array to Maximize Prefix Score

## 1. The instance and what has to be maximised

Take

$$
\texttt{nums} = [2, -1, 0, 1, -3, 3, -3],
$$

an array of $n = 7$ integers whose total sum is $-1$. Any permutation of these seven values is allowed, and each permutation produces a `prefix` array of running sums. The **score** of a permutation is the number of entries in its `prefix` array that are *strictly* positive, and the task is to report the largest score any permutation can reach. For this instance the answer is `6`.

The instance is a good one because it punishes three plausible shortcuts at once. Its total sum is negative, so some prefix must fail; it contains a zero, which changes no running sum but still occupies a prefix position; and it contains three negatives, so the ordering of the tail decides whether a positive running sum survives long enough to keep counting.

## 2. Prefix sums, the objective, and where the freedom lies

For a permutation $a_1, a_2, \dots, a_n$ of the array, the prefix sums are

$$
P_k = a_1 + a_2 + \dots + a_k, \qquad 1 \le k \le n,
$$

and the score is the number of indices $k$ with $P_k > 0$. Writing the answer as a sum of indicators makes the objective explicit:

$$
\text{score}(a) = \sum_{k=1}^{n} \bigl[\,P_k > 0\,\bigr],
\qquad
\bigl[\,P_k > 0\,\bigr] =
\begin{cases}
1 & \text{if } P_k > 0,\\
0 & \text{if } P_k \le 0 .
\end{cases}
$$

The freedom is purely *positional*: the multiset of values is fixed, so the total sum $P_n = -1$ is fixed and the last prefix can never be positive here. What the ordering does control is how long the running sum stays above zero. Note also that the test is strict, so a prefix equal to `0` scores nothing — a boundary that matters in Section 6.

## 3. The ordering that maximises every prefix at once

The original order is a trap: it looks harmless, but it wastes score.

| Position $k$ | Original order $a_k$ | Running sum $P_k$ | $P_k > 0$? | Descending order $a_k$ | Running sum $P_k$ | $P_k > 0$? |
|---|---|---|---|---|---|---|
| 1 | `2` | `2` | yes | `3` | `3` | yes |
| 2 | `-1` | `1` | yes | `2` | `5` | yes |
| 3 | `0` | `1` | yes | `1` | `6` | yes |
| 4 | `1` | `2` | yes | `0` | `6` | yes |
| 5 | `-3` | `-1` | no | `-1` | `5` | yes |
| 6 | `3` | `2` | yes | `-3` | `2` | yes |
| 7 | `-3` | `-1` | no | `-3` | `-1` | no |
| — | score | — | `5` | score | — | `6` |

The original order scores `5` because the `-3` at position $5$ pushes the running sum to `-1` while the largest value, `3`, has not been placed yet; that later positive restores positivity at position $6$, but the prefix at position $5$ is lost for good. The descending order — `[3, 2, 1, 0, -1, -3, -3]` — keeps the running sum positive for six positions, and its score is `6`.

The comparison shows the mechanism: a prefix is damaged only by elements placed too early, so the cheap fix is to spend the large values first and defer the damaging ones. Because $P_k = P_{k-1} + a_k$, each prefix is at least as large when the sequence is arranged in non-increasing order, and that is the classical majorisation statement: the sorted-descending sequence dominates every other ordering in every prefix simultaneously. No arrangement can have a larger $P_k$ at any position $k$ than the descending one, so no arrangement can make an extra position positive that the descending one leaves non-positive.

## 4. Executing the greedy sweep

Sort the values in non-increasing order and accumulate, counting strictly positive running sums:

| Step $k$ | Value added $a_k$ | Running sum after the step | $P_k > 0$? | Score so far | Comment |
|---|---|---|---|---|---|
| 1 | `3` | `3` | yes | 1 | The largest value alone already gives a positive prefix |
| 2 | `2` | `5` | yes | 2 | Two positives spent first |
| 3 | `1` | `6` | yes | 3 | The best possible sum of any three elements |
| 4 | `0` | `6` | yes | 4 | The zero costs nothing and still occupies a prefix position, so it is free score |
| 5 | `-1` | `5` | yes | 5 | The buffer of `6` absorbs the first negative |
| 6 | `-3` | `2` | yes | 6 | The buffer absorbs a second negative as well |
| 7 | `-3` | `-1` | no | 6 | The running sum finally drops below zero and the sweep can stop |

The first five steps spent the two positive values, the zero, and one negative while the running sum never left the positive region; step $6$ exhausted the remaining buffer, and step $7$ produced the first non-positive prefix. The score at that moment was `6`, and because the running sum can only fall from there — Section 5 — the answer is `6`.

Notice the plateau at steps $3$ and $4$: adding the zero produces a second prefix with the value `6`. Both entries are counted separately, which is exactly why zeros sitting inside the positive region are worth real score. A rule that counted only "positions holding a positive element" would return `3` here and would be wrong.

## 5. Why the sweep may stop at the first non-positive prefix

The early exit is not an optimisation detail; it is a theorem about the descending order. Let $a_1 \ge a_2 \ge \dots \ge a_n$ and let $P_k$ be the running sums of this order. The key observation is:

**Lemma.** $P_j \le 0$ for every $j \ge k$ whenever $P_k \le 0$.

*Reason.* If $P_k \le 0$ then the element $a_k$ itself must satisfy $a_k \le 0$: had $a_k$ been positive, then $a_1 \ge \dots \ge a_k > 0$ would make $P_k$ a sum of $k$ positive numbers, contradicting $P_k \le 0$. Since the sequence is non-increasing, every later element satisfies $a_j \le a_k \le 0$ for $j > k$, so each further step adds a non-positive amount and the running sum never rises again. Consequently the prefix sums exhibit a single sign change at most: once one of them is $\le 0$, all of the remaining ones are too.

Two consequences follow. First, the positions that score form a prefix of the sorted order, so the answer is simply the length of that prefix, which is the number of steps completed before the first non-positive running sum. Second, the sweep may legitimately stop at that first non-positive sum instead of scanning the negative tail; the tail can contribute nothing.

## 6. The upper bound, and why the sorted order attains it

The descending arrangement produces the exact sequence of maximum possible prefix sums. Let $S_k$ denote the largest sum obtainable from any $k$ elements of the array, which — for a fixed $k$ — is the sum of the $k$ largest values, precisely what the descending order accumulates at step $k$.

| $k$ | Maximum possible sum $S_k$ of $k$ elements | $S_k > 0$? | Meaning for the optimum |
|---|---|---|---|
| 1 | `3` | yes | Some positive prefix of length $1$ is possible |
| 2 | `5` | yes | Some positive prefix of length $2$ is possible |
| 3 | `6` | yes | Some positive prefix of length $3$ is possible |
| 4 | `6` | yes | Some positive prefix of length $4$ is possible |
| 5 | `5` | yes | Some positive prefix of length $5$ is possible |
| 6 | `2` | yes | Some positive prefix of length $6$ is possible |
| 7 | `-1` | no | Every prefix of length $7$ is the total sum, so no arrangement can score `7` |

The table certifies both halves of the answer. The upper bounds say that a positive prefix of length $7$ is impossible because every length-$7$ prefix equals $-1$, so `6` cannot be beaten. The descending trace of Section 4 shows that length `6` is actually achieved, so `6` is attainable. Any scoring arrangement must therefore have score at most `6`, and `6` is reached.

## 7. Boundary conditions and traps

| Situation | Instance | Outcome | Why |
|---|---|---|---|
| The whole array is one positive value | `nums = [5]` | `1` | The single prefix equals `5` and is positive |
| The whole array is one zero | `nums = [0]` | `0` | The prefix equals `0`, and the test is strict |
| A prefix lands exactly on zero | `nums = [-2, 2]` | `1` | Ordered as `[2, -2]`, the prefixes are `2` and `0`; only the first is positive |
| Zeros inside the positive region | `nums = [0, 1, 0]` | `3` | Ordered as `[1, 0, 0]`, all three prefixes equal `1`, and each zero adds another positive entry |
| No positive value exists at all | `nums = [-2, -3, 0]` | `0` | Every ordering starts with a non-positive value, so no prefix is positive |
| Zeros and negatives only | `nums = [0, -1, 0]` | `0` | The running sum is never above zero, so no prefix qualifies even though three prefixes exist |
| A negative tail longer than the buffer | `nums = [-3, 4, -1, -2]` | `3` | Ordered as `[4, -1, -2, -3]`, the prefixes are `4, 3, 1, -2`; the buffer covers two of the three negatives |
| Large magnitudes | Ten values of $\pm 10^{6}$ alternating | `9` | The running sum reaches $5 \cdot 10^{6}$, far beyond a 32-bit signed integer, so the accumulator must be wide enough |
| The total sum is negative | the instance of Section 1 | at most `6` | The final prefix is the fixed total $-1$, so position $n$ never scores |

The last row is worth separating from the others: a negative total does not merely *usually* cost one point, it forces the last prefix to be non-positive, so an array of length $n$ with a negative total can never score $n$. Two further traps follow from the definition. Counting positions whose *element* is positive rather than positions whose *prefix sum* is positive undercounts badly — the instance of Section 1 would report `3` instead of `6`. And treating a zero prefix as positive would inflate `nums = [-2, 2]` from `1` to `2`.

## 8. Why the reasoning is correct

**The descending order achieves the claimed score.** Its prefix sums are exactly $S_1, S_2, \dots, S_n$, the sums of the $k$ largest values. If $S_k \le 0$ for some $k$, then $a_k \le 0$ for the descending order, hence every value from position $k$ onwards is non-positive and $S_j \le S_k \le 0$ for all $j \ge k$. Therefore the set of positions where the descending order scores is $\{1, 2, \dots, m\}$ for some $m$, and its score equals $m$.

**No ordering can do better.** Suppose some ordering has a positive prefix of length $k$. The sum of its first $k$ elements is then positive, and those $k$ elements are $k$ elements of the array, so their sum is at most the largest sum any $k$ elements can reach, namely $S_k$. Hence $S_k > 0$ for that $k$. By the monotonicity argument of Section 5 applied to the descending order, $S_j \le 0$ for every $j > m$ where $m$ is the largest index with $S_m > 0$; combined with $S_k > 0$ this forces $k \le m$. Every positive prefix of every ordering therefore has length at most $m$, so no ordering scores more than $m$ positions, and the descending order attains $m$. The greedy is optimal, and the answer is precisely the number of positive prefix sums of the non-increasing arrangement.

**Why placing zeros between the positives and the negatives is harmless and useful.** A zero contributes nothing to the running sum but appends a prefix entry equal to the current positive sum, and by the lemma that sum is still positive at that point; so each zero inside the scoring prefix adds exactly one to the score. Placing zeros after the running sum has already gone non-positive would add nothing, and placing them before the positives would equally add nothing, because the prefix at that point would be `0`. The non-increasing order puts every zero exactly where it is worth one point, which is what the plateau at steps $3$ and $4$ of Section 4 demonstrates.

## 9. Complexity: sorting, scanning, and auxiliary space

**Time.** The work has two phases. Ordering the values in non-increasing order costs $\Theta(n \log n)$ comparisons, which dominates. The sweep then visits each position once, adding one value and performing one comparison per step, so it costs $O(n)$ — and because of the lemma in Section 5 it may stop at the first non-positive running sum, making the scan cost proportional to the scoring prefix rather than to $n$. The total is $\Theta(n \log n)$ in the worst case, which for $n \le 10^{5}$ is comfortable. Note that the values bounded by $\lvert \text{nums}[i] \rvert \le 10^{6}$ do not bound the running sum, which can reach $10^{11}$; the accumulator must hold sums of that size.

**Auxiliary space.** The accumulation itself needs one running sum, one counter, and one index, so the scan is $O(1)$ beyond its inputs. Producing the non-increasing arrangement requires storage for the reordered sequence, so the sorting step contributes $O(n)$ auxiliary space for a separate copy (or $O(\log n)$ if the arrangement is produced in place by an in-place comparison sort, while the standard library sort of a list allocates a temporary buffer of linear size). The bound to quote is therefore $O(n)$ auxiliary space in the usual implementation, with only $O(1)$ attributable to the counting logic.