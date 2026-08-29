## General

**The operation rule is deterministic.** At each step, the problem does not let us choose an arbitrary pair. It mandates the adjacent pair with minimum sum and resolves ties by choosing the leftmost one.

Therefore, “minimum number of operations” means simulate this forced process and stop at the earliest moment the current array becomes non-decreasing. There is no branching search over alternative merges.

The source copies the input with `arr = nums[:]` so that destructive merges do not alter the caller's `nums` list.

**Check the stopping condition before every merge.** Helper `is_non_decreasing` scans adjacent positions from left to right. If it finds `a[i] < a[i-1]`, the array violates non-decreasing order and returns false. If no inversion exists, it returns true.

The outer loop runs only while this check is false. Thus an already sorted input returns zero without performing the mandated operation unnecessarily.

**Find the leftmost minimum-sum adjacent pair.** The source initializes candidate index `k = 0` and sum `s = arr[0] + arr[1]`.

It then scans candidate starting indices one through `len(arr)-2`. For each sum `t`, it updates only when

`s > t`.

The strict comparison is crucial. A smaller sum replaces the candidate, but an equal sum leaves the earlier index unchanged. Since scanning proceeds left to right, `k` remains the leftmost pair among all pairs attaining the minimum.

Using `>=` instead would incorrectly move to a later equal-sum pair and violate the specified tie rule.

**Merge in place.** Once the target pair is known, `arr[k] = s` replaces its first value with the pair sum. `arr.pop(k + 1)` removes the second value, shifting later elements left. The result is exactly the array produced by replacing that adjacent pair with one element.

`ans` increases once per merge. Since every operation shortens the list by one, the loop must terminate after at most $n-1$ operations, when one element remains. A one-element array is automatically non-decreasing.

For `[5,2,3,1]`, adjacent sums are seven, five, and four, so pair `(3,1)` is forced and produces `[5,2,4]`. New sums are seven and six, so `(2,4)` is forced, producing `[5,6]`. The next stopping check succeeds and answer is two.

**Why stopping then gives the minimum operation count.** Let the deterministic sequence of arrays be $A_0,A_1,\ldots$, where each $A_{p+1}$ results from the mandated minimum-sum merge on $A_p$. Any legal execution must produce exactly this same sequence because both pair choice and tie resolution are fixed.

If $A_0$ is already non-decreasing, zero is clearly minimum. Otherwise, no legal execution can stop before the first index $p$ for which $A_p$ is non-decreasing, because its array after fewer operations is the same unsorted $A_q$. The source checks in order and returns exactly that first $p$.

**Why negative values cause no special case.** Pair sums may be negative and can become more negative after merges. Ordinary integer comparison still identifies the minimum. Non-decreasing order likewise uses the usual signed comparison. The algorithm does not assume sums increase over time.

**Input-copy behavior versus space.** The local editorial's first implementation mutates `nums` directly and can claim constant extra list storage. The protected source intentionally preserves the input by copying it, so its actual auxiliary space includes an $O(n)$ list. This agrees with the manifest.

## Complexity detail

At current length $L$, the non-decreasing check costs $O(L)$, scanning pair sums costs $O(L)$, and `pop` from the middle may shift $O(L)$ elements. One iteration is $O(L)$.

Lengths decrease from $n$ toward one, so total worst-case work is

$$
O(n+(n-1)+\cdots+1)=O(n^2).
$$

The copied list uses $O(n)$ auxiliary space. Scalars and helper call state are constant. These bounds match the manifest.

With $n\le50$, direct deterministic simulation is appropriate.

## Alternatives and edge cases

- **Choose a pair that repairs an inversion:** The operation does not permit strategic choice; only the minimum-sum pair may be merged.
- **Use `>=` in the minimum scan:** This selects the rightmost tied pair rather than the required leftmost pair.
- **Priority queue of pair sums:** It can accelerate selection for larger variants, but merges invalidate neighboring pairs and require linked-list/version bookkeeping.
- **Mutate the input list:** It saves the copy but changes caller-visible data; the protected source preserves `nums`.
- **Already non-decreasing:** The while condition fails immediately and returns zero.
- **One element:** It is non-decreasing by definition, so no access to `arr[1]` occurs.
- **Two unsorted elements:** Their only pair is merged, leaving one element and answer one.
- **Equal adjacent values:** They satisfy non-decreasing order and do not form an inversion.
- **Equal minimum sums:** Strict update preserves the first occurrence.
- **Negative pair sums:** They are compared normally and may be selected even when other sums are positive.
- **Merged value creates new inversions:** The next full stopping and pair scans recompute from the updated array.
- **Maximum operations:** Every merge reduces length, so at most $n-1$ operations occur.
