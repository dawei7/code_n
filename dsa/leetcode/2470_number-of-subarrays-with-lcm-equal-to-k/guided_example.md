# Guided Example: Number of Subarrays With LCM Equal to K

## 1. The window LCM as a join in the divisor lattice

For a window $[i, j]$ write

$$
L(i, j) = \operatorname{lcm}\bigl(\texttt{nums}[i], \texttt{nums}[i+1], \dots, \texttt{nums}[j]\bigr).
$$

The LCM is the **join** operation of the divisor lattice: it is the least number
that every element of the window divides. Two facts about the join drive the
entire solution.

The first is the extension recurrence. Widening a window by one element on the
right only adds a constraint to the join, so

$$
L(i, j+1) = \operatorname{lcm}\bigl(L(i, j),\, \texttt{nums}[j+1]\bigr)
\quad\text{and}\quad
L(i, j) \mid L(i, j+1).
$$

Because divisibility implies $L(i, j) \le L(i, j+1)$, the window LCM is
**non-decreasing** as the window grows to the right. It never falls back, and it
only ever takes values that are multiples of the value before it.

The second fact is closure. Once a window's LCM is some value $L$, every later
window starting at the same $i$ has LCM divisible by $L$. So if $L$ fails to
divide the target $k$, no descendant can divide $k$ either.

Here is the join table for the divisors of $k = 6$ together with the intruder
$7$ that actually appears in the first official example. Reading a row tells you
what one more element does to the current window LCM.

| Current $L(i,j)$ | $+1$ | $+2$ | $+3$ | $+6$ | $+7$ | Reading |
|---|---|---|---|---|---|---|
| $1$ | $1$ | $2$ | $3$ | $6$ | $7$ | the seed absorbs any element unchanged |
| $2$ | $2$ | $2$ | $6$ | $6$ | $14$ | jumping to $6$ is legal, since $2 \mid 6$ |
| $3$ | $3$ | $6$ | $3$ | $6$ | $21$ | symmetric to the row above |
| $6$ | $6$ | $6$ | $6$ | $6$ | $42$ | $6$ is stable under divisors of $k$, broken by $7$ |
| $7$ | $7$ | $14$ | $21$ | $42$ | $7$ | an element that misses $k$ can never be repaired |

Every entry in the last row is outside the divisor set of $6$; the state
$L = 7$ is therefore a **dead state** for the target $6$.

## 2. Three structural lemmas that fully determine the algorithm

**Lemma 1 (monotonicity).** For fixed $i$, $L(i,j) \mid L(i,j+1)$, hence $L$ is
non-decreasing in $j$. *Consequence:* if $L(i,j) > k$ then $L(i,j') \ge k+1$
for every $j' \ge j$, so no longer window from $i$ can have LCM exactly $k$.

**Lemma 2 (divisor closure).** If $L(i,j) \nmid k$, then $L(i,j') \nmid k$ for
every $j' \ge j$. *Proof:* $L(i,j) \mid L(i,j')$ by Lemma 1; if $L(i,j')$ also
divided $k$, transitivity of divisibility would force $L(i,j) \mid k$, contrary
to the hypothesis. *Consequence:* the first failure to divide $k$ is a sound and
complete stopping signal — no valid endpoint hides beyond it.

**Lemma 3 (necessity inside a valid window).** If a window has LCM exactly $k$,
then each of its elements divides $k$, because the LCM is a common multiple of
them. Equivalently, any element with `k % nums[x] != 0` can never be part of an
answer window.

A counting consequence follows: for a fixed starting index, every reachable
LCM value divides $k$, and by Lemma 1 the sequence of values is non-decreasing,
so each time it changes it strictly increases through the divisor lattice of
$k$. The number of distinct states on one starting index is therefore at most
$\tau(k)$, the divisor count of $k$. For $k \le 1000$ we have
$\tau(k) \le 32$, attained at $k = 840$; this bound appears again in the
complexity analysis.

## 3. Worked trace of the official instance `nums = [3,6,2,7,1]`, `k = 6`

Fix a starting index $i$, seed $L = \texttt{nums}[i]$, and sweep $j$ to the
right, updating $L$ by the extension recurrence. Count every position where the
updated $L$ equals $6$, and abandon the starting index the moment $L \nmid 6$.

| Start $i$ | Right end $j$ | `nums[j]` | $L$ before | $L$ after join | $L = k$? | Action taken |
|---|---|---|---|---|---|---|
| 0 | 0 | `3` | seed | $3$ | no | $3 \mid 6$, so extend |
| 0 | 1 | `6` | $3$ | $6$ | **yes** | count window `[3, 6]` |
| 0 | 2 | `2` | $6$ | $6$ | **yes** | count window `[3, 6, 2]` |
| 0 | 3 | `7` | $6$ | $42$ | no | $42 \nmid 6$: abandon start $0$ |
| 1 | 1 | `6` | seed | $6$ | **yes** | count window `[6]` |
| 1 | 2 | `2` | $6$ | $6$ | **yes** | count window `[6, 2]` |
| 1 | 3 | `7` | $6$ | $42$ | no | $42 \nmid 6$: abandon start $1$ |
| 2 | 2 | `2` | seed | $2$ | no | $2 \mid 6$, so extend |
| 2 | 3 | `7` | $2$ | $14$ | no | $14 \nmid 6$: abandon start $2$ |
| 3 | 3 | `7` | seed | $7$ | no | $7 \nmid 6$: abandon start $3$ |
| 4 | 4 | `1` | seed | $1$ | no | $1 \mid 6$, window ends at the array end |

The first two starting indices each contribute two windows, and the last three
contribute none, for a total of $4$ — the official answer. Per-start totals:

| Start $i$ | Seed `nums[i]` | Windows counted | Stop position | Stop reason | Running total |
|---|---|---|---|---|---|
| 0 | `3` | 2 | $j = 3$ | $L = 42$ violates $L \mid 6$ | 2 |
| 1 | `6` | 2 | $j = 3$ | $L = 42$ violates $L \mid 6$ | 4 |
| 2 | `2` | 0 | $j = 3$ | $L = 14$ violates $L \mid 6$ | 4 |
| 3 | `7` | 0 | $j = 3$ | seed $7$ already violates $L \mid 6$ | 4 |
| 4 | `1` | 0 | $j = 4$ (exhausted) | array ends; $L = 1 \ne 6$ | 4 |

Note how start $3$ dies before extending at all, and how the single element `7`
is the common killer of three different starting indices. Without Lemma 2 the
method would keep testing windows `[3,6,2,7]`, `[3,6,2,7,1]` and every longer
window from start $0$ even though $42$ can never shrink.

## 4. Boundary analysis

Each row is a distinct way the divisor structure can behave at an extreme. All
values are recomputed from the recurrence, and all match the authored
expectations.

| Boundary instance | Input | Expected | Mechanism that decides it |
|---|---|---|---|
| Target is $1$ | `nums = [1,1,1]`, `k = 1` | 6 | $L$ stays $1$ forever, so all $\binom{4}{2} = 6$ non-empty windows qualify |
| Single element equal to $k$ | `nums = [6]`, `k = 6` | 1 | the seed alone already equals the target |
| Single element not dividing $k$ | `nums = [3]`, `k = 2` | 0 | $3 \nmid 2$; the only window is dead on arrival |
| Element above $k$ | `nums = [12,6]`, `k = 6` | 1 | $12 \nmid 6$ kills start $0$; start $1$ counts `[6]` |
| Repeated target copies | `nums = [6,6,6]`, `k = 6` | 6 | $6$ is stable under the join, so every window is valid |
| Non-divisor separator | `nums = [2,5,3,6]`, `k = 6` | 2 | $5$ and the joins $10$, $15$ poison every window crossing them |
| Plateau strictly below $k$ | `nums = [1,2,4,3,2,6]`, `k = 12` | 9 | from start $3$ the values are $3 \to 6 \to 6$: never equal to $12$, never breaking $L \mid 12$ |
| Factors that must combine | `nums = [2,3,2]`, `k = 6` | 3 | no single element is $6$; the target appears only after joins |

The plateau row is the subtle one. The stopping test is **$L \mid k$**, not
$L < k$: an LCM can sit strictly below the target indefinitely, as
$L = 6$ does for $k = 12$, and the sweep must reach the end of the array rather
than break early. Conversely, the moment $L \nmid k$ the sweep must stop even
though $L$ might still be smaller than some future value of $k$.

## 5. Invariant and why the counting is exact

**State invariant.** At the top of each inner iteration the variable $L$ equals
$L(i, j)$ for the current start $i$ and right end $j$, and the accumulator holds
the number of pairs $(i', j')$ already examined with $L(i', j') = k$. The
invariant is established when $L$ is seeded with `nums[i]`, which is exactly
$L(i,i)$, and is preserved because the update assigns the join with
`nums[j+1]`, which is the definition of $L(i, j+1)$.

**Soundness.** Every increment happens at a position where the maintained $L$
provably equals $k$, so each counted window really is a window whose LCM is $k$;
the accumulator can never overcount.

**Completeness.** Consider any window $[i, j]$ with $L(i,j) = k$. When the outer
loop reaches start $i$, the sweep visits $j$ and computes exactly $L(i,j)$, so
the window is counted, unless the sweep stopped earlier at some $j'' < j$ with
$L(i, j'') \nmid k$. That early stop is impossible here: by Lemma 1
$L(i, j'') \mid L(i, j) = k$, contradicting $L(i, j'') \nmid k$. Hence no valid
window is skipped, and the total is exact. Lemma 3 guarantees in addition that a
window containing an element that does not divide $k$ can never be counted, so
the abandon rule discards only windows that could not have contributed.

## 6. Alternatives and what each one costs

| Method | How it counts | Time | Auxiliary space | Verdict |
|---|---|---|---|---|
| Recompute every window from scratch | for each of the $\frac{n(n+1)}{2}$ windows, take the LCM of all its elements | $O(n^3)$ | $O(1)$ | correct but cubic; discards the join recurrence |
| Incremental extension with the divisor cut (the method traced above) | seed at $i$, extend $j$ and join one element at a time, stop when $L \nmid k$ | $O(n^2)$ worst case | $O(1)$ | the canonical solution; the cut is a constant-factor win, not an asymptotic one |
| Compressed divisor states | sweep the right end once, keeping the multiset of (LCM value, number of starts) pairs for windows ending here, merging equal values | $O(n \cdot \tau(k))$ | $O(\tau(k))$ | exploits the $\tau(k) \le 32$ state bound; best asymptotic cost |
| Enumerate divisors of $k$ first | keep only elements dividing $k$; anything else splits the array into independent runs | $O(n)$ filter plus the method above | $O(n)$ or $O(1)$ | useful preprocessing, same worst-case count as the cut |

The strategy table shows the honest trade: the extension method is quadratic in
the worst case, and that worst case is reachable — with `nums` equal to $n$
copies of `1` and `k = 1`, or $n$ copies of $2$ with `k = 4`, the divisor test
never fails and the sweep always runs to the end of the array. For
$n \le 1000$ this is at most about $500{,}500$ joins, which is comfortable, and
it needs no extra memory at all. The compressed variant is the right answer if
the same problem is asked with a much larger $n$, because merging equal LCM
values caps the live state at $\tau(k)$ entries.

## 7. Verification against the authored cases

| Case | `nums` | `k` | Computed count | Authored expectation |
|---|---|---|---|---|
| `sample-1` | `[3,6,2,7,1]` | 6 | 4 | 4 |
| `sample-2` | `[3]` | 2 | 0 | 0 |
| `trial-all-ones` | `[1,1,1]` | 1 | 6 | 6 |
| `trial-composed-target` | `[2,3,2]` | 6 | 3 | 3 |
| `trial-single-target` | `[6]` | 6 | 1 | 1 |
| `trial-invalid-divider-resets` | `[2,5,3,6]` | 6 | 2 | 2 |
| `trial-repeated-target` | `[6,6,6]` | 6 | 6 | 6 |
| `trial-over-target` | `[12,6]` | 6 | 1 | 1 |
| `trial-multiple-lcm-states` | `[1,2,4,3,2,6]` | 12 | 9 | 9 |

For the last case the per-start contributions are $3, 3, 3, 0, 0, 0$: starts
$0$, $1$ and $2$ all converge on $L = 12$ and then stay there for the remaining
positions, which is why three starting indices each contribute three windows.

## 8. Derived time and auxiliary-space complexity

Let $n = \texttt{nums.length}$, let $\tau(k)$ be the number of divisors of $k$,
and write $T(n, k)$ for the number of join operations.

$$
T(n, k) = O(n^2), \qquad S_{\text{aux}}(n, k) = O(1)
\quad\text{for the canonical extension method}
$$

**Time.** The outer loop performs $n$ sweeps. A sweep from start $i$ visits at
most $n - i$ right ends before either hitting the array end or hitting the first
violation of $L \mid k$, so the total number of joins is bounded by

$$
\sum_{i=0}^{n-1} (n - i) = \frac{n(n+1)}{2},
$$

which is $\Theta(n^2)$ and is attained, for example, by `nums` filled with $1$
and $k = 1$ or by `nums` filled with $2$ and $k = 4$. Each join costs one
greatest-common-divisor computation on values bounded by $k \cdot \max
\texttt{nums}[i] \le 10^6$, which is $O(\log k)$ word operations but is
independent of $n$; the quadratic term dominates. With the divisor-state
bound of Lemma 1, the same quantity is $O(n \cdot \min(n, \tau(k)))$: for a
fixed start the LCM strictly increases whenever it changes while remaining a
divisor of $k$, so at most $\tau(k)$ of the visited positions can change the
state, and since $\tau(k) \le 32$ for every $k \le 1000$, the compressed
variant runs in $O(n \cdot \tau(k)) \le O(32n)$.

**Auxiliary space.** The extension method stores only the current start index,
the current right end, the running value $L$ and the counter. No window contents
are materialized and no table indexed by the input is allocated, so auxiliary
space is $\Theta(1)$ — the input array is read in place and only the returned
integer is produced. The compressed alternative instead keeps at most $\tau(k)$
state entries alive for the current right end, which is $O(\tau(k)) = O(1)$ in
practice but $O(\tau(k))$ in the parameter $k$.