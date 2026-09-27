# Guided Example: Minimum Penalty for a Shop

## 1. The Penalty as a Function of the Closing Hour

The visit log is a string `customers` of length $n$ over the alphabet
`{'Y', 'N'}`. Reading index $i$ as the $i$-th hour counted from zero, a `'Y'`
means customers arrived in that hour and an `'N'` means none did.

The shop's closing hour is a parameter $j$ with $0 \le j \le n$. Because a shop
that closes at hour $j$ is already shut *during* hour $j$, the closing choice
slices the timeline into two complementary halves:

- hours $0, 1, \dots, j-1$ are **open hours**;
- hours $j, j+1, \dots, n-1$ are **closed hours**.

The penalty charges every mismatch between the plan and the log:

- an open hour with no customers costs $1$;
- a closed hour with customers costs $1$;
- an open hour with customers and a closed hour with no customers both cost $0$.

So the objective is the Hamming-style disagreement count

$$
P(j) \;=\; \#\{i < j : \texttt{customers}[i] = \texttt{'N'}\}
\;+\; \#\{i \ge j : \texttt{customers}[i] = \texttt{'Y'}\} .
$$

The return value is the *smallest* $j$ attaining $\min_{0 \le j \le n} P(j)$,
which makes the tie-break part of the specification rather than an
afterthought. Note the two extreme closing times are both legal: $j = 0$ closes
the shop at once and pays only for the customers already turned away, while
$j = n$ never closes early and pays only for the empty hours.

## 2. The Split into a Prefix and a Suffix

The definition naturally separates into one prefix quantity and one suffix
quantity. Define

$$
A(j) = \#\{i < j : \texttt{customers}[i] = \texttt{'N'}\}, \qquad
B(j) = \#\{i \ge j : \texttt{customers}[i] = \texttt{'Y'}\},
$$

so that $P(j) = A(j) + B(j)$. Both are monotone in $j$ but in opposite
directions: $A(j)$ is non-decreasing because opening more hours exposes more
opportunities to meet an `'N'`, and $B(j)$ is non-increasing because closing
earlier leaves more hours in which a `'Y'` can be missed. The penalty is the sum
of a rising and a falling staircase, which is exactly the shape that admits a
single-pass minimum search.

Two identities make the arithmetic compact and give the analysis a way to check
itself. The first is a *continuity* identity at each individual hour: the
penalty counts the hours that were misjudged, so the hours that were handled
correctly complete the count,

$$
P(j) + \#\{i < j : \texttt{customers}[i] = \texttt{'Y'}\}
     + \#\{i \ge j : \texttt{customers}[i] = \texttt{'N'}\} = n .
$$

The two added terms are precisely the two *agreement* patterns — an open hour
with customers and a closed hour with no customers — that the penalty never
charges. For any $j$ the three counts partition the $n$ log positions, so the
identity holds by definition and is the quickest way to verify a hand-built
penalty table.

The second is the exact sum over all closing hours. Position $i$ contributes to
$P(j)$ as an empty open hour for the $n - i$ closing hours $j > i$ when it is an
`'N'`, and as a busy closed hour for the $i + 1$ closing hours $j \le i$ when it
is a `'Y'`. Hence

$$
\sum_{j=0}^{n} P(j)
= \sum_{i \,:\, \texttt{customers}[i] = \texttt{'N'}} (n - i)
+ \sum_{i \,:\, \texttt{customers}[i] = \texttt{'Y'}} (i + 1).
$$

This is not a constant times $n$: for five `'Y'` characters the sum is
$1 + 2 + 3 + 4 + 5 = 15$ while $n = 5$. The useful global fact is instead the
boundary pair. Writing the total customer count as

$$
Y_{\text{total}} = \#\{i : \texttt{customers}[i] = \texttt{'Y'}\},
$$

the two extremes are $P(0) = Y_{\text{total}}$ (closed the whole time) and
$P(n) = n - Y_{\text{total}}$ (open the whole time), so the optimum is at most

$$
\min\left(Y_{\text{total}},\; n - Y_{\text{total}}\right) \;\le\; \frac{n}{2},
$$

because both extreme closing hours are always legal candidates. That is the
bound a computed penalty sequence must respect, and it is tight: an all-`Y` log
attains the optimum only at $j = n$ and reaches it by decreasing from
$P(0) = n$ all the way down to $0$.

## 3. The Exchange Recurrence Between Neighbouring Hours

The decisive observation is that moving the closing hour by one hour moves
exactly one log position across the open/closed boundary and touches no other
position. When $j$ advances to $j+1$, the hour $j$ stops being an open hour and
becomes a closed hour:

- if `customers[j] = 'N'`, the hour was costing $1$ as an open empty hour and
  now costs $0$ as a closed empty hour, so the penalty **drops** by $1$;
- if `customers[j] = 'Y'`, the hour was costing $0$ as an open busy hour and now
  costs $1$ as a closed busy hour, so the penalty **rises** by $1$.

Incrementally,

$$
P(j+1) = P(j) + \begin{cases}
-1, & \texttt{customers}[j] = \texttt{'Y'} \\[2pt]
+1, & \texttt{customers}[j] = \texttt{'N'}
\end{cases}
$$

This is the whole algorithm: each character of the log contributes exactly one
$\pm 1$ step to a running total, the running total after $j$ steps is $P(j)$, and
the answer is the first index at which the running total attains its global
minimum. Because a step of size $1$ changes the parity of the total at every
hour, and $P(0) = Y_{\text{total}}$, the sequence visits both parities in
alternation — which is why the optimal value can never be larger than $1$ for
long logs and why exact ties are common rather than exotic.

The invariant maintained by the method is worth naming precisely:

> **Invariant.** Before processing the character at index $j$, the running
> counter holds $P(j)$, and the stored best value is $\min_{0 \le k \le j} P(k)$,
> with the stored answer being the smallest $k$ that attains it.

The invariant starts true at $j = 0$: the counter is $Y_{\text{total}} = P(0)$
and the candidate answer is $0$, which is trivially the earliest argmin on a
one-element list. Each step restores it by applying the recurrence to obtain
$P(j+1)$ and then updating the stored best **only on a strict improvement**,
never on a tie. That strictness is the entire tie-break mechanism: equal-cost
later hours are ignored because the earlier hour already claims the record.

## 4. Worked Instance: `customers = "YYNY"`

We trace the first official example, which is chosen because the minimum is
attained twice — at hours $2$ and $4$ — so the tie-break rule is load-bearing.

The four log positions are indexed $0$ to $3$, and there are five candidate
closing hours $0$ to $4$. Starting from $j = 0$ the shop is closed at every
hour, so the penalty is the total number of `'Y'` characters: there are three of
them, giving $P(0) = 3$. Then each log character is applied in order as a
$\pm 1$ step.

| Log index | `customers[j]` | Step applied | Transition | Resulting hour $j+1$ | $P(j+1)$ | Best so far | Earliest argmin |
|:---:|:---:|:---:|:---|:---:|:---:|:---:|:---:|
| — | — | — | initial value $Y_{\text{total}} = 3$ | 0 | 3 | 3 | `0` |
| 0 | `Y` | $-1$ | $3 - 1$ | 1 | 2 | 2 | `1` (strict improvement) |
| 1 | `Y` | $-1$ | $2 - 1$ | 2 | 1 | 1 | `2` (strict improvement) |
| 2 | `N` | $+1$ | $1 + 1$ | 3 | 2 | 1 | `2` (unchanged) |
| 3 | `Y` | $-1$ | $2 - 1$ | 4 | 1 | 1 | `2` (tie, not an improvement) |

The returned answer is `2`, matching the official output. The final row is the
trap: hour $4$ also achieves penalty $1$, and an implementation that updates its
record on `cost <= best` instead of `cost < best` would answer `4`. The
specification asks for the earliest hour, so the strict comparison is required.

The same run can be read directly from the prefix/suffix decomposition of
section 2, which is the check that the recurrence has not drifted:

| Closing hour $j$ | Open hours | Empty open hours $A(j)$ | Closed hours | Missed customers $B(j)$ | $P(j) = A + B$ | Optimal? |
|:---:|:---|:---:|:---|:---:|:---:|:---:|
| 0 | none | 0 | `Y Y N Y` | 3 | 3 | no |
| 1 | `Y` | 0 | `Y N Y` | 2 | 2 | no |
| 2 | `Y Y` | 0 | `N Y` | 1 | 1 | **yes, earliest** |
| 3 | `Y Y N` | 1 | `Y` | 1 | 2 | no |
| 4 | `Y Y N Y` | 1 | none | 0 | 1 | yes, but later |

Every row agrees with the incremental table. The two tables are cross-checks on
each other: one produces $P(j)$ from a running $\pm 1$ counter, the other
computes it from two independent prefix/suffix counts, and a disagreement would
localise an indexing error immediately. The continuity identity of section 2 is
also visible here — at $j = 2$ the misjudged hours number $1$ and the correctly
handled hours number $3$, totalling $n = 4$; at $j = 4$ the split is $1$ and
$3$ again, since hours $0$ to $2$ were busy while open and hour $3$ was the
single empty hour that was correctly closed on.

## 5. Choosing the Representative Instance: Why Not All-`N` or All-`Y`

The degenerate inputs are pedagogically weak because the answer is forced by a
monotone penalty sequence. The table contrasts them with the traced instance.

| Instance | Penalty sequence $P(0), \dots, P(n)$ | Behaviour | Answer |
|:---|:---|:---|:---:|
| `"NNNNN"` | 0, 1, 2, 3, 4, 5 | every step is $+1$; the minimum is at the start | `0` |
| `"YYYY"` | 4, 3, 2, 1, 0 | every step is $-1$; the minimum is at the end | `4` |
| `"YYNY"` | 3, 2, 1, 2, 1 | rises then falls; minimum attained twice | `2` |
| `"YNYN"` | 2, 1, 2, 1, 2 | alternates; two local minima, equal value | `1` |
| `"NYYN"` | 2, 3, 2, 1, 2 | unique interior minimum | `3` |
| `"NY"` | 1, 0, 1 | unique interior minimum | `0` |
| `"YN"` | 1, 0, 1 | the mirror image; same sequence, different order | `1` |
| `"Y"` | 1, 0 | minimum at the only non-trivial hour | `1` |
| `"N"` | 0, 1 | minimum at the start | `0` |

All-`N` and all-`Y` inputs exercise only one direction of the recurrence and
never produce a tie, so they cannot reveal the tie-break requirement. The
alternating instances `"YYNY"` and `"YNYN"` do: in `"YNYN"` the running cost
takes the value $1$ at hours $1$ and $3$, and the earliest is returned. Reading
the sequences also confirms the two structural facts of section 2: the sequence
touches penalty $0$ exactly when some closing hour is perfect, and whenever a
perfect hour exists it is the unique minimum and the answer is forced.

## 6. Boundary and Degenerate Cases

The constraint $1 \le n \le 10^{5}$ means the short strings are legal inputs and
must be handled by the same loop, with no special case.

| Case | $n$ | Candidate hours | Why it matters | Answer |
|:---|:---:|:---:|:---|:---:|
| `"Y"` | 1 | 0, 1 | closing immediately costs 1, staying open costs 0; the optimum is at the far end | `1` |
| `"N"` | 1 | 0, 1 | closing immediately costs 0 and is already optimal | `0` |
| `"NY"` | 2 | 0, 1, 2 | hours 0 and 2 both cost 1; the earliest is chosen | `0` |
| `"YN"` | 2 | 0, 1, 2 | the mirror image: only hour 1 costs 0 | `1` |
| `"YYY"` | 3 | 0..3 | minimum at the last hour because every step lowers the cost | `3` |
| all-`N` of length $n$ | any | 0..n | cost increases by 1 per hour; the answer is always `0` | `0` |
| all-`Y` of length $n$ | any | 0..n | cost decreases by 1 per hour; the answer is always `n` | `n` |

The mirrored pair `"NY"` and `"YN"` is the sharpest boundary check. In `"NY"`
the empty hour comes first, so closing immediately trades a missed customer for
an avoided empty hour and the two effects cancel — the optimum sits at the
boundary $j = 0$, which means the loop never performs a strict improvement and
the pre-initialised answer survives. In `"YN"` the busy hour comes first, so
closing at $j = 0$ is bad and the single interior hour $j = 1$ is perfect. An
implementation that initialised its answer only inside the loop would fail the
`"NY"`, `"N"`, and all-`N` cases; the flat initialisation is what makes the
left boundary a first-class candidate.

## 7. Alternatives and Their Trade-offs

| Strategy | Extra space | Time | Why it loses or when it is appropriate |
|:---|:---|:---|:---|
| Recompute each $P(j)$ from scratch | $O(1)$ | $O(n^2)$ | Correct and tiny in memory, but $10^{10}$ character inspections at the maximum $n$; unusable. |
| Prefix array plus suffix array | $O(n)$ | $O(n)$ | Natural if $P(j)$ is needed for many $j$ after preprocessing; here only the argmin is requested, so the extra arrays are wasted. |
| Running counter with strict improvement | $O(1)$ | $O(n)$ | The chosen method: one pass, one counter, one best value, no array at all. |
| Scanning backwards for the latest argmin | $O(1)$ | $O(n)$ | Valid but answers the wrong tie-break; the specification asks for the earliest hour. |
| Dynamic programming over "closed or open" prefixes | $O(n)$ or $O(1)$ | $O(n)$ | Structurally identical to the running counter; the DP framing adds state that the recurrence already collapses. |

The running counter wins because the recurrence of section 3 makes every
prefix quantity derivable from its predecessor with a single $\pm 1$ update, so
no prefix or suffix array ever has to be stored.

## 8. Complexity

Let $n = \lvert \texttt{customers} \rvert$; the constraints give $1 \le n \le
10^{5}$.

- **Time:** $O(n)$, in fact exactly $\Theta(n)$. One initial pass counts the
  `'Y'` characters to obtain $P(0)$, and then a single forward pass applies one
  $\pm 1$ step per character together with one comparison. No closing hour is
  ever evaluated from scratch. The output is a single index, but every character
  must still be read at least once, so $\Omega(n)$ is a genuine lower bound and
  the bound is tight.
- **Auxiliary space:** $O(1)$. The state is the running penalty, the best
  penalty seen, and the best hour — three integers. The input string is
  read-only and no prefix or suffix array is materialised, which is the decisive
  improvement over the $O(n)$ prefix-plus-suffix formulation.

One structural bound from section 2 keeps the search honest rather than fast.
Because both extreme closing hours are legal, the optimum never exceeds
$\min(Y_{\text{total}}, n - Y_{\text{total}}) \le n/2$, and the penalty sequence
moves by exactly one unit per hour, so it meets its minimum at the earliest
opportunity without ever overshooting and needing to backtrack. The
strict-improvement rule then guarantees that the *first* hour reaching that
minimum is the one returned, which is the specification's tie-break.