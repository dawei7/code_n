## General

**Transform the inequality into a one-dimensional comparison**

The original condition for $i<j$ is

$$
\texttt{nums1}[i] - \texttt{nums1}[j]
\le
\texttt{nums2}[i] - \texttt{nums2}[j] + \texttt{diff}.
$$

Move the terms belonging to the same index together and define

$$
v_t = \texttt{nums1}[t] - \texttt{nums2}[t].
$$

The condition becomes

$$
v_i \le v_j + \texttt{diff}.
$$

Now process indices from left to right. At current index $j$, every value previously inserted belongs to some $i<j$, so the index-order requirement is automatic. The only remaining task is to count earlier transformed values no greater than the threshold $v_j+\texttt{diff}$.

**What the Fenwick tree stores**

A Fenwick tree, or binary indexed tree, stores frequencies over integer positions and supports two operations:

- `update(x, 1)` records one more earlier transformed value at position `x`.
- `query(x)` returns the total frequency in positions 1 through `x`, inclusive.

The transformed values may be negative. From the constraints,

$$
-20000 \le v_t \le 20000.
$$

The exact source adds an offset of 40000, mapping update positions into the positive interval from 20000 through 60000. A query threshold can additionally include `diff`, so `v + diff + 40000` lies from 10000 through 70000. All positions fit safely inside the tree of size $10^5$.

The local variant summary calls this “coordinate-compressed,” but the exact implementation does not sort and compress coordinates. It uses a fixed numeric offset and a fixed-size Fenwick tree based on the stated bounds. That distinction matters when adapting the method to wider or unbounded values.

**How Fenwick updates work**

The internal array `c` is one-indexed. The helper `lowbit(x) = x & -x` isolates the least significant set bit. At a position `x`, `c[x]` stores the sum for a block whose length is `lowbit(x)` and whose right endpoint is `x`.

To add `delta` at one point, `update` changes `c[x]` and then advances by `lowbit(x)`. Each new index represents a larger block that contains the original point. The loop ends after passing `self.n`.

This update position must never be zero because `lowbit(0)` is zero and the loop would not advance. The chosen offset and transformed-value bounds guarantee a minimum update index of 20000, so the implementation is safe for every valid input.

**How prefix queries work**

To compute the number of inserted values at positions at most `x`, `query` adds `c[x]` and removes the last covered block by subtracting `lowbit(x)`. The selected blocks are disjoint and together cover positions 1 through the original `x`. The index eventually reaches zero.

Because every update and query uses the same offset, an earlier value $v_i$ contributes to

`tree.query(v_j + diff + 40000)`

if and only if

$$
v_i + 40000 \le v_j + \texttt{diff} + 40000,
$$

which is equivalent to the required $v_i \le v_j+\texttt{diff}$. The prefix query is inclusive, correctly preserving the original `<=` rather than accidentally enforcing a strict inequality.

**Query before inserting the current value**

For each aligned pair `a, b`, the code computes `v = a - b`. It first adds the query result to `ans` and only afterward calls `tree.update(v + 40000, 1)`.

This order enforces $i<j$. At query time, the tree contains exactly the transformed values for indices strictly earlier than the current one. If the current value were inserted first, it could count the invalid self-pair $(j,j)$ whenever `diff >= 0`.

After the update, the current transformed value becomes available to all later indices.

For `nums1 = [3, 2, 5]` and `nums2 = [2, 2, 1]`, the transformed sequence is `[1, 0, 4]`. With `diff = 1`, the first index finds no earlier values and inserts 1. At the second value 0, the threshold is 1, so the earlier 1 is counted. At the third value 4, the threshold is 5, so both earlier values are counted. The total is 3.

**Why every valid pair is counted once**

Consider a pair $(i,j)$ with $i<j$. When the scan reaches $j$, $v_i$ has been inserted exactly once and $v_j$ has not yet been inserted. The prefix query includes $v_i$ exactly when its transformed inequality holds. Thus each valid pair contributes once at its later endpoint, and each invalid pair contributes zero.

Conversely, every frequency returned by the query belongs to an earlier index and satisfies the threshold, so every unit added to `ans` represents a valid pair. This establishes both completeness and absence of overcounting.

## Complexity detail

Let $n$ be the common array length and let $C=100000$ be the fixed Fenwick capacity. One update and one query each visit $O(\log C)$ tree positions. The scan therefore costs $O(n\log C)$ time. Since $C$ is a constraint-derived constant, this is technically $O(n)$ with respect to $n$ alone; the broader and commonly stated bound $O(n\log n)$ in the manifest is a safe upper description for a dynamically compressed version, but it is not the tightest description of this exact fixed-domain code.

The tree allocates $C+1$ integers, so its space is $O(C)$. Under the fixed constraints that is constant with respect to $n$, though it is a large constant allocation. If $C$ scales with the numeric domain, it should be stated explicitly rather than called coordinate-compressed $O(n)$ storage. The scalar accumulator and loop variables use $O(1)$ additional space.

The answer can be as large as $\binom{n}{2}$, about five billion for $n=10^5$. Python integers handle it. Fixed-width implementations need a 64-bit answer type.

## Alternatives and edge cases

- **True coordinate compression:** Collect every update value and relevant query boundary, sort unique coordinates, and use ranks in a Fenwick tree of size $O(n)$. This supports arbitrary integer magnitudes and matches the local summary, at the cost of preprocessing and an extra value array.
- **Merge-sort counting:** Recursively sort transformed values and count cross-half pairs satisfying $v_i \le v_j+\texttt{diff}$. This also achieves $O(n\log n)$ time and $O(n)$ space without relying on bounded values.
- **Balanced search tree with order statistics:** Insert prior values and ask how many are at most the threshold. Python has no built-in order-statistic tree, and a plain sorted list would make insertion linear.
- **Quadratic pair enumeration:** Testing every $(i,j)$ mirrors the definition but takes $O(n^2)$ time, which is too slow for $10^5$ elements.
- **Negative transformed values:** The 40000 offset makes every update index positive; omitting it would make the one-indexed Fenwick operations invalid.
- **Negative `diff`:** The query threshold may be below the current transformed value. The same inclusive prefix query handles it without a special case.
- **Equality at the boundary:** A prior value exactly equal to `v + diff` must count. Fenwick `query` is inclusive, so it does.
- **Duplicate transformed values:** Frequencies, rather than boolean presence, are stored. Every earlier index with the same value contributes separately.
- **Self-pairs:** Querying before updating ensures the current index is absent and cannot pair with itself.
- **Fixed-domain dependency:** The literal size and offset are safe only because the supplied value bounds imply update indices 20000 through 60000 and query indices 10000 through 70000.
- **Large answer:** The pair count may exceed 32-bit signed range even though inputs are small, so the accumulator's numeric capacity matters in other languages.
