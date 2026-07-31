## General

Fix a right endpoint. If a substring beginning at some index is valid, moving its start farther left only adds characters and therefore preserves validity. The valid starts for that endpoint consequently form a prefix of all possible start indices. The task is to find the boundary of that prefix without testing every substring.

Maintain frequencies for a sliding window `s[left..right]` and a counter `qualifying` that records how many letters currently appear at least $k$ times. When the new rightmost character's frequency changes from $k-1$ to $k$, increment `qualifying`. Larger frequencies do not create another qualifying letter and require no further counter change.

While `qualifying` is positive, remove characters from the left. If the outgoing character currently has frequency exactly $k$, its removal drops that letter below the threshold, so decrement `qualifying` before reducing the stored frequency. Continue until no letter reaches $k$ occurrences.

The remaining window `s[left..right]` is the first invalid suffix ending at `right`. Every start smaller than `left` was removed while the window was still valid, so exactly `left` substrings ending at this position qualify. Add `left` to the answer, then advance the right endpoint.

This counts every valid substring once by its right endpoint. Both pointers only advance: each character enters the window once and leaves it at most once. The threshold counter also handles several simultaneously qualifying letters; shrinking stops only after the last one drops below $k$.

## Complexity detail

Let $n=\lvert\texttt{s}\rvert$. The right pointer advances $n$ times and the left pointer advances at most $n$ times across the entire scan, giving $O(n)$ time. The frequency array has exactly 26 entries because the alphabet is fixed, so auxiliary space is $O(1)$. The linear bound is necessary for the legal maximum $n=3\cdot10^5$; enumerating all substrings can require quadratic work.

## Alternatives and edge cases

- **Enumerate all starts and ends:** Maintaining a counter while extending from every start is correct but takes $O(n^2)$ time, which is infeasible at the maximum length.
- **Binary search the first valid end for each start:** Validity is monotone, but rebuilding or querying frequency state for each search adds complexity that the two-pointer boundary avoids.
- **Rescan all 26 frequencies after every update:** This is still asymptotically linear for the fixed alphabet, but threshold-crossing events express the invariant directly and avoid repeated scans.
- **k equals one:** Every substring qualifies, and the accumulated contribution is $n(n+1)/2$.
- **Threshold never reached:** `left` remains zero for every endpoint, producing an answer of zero.
- **Only the entire string qualifies:** The boundary stays at zero until the last endpoint, then contributes exactly one start.
- **Several letters reach the threshold:** Removing the most recently added letter is not sufficient; the window remains valid until every qualifying letter has fallen below $k$.
- **Removal boundary:** Update `qualifying` when the outgoing frequency equals $k$, before decrementing it to $k-1$.
