## General

**Maintain what each growing prefix has seen**

At index $i$, the desired value is:

$$
|\{A[0],\ldots,A[i]\}
\cap
\{B[0],\ldots,B[i]\}|.
$$

The exact solution uses two counters:

- `cnt1` for values in the current prefix of `A`;
- `cnt2` for values in the current prefix of `B`.

Because both arrays are permutations, each frequency is either zero or one. Counters still provide a uniform way to express how much multiplicity the two prefixes share.

**Grow both prefixes together**

`zip(A, B)` produces pairs `(A[i], B[i])` in increasing index order. The arrays have equal length, so no value is truncated.

For each pair `(a,b)`:

- increment `cnt1[a]`;
- increment `cnt2[b]`;
- compute the size of their current multiset intersection;
- append it to `ans`.

The count is measured after both current values are inserted, which matches prefixes ending at the current index inclusively.

**Why the minimum of two frequencies measures overlap**

For value $x$, the number of copies shared by two multisets is:

$$
\min(\texttt{cnt1[x]},\texttt{cnt2[x]}).
$$

Summing over values seen in the first prefix gives:

`sum(min(v, cnt2[x]) for x, v in cnt1.items())`.

Under the permutation guarantee, this contribution is one exactly when $x$ has appeared in both prefixes and zero otherwise.

Thus the sum is the number of common distinct values.

**Why iterating only `cnt1` keys is sufficient**

A value present only in `cnt2` contributes zero to the intersection because its `cnt1` frequency is zero.

Such values do not need explicit iteration. Every positive intersection contribution must correspond to a key already in `cnt1`.

`defaultdict`-style Counter access `cnt2[x]` returns zero for missing values without inserting a meaningful positive count.

**Trace the first example**

For `A = [1,3,2,4]` and `B = [3,1,2,4]`:

- index zero: first prefix has one, second has three, intersection size zero;
- index one: both prefixes contain one and three, size two;
- index two: both additionally contain two, size three;
- index three: both contain all four values, size four.

The result is `[0,2,3,4]`.

**Why a common count can increase by two**

At one index, `a` and `b` can be different.

If `a` was already seen in B's prefix and `b` was already seen in A's prefix, adding the two current elements completes two different common values simultaneously.

This is why changes are not limited to zero or one. Recomputing the full intersection naturally captures either increase.


After processing index $i$:

- `cnt1[x]` equals occurrences of $x$ in `A[0..i]`;
- `cnt2[x]` equals occurrences of $x$ in `B[0..i]`.

The increments establish these statements directly from the previous prefixes.

For each value, the minimum frequency is precisely the number of copies common to both multisets. Summing these contributions therefore produces `C[i]`. Appending after every iteration gives the complete prefix common array in order.

**Exact implementation versus the manifest**

The manifest records $O(n)$ time and describes counting when a value becomes present in both prefixes.

The exact source instead recomputes the intersection sum over every key currently in `cnt1` at each index. Since `A` is a permutation, the number of keys grows as:

$$
1,2,\ldots,n.
$$

Total work is therefore:

$$
1+2+\cdots+n=O(n^2).
$$

This document describes that exact behavior rather than attributing the absent incremental optimization to it.

**How the linear method would improve it**

A frequency array could track how many times each value has appeared across both current prefixes.

At each index, increment counts for `A[i]` and `B[i]`. Whenever a value's combined count reaches two for the first time, it becomes common and increments a running total.

Because permutations contain each value once per array, this reaches true common status exactly once. That yields $O(n)$ time.

**Why counters remain correct beyond permutations**

The minimum-frequency expression actually computes multiset intersection size even with duplicates. However, the problem defines permutations and asks for numbers present in both, so duplicates are absent and the meaning reduces to distinct common values.

## Complexity detail

At prefix length $i+1$, the exact sum scans $i+1$ keys. Across all prefixes, time is $O(n^2)$.

The two counters can each hold $n$ keys, and the answer stores $n$ integers, giving $O(n)$ space.

The manifest's $O(n)$ bound belongs to the incremental frequency method, not this exact implementation.

## Alternatives and edge cases

- **Incremental frequency array:** Update a running common count only when a value has appeared in both prefixes, achieving $O(n)$ time.
- **Two prefix sets and intersection:** Rebuilding `setA & setB` each time is also potentially quadratic.
- **Brute nested search:** Repeated membership scans can become cubic if implemented carelessly.
- **Length one:** The same sole permutation value appears in both, so result is `[1]`.
- **Different first values:** The first answer is zero.
- **Same current value:** It can add one newly common value, not two.
- **Cross-completed values:** Different `a` and `b` can raise the count by two.
- **Final prefix:** Both contain all values from one through $n$, so final answer is $n$.
- **Permutation guarantee:** Counter frequencies never exceed one.
- **Input preservation:** Both arrays are read only.
