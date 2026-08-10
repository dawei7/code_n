## General

**Choose the cooking order before choosing the subset**

For any fixed set of dishes, lower satisfaction should be cooked earlier and higher satisfaction later. Consider two consecutive dishes with satisfactions $a>b$ at times $t$ and $t+1$. Their contribution is $ta+(t+1)b$. Swapping them gives $tb+(t+1)a$, larger by $a-b>0$. Therefore every inversion can be improved, and an optimal order is nondecreasing satisfaction.

The remaining question is which low-satisfaction dishes should be included. After sorting, an optimal chosen set is a suffix of the ascending order: if a lower value is included while a higher excluded value exists, replacing the lower one cannot reduce any coefficient. The exact code sorts in the equivalent reverse direction and grows this chosen suffix from its largest end.

**Why scan from largest to smallest**

`satisfaction.sort(reverse=True)` places the largest values first. The loop considers adding progressively smaller dishes. Although this scan order is descending, the final cooking order of the selected dishes is ascending: each newly considered smaller value would be prepended before all previously selected larger dishes.

Two accumulators describe the current chosen set:

- `s` is the sum of selected satisfaction values.
- `ans` is their optimal like-time coefficient in ascending cooking order.

**Derive the marginal gain `s`**

Suppose some larger dishes are already selected and optimally ordered. Add new value `x`, which is no larger than any of them. It belongs at time one, while every existing dish shifts one time unit later.

The new dish contributes `x * 1`. Shifting every old dish later adds one extra copy of each old satisfaction. Therefore the total increase is

$$
x+\text{sum of old satisfactions}
=
\text{sum of the enlarged selected set}.
$$

The code first performs `s += x`, so `s` becomes exactly this marginal gain. If positive, `ans += s` updates the objective to the value for the enlarged set.

For selected values 5 alone, `s=5` and `ans=5`. Adding zero in front makes `s=5` again and raises `ans` to 10, corresponding to $0\cdot1+5\cdot2$. Adding $-1$ makes `s=4` and raises `ans` to 14, corresponding to $-1\cdot1+0\cdot2+5\cdot3$.

**Why stop when `s <= 0`**

If the enlarged set sum is zero or negative, prepending the current dish does not improve the objective. Every future candidate is no larger than the current `x` because of descending sorting. Adding another such value makes the cumulative sum no greater, so all later marginal gains will also be nonpositive.

There is therefore no reason to continue. The best objective has already been recorded before this non-improving addition.

The code does update `s` with the rejected `x` before checking, but it breaks before adding that nonpositive value to `ans`. Since the loop ends immediately, retaining the changed `s` has no side effect.

If `s == 0`, including the dish would tie rather than improve the maximum. The problem asks only for the maximum value, so excluding it is fine.

**All-negative and mixed cases**

When all values are negative, the first cumulative sum is nonpositive and the method returns initial `ans=0`, corresponding to cooking no dishes.

Positive dishes are always accepted initially. Zero or modestly negative dishes may also be accepted when their own negative contribution is outweighed by shifting the already selected positive dishes to later, more valuable times.

This is why simply discarding every nonpositive satisfaction value is wrong: the sample's $-1$ increases the total from 10 to 14 when placed before zero and five.

**Why the greedy method is correct**

The exchange argument proves any chosen set is optimally ordered ascending. The replacement argument proves some optimum is a suffix of the globally ascending values, which the descending scan enumerates by repeatedly prepending the next smaller value.

For each such suffix extension, its objective differs from the previous suffix by exactly the new cumulative sum `s`. These marginal gains are nonincreasing once values become smaller. The algorithm accepts every positive marginal gain and stops at the first nonpositive one; no later suffix can improve the objective. Thus `ans` is the maximum over all valid chosen suffixes and therefore over all dish subsets and orders.

## Complexity detail

Let $n$ be the number of dishes. Sorting takes $O(n\log n)$ time, and the scan is $O(n)$, so total time is $O(n\log n)$.

The sort mutates the input list. Python's Timsort can use $O(n)$ temporary storage in the worst case, while the greedy scan uses only two scalar accumulators. Thus the manifest's $O(n)$ space bound accurately includes sorting workspace. If language-specific in-place sorting uses less auxiliary memory, the scan itself remains $O(1)$.

## Alternatives and edge cases

- **Quadratic dynamic programming:** Track dish index and number already cooked after sorting. It is correct but uses many states that the greedy marginal-gain observation eliminates.
- **Enumerate every sorted suffix:** Recompute each suffix coefficient directly. It is conceptually close but can cost $O(n^2)$.
- **Discard all negative values:** This is incorrect because a small negative dish can increase the coefficients of larger later dishes enough to improve the total.
- **All negative values:** The first cumulative sum is nonpositive and returning zero correctly means cook nothing.
- **All positive values:** Every cumulative sum stays positive, so all dishes are selected.
- **Zero satisfaction:** It may be useful because placing it first shifts positive dishes later at no direct penalty.
- **Cumulative sum equals zero:** Adding the current dish only ties the objective, so stopping preserves a maximum.
- **Repeated values:** Sorting and cumulative sums handle them without any special case.
- **Input mutation:** `sort(reverse=True)` changes `satisfaction`; use `sorted` when callers need the original order.
- **Cooking order:** The scan is descending, but selected dishes are conceptually cooked in ascending order because each new value is prepended.
- **Positive marginal gain:** `ans += s` is derived from shifting every previously selected dish one position later.
