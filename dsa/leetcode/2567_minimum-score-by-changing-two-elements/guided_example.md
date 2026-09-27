# Guided Example: Minimum Score by Changing Two Elements

## 1. The two scores are properties of the sorted multiset

Sort a copy of `nums` in non-decreasing order and name the result $b_0 \le b_1 \le \dots \le b_{n-1}$.

- The **high score** is the maximum absolute difference, which the sorted order exposes immediately: it is $b_{n-1} - b_0$.
- The **low score** is the minimum absolute difference. Over a sorted sequence it is attained by some pair of *neighbours*: for any $i < j$,
  $$b_j - b_i \;=\; \sum_{t=i}^{j-1}\bigl(b_{t+1}-b_t\bigr) \;\ge\; \min_{0 \le t < n-1}\bigl(b_{t+1}-b_t\bigr),$$
  because a sum of non-negative gaps is at least its smallest term. So the low score equals the smallest upward gap,
  $$\text{low} \;=\; \min_{0 \le t < n-1}\bigl(b_{t+1}-b_t\bigr).$$

Sorting therefore costs nothing in correctness: both scores depend only on the multiset of values, never on which index held which value. The answer is a function of values alone, so we may reason about sorted order throughout and forget the original positions.

For the instance we trace, `nums = [1,4,7,8,5]`:

| Sorted index $i$ | 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|---|
| Value $b_i$ | 1 | 4 | 5 | 7 | 8 |
| Upward gap $b_{i+1}-b_i$ | 3 | 1 | 2 | 1 | — |

The untouched input has high score $8-1 = 7$, low score $1$, and total score $8$. Our task is to drive that total as low as possible by rewriting two entries.

## 2. What changing two elements can and cannot buy

We may pick two positions and give them arbitrary new integer values. Call the remaining $n-2$ values the **untouched multiset** $S$, with $\min S$ and $\max S$; because $n \ge 3$, $S$ is non-empty.

**The high score cannot drop below $\operatorname{range}(S) = \max S - \min S$.** Values in $S$ survive in the final array, so the final maximum is at least $\max S$ and the final minimum is at most $\min S$. Conversely, if both new values are placed inside $[\min S, \max S]$, the final maximum is exactly $\max S$ and the final minimum is exactly $\min S$, so the high score equals $\operatorname{range}(S)$.

**The low score can always be made $0$ without disturbing that range.** Set both new values to the same value, say $\min S$. Two equal entries give an absolute difference of $0$, and $0$ is the smallest value any absolute difference can take, so the low score is minimal. Nothing is placed outside $[\min S, \max S]$.

Both goals are achieved by one placement, so for a chosen pair of positions the best reachable score is exactly $\operatorname{range}(S)$, and the problem reduces to a purely combinatorial question: which two elements should be left out of the sorted order to shrink the untouched range the most?

| New values | Final multiset | High score | Low score | Total |
|---|---|---|---|---|
| both set to 6 | `{5,6,6,7,8}` | 3 | 0 | 3 |
| both set to 5 (that is, $\min S$) | `{5,5,5,7,8}` | 3 | 0 | 3 |
| 5 and 20, one of them outside the range | `{5,5,7,8,20}` | 15 | 0 | 15 |
| the original 1 and 4, unchanged | `{1,4,5,7,8}` | 7 | 1 | 8 |

The last two rows show why the placement rule matters: pushing a new value outside $[\min S, \max S]$ enlarges the range the score measures.

## 3. Which two elements to leave out

Removing an element strictly between $\min S$ and $\max S$ cannot shrink the range at all — the extremes are still present. Only removals at the two ends of the sorted order matter, and only two removals are available. Describe a plan by the pair $(i, r)$ where $i$ is how many of the smallest values are removed and $r$ is how many of the largest are removed, with $i + r \le 2$; any unused removal is spent on an interior element and changes nothing. The untouched extremes are then $b_i$ and $b_{n-1-r}$, giving the candidate score

$$\operatorname{range}(i,r) \;=\; b_{n-1-r} - b_i.$$

Two monotonicities make the search tiny: raising $i$ can only raise the lower end, and raising $r$ can only lower the upper end. So for a fixed budget $i + r = 2$ the candidates form a frontier of only three plans, and plans with $i + r < 2$ are dominated by those. Enumerating every plan for `nums = [1,4,7,8,5]`:

| Smallest removed $i$ | Largest removed $r$ | Untouched extremes $(b_i,\,b_{n-1-r})$ | Range $b_{n-1-r}-b_i$ | Effect of the two changes |
|---|---|---|---|---|
| 0 | 0 | $(b_0,b_4) = (1,8)$ | 7 | both changes land in the interior, range unchanged |
| 0 | 1 | $(b_0,b_3) = (1,7)$ | 6 | one change at the top, one wasted inside |
| 1 | 0 | $(b_1,b_4) = (4,8)$ | 4 | one change at the bottom, one wasted inside |
| 0 | 2 | $(b_0,b_2) = (1,5)$ | 4 | both changes at the top, removing 7 and 8 |
| 1 | 1 | $(b_1,b_3) = (4,7)$ | 3 | one change at each end |
| 2 | 0 | $(b_2,b_4) = (5,8)$ | 3 | both changes at the bottom, removing 1 and 4 |

The minimum over the frontier is $3$, attained by $(2,0)$ and by $(1,1)$. The three plans that the problem's structure selects are precisely the frontier rows with $i + r = 2$: $b_{n-1}-b_2 = 8-5 = 3$, $b_{n-2}-b_1 = 7-4 = 3$, and $b_{n-3}-b_0 = 5-1 = 4$.

Selecting $(2,0)$ means the untouched multiset is $S = \{5,7,8\}$ with $\operatorname{range}(S) = 3$, and the changed entries can be set to $6$ (inside the range), producing `{5,6,6,7,8}`. Its high score is $8-5 = 3$, its low score is $|6-6| = 0$, and the total is $3$ — the authored expectation for this input.

## 4. Why the reduction is complete

Two independent checks confirm that no cleverer plan exists.

- **No plan with interior removals can be better.** If a retained interior value exists, the untouched minimum and maximum are still present, so the range is unchanged; this is row $(0,0)$ above, and it is dominated by any frontier row.
- **No plan can use fewer than two end removals to beat the frontier.** For a fixed count $i + r = 2$, monotonicity in $i$ and $r$ leaves only the three corner plans; for $i + r < 2$ the untouched range is a superset range of at least one corner plan, so it can only be larger.
- **The low score never constrains the choice.** It is zeroed after the positions are chosen, so it contributes $0$ to every candidate score and cannot break the tie in favour of a different plan.
- **Every plan's new values stay legal.** The statement allows arbitrary replacement values and the two replacements may coincide, as the reference explanation itself demonstrates by making two entries equal.

Hence the answer is

$$\min\Bigl(b_{n-1}-b_2,\; b_{n-2}-b_1,\; b_{n-3}-b_0\Bigr),$$

with the convention that indices stay inside $[0, n-1]$; for $n = 3$ all three expressions collapse to $0$.

## 5. The same rule across boundary inputs

| `nums` | The three candidate ranges | Winning plan | Minimum score |
|---|---|---|---|
| `[1,4,7,8,5]` | 3, 3, 4 | drop 1 and 4, or drop 1 and 8 | 3 |
| `[1,4,3]` | 0, 0, 0 | change any two of the three values | 0 |
| `[31,25,72,79,74,65]` | 14, 43, 47 | drop the two smallest, 25 and 31 | 14 |
| `[1,2,3,100,101]` | 98, 98, 2 | drop the two largest, 100 and 101 | 2 |
| `[1,100,101,102,1000]` | 899, 2, 100 | drop 1 and 1000, one at each end | 2 |
| `[1,50,75,100]` | 25, 25, 49 | drop 1 and 100, or drop 1 and 50 | 25 |
| `[5,5,5,5,5]` | 0, 0, 0 | values are already equal | 0 |
| `[1,1,2,10,10]` | 8, 9, 1 | drop both copies of 10 | 1 |
| `[1,999999998,999999999,1000000000]` | 1, 1, 999999997 | drop either extreme pair | 1 |

Rows three, five and eight show that each of the three plans can be the unique winner: the optimum genuinely depends on which end carries the heavy values, which is why all three candidates must be evaluated. The duplicate row deserves attention: `1` occurs twice at the bottom and `10` twice at the top, so shrinking the range requires deleting *both* copies of one extreme; deleting one copy from each end leaves the pair `1,1` and `10,10` partially intact and yields $9$. The fourth row is the mirror image, where two large outliers must both be sacrificed, and the last row shows that values near $10^9$ use exactly the same subtraction.

## 6. Traps the instance exposes

| Tempting reasoning | Where it breaks | Correct view |
|---|---|---|
| "Change two interior elements so the extremes stay put." | On `[1,4,7,8,5]` this plan scores $7$. | Interior removals leave the range untouched; only end removals shrink it. |
| "Spend one change at each end, it is always balanced." | On `[1,2,3,100,101]` that plan scores $98$. | Balance is not the criterion; the plan that deletes the offending end wins. |
| "The low score will cost something no matter what." | The low score is $0$ in every optimal plan here. | Set the two changed entries equal, or equal to an existing value; a zero difference always exists. |
| "Two equal values must both be deleted one at a time, so duplicates are irrelevant." | On `[1,1,2,10,10]` ignoring multiplicity gives $9$ instead of $1$. | Multiplicity matters: the removal budget must cover every copy of the extreme being eliminated. |
| "The new values must stay inside the original value range." | Placing $20$ into `[1,4,7,8,5]` raises the score to $15$. | The correct requirement is narrower: stay inside the *untouched* range $[\min S,\max S]$. |
| "Sorting destroys index information that the answer needs." | — | The score is defined on values, so sorting is a safe re-encoding; no reported quantity refers to a position. |

## 7. Time and auxiliary space

Let $n = \texttt{nums.length}$.

- **Time** $O(n\log n)$: the comparisons that determine the answer need the three smallest and the three largest values, which sorting provides in $O(n\log n)$; afterwards the three candidate differences are evaluated in $O(1)$. Selecting the required order statistics without sorting would still require linear selection per rank, and sorting once is the simplest route; no asymptotically cheaper comparison-based method is needed for the stated bounds.
- **Auxiliary space** $O(n)$ for the sorted copy of the array, or $O(\log n)$ stack space if the input is sorted in place. The algorithm keeps only three candidate differences and the sorted order itself; it builds no table of pairs and never enumerates the $\binom{n}{2}$ possible change positions.

The final three-way minimum uses the sorted array's first three and last three entries, so a single ordering pass is the only super-constant work performed.
