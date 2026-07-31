## General

**Start with every mandatory index.** If `nums1[i] == nums2[i]`, index `i` must participate in some swap; otherwise its value never changes and the final condition still fails. Select all such indices, add their indices to `cost`, and count their common values. Once a feasible permutation among selected positions exists, those indices can be arranged through swaps with total index contribution equal to this selected-index sum.

**Identify the only possible imbalance.** Let `selected` be the selected-set size, and let `dominant_count` be the largest frequency of one conflicting value `dominant_value`. Each copy of that value must move to a selected destination whose forbidden `nums2` value is different. There are `selected - dominant_count` such destinations among the mandatory indices. Therefore feasibility requires

$$
2 \cdot \texttt{dominant_count} \leq \texttt{selected}.
$$

All non-dominant conflicting values collectively fit once this largest frequency fits, so this single balance condition is sufficient.

**Add the cheapest safe helpers.** If the dominant value occupies more than half the mandatory set, scan all indices in increasing order. A non-conflicting index is a safe helper when both its current `nums1` value and its forbidden `nums2` value differ from `dominant_value`. Including it adds one destination without adding another dominant copy or creating an unavoidable equality.

Each helper increases `selected` by one while leaving `dominant_count` unchanged. Because indices are considered from smallest to largest, the algorithm adds the cheapest eligible helpers and stops immediately when the balance inequality holds. If the scan ends first, no remaining index can reduce the imbalance, so the task is impossible. Otherwise the selected values can be permuted to avoid every selected forbidden value, while all unselected indices were already unequal.

## Complexity detail

Let $n = \lvert\texttt{nums1}\rvert = \lvert\texttt{nums2}\rvert$. Two linear scans take $O(n)$ time. The frequency map stores at most $n$ distinct conflicting values, so auxiliary space is $O(n)$.

## Alternatives and edge cases

- **Explicit swap construction:** Materializing cycles proves a concrete rearrangement but is unnecessary when only the minimum cost is requested; the balance condition already proves existence.
- **Repeated helper search:** Finding one helper per full-array scan preserves greedy cost order but can degrade to $O(n^2)$ time.
- **No initial conflicts:** The mandatory set is empty, the balance condition already holds, and the answer is `0`.
- **One dominant conflicting value:** Safe helpers must have both corresponding values different from it; checking only one array can create a new equality.
- **Balanced mandatory set:** No helper indices are needed, even if several different values tie for the largest frequency.
- **Insufficient helpers:** Return `-1` when the dominant frequency remains more than half after every eligible position has been considered.
