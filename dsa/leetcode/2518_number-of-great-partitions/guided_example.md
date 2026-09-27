# Guided Example: Number of Great Partitions

## 1. The Instance and What Must Be Counted

We are given an array of **positive** integers and a threshold $k$. A partition splits the array into two **ordered** groups so that every element lands in exactly one group, and the partition is *great* when each group's total is at least $k$. Two partitions are distinct when some element is placed in a different group. We must count the great partitions modulo $10^{9}+7$.

We work the first official instance:

- `nums` = `[1, 2, 3, 4]`
- `k` = `4`

The total is $1+2+3+4 = 10$ and the required output is `6`. The lesson is the *method*: enumerating partitions directly explodes as $2^{n}$, but the condition "each side reaches $k$" can be counted from the opposite direction — count the assignments in which one named group falls **short** of $k$, and subtract. That inversion is what makes the problem tractable, and this instance is small enough that every number in the inversion can be checked by hand.

## 2. Assignments, Not Subsets: Why the Groups Are Labelled

Model a partition as a function that sends each index $i$ to one of two labels, say group $A$ and group $B$. Because the labels are ordered and distinct, the number of raw assignments is exactly

$$\lvert\{A \subseteq \{0,\dots,n-1\}\} \rvert = 2^{n},$$

where the subset $A$ names the members of group $A$ and its complement names the members of group $B$. The pair $(A, B)$ and the pair $(B, A)$ are **different** partitions even though they contain the same two groups. For $n = 4$ there are $2^{4} = 16$ assignments in total, and the count of great ones must respect that labelling.

Write the group sums as

$$S(A) = \sum_{i \in A} \texttt{nums[i]}, \qquad S(\overline{A}) = \Sigma - S(A), \qquad \Sigma = \sum_{i=0}^{n-1} \texttt{nums[i]},$$

so that $S(A) + S(\overline{A}) = \Sigma$ for every assignment. An assignment is great exactly when

$$S(A) \ge k \quad \text{and} \quad S(\overline{A}) \ge k.$$

Two immediate consequences frame everything that follows. Because all values are positive and $k \ge 1$, an empty group has sum $0 < k$, so a great partition never leaves a group empty. And because the two sums are complementary, they cannot both be small: if $\Sigma < 2k$ then for every assignment at least one side is below $k$, so the answer is $0$ and no counting is needed at all. Here $\Sigma = 10 \ge 2 \cdot 4 = 8$, so the counting path is live.

## 3. Complement Counting and Inclusion–Exclusion

Let $X$ be the number of assignments whose group $A$ has sum below $k$:

$$X = \lvert\{\, A : S(A) < k \,\}\rvert.$$

By the complement relation, the map $A \mapsto \overline{A}$ is a bijection of the assignment space, so the number of assignments whose **group $B$** has sum below $k$ is also $X$. The bad assignments — those that fail the great condition — are exactly those with $S(A) < k$ or $S(\overline{A}) < k$. Inclusion–exclusion gives

$$\#\text{bad} = X + X - \lvert\{\, A : S(A) < k \ \text{and}\ S(\overline{A}) < k \,\}\rvert.$$

The intersection term is zero whenever $\Sigma \ge 2k$, because $S(A) < k$ and $S(\overline{A}) < k$ together force $\Sigma = S(A) + S(\overline{A}) < 2k$, a contradiction. Under that guard the answer collapses to a clean formula:

$$\#\text{great} = 2^{n} - 2X \pmod{10^{9}+7}.$$

So the whole problem reduces to counting subsets $A$ of the index set whose sum is at most $k-1$. With $k = 4$ the small subset sums live in $\{0, 1, 2, 3\}$; every element of value $4$ or more is automatically excluded from every small subset, which is a useful structural shortcut rather than a special case.

## 4. Census of the Small Subsets

Enumerating all $16$ subsets of `{1, 2, 3, 4}` and keeping those with sum below $4$:

| Subset $A$ (by value) | $S(A)$ | Below $k = 4$? | Counted by the DP in column $j = S(A)$ |
|:---|:---:|:---:|:---|
| $\varnothing$ | 0 | yes | $f[n][0]$ |
| `{1}` | 1 | yes | $f[n][1]$ |
| `{2}` | 2 | yes | $f[n][2]$ |
| `{3}` | 3 | yes | $f[n][3]$ |
| `{1, 2}` | 3 | yes | $f[n][3]$ |
| `{4}`, `{1,3}`, `{2,3}`, `{1,4}`, `{2,4}`, `{3,4}`, `{1,2,3}`, `{1,2,4}`, `{1,3,4}`, `{2,3,4}`, `{1,2,3,4}` | at least 4 | no | excluded |

The surviving subsets are five, so $X = 5$. Reading the table columnwise explains the DP shape: the census is indexed by the **exact** sum, not by a yes/no flag, because two different subsets (`{3}` and `{1,2}`) share the sum $3$ and both must be counted separately. Concretely, the small-sum histogram is

| Exact sum $j$ | 0 | 1 | 2 | 3 | Total $X$ |
|:---|:---:|:---:|:---:|:---:|:---:|
| Number of subsets of `[1,2,3,4]` with $S(A) = j$ | 1 | 1 | 1 | 2 | 5 |

Then $\#\text{great} = 16 - 2 \cdot 5 = 6$, matching the required output before any modular reduction. This is the single most useful check on the whole method: the histogram totals $X$, and the formula turns it into the answer.

## 5. Building the Histogram Incrementally

Adding elements one at a time turns the census into a small dynamic program. Let $f[i][j]$ be the number of subsets of the first $i$ elements whose sum is exactly $j$, for $j \in \{0, 1, \dots, k-1\}$ — sums of $k$ or more are irrelevant because they can never mark a group as short. Every subset either omits the new element or includes it, and those two families are disjoint, so

$$f[i][j] = f[i-1][j] + \big[\, j \ge \texttt{nums[i-1]} \,\big] \cdot f[i-1][\, j - \texttt{nums[i-1]} \,],$$

with the base case $f[0][0] = 1$ and $f[0][j] = 0$ for $j > 0$ — the empty subset is the only subset of no elements. The guard $j \ge \texttt{nums[i-1]}$ is exactly what keeps an element of size $k$ or larger out of every small subset: for such an element the second term is never taken.

Running the recurrence on `[1, 2, 3, 4]` with $k = 4$, so that $j$ ranges over $\{0,1,2,3\}$:

| Step $i$ | Element added | $f[i][0]$ | $f[i][1]$ | $f[i][2]$ | $f[i][3]$ | Row total |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | none (base) | 1 | 0 | 0 | 0 | 1 |
| 1 | 1 | 1 | 1 | 0 | 0 | 2 |
| 2 | 2 | 1 | 1 | 1 | 1 | 4 |
| 3 | 3 | 1 | 1 | 1 | 2 | 5 |
| 4 | 4 | 1 | 1 | 1 | 2 | 5 |

Three readings of this table carry the intuition:

- **Row 2.** After `1` and `2` are available, every one of the four subsets is small, so each of the four achievable sums $0, 1, 2, 3$ is hit once and the row total is $4 = 2^{2}$.
- **Row 3.** Adding `3` creates the subset `{3}` (contributing to $j = 3$) and the subset `{1,2}` (also $j = 3$, via $f[2][0]$), which is why $f[3][3]$ jumps to $2$ while the other columns are unchanged. The two subsets are distinct index sets with equal value, and the histogram counts both.
- **Row 4.** Element `4` satisfies $4 \ge k$, so the guarded second term never fires and the row is a verbatim copy of row 3. The remaining element is still assigned to a group by every one of the $16$ assignments — it simply can never be part of a *short* group, because putting it anywhere already pushes that group to at least $4$.

The final row is the histogram: $1 + 1 + 1 + 2 = 5$, so $X = 5$ and $\#\text{great} = 2^{4} - 2 \cdot 5 = 6$.

## 6. Correctness and the Counting Invariants

**DP invariant.** After step $i$, the entry $f[i][j]$ equals the number of index subsets of `{nums[0], ..., nums[i-1]}` whose value sum is exactly $j$, for every $j < k$.

*Initialization.* Before any element is considered, only the empty subset exists, with sum $0$, so $f[0][0] = 1$ and all other entries are $0$.

*Preservation.* Every subset of the first $i$ elements either omits element $i-1$ — these are precisely the subsets counted by $f[i-1][j]$ — or contains it, in which case removing it leaves a subset of the first $i-1$ elements with sum $j - \texttt{nums[i-1]}$, and this correspondence is a bijection. The two families are disjoint, so their sizes add; the guard on $j$ merely records that a negative remainder has no subsets. Entries with $j \ge k$ are deliberately never formed: a subset with sum at least $k$ can never witness a below-$k$ group, so it cannot influence the answer.

*Termination.* Row $n$ is the complete histogram, and $X = \sum_{j=0}^{k-1} f[n][j]$ counts exactly the assignments in which group $A$ is short.

**Answer invariant.** With $\Sigma = 10 \ge 2k = 8$, the great count is $2^{n} - 2X$, and the result is reduced modulo $10^{9}+7$ with a correction of $+10^{9}+7$ before the final reduction so that the subtraction never returns a negative residue. Each of the $6$ counted assignments is a real partition of this instance; the next section lists them.

## 7. The Six Great Partitions, and Why They Pair Up

| # | Group $A$ | Group $B$ | $S(A)$ | $S(\overline{A})$ | Mirror of |
|:---:|:---|:---|:---:|:---:|:---:|
| 1 | `[1, 2, 3]` | `[4]` | 6 | 4 | #6 |
| 2 | `[1, 3]` | `[2, 4]` | 4 | 6 | #5 |
| 3 | `[1, 4]` | `[2, 3]` | 5 | 5 | #4 |
| 4 | `[2, 3]` | `[1, 4]` | 5 | 5 | #3 |
| 5 | `[2, 4]` | `[1, 3]` | 6 | 4 | #2 |
| 6 | `[4]` | `[1, 2, 3]` | 4 | 6 | #1 |

All twelve group sums are at least $4$, and the list is closed under swapping the groups — the six partitions form three mirror pairs, exactly as the factor $2$ in the subtraction suggests. The same pairing explains why we subtract $2X$ and not $X$: the five small subsets are the five ways to make group $A$ short, and their complements are the five ways to make group $B$ short, and every bad assignment appears once in one of those two families because the intersection is empty here.

## 8. Traps and Boundary Behaviour

| Scenario | Instance | Arithmetic | Result | Why the rule still holds |
|:---|:---|:---|:---:|:---|
| total supports the guard but no assignment qualifies | `nums = [3,3,3]`, `k = 4` | $\Sigma = 9 \ge 8$, $X = 4$ (empty set plus the three singletons) | 0 | $2^{3} - 2 \cdot 4 = 0$; the guard and the formula agree whenever $\Sigma \ge 2k$. |
| genuinely insufficient total | `nums = [1,2,3]`, `k = 4` | $6 < 8$ | 0 | Every assignment leaves one side below $k$, so the intersection term stops being zero and the formula must be abandoned; the guard returns $0$ first. |
| an element at least $k$ | `nums = [1,2,3,4]`, `k = 4`, value `4` | guarded term never fires for $j \le 3$ | — | Such an element cannot belong to a short group, so the DP row is unchanged; treating it as ordinary would corrupt the histogram. |
| equal values, distinct indices | `nums = [6,6]`, `k = 2` | $X = 1$, $2^{2} - 2 = 2$ | 2 | Subsets are index sets: `{nums[0]}` and `{nums[1]}` are different assignments even though both read `[6]`. Value identity is not index identity. |
| two identical halves | `nums = [2,2,2,2]`, `k = 4` | $X = 5$, $2^{4} - 10 = 6$ | 6 | Only $\binom{4}{2} = 6$ assignments give each side sum $4$; the histogram must count size-$1$ subsets as short, which it does. |
| one element only | `nums = [100]`, `k = 1` | $X = 1$, $2^{1} - 2 = 0$ | 0 | A single element cannot populate both groups, so no assignment can be great. |
| very large answer | `nums` = forty `1`s, `k = 1` | $2^{40} - 2$ then reduced | 511620081 | The count must be computed mod $10^{9}+7$; the DP entries are also reduced so intermediate sums stay bounded. |

A semantic trap that costs solutions is the meaning of "ordered". If the two groups were unlabelled, each mirror pair would collapse to one object and the answer would be $3$ for this instance, not $6$. The problem's distinctness rule — an element in a different group makes a different partition — confirms the labelled reading, and the enumeration table above shows all six.

## 9. Complexity: Time and Auxiliary Space

**Time.** The table has $n+1$ rows and $k$ columns, and each entry is formed with one addition and one modular reduction, so the DP costs

$$T(n, k) = \mathrm{O}(n \cdot k)$$

with $n = \texttt{nums.length}$. The preliminary total sum is a single $\mathrm{O}(n)$ pass, which is dominated by the table. Each element larger than or equal to $k$ still occupies its row, but its guard simply copies the previous row; the asymptotics are unchanged and the constant is small because the inner loop never exceeds $k$ iterations, i.e. at most $1000$ here regardless of how large the element values are.

**Auxiliary space.** The recurrence for row $i$ reads only row $i-1$, so the full table is not required. Keeping two row vectors of length $k$ — or one vector updated in place if the column order makes the read-before-write safe — is enough, giving

$$S_{\text{aux}}(n, k) = \mathrm{O}(k).$$

The histogram of the final row is summed to produce $X$, and the power $2^{n}$ is accumulated by repeated doubling under the modulus, so no array of size $n$ and no big-integer power is ever materialized. The stated bound $k \le 1000$ is what keeps this auxiliary vector comfortably small.

## 10. Alternatives and Their Trade-offs

| Alternative | How it would work | Cost | Why it is not preferred |
|:---|:---|:---|:---|
| Enumerate all $2^{n}$ assignments | Test $S(A) \ge k$ and $S(\overline{A}) \ge k$ for every subset. | $\mathrm{O}(n \cdot 2^{n})$ time | Correct but hopeless at $n = 1000$; it also makes the complement structure invisible instead of exploiting it. |
| Meet in the middle over values | Split the array in halves and combine half-histograms up to $k$. | $\mathrm{O}(2^{n/2})$ time | Still exponential; the threshold structure of the problem allows a polynomial count, so trading one exponential for a smaller one is not progress. |
| Count great assignments directly with a $2 \times k$ DP | Track both partial group sums up to $k$. | $\mathrm{O}(n \cdot k^{2})$ time | Correct but needs two sum dimensions; counting the *complement* needs one dimension and a factor $2$, because the two group sums are linked by $\Sigma$. |
| Count short subsets and forget the factor $2$ | Subtract $X$ instead of $2X$. | $\mathrm{O}(n \cdot k)$ time | Under-counts the bad assignments: the mirror of every short-$A$ assignment is a short-$B$ assignment, and both must be removed. |
| Full $n \times k$ table without rolling rows | Keep every intermediate row. | $\mathrm{O}(n \cdot k)$ space | Same answer, more memory; only the previous row is ever consulted, so the extra rows are pure bookkeeping. |

The transferable idea is the inversion itself: when a condition must hold on **both** sides of a two-way split, count the one-sided failures. They are usually far easier to enumerate, and here they reduce to a classic subset-sum histogram with a single bounded dimension.