## General

Fix a prospective second index `right`. Its valid first indices are exactly `0` through `right - k`. Among those positions, only the greatest array value can produce the best pair ending at `right`. This turns the apparent pair enumeration into a maintained prefix maximum.

Scan `right` from `k` through `n - 1`. Before evaluating that endpoint, incorporate `nums[right - k]` into `best_left`. After this update, `best_left` is precisely the maximum of `nums[0:right - k + 1]`, so `best_left + nums[right]` is the greatest sum of any valid pair whose second index is `right`. Compare that value with the global answer.

Every legal pair has one second index visited by the scan. For that index, the maintained prefix includes its first endpoint, and using the prefix maximum can only improve the sum. Conversely, the value represented by `best_left` always comes from an index at most `right - k`, so every candidate considered is valid. Taking the maximum across all right endpoints therefore yields exactly the required answer.

## Complexity detail

Let $n = \lvert\texttt{nums}\rvert$. Each index becomes newly eligible once and each right endpoint is processed once, giving $O(n)$ time. Only the prefix maximum and global answer are stored, so the auxiliary space is $O(1)$.

## Alternatives and edge cases

- **Enumerate every valid pair:** Directly checking all `(i, j)` is correct but requires $O(n^2)$ time when `k` is small.
- **Prefix-maximum array:** Precomputing every prefix maximum also gives $O(n)$ time, but it spends $O(n)$ space when one running value is sufficient.
- **Heap or segment tree:** These structures can query earlier maxima but add logarithmic work and storage even though the eligible prefix only grows.
- **`k = 1`:** Every pair with increasing indices is valid; the method still selects the two values giving the greatest legal sum.
- **`k = n - 1`:** Only `(0, n - 1)` is valid, and the scan evaluates exactly that pair.
- **Large values:** A pair sum can reach $2 \times 10^9$; implementations should use a numeric type that represents this bound safely.
- **Large values too close together:** Two individually large entries cannot be paired unless their indices differ by at least `k`.
