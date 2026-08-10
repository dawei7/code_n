## General

**Only equal values interact**

For index $i$, the answer sums distances only to indices $j$ satisfying `nums[j] == nums[i]`. Indices holding different values never contribute to one another.

The dictionary `d` groups indices by value. Scanning `nums` from left to right appends each index to its value's list, so every group is automatically sorted:

$$
a_0<a_1<\cdots<a_{m-1}.
$$

The groups are independent. Once the solution can compute all distance sums for one sorted list, it can repeat that work for every value and write results into the corresponding original positions.

**Split every absolute distance by side**

At group position $i$, all earlier indices are smaller than $a_i$, while all later indices are larger. Therefore,

$$
\sum_{j=0}^{m-1}|a_i-a_j|
=
\sum_{j<i}(a_i-a_j)
+
\sum_{j>i}(a_j-a_i).
$$

Call the first quantity `left` and the second `right`. The distance to $a_i$ itself is zero and need not be handled separately.

A direct computation for each $i$ would repeat most of the same subtractions and take $O(m^2)$ for one large group. The exact solution instead maintains how `left` and `right` change when moving from one group index to the next.

**Initialize at the first occurrence**

At $a_0$, there are no earlier positions, so `left = 0`.

Every other occurrence lies to the right. Its total distance from $a_0$ is

$$
\sum_{j=0}^{m-1}(a_j-a_0)
=
\sum_{j=0}^{m-1}a_j-ma_0.
$$

The code computes this as

`right = sum(idx) - len(idx) * idx[0]`.

Including $j=0$ is harmless because its term is zero. Thus `left + right` is already the complete answer for the first index.

**Move the reference point to the next occurrence**

Suppose the scan moves from $a_i$ to $a_{i+1}$. Let

$$
\delta=a_{i+1}-a_i.
$$

There are $i+1$ group positions at or to the left of $a_i$: $a_0$ through $a_i$. When the reference moves right by $\delta$, its distance to each of those positions increases by $\delta$. Therefore,

$$
left\mathrel{+}=\delta(i+1).
$$

There are $m-i-1$ positions from $a_{i+1}$ through $a_{m-1}$ that were represented in the previous `right` quantity. Moving the reference right by $\delta$ reduces its distance to each by $\delta$. Hence,

$$
right\mathrel{-}=\delta(m-i-1).
$$

These are exactly the two update statements in the source. After them, `left` and `right` describe distances from the next occurrence $a_{i+1}$, ready for the following loop iteration.

**Why the update counts include these endpoints**

The multiplier $i+1$ includes $a_i$. Its distance was zero at the old reference and becomes $\delta$ at the new one, so it belongs in the increased left contribution.

The multiplier $m-i-1$ includes $a_{i+1}$. Its old distance was $\delta$ and its new distance is zero, so it belongs in the decreased right contribution.

This endpoint accounting is a common source of off-by-one errors. Writing the actual sets on both sides makes the multipliers inevitable rather than memorized.

**Establish correctness group by group**

At the start of loop iteration $i$, maintain:

- `left` equals the sum of distances from $a_i$ to group positions before it;
- `right` equals the sum of distances from $a_i$ to group positions after it.

The initialization proves the statement for $i=0$. Adding the two quantities gives the definition of the required answer, so the assignment `ans[idx[i]] = left + right` is correct.

The gap update just derived transforms both sums exactly to those for $a_{i+1}$, establishing the invariant for the next iteration. By induction, every original index in the group receives its correct distance sum.

Every array index belongs to exactly one value group, so processing all dictionary lists fills the entire answer correctly.

**Trace the repeated-one group**

For `nums = [1,3,1,1,2]`, value one occurs at `idx = [0,2,3]`.

At index zero:

$$
left=0,\qquad right=(0+2+3)-3\cdot0=5.
$$

So `ans[0] = 5`.

Move by gap two to group position one. There is one old-left-or-current position, so `left` increases by $2\cdot1=2$. Two positions were on the right, so `right` decreases by $2\cdot2=4$, becoming one. The answer at original index two is $2+1=3$.

Move by gap one to original index three. `left` increases by $1\cdot2=2$, becoming four, and `right` decreases by $1\cdot1=1$, becoming zero. Thus `ans[3] = 4`.

Values three and two each form singleton groups. For a singleton, initialization gives both contributions zero, so their answers remain zero.

**Why large values do not matter**

The algorithm groups by the numerical values but never subtracts those values. It subtracts only indices, whose range is zero through $n-1$. A value as large as $10^9$ is merely a dictionary key and has no effect on arithmetic complexity.

The largest result can be quadratic in $n$, so a fixed-width language needs a sufficiently wide integer type. Python integers grow automatically and avoid overflow.

## Complexity detail

Let $n=|\texttt{nums}|$. Group construction visits every index once, taking expected $O(n)$ time with hash-map operations.

For a group of size $m$, `sum(idx)` and its loop each take $O(m)$. The group sizes sum to $n$, so all groups together take $O(n)$ time. Total expected running time is $O(n)$.

The grouped index lists collectively store exactly $n$ indices, and the answer stores $n$ integers. Dictionary overhead is at most one entry per distinct value. Total space is $O(n)$. Excluding the required result, auxiliary storage is still $O(n)$ because of the groups.

## Alternatives and edge cases

- **Prefix sums per group:** Store cumulative index sums and calculate left and right formulas independently for each occurrence. This is also $O(n)$ but uses an additional prefix structure or variables.
- **Two global passes:** Maintain count and index-sum maps left-to-right, then right-to-left, adding each side's contribution directly to the answer.
- **Pairwise comparison:** Comparing every equal-value pair and adding its distance to both endpoints can take $O(n^2)$ when all values match.
- **Singleton group:** Both side contributions are zero, so the answer is zero.
- **All values distinct:** Every group is a singleton and the entire output is zeroes.
- **All values equal:** One group contains all indices; the recurrence still processes it in linear time.
- **Adjacent equal occurrences:** A gap of one is handled by the same weighted update.
- **Widely separated occurrences:** The actual gap scales both contribution changes correctly.
- **Large input values:** They are dictionary keys only; distances depend on indices, not value magnitude.
- **Input preservation:** Grouping reads `nums` without sorting or modifying it.
