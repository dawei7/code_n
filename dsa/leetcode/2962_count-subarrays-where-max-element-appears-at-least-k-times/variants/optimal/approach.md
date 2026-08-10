## General

**Reduce the property to occurrences of one fixed value**

The relevant maximum is the maximum of the entire input array, not the maximum chosen independently for each subarray. The solution first computes `mx = max(nums)`. A subarray qualifies exactly when it contains at least `k` occurrences of this fixed value `mx`. Values smaller than `mx` affect subarray boundaries and counts but never change whether the occurrence threshold has been reached.

The implementation uses two pointers in a less common but very useful orientation. The outer loop moves the left endpoint from left to right. Pointer `j` is an exclusive right boundary that only moves forward. Variable `cnt` is the number of occurrences of `mx` in the current window beginning at the outer-loop position and ending at `j - 1`.

**Find the earliest valid ending for each start**

For a fixed left endpoint, the inner loop advances `j` while `cnt < k`. Each newly included `nums[j]` increases `cnt` only if it equals `mx`, and then `j` advances. The loop stops in one of two states:

1. `cnt == k`, meaning the window through index `j - 1` has just reached the required number of maxima; or
2. `j == n` while `cnt < k`, meaning even the entire remaining suffix does not contain enough maxima.

In the first state, `j - 1` is the earliest valid ending for the current start. It is earliest because the loop stopped at the first moment the count reached `k`. Every later ending remains valid: extending a window cannot remove an occurrence. The valid ending indices are therefore `j - 1, j, ..., n - 1`, a total of

`n - (j - 1) = n - j + 1`.

That is exactly the amount added to `ans`.

**Move to the next start without rebuilding the window**

At the end of an outer iteration, `x` is the element at the current left endpoint. The line `cnt -= x == mx` removes its contribution before the outer loop proceeds to the next start. If `x` is smaller than `mx`, the count is unchanged. If it equals `mx`, the count falls from `k` to `k - 1`, so the next inner loop advances `j` until it finds the next occurrence needed for the shifted window.

Pointer `j` never moves backward. All elements before `j` have already been included, except those removed one at a time from the left. This reuse is what makes the total work linear.

For example, take `nums = [1, 3, 2, 3, 3]` and `k = 2`. Here `mx = 3`. For start zero, `j` advances through index three, becoming four, and the earliest valid ending is three. Endings three and four work, so the contribution is two. Removing the left value one does not change `cnt`. For start one, the same earliest ending still works and again contributes two. Removing the `3` at start one lowers `cnt`, so `j` advances once to include the last `3`. The subsequent compatible starts are counted in the same way.

**Why breaking early is correct**

If the inner loop reaches `j == n` and still has `cnt < k`, the suffix from the current left endpoint to the end contains fewer than `k` maxima. Moving the left endpoint right only removes elements and cannot introduce a new maximum occurrence. Therefore no later start can yield a qualifying subarray, and `break` safely ends the outer scan.

**Why every qualifying subarray is counted once**

Fix a start index $L$. If its suffix contains at least `k` copies of `mx`, the inner loop identifies the unique earliest valid end $R$. The algorithm counts all pairs $(L,E)$ with $E \ge R$, and those are exactly the qualifying subarrays beginning at $L$. If the suffix contains too few copies, it counts none and terminates because every later suffix also contains too few.

Different outer iterations use different start indices, so no subarray can be counted twice. Since every possible start is processed until qualification becomes impossible, no qualifying subarray is missed.

The initialization `ans = cnt = j = 0` describes an empty window starting at zero. Although the outer loop is written as `for x in nums` rather than with an explicit left index, each successive `x` is precisely the element leaving the window.

## Complexity detail

Let $N$ be the length of `nums`. Finding `mx` takes $O(N)$ time. The outer loop visits each possible left endpoint at most once. Across all iterations, `j` advances from zero to at most $N$ and never retreats, so the inner loop performs at most $N$ total inclusions. The complete running time is $O(N)$.

Only `mx`, `n`, `ans`, `cnt`, `j`, and loop scalars are stored, giving $O(1)$ auxiliary space. The input array is read but not modified.

The answer can be quadratic in $N$ because there are $N(N+1)/2$ subarrays, but Python integers safely grow to represent it. Output magnitude does not imply quadratic running time.

## Alternatives and edge cases

- **Enumerating every subarray:** Counting maxima for all start/end pairs takes at least $O(N^2)$ time and repeats heavily overlapping work.
- **Store maximum positions:** One can collect every index where `nums[i] == mx` and derive contributions from groups of `k` positions. That is also linear but uses $O(N)$ space in the worst case.
- **Right-oriented sliding window:** Another formulation extends a right endpoint and counts valid starts. It is correct, but its counting formula differs; the exact implementation here counts valid endings for each start.
- **Off-by-one in `n - j + 1`:** `j` is exclusive. Once the $k$th maximum is at `j - 1`, there are $n - j + 1$ inclusive ending positions.
- **`k = 1`:** For each start, the first occurrence of the global maximum determines the earliest valid end; every later end is counted.
- **All elements equal to the maximum:** Every subarray of length at least `k` qualifies, and the pointers produce the corresponding triangular count.
- **Fewer than `k` maxima in the whole array:** The first inner scan reaches the end with `cnt < k`, the loop breaks, and the answer is zero.
- **Removing the left endpoint:** Decrementing `cnt` only when `x == mx` is essential; smaller values have no effect on the tracked condition.
- **Input preservation:** Neither pointer operation changes `nums`.
