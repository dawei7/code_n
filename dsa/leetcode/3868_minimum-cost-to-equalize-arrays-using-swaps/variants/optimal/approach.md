## General

**Discard positions, but preserve multiplicities**

Because swaps within either array are free, every permutation of `nums1` and every permutation of `nums2` is available at no cost. Positions therefore impose no restriction: the problem is entirely about how many copies of each value belong to each array. Build frequency maps $c_1(v)$ and $c_2(v)$ over every value $v$ appearing in either input.

**Recognize exactly when equalization is possible**

The two final arrays must each contain half of all copies of every value. Thus $c_1(v)+c_2(v)$ must be even for every $v$; if any combined frequency is odd, no distribution can give both arrays the same count and the answer is `-1`.

Suppose every combined count is even. Define the signed imbalance

$$
d(v)=c_1(v)-c_2(v).
$$

Every $d(v)$ is then even. A positive value identifies copies that must move from `nums1` to `nums2`, while a negative value identifies copies that must move in the opposite direction. Since both arrays have length $N$, the positive and negative imbalances have equal total magnitude.

**Count what one paid swap repairs**

Free rearrangement lets one selected surplus value in `nums1` and one selected surplus value in `nums2` be placed at the same index. Swapping across that index transfers both values to the side where each is needed. Their two absolute imbalances each decrease by `2`, so one paid swap decreases $\sum_v \lvert d(v)\rvert$ by exactly `4`.

No paid operation can decrease that sum by more than `4`, which makes $\frac14\sum_v\lvert d(v)\rvert$ a lower bound. Pairing arbitrary surplus copies from opposite arrays achieves this decrease on every paid swap until all imbalances vanish, so the bound is attainable. The minimum cost is therefore

$$
\frac{1}{4}\sum_v \lvert c_1(v)-c_2(v)\rvert.
$$

## Complexity detail

Let $U$ be the number of distinct values across both arrays. Counting both length-$N$ arrays costs $O(N)$ time. Visiting the union of their keys costs $O(U)$, and $U\le 2N$, so the total time is $O(N)$. The two frequency maps and their key union require $O(U)$ auxiliary space.

The benchmark defines size as $N$, the length of each input array. Every tier uses disjoint groups of values that occur twice within exactly one array. This makes all combined frequencies even, forces a nonzero answer, and exposes implementations that repeatedly scan both arrays to obtain each distinct value's frequency. The accepted two-map solution and an independently structured signed-balance map should retain linear scaling, while an explicit per-value nested scan performs $O(N^2)$ work and should fail only the scaling verdict.

## Alternatives and edge cases

- **One signed balance map:** Add `1` for each occurrence in `nums1` and subtract `1` for each occurrence in `nums2`; the parity and absolute-sum calculation is equivalent and uses one map instead of two.
- **Sort both arrays:** Sorting can expose corresponding excess groups and leads to a correct $O(N\log N)$ method, but frequency counting reaches the required linear bound directly.
- **Repeated full-array counts:** Calling a linear count for every distinct value is functionally correct, but with $U=\Theta(N)$ it takes $O(NU)=O(N^2)$ time.
- **Odd combined frequency:** One value with an odd total count makes equality impossible, even if all other values are already balanced.
- **Already equal multisets:** The arrays may have different orders yet require cost `0`, because free in-array swaps can align them.
- **Large imbalances:** Many copies of one value may need to cross in one direction, but every paid swap simultaneously carries a needed value back, so the absolute-difference sum still divides by `4`.
- **Input boundaries:** The reasoning is unchanged at the minimum length and for values at $8\cdot10^4$; hash-map keys store values rather than allocating by the numeric bound.
