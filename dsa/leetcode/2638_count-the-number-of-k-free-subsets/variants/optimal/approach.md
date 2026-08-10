## General

**Turn forbidden differences into independent chains**

Two selected values conflict exactly when their absolute difference is $k$.

If $a-b=k$, then $a$ and $b$ have the same remainder modulo $k$. Values with different remainders can never differ by exactly $k$.

Therefore, the solution partitions the sorted values by `x % k`. Each remainder group can be solved independently, and the numbers of choices from different groups can later be multiplied.

**Why sorting makes each group a path**

`nums.sort()` orders all values. Appending them to their remainder lists preserves increasing order inside every group:

$$
a_0<a_1<\cdots<a_{m-1}.
$$

Within one remainder group, every difference is a positive multiple of $k$. A forbidden difference occurs precisely when two values differ by one multiple of $k$.

If `arr[i] - arr[i - 1] > k`, then the gap is at least $2k$. The current value cannot differ by $k$ from any still earlier value because those are even smaller.

Thus every conflict is between consecutive group values whose gap is exactly $k$. The conflict graph is a sequence of path segments, which admits a two-state counting recurrence.

**Define the prefix count**

Let `f[i]` be the number of valid selections from the first $i$ values of one remainder group.

The empty prefix has exactly one subset, the empty set:

$$
f[0]=1.
$$

A one-value prefix has two subsets, choose it or skip it:

$$
f[1]=2.
$$

Every group is nonempty when processed, so assigning both base cases is safe.

**Case one: the new value conflicts with its predecessor**

Suppose:

$$
a_{i-1}-a_{i-2}=k.
$$

Partition valid subsets of the first $i$ values into two disjoint categories:

- subsets that skip $a_{i-1}$: any valid subset of the first $i-1$ values, giving $f[i-1]$ choices;
- subsets that take $a_{i-1}$: they must skip $a_{i-2}$, while the first $i-2$ values can be chosen validly in $f[i-2]$ ways.

Therefore:

$$
f[i]=f[i-1]+f[i-2].
$$

This is the familiar independent-set recurrence for a path.

**Case two: the new value has no conflict**

If the consecutive gap is not $k$, it must be larger than $k$ within the same remainder group. The current value conflicts with no earlier value.

Every valid subset of the previous prefix can either:

- omit the current value, or
- include it.

These choices are independent and distinct, so:

$$
f[i]=2f[i-1].
$$

This also correctly starts a new disconnected path segment after a large gap.

**Multiply independent remainder choices**

For one remainder group of size $m$, `f[m]` counts all valid selections from that group, including selecting nothing.

Choose one valid subset independently from every group. Their union is globally k-free because cross-group values cannot differ by $k$.

Conversely, every global k-free subset restricts to one valid choice in each remainder group. This is a bijection, so the product rule gives:

$$
\texttt{ans}=\prod_{\text{groups }G} f_G[|G|].
$$

`ans` starts at one, the multiplicative identity.

**Trace the first example**

For `nums = [5,4,6]` and $k=1$, every value has remainder zero. Sorting gives `[4,5,6]`.

- $f[0]=1$ and $f[1]=2$;
- five differs from four by one, so $f[2]=2+1=3$;
- six differs from five by one, so $f[3]=3+2=5$.

The five subsets are empty, each singleton, and pair `{4,6}`. Adjacent numerical pairs are forbidden.

**Trace completely independent values**

If no two values differ by $k$, every group either has isolated values or gaps exceeding $k$. Each transition doubles the count.

Across $n$ values, the product becomes $2^n$, correctly counting every possible subset.

**Why distinctness matters**

The input values are distinct. Therefore, one group never contains a zero gap, and each value is one selectable element.

With duplicates, equal values would represent separate choices and require frequency-aware weights. The exact recurrence intentionally relies on the distinct-element contract.


Induct on prefix length $i$. Base cases enumerate all subsets directly. For the next value, every valid subset either includes it or not.

When a conflict edge exists, inclusion forces exclusion of exactly the predecessor; no earlier conflict is possible beyond that predecessor. When no edge exists, inclusion is unrestricted.

The recurrence exhausts these disjoint cases without overlap, so `f[i]` is correct. The product bijection then proves the global answer.

## Complexity detail

Let $n=\texttt{nums.length}$. Sorting costs $O(n\log n)$. Grouping and all DP loops collectively process each value once, adding $O(n)$ time. Total time is $O(n\log n)$.

Remainder lists collectively store $n$ values. A DP array for one group can contain up to $n+1$ entries. Total auxiliary space is $O(n)$.

The input list is mutated by sorting.

## Alternatives and edge cases

- **Backtracking all subsets:** Direct but costs $O(2^n)$ for up to 50 values.
- **Conflict graph DP:** Building edges reveals disjoint paths; modulo grouping constructs those paths more directly.
- **Two scalar DP states:** `f[i-2]` and `f[i-1]` are sufficient, reducing per-group DP storage to $O(1)$ beyond groups.
- **No conflicts:** Every subset is valid, yielding $2^n$.
- **One value in a group:** It contributes two choices.
- **Consecutive chain:** Counts follow the path-independent-set Fibonacci recurrence.
- **Gap greater than `k`:** It breaks the conflict path and doubles the prior count.
- **Different remainders:** Such values are always independent for difference exactly $k$.
- **Empty subset:** Included through `f[0]=1` and the product.
- **Input mutation:** Sorting changes `nums` order but not the subset-counting meaning.
