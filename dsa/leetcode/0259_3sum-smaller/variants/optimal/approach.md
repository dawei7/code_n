## General

The task counts index triplets, not distinct value triples. A cubic solution can test every choice of three indices, but sorting reveals monotonic relationships that let one comparison count many triplets at once.

After `nums.sort()`, the solution fixes the first position `i`. It then searches pairs to the right with two pointers:

- `j = i + 1` is the smallest still-unprocessed second position;
- `k = n - 1` is the largest still-possible third position.

The ordering `i < j < k` is built into these pointer ranges, so every counted combination uses three distinct positions.

**Sorting does not lose index multiplicity**

Sorting rearranges occurrences, but it is a bijection between original array positions and sorted positions. Every occurrence remains present exactly once. If equal values appear several times, their sorted positions are still separate choices, and pointer-distance counting includes each index combination. This is why the method can sort even though the problem phrases the answer using original indices.

**When the largest current sum is small enough**

For fixed `i` and `j`, first test

$$
x=\text{nums}[i]+\text{nums}[j]+\text{nums}[k].
$$

If $x<target$, then replacing `k` by any position `p` with $j<p\le k$ cannot increase the sum, because the array is sorted and `nums[p] <= nums[k]`. Therefore, every triplet

$$
(i,j,j+1),(i,j,j+2),\ldots,(i,j,k)
$$

is valid. There are exactly `k - j` such third positions, so the algorithm adds that number to `ans` in one operation.

All triples using this fixed `i` and `j` within the remaining range have now been counted. The solution advances `j` to discover triples with the next second position. It does not decrease `k`, because the larger second value may or may not still work with the same far-right endpoint; testing will decide.

**When the sum is too large**

If $x\ge target$, the triplet at the current boundaries is invalid. More importantly, keeping the same `k` and moving `j` right cannot help: every later second value is at least `nums[j]`, so the sum would stay the same or grow. Thus no valid remaining pair for this fixed `i` can use the current third position `k`.

The only useful move is `k -= 1`, replacing the largest candidate by a smaller value. This discards no valid triplet.

The strict comparison matters. A sum equal to `target` does not qualify, so it follows the same branch as a larger sum and moves `k` left.

**Trace through the first example**

For `nums = [-2, 0, 1, 3]` and `target = 2`, the array is already sorted.

Fix `i = 0`, so `nums[i] = -2`. Begin with `j = 1` at `0` and `k = 3` at `3`.

- The sum is `-2 + 0 + 3 = 1`, which is below `2`. Every third position from `j + 1` through `k` works: positions `2` and `3`, representing `[-2,0,1]` and `[-2,0,3]`. Add `k - j = 2`, then advance `j`.
- Now `j = 2` and `k = 3`. The sum is `-2 + 1 + 3 = 2`, equal to the target and therefore invalid. Decrement `k`, ending the inner loop.

Fixing `i = 1` leaves `j = 2` and `k = 3`. The sum `0 + 1 + 3 = 4` is too large; `k` moves left and the loop ends. The final count is `2`.

**Why every valid triplet is counted once**

The outer loop assigns every triplet a unique first sorted position `i`. Within that iteration, a valid triplet has one unique second position `j`. When the algorithm eventually processes that `j`, either the current `k` is at least the triplet's third position and the valid block count includes it, or oversized endpoints have already been removed because they cannot work with any remaining `j`. The triplet is therefore included.

Once a valid block is counted, `j` advances, so no triplet with that second position can be counted again. When `k` decreases, the argument above proves no valid combination using that `k` with any unprocessed `j` is lost. These two safe pointer moves exhaust all pairs exactly once for each `i`.

**Why the outer loop stops at `n - 2`**

`i` must leave room for two later positions. Python's `range(n - 2)` produces first indices from `0` through `n - 3`. If the array has fewer than three elements, the range is empty and the answer correctly remains zero.

## Complexity detail

Let $n$ be the number of elements. Sorting takes $O(n\log n)$ time. For one fixed `i`, each inner-loop iteration moves either `j` right or `k` left. Neither pointer reverses direction, so that scan takes $O(n)$ time. Repeating it for $O(n)$ first positions costs $O(n^2)$, which dominates sorting. Total time is $O(n^2)$.

Python's in-place Timsort can use $O(n)$ temporary storage in the worst case. The pointer scan itself uses only constant scalar space. Therefore, the language-specific auxiliary space bound is $O(n)$, matching the manifest. In a language with an $O(1)$-auxiliary in-place sort, the same algorithm's extra-space bound could be constant.

The source mutates `nums` by sorting it. The contract does not require original order preservation. Sorting a copy would avoid mutation but would still use $O(n)$ space.

## Alternatives and edge cases

- **Three nested loops:** Test every triplet directly in $O(n^3)$ time and $O(1)$ extra space. It is simple but too slow near `n = 3500`.
- **Binary search for each `(i, j)`:** Find the last valid `k` in the sorted suffix, giving $O(n^2\log n)$ time. Two pointers reuse monotonic progress and remove the logarithmic factor.
- **Frequency counting over the bounded value range:** Since values lie from `-100` to `100`, a combinatorial frequency method is possible, but it requires careful multiplicity cases. The sorted two-pointer method is more general.
- **Sum exactly equals target:** It is invalid because the condition is strictly smaller; the code correctly moves `k` left.
- **Duplicate values:** They remain distinct sorted positions. Adding `k - j` counts index triplets with equal values according to their multiplicity.
- **All negative values:** Sorting and monotonic sum arguments remain valid; signs do not change pointer logic.
- **Empty, one-element, or two-element input:** No first position leaves two later indices, so the function returns zero.
- **Exactly three elements:** The inner loop performs one comparison and returns either one or zero.
- **All triples valid:** For each `i` and `j`, the algorithm counts the entire remaining right block, efficiently accumulating $\binom{n}{3}$.
- **No triples valid:** The right pointer repeatedly moves left for each `i`; runtime remains quadratic in the worst case.
- **Input mutation:** `nums.sort()` destroys original ordering. Use `sorted(nums)` when the caller must retain it.
- **Answer size:** The constraints guarantee the count fits within $10^9$; Python would handle larger integers anyway.
