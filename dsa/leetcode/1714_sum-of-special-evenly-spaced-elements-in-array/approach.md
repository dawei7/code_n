## General

**A query follows one arithmetic progression of indices**

Query `[x,y]` asks for

$$
\texttt{nums}[x]+\texttt{nums}[x+y]+\texttt{nums}[x+2y]+\cdots
$$

while indices remain below $n$. Computing that sum directly takes about $n/y$ terms. This is cheap for large step `y` but expensive when `y` is small, especially across many queries.

The source uses square-root decomposition: precompute answers for every small step and enumerate terms only for large steps.

**Choose the small-step boundary**

`m = int(sqrt(n))` is $\lfloor\sqrt n\rfloor$. Steps `1` through `m` are treated as small. Steps greater than `m` are large.

There are only $m$ small step sizes, so storing information for all of them is manageable compared with precomputing all $n$ possible steps. A large step visits at most roughly $n/(m+1)+1=O(\sqrt n)$ array positions, making direct evaluation bounded.

**Define a step-specific suffix recurrence**

`suf` is a table with rows zero through `m` and columns zero through `n`. Row zero is unused. Column `n` acts as a zero sentinel.

For a small step `i`, define

$$
\texttt{suf}[i][j]
=
\texttt{nums}[j]
+\texttt{nums}[j+i]
+\texttt{nums}[j+2i]+\cdots
$$

for valid indices. The recurrence is

$$
\texttt{suf}[i][j]
=
\texttt{nums}[j]+\texttt{suf}[i][j+i].
$$

The source fills `j` from `n-1` down to zero, so `j+i` has already been computed whenever it is inside the array.

**Use the sentinel for an out-of-range next position**

The implementation reads

`suf[i][min(n, j + i)]`.

If `j+i<n`, this is the next progression sum. If `j+i>=n`, `min` chooses column `n`, whose initialized value is zero. Thus the last term of every progression is simply `nums[j] + 0`, with no separate branch.

Even if `j+i` exceeds `n` by more than one, clamping to the same sentinel is correct because every such next index is out of range.

**Answer small steps in constant time**

For query `[x,y]` with `y <= m`, the complete requested progression was precomputed exactly as `suf[y][x]`. The source appends `suf[y][x] % mod`.

Precomputed entries are not reduced modulo during construction. Python integers preserve the exact sum, and reducing at query time gives the required remainder.

**Answer large steps directly**

For `y > m`, `nums[x::y]` creates the list of elements beginning at `x` and then every `y` positions. This is precisely the query's divisibility condition because selected indices are `x+ty`.

`sum(...) % mod` then produces the answer. The slice contains only $O(n/y)=O(\sqrt n)$ elements for a large step, so no large-step table is necessary.

The answer list receives one result per query in original order.

**Why the split is correct**

Every positive `y` falls into exactly one branch. In the small branch, backward induction on `j` proves that `suf[y][j]` equals the progression sum from `j`. The base is an out-of-range next index mapping to zero, and the recurrence adds exactly the current term.

In the large branch, Python's extended slice enumerates exactly the same index progression. Therefore both branches compute the contract's sum, and modulo reduction preserves the required answer.

For `nums=[0,1,2,3,4,5,6,7]` and query `[0,3]`, the relevant progression is indices zero, three, and six. Whether step three is precomputed depends on `m`, but the selected values remain zero, three, and six, totaling nine.

## Complexity detail

Let $q$ be the number of queries and $S=\lfloor\sqrt n\rfloor$. Building each of $S$ small-step rows scans all $n$ indices, costing $O(nS)$ time.

A small-step query costs $O(1)$. A large-step query visits $O(n/y)$ terms, and `y>S` makes this $O(n/S)=O(S)$ up to rounding. Across all queries, time is therefore

$$
O(nS+qS)=O((n+q)S),
$$

matching the manifest's time bound.

The table contains $(S+1)(n+1)$ Python integers, using $O(nS)$ space. The result uses $O(q)$, and a large-step slice temporarily uses $O(S)$ elements. Peak space is $O(nS+q)$.

The manifest's $O(n+q)$ space does not match this exact two-dimensional `suf` allocation. Achieving linear storage would require a different query grouping or more selective precomputation not present in `solution.py`.

## Alternatives and edge cases

- **Direct sum for every query:** It uses little persistent state but can cost $O(qn)$ when many queries have step one.
- **Precompute every step:** It answers all queries in constant time but uses $O(n^2)$ time and space.
- **Group queries by small step:** Compute only step rows that are actually requested, potentially saving memory on sparse workloads.
- **Offline accumulation with linear storage:** More specialized organization can reduce the table footprint, but it is not the exact source.
- **Step one:** `suf[1][x]` is the ordinary suffix sum from `x`.
- **Step greater than remaining length:** The slice contains only `nums[x]`.
- **Start at last index:** Every positive step produces a one-element sum.
- **Zero values:** They contribute normally and do not affect recurrence validity.
- **Large element sums:** Python integers avoid overflow before modulo reduction.
- **Modulo timing:** Reducing only at query time is equivalent to modular recurrence but may store larger integers.
- **Square-root rounding:** `int(sqrt(n))` floors the threshold; the large branch still has $O(\sqrt n)$ terms.
- **Sentinel column:** It must stay zero for every row so clamped out-of-range recurrences terminate correctly.
- **Slice allocation:** `nums[x::y]` creates a temporary list rather than streaming its terms.
