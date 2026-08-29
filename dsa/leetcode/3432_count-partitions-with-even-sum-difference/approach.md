## General

**Track the two sums at each legal split.** A partition after index $i$ is legal only for $0\le i<n-1$, because both sides must be non-empty. The source starts with

`l = 0`

and

`r = sum(nums)`.

Before the first partition is evaluated, all values belong to the right sum. For each `x` in `nums[:-1]`, moving that value across the boundary is represented by `l += x` and `r -= x`. At that moment, `l` is the sum through the current index and `r` is the sum of all later elements.

The expression

`(l - r) % 2 == 0`

tests whether the difference is even. In Python, a Boolean is an integer subclass: `True` adds one and `False` adds zero. Thus `ans += ...` increments the count exactly for valid partitions.

The loop intentionally excludes the final array element. Moving it to the left would leave an empty right subarray, which is not a partition under the definition.

**The parity is actually the same for every partition.** Let $T$ be the total array sum, $L$ a partition's left sum, and $R$ its right sum. Since $T=L+R$,

$$
L-R=(L+R)-2R=T-2R.
$$

The term $2R$ is always even. Therefore,

$$
(L-R)\bmod2=T\bmod2.
$$

Every partition difference has exactly the same parity as the total sum. If $T$ is even, all $n-1$ legal partitions qualify. If $T$ is odd, none qualify.

The protected source still updates and checks the two running sums explicitly rather than returning `n - 1` or zero from total parity. Its result is the same because each loop test evaluates that invariant.

For `[10,10,3,7,6]`, the total is $36$, which is even. The four running differences are $-16$, $4$, $10$, and $24$, all even, so the answer is four.

For `[1,2,2]`, the total is $5$, which is odd. The two differences are $-3$ and $1$, both odd, so no partition is counted.

For `[2,4,6,8]`, total $20$ is even and all three possible boundaries qualify.

**Why negative differences are handled correctly.** A left sum can be smaller than a right sum, producing a negative difference such as $-16$. Python's modulo still returns zero exactly for an even integer, regardless of sign. No absolute value is needed because negating an integer does not change whether it is even.

**Why the running invariant is correct.** Initially, `l + r` equals the total. Each iteration adds the same `x` to `l` that it subtracts from `r`, preserving their total while moving the boundary one element right. After processing the element at index $i$, the two variables exactly equal the sums of the statement's two subarrays. The Boolean test therefore classifies that partition correctly. Since the loop visits every legal boundary once, `ans` is exact.

**There is a simpler mathematical implementation, but the explanation follows this source.** The local editorial directly checks `sum(nums) % 2` and returns either `len(nums) - 1` or zero. That removes the second loop. Both versions remain $O(n)$ because computing the total already scans the array. The protected source makes the per-boundary sums explicit, which can be pedagogically useful even though parity proves the checks are identical.

There is also an exact Python memory detail: `nums[:-1]` creates a new list containing the first $n-1$ references before iteration. The scalar algorithm could instead use an index loop or `islice` to remain constant-space, but this file uses a slice.

## Complexity detail

Let $n=\lvert\texttt{nums}\rvert$. `sum(nums)` takes $O(n)$ time. Creating `nums[:-1]` takes $O(n)$ time, and the loop scans its $n-1$ entries in $O(n)$ time. Total time is $O(n)$.

The running sums and answer are constant-size. However, the exact Python slice `nums[:-1]` allocates a list of $n-1$ references, so peak auxiliary space is $O(n)$ for this source. The manifest's $O(1)$ space describes an index-based loop or the direct total-parity formula, not the literal slicing implementation.

## Alternatives and edge cases

- **Total-parity formula:** Return `len(nums) - 1 if sum(nums) % 2 == 0 else 0`. This is equally linear in time and genuinely $O(1)$ auxiliary space.
- **Prefix-sum array:** It can calculate both side sums at every boundary, but storing all prefixes uses unnecessary $O(n)$ space beyond the slice already present here.
- **Recompute each side:** Summing left and right subarrays separately for every partition takes $O(n^2)$ time.
- **Two elements:** There is exactly one legal partition. It qualifies precisely when the total of the two elements is even.
- **Even total:** Left and right sums have the same parity, so their difference is even at every boundary.
- **Odd total:** One side sum is even and the other odd, so every difference is odd.
- **Negative difference:** Modulo two classifies its parity correctly; absolute value would not change the result.
- **Non-empty sides:** Iterating only through `nums[:-1]` prevents a split after the final element.
- **Boolean arithmetic:** In Python, adding the comparison result increments by one only for true, making the compact count valid.
- **Input preservation:** Slicing copies references but does not modify `nums`.
