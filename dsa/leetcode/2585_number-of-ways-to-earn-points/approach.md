## General

**Each type contributes one bounded choice**

For type $i$, choose an integer $k_i$ between zero and `count[i]`. That choice contributes

$$
k_i\cdot\texttt{marks[i]}
$$

points. Questions within a type are indistinguishable, so choosing three questions of one type is one choice, not a binomial number of choices among individual question identities.

The task is to count vectors of chosen counts whose total is exactly `target`. This is bounded knapsack counting.

**Meaning of the DP table**

Let `f[i][j]` be the number of ways to earn exactly $j$ points using only the first $i$ question types.

The table has `n + 1` rows and `target + 1` columns. Row zero represents using no types. There is exactly one way to earn zero points with no types—choose nothing—so `f[0][0] = 1`. Every positive score in row zero remains zero.

The desired answer is `f[n][target]` after every type has been considered.

**Transition for one type**

Suppose the current type provides at most `count` questions worth `marks` each. To finish with total $j$, the solution may answer $k$ of this type for any

$$
0\le k\le\texttt{count}
$$

such that $k\cdot\texttt{marks}\le j$.

After choosing those $k$ questions, previous types must contribute exactly

$$
j-k\cdot\texttt{marks}.
$$

That subproblem has `f[i - 1][j - k * marks]` ways. Summing over every legal $k$ gives

$$
f[i][j]
=
\sum_{\substack{0\le k\le count\\k\cdot marks\le j}}
f[i-1][j-k\cdot marks].
$$

The innermost code checks `j >= k * marks` before adding the term.

**Why there is no combination multiplier**

If there are six one-point questions of the same type and the choice is $k=4$, the statement treats all choices of four as identical. The DP transition adds the previous count once for $k=4$.

Multiplying by “six choose four” would count individual questions as distinguishable and contradict the contract. Different ways arise only from different counts across types.

**Why every way is counted once**

Take any valid exam plan. Its number $k$ of answered questions from the final type is uniquely determined. Removing that contribution leaves a plan counted in `f[n-1][target-k*marks]`. The transition includes it under exactly that $k$.

Conversely, every previous-type plan from one transition term plus $k$ current questions earns exactly the target and respects the bound. Different $k$ values or different previous plans produce different count vectors. Thus the recurrence is complete and has no duplicates.

Induction over the rows proves every table entry has its stated meaning.

**Trace a small target**

For `target = 5` and types `[[50,1],[50,2],[50,5]]`:

- after the one-point type, every score zero through five has one way;
- adding the two-point type makes score five possible with $(5,0)$, $(3,1)$, or $(1,2)$ counts;
- the five-point type adds the separate choice $(0,0,1)$.

The final count is four.

**Modulo handling**

Each addition is reduced modulo $10^9+7$. Modular addition preserves the final count modulo the same number:

$$
(a+b)\bmod M=((a\bmod M)+(b\bmod M))\bmod M.
$$

Reducing incrementally prevents table values from growing with the enormous number of possible count combinations.

**Exact implementation versus manifest**

The manifest describes an optimized sliding-window bounded knapsack with $O(n\cdot target)$ time and $O(target)$ space. The checked-in solution is the direct three-loop recurrence with a full two-dimensional table.

It tries every $k$ from zero through `count` for every type and target score, even after `k * marks > j`; the condition merely skips the addition. This is simpler to derive but has an extra factor of the maximum count.

## Complexity detail

Let $n$ be the number of types, $T$ the target, and $C$ the maximum `count`. The loops perform $(n)(T+1)(C+1)$ condition checks, giving $O(nTC)$ time. This differs from the manifest's $O(nT)$ optimized bound.

The table contains $(n+1)(T+1)$ integers, so exact auxiliary space is $O(nT)$, not the manifest's $O(T)$. Scalar loop state is constant beyond the table.

## Alternatives and edge cases

- **Sliding window by remainder class:** For each marks value, maintain rolling sums across scores with the same remainder, reducing time to $O(nT)$ and space to $O(T)$.
- **One-dimensional backward DP repeated per copy:** Treating copies separately can overcount indistinguishable questions unless bounded transitions are designed carefully.
- **Recursive memoization:** It expresses the same state but may explore all count branches and incur recursion overhead.
- **Zero questions of a type:** The $k=0$ term copies all previous ways into the new row.
- **Marks greater than target:** Only $k=0$ can contribute, so the type changes nothing.
- **Exact target only:** Scores below or above target are not acceptable final answers; column `target` is returned.
- **Indistinguishable questions:** No binomial coefficient belongs in the transition.
- **Target unreachable:** The final table cell remains zero.
- **Modulo:** Every transition addition is reduced, keeping values bounded.
- **Manifest distinction:** The current source is direct bounded enumeration, not the optimized sliding-window method.
