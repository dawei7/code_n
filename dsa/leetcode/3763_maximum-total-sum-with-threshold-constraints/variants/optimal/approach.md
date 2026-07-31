## General

At a given step, every unused index whose threshold has already been reached belongs to one available pool. Choosing any member removes exactly one item from that pool and advances the step, while future releases depend only on the new step—not on which available index was removed. Thus, selection order cannot change whether a later step is reached.

Moreover, the process stops only when the available pool is empty. At that moment every index released so far has necessarily been chosen, so their contribution sum is fixed as well. Despite the optimization wording, all legal choice orders produce the same final chosen set and total.

Use the bound `1 <= threshold[i] <= n` to bucket both the number and the sum of indices released at each step. At step `s`, add bucket `s` to the available count and released sum. If the count is zero, the process ends and the released sum is exactly the total already chosen. Otherwise consume one available index and continue. If all $n$ steps succeed, every index has been chosen and the accumulated bucket sum is the answer.

## Complexity detail

Let $n$ be the common array length. Filling the threshold buckets and scanning steps `1` through `n` each take $O(n)$ time. The two bucket arrays occupy $O(n)$ auxiliary space.

## Alternatives and edge cases

- **Sort thresholds plus a heap:** Releasing indices in sorted order and selecting an available value is correct but costs $O(n\log n)$ even though choice order cannot affect the result.
- **Scan all unused indices each step:** This directly simulates eligibility and can take $O(n^2)$ time.
- **No threshold-one index:** The available pool is empty at the first step, so the result is `0`.
- **Temporary empty pool:** Future thresholds do not matter once a step begins with no available index; the process ends immediately.
- **Multiple available indices:** Their consumption order may change intermediate totals but not the final total or reachability.
- **Large contributions:** The answer can exceed 32-bit range because up to $10^5$ values of $10^9$ may be selected.
- **All indices reachable:** If every step can consume an available item, the answer is the sum of all `nums` values.
