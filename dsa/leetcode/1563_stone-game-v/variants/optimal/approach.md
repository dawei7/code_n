## General
**Write the interval recurrence**

Let $F(i,j)$ be the best future score when stones $i$ through $j$ remain, and let $S(i,j)$ be their sum from a prefix-sum array. Splitting after $k$ creates sums $S(i,k)$ and $S(k+1,j)$. If the left sum is smaller, the transition is $S(i,k)+F(i,k)$; if the right sum is smaller, it is $S(k+1,j)+F(k+1,j)$. When they are equal, Alice chooses the larger of those two continuations. A one-stone interval has score zero.

Trying every $k$ for every interval is cubic. The optimization groups all splits that retain the left side and all splits that retain the right side.

**Precompute the best legal continuation on each side**

Define $L(i,k)$ as the maximum of $F(i,x)+S(i,x)$ over $i \le x \le k$. Define $R(k,j)$ symmetrically as the maximum of $F(x,j)+S(x,j)$ over $k \le x \le j$. These tables answer the best left-retaining or right-retaining transition over a whole range in constant time.

For fixed $(i,j)$, positive stone values make $S(i,k)$ strictly increase with $k$. Therefore all splits satisfying $2S(i,k) \le S(i,j)$ form a prefix, while all satisfying $2S(i,k) \ge S(i,j)$ form a suffix. Find the first crossing where the left sum is at least half the total. The appropriate entry of $L$ covers every legal left-retaining split, and the corresponding entry of $R$ covers every legal right-retaining split. At exact equality, both sides are included, matching Alice's choice.

**Move the crossing monotonically**

Process left endpoints from right to left and right endpoints from left to right. For a fixed `left`, extending `right` only increases the interval total, so the first half-sum crossing never moves left. A single pointer advances at most $N$ times across all intervals sharing that left endpoint. After computing $F(i,j)$, update $L(i,j)$ from $L(i,j-1)$ and update $R(i,j)$ from $R(i+1,j)$, making the value available to larger intervals.

This order guarantees that every shorter subinterval and every needed range maximum has already been computed. The resulting transition examines no individual split repeatedly and is equivalent to the full recurrence.

## Complexity detail
There are $O(N^2)$ intervals. Each interval performs constant work, while each crossing pointer advances only $O(N)$ times for its fixed left endpoint. Total time is $O(N^2)$.

The score, left-maximum, and right-maximum tables each contain $N^2$ entries, and the prefix sums contain $N+1$, so space is $O(N^2)$.

## Alternatives and edge cases
- **Direct interval DP:** enumerate every split for every interval. It follows the recurrence directly but takes $O(N^3)$ time.
- **Binary-search crossing:** locate the half-sum boundary separately for every interval and use the same range maxima. This is simpler to derive but costs $O(N^2\log N)$ time.
- **Top-down memoization:** cache interval results while trying splits. It removes repeated states but still performs cubic split work in the worst case.
- **One stone:** no legal split exists, so the score is zero.
- **Equal split sums:** both remaining sides are legal, and the transition must choose the continuation with the larger future score.
- **No crossing before the last stone:** every legal split keeps the left side, so the left range maximum covers all split points.
- **Large values:** prefix sums may exceed a 32-bit integer even though each stone is bounded, so implementations in fixed-width languages should use a wide integer type.
- **Repeated values:** positivity, rather than distinctness, supplies the monotone sum property.
