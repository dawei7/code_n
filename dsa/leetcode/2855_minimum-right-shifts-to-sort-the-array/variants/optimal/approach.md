## General

**A sortable rotation has at most one descent.** Right shifts only rotate the circular order of distinct values. If a rotation can become strictly increasing, the original array must consist of an increasing suffix followed circularly by an increasing prefix, with one drop at their boundary.

The intended solution is therefore to find the first descent, verify that everything after it forms the smaller increasing block, and move that block to the front.

**Find the end of the initial increasing prefix.** The source starts `i = 1` and advances while `nums[i - 1] < nums[i]`.

If `i == n`, the entire array is already strictly increasing. Later `n - i` returns zero, which is correct.

Otherwise, `i` is the index immediately after the first descent. It is the only possible rotation boundary: any sorted rotation must begin with the smaller value at this drop.

**Validate most of the suffix.** The source sets `k = i + 1` and advances while

`nums[k - 1] < nums[k] < nums[0]`.

This chained comparison checks that each next suffix element is larger than its predecessor but still smaller than the first element of the original prefix. When the suffix has at least two elements, the first iteration also implies `nums[i] < nums[0]` because `nums[i] < nums[i+1] < nums[0]`.

If validation stops before the end, `k < n` and the method returns negative one. Otherwise, it returns `n - i`.

For a valid rotated array such as `[3,4,5,1,2]`, `i = 3` and the suffix length is two. Two right shifts move `[1,2]` before `[3,4,5]` and produce sorted order.

**Why `n - i` is the needed shift count when validation is valid.** One right shift moves the last element to the front. Repeating it for the suffix length moves the entire suffix to the front while preserving its internal order. Since both blocks are increasing and every suffix value is smaller than every prefix value, their concatenation is strictly increasing.

Distinct values make the sorted order unique, so no different nonzero rotation can also be sorted. The suffix length is therefore the minimum positive shift count.

**A correctness defect in the exact source.** When the suffix contains exactly one element, `k = i + 1 = n` and the validation loop never runs. The code never checks whether that sole suffix element is smaller than `nums[0]`.

For valid input `nums = [1, 3, 2]`:

- The first loop stops at `i = 2` because three is greater than two.
- `k = 3`, so the second loop is skipped.
- The source returns `n - i = 1`.

But one right shift produces `[2,1,3]`, which is not sorted, and no rotation sorts `[1,3,2]`. The correct answer is negative one.

Thus, the exact implementation does not satisfy the full stated contract. Its reasoning is correct for already sorted arrays, valid rotations, invalid arrays detected inside a suffix of length at least two, and two-element inputs, but it misses this legal edge family where the first descent occurs before a one-element suffix whose value exceeds the first element.

**How to repair the validation.** After finding a descent:

- Verify the suffix `nums[i:]` is strictly increasing.
- Verify its largest value `nums[-1]` is smaller than the prefix's smallest value `nums[0]`.

Because both blocks are increasing, comparing these boundary extrema proves every suffix value is below every prefix value. An explicit check also handles a one-element suffix.

The approach document must distinguish this repaired invariant from what the exact source actually checks; no solution file is changed here.

## Complexity detail

The first pointer moves from one to at most $n$. The second pointer also moves only forward through the remaining suffix. Total time is $O(n)$.

Only `n`, `i`, and `k` are stored, so auxiliary space is $O(1)$. The input list is not mutated.

The defect is semantic rather than asymptotic: failing to inspect one boundary value does not change the linear time or constant space.

At $n=1$, the first loop is skipped and the source returns zero, correctly recognizing the one-element array as sorted.

## Alternatives and edge cases

- **Corrected boundary scan:** Find the first descent, reject a second descent, require `nums[-1] < nums[0]` when a descent exists, and return the suffix length. This retains $O(n)$ time and $O(1)$ space.
- **Count circular descents:** A rotation of a distinct sorted array has exactly one circular descent unless already sorted. Care is needed because the wrap pair in an already sorted array is itself a circular descent.
- **Try every right shift:** Construct or compare all rotations in $O(n^2)$ time. It is simple at $n=100$ but unnecessary.
- **Already sorted:** `i == n` and zero shifts are returned.
- **Valid one-element suffix:** An array such as `[2,3,1]` correctly returns one because the final value is below the first.
- **Invalid one-element suffix:** `[1,3,2]` exposes the exact source defect; it returns one instead of negative one.
- **Suffix length at least two:** The chained first comparison indirectly checks the suffix's first value against `nums[0]`.
- **Second descent:** Suffix monotonicity fails and the source returns negative one.
- **Two-element descending array:** The one-element suffix is necessarily smaller than the first, so one shift is valid.
- **Distinctness:** It turns nondecreasing checks into strict comparisons and guarantees a unique sorted rotation.
- **Input preservation:** The method calculates a shift count without performing rotations.
- **Manifest claim:** The intended boundary validation is sound, but the exact implementation omits one required edge check.
