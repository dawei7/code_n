## General

**Represent a partition as a signed sum**

Call the two destination arrays $A$ and $B$. Assign a positive sign to every element placed in $A$ and a negative sign to every element placed in $B$. Then

$$
\sum A-\sum B
$$

is exactly the sum of those signed contributions, and the requested objective is its absolute value.

The extra restriction is cardinality: because the input has $2n$ elements, exactly $n$ signs must be positive and $n$ must be negative.

**Split the input for meet in the middle**

Enumerating all assignments directly would inspect $2^{2n}$ possibilities. The source splits `nums` into two halves of length `n` and enumerates only the `2^n` masks for each half.

For one mask, a set bit means the corresponding element is assigned to $A$ and contributes positively. An unset bit means it is assigned to $B$ and contributes negatively.

For the first half, the loop computes signed difference `s` and number of selected positive elements `cnt`, then stores `s` in `f[cnt]`. It performs the analogous calculation for the second half and stores `s1` in `g[cnt1]`.

The same numeric mask is used to generate one entry for each half during an iteration, but the stored collections are independent. Because the loop visits every possible mask, both `f` and `g` receive every subset pattern for their respective half. A later combination may pair values produced by completely different masks.

**Why grouping by selected count is necessary**

Suppose a first-half assignment selects `i` elements for $A$. To make $A$ contain exactly `n` elements overall, the second-half assignment must select exactly `n-i` elements.

That is why the combination phase pairs `f[i]` with `g[n-i]`. Every combined pair has $i+(n-i)=n$ positive signs and therefore produces two destination arrays of the required equal length.

Without this grouping, a very small signed difference might correspond to partitions with unequal numbers of elements and would be invalid.

**Why adding the two half differences works**

For a chosen first-half signed difference `a` and compatible second-half difference `b`, their sum is

$$
a+b=
\left(\sum A_{\text{left}}-\sum B_{\text{left}}\right)
+\left(\sum A_{\text{right}}-\sum B_{\text{right}}\right)
=\sum A-\sum B.
$$

The objective for that full partition is therefore `abs(a + b)`. The algorithm must find, over every compatible count group, the pair whose sum is closest to zero.

**Use binary search for the closest complement**

For a fixed `a`, the ideal second-half value would be `b=-a`. The source sorts the compatible values `g[n-i]` and binary-searches for the first entry greater than or equal to `-a`.

The closest sorted value to a target must be either that lower-bound entry or its immediate predecessor. The code evaluates `gi[left]` and, when `left > 0`, `gi[left - 1]`. Any entry farther left is no greater than the predecessor and therefore no closer to the target; any entry farther right is no smaller than the lower bound and likewise cannot be closer.

Each candidate updates `ans` with `abs(a + b)`.

**Why the lower-bound code is safe**

Every count from zero through `n` has at least one subset mask, so each compatible `gi` is nonempty. The binary search initializes `left=0` and `right=len(gi)-1` and converges to a valid index.

If every value is below `-a`, it ends at the final index, the closest value from below. If every value is at least `-a`, it ends at index zero. Exact equality immediately gives a possible difference of zero, the globally smallest result.

**Why sets do not lose necessary information**

`f` and `g` store signed differences in sets. Two different masks with the same selected count and same signed difference are interchangeable for the objective: when paired with any compatible other-half difference, they produce the same total difference.

The problem asks only for the minimum value, not the actual partition or the number of ways to achieve it. Deduplicating equal half differences therefore cannot remove a uniquely better result.

**Trace the four-element example**

For `nums = [3,9,7,3]`, each half has length two. In the first half, selecting both elements gives signed difference twelve, selecting neither gives negative twelve, and selecting one gives either negative six or positive six.

In the second half, choosing one element for $A$ produces differences four or negative four. To construct an $A$ of size two using one element from each half, pair the first-half difference six with second-half difference negative four. Their sum is two, corresponding for example to $A=[9,3]$ and $B=[3,7]$. The absolute difference is two.

Other count splits, including taking both $A$ elements from one half, are also examined. The minimum across all groups is returned.

**Why every valid partition is considered**

Take any legal partition. Its choices in the first half define one enumerated mask with some count `i` and signed difference in `f[i]`. Its choices in the second half define another enumerated mask with count `n-i` and difference in `g[n-i]`.

During group `i`, the algorithm considers the first difference and binary-searches for the closest possible second difference. Even if it does not select this partition's exact second value, it selects one at least as close to `-a`, so it cannot produce a worse minimum for that first choice.

Conversely, every pair the algorithm combines has complementary counts and comes from real half assignments, so it represents a legal full partition. The minimum is thus taken over exactly valid possibilities and is globally optimal.

**Negative input values require no special case**

A negative number assigned to $A$ contributes its negative value; assigned to $B$, subtracting it contributes positively. This is exactly what the signed-difference formula requires. Sorting and binary search work with negative, zero, and positive half differences uniformly.

## Complexity detail

Here $n$ is half the input length. The mask-generation loop has $2^n$ masks and examines $n$ bit positions for each, taking $O(n2^n)$ time.

Across all count groups, each side stores at most $2^n$ distinct signed differences. Sorting all groups costs at most $O(n2^n)$ in total because the logarithm of any group size is at most $n$. Binary-searching once for each first-half difference adds another $O(n2^n)$ worst-case time. Overall time is $O(n2^n)$.

The stored sets and temporary sorted lists contain $O(2^n)$ total values per side, so space is $O(2^n)$. Deduplication can reduce actual usage but does not worsen this bound.

## Alternatives and edge cases

- **Enumerate all full assignments:** Costs $O(2^{2n})$ and misses the meet-in-the-middle advantage.
- **Subset sums using the total sum:** Minimize `abs(total - 2 * selected_sum)` with exactly `n` selected elements; it is algebraically equivalent.
- **Dynamic programming by numerical sum:** Input magnitudes make a sum-indexed table impractically large.
- **Brute-force combinations:** Enumerating all $\binom{2n}{n}$ equal-size selections remains much larger than the half enumeration.
- **Difference zero:** It is globally optimal and corresponds to equal partition sums.
- **One element per destination:** Both possible assignments are represented when `n=1`.
- **All values negative:** Signed sums and absolute value remain valid.
- **Duplicate values or differences:** Sets safely merge equivalent objective states.
- **Choose zero elements from one half:** Group `f[0]` pairs with `g[n]`.
- **Choose all elements from one half:** Group `f[n]` pairs with `g[0]`.
- **Even group size is irrelevant:** Binary search operates on distinct sorted differences, not original subset multiplicities.
- **Exact complement absent:** Checking the lower bound and predecessor finds the nearest available value.
- **Input preservation:** Masks read `nums` without modifying it.
