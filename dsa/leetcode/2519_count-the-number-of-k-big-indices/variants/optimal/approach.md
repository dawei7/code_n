## General

**Each index needs two strict-smaller counts**

Index `i` is `k`-big only when:

- at least `k` earlier indices contain values strictly smaller than `nums[i]`;
- at least `k` later indices contain values strictly smaller than `nums[i]`.

The scan needs dynamic frequency summaries for values on the left and right. A Binary Indexed Tree, also called a Fenwick tree, supports:

- adding or removing one occurrence of a value;
- querying how many stored values are at most a threshold.

Because every value lies from 1 through `n`, values can be used directly as one-based Fenwick indices without coordinate compression.

**Fenwick tree representation**

`self.c[x]` stores the total frequency over a specific suffix of the prefix ending at `x`. Its range length is the lowest set bit `x&-x`.

`update(x,delta)` adds `delta` to every Fenwick block containing position `x`. Moving with

`x += x&-x`

reaches progressively larger covering blocks.

`query(x)` returns the sum of frequencies at positions 1 through `x`. It adds the block ending at `x`, then removes that block's lowest set bit with

`x -= x&-x`

until reaching zero.

Both methods touch only $O(\log n)$ tree entries.

**Initialize all values on the right**

`tree1` will represent values strictly left of the current index. It begins empty.

`tree2` will represent values strictly right of the current index. The code first inserts every array value into `tree2`. At this moment it technically contains the whole array, but each current occurrence is removed before queries are made.

Two separate trees let both side counts be obtained during one left-to-right pass.

**Maintain exact side membership**

For current value `v`, the scan performs operations in this order:

1. `tree2.update(v,-1)` removes the current occurrence, so `tree2` now contains only later indices.
2. Query both trees for values through `v-1`.
3. `tree1.update(v,1)` inserts the current occurrence for future indices.

Before step two, `tree1` contains exactly earlier elements and `tree2` contains exactly later elements. This invariant holds at every iteration.

Removing before querying prevents the current index from being mistaken for a right-side index. Inserting afterward prevents it from being mistaken for a left-side index.

**Use `v-1` for strict inequality**

`query(v-1)` counts values at most `v-1`, which for integer values is exactly the count strictly smaller than `v`.

Querying `v` would incorrectly include equal values. Equal-valued elements do not satisfy the problem's strict `<` condition.

When `v=1`, the query argument is zero. The Fenwick loop performs no iterations and returns zero, correctly reflecting that no allowed value is smaller than one.

**Turn two threshold comparisons into one count**

The expression

`tree1.query(v-1)>=k and tree2.query(v-1)>=k`

is true exactly when both requirements hold. In Python, Boolean `True` adds as one and `False` as zero, so `ans+=...` increments only for a `k`-big index.

Short-circuiting means the right query may be skipped if the left side already has fewer than `k` values. This can save work in practice without affecting the worst-case bound.

**Trace the side invariant**

At the first index, `tree1` is empty, so no positive `k` can pass the left condition. After processing it, its value enters `tree1`.

At the final index, removing its value leaves `tree2` empty, so the right condition fails. This matches the fact that endpoints cannot be `k`-big for positive `k`.

Middle indices are evaluated against exactly their true prefix and suffix multisets, including repeated values with their full occurrence counts.

**Why frequencies rather than distinct values matter**

The definition asks for different indices, not different values. If three earlier indices all contain 2 and current value is 5, all three count.

Fenwick updates add one per occurrence, so prefix sums count indices and preserve duplicates correctly.


At each query moment, the two trees exactly represent the current index's left and right sides. Their `v-1` prefix sums are exactly the required strict-smaller index counts. The algorithm increments precisely when both reach `k`, so the final total is the number of `k`-big indices.

## Complexity detail

Building `tree2` performs $n$ updates at $O(\log n)$ each. The main scan performs one removal, up to two queries, and one insertion per element, each $O(\log n)$. Total time is $O(n\log n)$.

Each Fenwick tree has `n+1` integers, so two trees use $O(n)$ auxiliary space. All other state is constant.

The answer is at most `n`.

## Alternatives and edge cases

- **Two sorted multisets:** Balanced search trees can maintain sides but are more complex and may not provide direct rank counts.
- **Coordinate compression:** Required for arbitrary large values, but unnecessary because values already lie in `[1,n]`.
- **Equal values:** They are excluded by querying `v-1`.
- **Duplicate smaller values:** Each different index contributes separately.
- **`v=1`:** No smaller positive value exists, so both queries return zero.
- **Large `k`:** If either side has fewer than `k` total indices, the condition naturally fails.
- **First and last indices:** One required side is empty.
- **Removal order:** Remove current from the right tree before querying.
- **Insertion order:** Add current to the left tree only after querying.
- **Boolean addition:** A true conjunction contributes exactly one to `ans`.
