# Guided Example: Count Subarrays With Median K

## 1. Turning a Median Question into a Balance Question

`nums` is a permutation of the distinct integers from $1$ to $n$, so the value $k$ occurs at
exactly one index. Call that index $p$. Every subarray whose median must be checked therefore
either contains $p$ or does not — and a subarray that omits $k$ entirely cannot have median $k$,
since $k$ would then not be an element of the subarray at all. So the search space is exactly the
set of subarrays containing position $p$.

For such a subarray, what matters is not the actual values but how they compare with $k$. Let

$$
a = \#\{\,i \in [l, r] : \text{nums}[i] > k\,\}, \qquad
b = \#\{\,i \in [l, r] : \text{nums}[i] < k\,\}.
$$

Because the integers are distinct, exactly one element equals $k$, so the subarray length is
$L = a + b + 1$. After sorting the subarray ascending, the $b$ values smaller than $k$ come first,
so $k$ occupies zero-based rank $b$. The problem defines the median of an even-length array as the
**left** middle element, which is rank $\lfloor (L - 1)/2 \rfloor$ in general.

Setting the two ranks equal and simplifying:

$$
b = \left\lfloor \frac{a + b}{2} \right\rfloor
\quad\Longleftrightarrow\quad
\begin{cases}
b = a & a + b \text{ even},\\[2pt]
b = a - 1 & a + b \text{ odd}.
\end{cases}
$$

Both cases are captured by the single condition

$$
x \;=\; a - b \;\in\; \{0, 1\}.
$$

This is the whole reduction. The sign of each element relative to $k$ becomes a step
$+1$ when `nums[i] > k` and $-1$ when `nums[i] < k`, and a subarray containing $p$ has median
$k$ exactly when the sum of its steps, $x$, is $0$ or $1$.

## 2. Splitting at the Pivot

Every subarray containing $p$ decomposes uniquely as

$$
[l, r] \;=\; \underbrace{[l, p-1]}_{\text{left wing}} \;\cup\; \{p\} \;\cup\; \underbrace{[p+1, r]}_{\text{right wing}},
$$

where either wing may be empty. Define the wing balances

$$
X_L(l) = \sum_{i=l}^{p-1} \sigma_i, \qquad
X_R(r) = \sum_{i=p+1}^{r} \sigma_i,
\qquad \sigma_i = \begin{cases} +1, & \text{nums}[i] > k,\\ -1, & \text{nums}[i] < k,\end{cases}
$$

with $\sigma_p$ contributing nothing. The pivot itself contributes $0$, so the balance of the full
subarray is $x = X_L(l) + X_R(r)$, and the acceptance test becomes

$$
X_L(l) + X_R(r) \in \{0, 1\}
\quad\Longleftrightarrow\quad
X_R(r) \in \{\,-X_L(l),\; 1 - X_L(l)\,\}.
$$

That equivalence is the algorithmic key. The right wing is scanned once and its balance values are
binned into a frequency table. Then each left wing only has to look up two specific bins instead of
re-examining every right wing. A left wing with $X_L(l) = 0$ pairs with right balances $0$ and $1$;
a left wing with $X_L(l) = -1$ pairs with right balances $1$ and $2$; and so on.

## 3. Worked Trace on the Official Instance

The first official example is `nums = [3,2,1,4,5]` with `k = 4`, expected answer `3`. The pivot is
index $p = 3$, and the sign map is computed once:

| Index $i$ | 0 | 1 | 2 | 3 | 4 |
|:---|:---:|:---:|:---:|:---:|:---:|
| `nums[i]` | `3` | `2` | `1` | `4` | `5` |
| Relation to `k = 4` | less | less | less | equal | greater |
| Step $\sigma_i$ | $-1$ | $-1$ | $-1$ | $0$ | $+1$ |

**Right wing scan.** Walking right from $p$ and maintaining the running balance, each extension of
the right wing is a candidate subarray ending at the current index.

| $r$ | `nums[r]` | $\sigma_r$ | $X_R(r)$ | Accepts as `[p, r]`? | Frequency table after |
|:---:|:---:|:---:|:---:|:---:|:---|
| 4 | `5` | $+1$ | $1$ | yes, $1 \in \{0,1\}$ | $\{1 \mapsto 1\}$ |

**Left wing scan.** Now walk left from $p$, tracking $X_L(l)$, and combine.

| $l$ | `nums[l]` | $\sigma_l$ | $X_L(l)$ | Accepts as `[l, p]`? | Bins $-X_L$ and $1 - X_L$ | Count from table | Subarrays added |
|:---:|:---:|:---:|:---:|:---:|:---|:---:|:---|
| 2 | `1` | $-1$ | $-1$ | no | $1$ and $2$ | $1 + 0 = 1$ | `[1,4,5]` |
| 1 | `2` | $-1$ | $-2$ | no | $2$ and $3$ | $0 + 0 = 0$ | none |
| 0 | `3` | $-1$ | $-3$ | no | $3$ and $4$ | $0 + 0 = 0$ | none |

The running total is $1$ for the pivot alone, plus $1$ from the right wing (`[4,5]`), plus $1$ from
the left-right pairing (`[1,4,5]`), giving $1 + 1 + 1 = 3$, matching the expected output.

## 4. Exhaustive Cross-Check of the Reduction

The reduction is only trustworthy if it agrees with actual sorted medians. Every subarray of the
official instance that contains index $3$ is listed below with its true sorted median.

| Subarray indices | Values | $a$ (greater) | $b$ (less) | $x = a - b$ | True sorted subarray | Median | Counted? |
|:---|:---|:---:|:---:|:---:|:---|:---:|:---:|
| `[3, 3]` | `[4]` | 0 | 0 | 0 | `[4]` | `4` | yes |
| `[3, 4]` | `[4,5]` | 1 | 0 | 1 | `[4,5]` | `4` | yes |
| `[2, 3]` | `[1,4]` | 0 | 1 | $-1$ | `[1,4]` | `1` | no |
| `[2, 4]` | `[1,4,5]` | 1 | 1 | 0 | `[1,4,5]` | `4` | yes |
| `[1, 3]` | `[2,1,4]` | 0 | 2 | $-2$ | `[1,2,4]` | `2` | no |
| `[1, 4]` | `[2,1,4,5]` | 1 | 2 | $-1$ | `[1,2,4,5]` | `2` | no |
| `[0, 3]` | `[3,2,1,4]` | 0 | 3 | $-3$ | `[1,2,3,4]` | `2` | no |
| `[0, 4]` | `[3,2,1,4,5]` | 1 | 3 | $-2$ | `[1,2,3,4,5]` | `3` | no |

The three accepted rows are exactly the three subarrays the official explanation names, and the
$-1$ rejection of `[2,1,4,5]` shows why even length plus a balanced feel is not enough: that
subarray has length $4$, and its left middle element is `2`, not `4`.

## 5. A Two-Sided Instance That Exercises Both Bins

`nums = [4,1,6,3,5,2,7]` with `k = 5` (expected `4`) has wings on both sides, so each lookup hits a
non-trivial frequency table. The pivot is index $4$. Sign map: $4<5 \Rightarrow -1$,
$1<5 \Rightarrow -1$, $6>5 \Rightarrow +1$, $3<5 \Rightarrow -1$, $2<5 \Rightarrow -1$,
$7>5 \Rightarrow +1$.

Right wing:

| $r$ | `nums[r]` | $\sigma_r$ | $X_R(r)$ | Accepts as `[p, r]`? | Table after |
|:---:|:---:|:---:|:---:|:---:|:---|
| 5 | `2` | $-1$ | $-1$ | no | $\{-1 \mapsto 1\}$ |
| 6 | `7` | $+1$ | $0$ | yes, `[5,2,7]` | $\{-1 \mapsto 1,\; 0 \mapsto 1\}$ |

Left wing:

| $l$ | `nums[l]` | $\sigma_l$ | $X_L(l)$ | Accepts as `[l, p]`? | Bins $-X_L$ and $1 - X_L$ | Count | Subarrays added |
|:---:|:---:|:---:|:---:|:---:|:---|:---:|:---|
| 3 | `3` | $-1$ | $-1$ | no | $1$ and $2$ | $0 + 0 = 0$ | none |
| 2 | `6` | $+1$ | $0$ | yes, `[6,3,5]` | $0$ and $1$ | $1 + 0 = 1$ | `[6,3,5,2,7]` |
| 1 | `1` | $-1$ | $-1$ | no | $1$ and $2$ | $0 + 0 = 0$ | none |
| 0 | `4` | $-1$ | $-2$ | no | $2$ and $3$ | $0 + 0 = 0$ | none |

Running total: $1$ (pivot `[5]`) $+ 1$ (`[5,2,7]`) $+ 1$ (`[6,3,5]`) $+ 1$ (`[6,3,5,2,7]`) $= 4$.
The paired subarray `[6,3,5,2,7]` sorts to `[2,3,5,6,7]`, whose middle element is `5`, confirming the
answer independently. Note also that the left wing at $l = 3$ produces balance $-1$ and pairs
successfully with nothing, even though the table is non-empty — the bins it needs, $1$ and $2$, are
simply absent. A careless implementation that checked "is the table non-empty?" instead of the two
specific bins would over-count here.

## 6. Invariant and Correctness

**Invariant.** After finishing the right wing scan up to index $r$, the frequency table holds
exactly $\text{cnt}[v] = \#\{\,r' \in [p+1, r] : X_R(r') = v\,\}$, and the accumulated answer
equals the number of valid subarrays whose right endpoint is at most $r$ and whose left endpoint is
at least $p$.

**Preservation.** Extending the right wing by one index updates the running balance by a single
step and inserts that one balance into the table; extending the left wing by one index updates
$X_L$ by a single step and consults exactly the two bins that complete the acceptance test. No
previously counted subarray is revisited, and no new subarray is missed, because every subarray
containing $p$ is enumerated exactly once by its pair $(l, r)$.

**Completeness and soundness.** Every subarray containing $p$ corresponds to a unique pair
$(l, r)$ that the two scans visit, and the balance of that subarray is $X_L(l) + X_R(r)$ by
additivity of the step sum. By Section 1, that subarray has median $k$ exactly when this balance is
$0$ or $1$, which is precisely the condition the lookups encode. So the method counts every valid
subarray once (soundness) and omits none (completeness).

**Why the pivot is always included.** Since `nums` has distinct values, no subarray omitting $p$
can contain the value $k$, so its median cannot be $k$. Starting the count at $1$ for the singleton
`[p, p]` therefore does not skip any case; it is the unique subarray with both wings empty.

## 7. Boundary Analysis

Every row below is an authored case, and each expected count is reproduced by the rule.

| Instance | `nums` | `k` | Pivot $p$ | Expected | Why it matters |
|:---|:---|:---:|:---:|:---:|:---|
| Single element | `[1]` | `1` | 0 | 1 | Both wings are empty; only the `x = 0` case exists. |
| Maximum value at pivot | `[2,3,1]` | `3` | 1 | 1 | Every nonzero balance is $-1$, so no pairing succeeds and only `[3]` counts. |
| Pivot in the middle | `[1,2,3]` | `2` | 1 | 3 | One right wing with $X_R = 1$ and one left wing with $X_L = -1$ that pairs with it. |
| Pivot at the first index | `[2,1,4,3]` | `2` | 0 | 3 | The left wing is empty; all three counted subarrays share $l = 0$. |
| Pivot at the last index | `[3,1,4,2]` | `2` | 3 | 4 | The right wing and therefore the frequency table are empty; only `x \in \{0,1\}` on the left is used. |
| `k` is the maximum | `[1,4,2,3]` | `4` | 1 | 1 | Every step is $-1$, so the balance decreases monotonically and never re-enters $\{0,1\}$. |
| Alternating signs | `[4,1,6,3,5,2,7]` | `5` | 4 | 4 | Both bins are exercised with repeated balance values on each side. |

Two of these rows deserve emphasis. When the pivot is the array maximum, the balance is strictly
decreasing as the subarray grows in either direction, so $\{0,1\}$ is reachable only at length $1$ —
the method finds this without any special case. When the pivot is at the array boundary, one whole
scan degenerates to zero iterations, which is exactly what a correct implementation must tolerate:
an empty frequency table and a lookup of $0$.

## 8. Alternatives and Their Costs

| Approach | Idea | Verdict |
|:---|:---|:---|
| Enumerate and sort | For each subarray, sort a copy and read the left middle element. | Correct but $O(n^3 \log n)$ on $n \le 10^{5}$; hopeless. |
| Enumerate with running counts | For each left endpoint, extend right while tracking $a$ and $b$. | $O(n^2)$ time, $O(1)$ space; still far too slow at the constraint limit. |
| Balance reduction with a frequency table | Bin right-wing balances, match two bins per left wing. | Chosen method: one pass right, one pass left, linear time. |
| Balanced tree or Fenwick over balances | Insert right-wing balances into an ordered index and range-count. | Correct but $O(n \log n)$; unnecessary because balances lie in $[-n, n]$, a range already indexable directly. |
| Per-value sweep of the whole array | Recount signs from scratch for each candidate subarray. | Repeats work that prefix accumulation makes free. |

The frequency-table row is not merely the fastest option; it is the only one that scales. The
balance reduction is what makes binning possible, because it converts a comparison-heavy ordering
question into a small-integer sum that can be accumulated incrementally.

## 9. Complexity Derivation

Let $n = \lvert \text{nums} \rvert$.

**Time.** Locating the pivot costs one linear scan, $O(n)$. The right wing is scanned once, with a
constant number of operations per element: one sign test, one balance update, one range check, one
table insertion. The left wing is likewise scanned once, with one sign test, one balance update,
one range check, and two constant-time table lookups. No element is examined more than a constant
number of times, so the total is $O(n)$. The pairing step has no nested loop: the two scans are
sequential, not nested, which is the entire point of pre-binning the right wing. At $n = 10^{5}$
this is a few hundred thousand operations.

**Auxiliary space.** The frequency table holds one entry per distinct right-wing balance value.
Balances are integers in $[-n, n]$, so there are at most $2n + 1$ possible keys and at most $n$
keys actually inserted — $O(n)$ in the worst case, and much less for a single-sided instance where
the table stays empty. The running balances, the pivot index, and the answer are a constant number
of integers, $O(1)$. Nothing is sorted, and no copy of `nums` is made, so the only super-constant
storage is the table.

**Why the space cannot be reduced to $O(1)$ easily.** The right-wing balances are consumed in a
different order from the left-wing queries, so they must be retained; any $O(1)$-space variant
would have to rescan the right wing per left endpoint, paying $O(n^2)$ time. The $O(n)$ table is the
deliberate purchase that buys the linear time bound.
