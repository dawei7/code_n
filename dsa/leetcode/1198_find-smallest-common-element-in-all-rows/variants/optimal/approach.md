## General
**Count row membership directly.** Allocate a frequency table indexed by the allowed values from 1 through $10^4$. Scan the rows in order and increment the frequency of each encountered value. Strict increase guarantees that a value contributes at most once per row, so its frequency equals the number of processed rows containing it without needing a per-row set.

**Return when the final required occurrence appears.** A value is common exactly when its frequency reaches $m$. This can first happen while processing the last row. Because that row is strictly increasing and scanned from left to right, the first value to reach $m$ is also the smallest common element. If no frequency reaches $m$ by the end, return `-1`.

## Complexity detail
The scan visits each of the $mn$ matrix entries once and performs constant work per entry, giving $O(mn)$ time. The frequency table has exactly 10001 slots because the value domain is fixed at $10^4$; its size does not grow with $m$ or $n$, so auxiliary space is $O(1)$ under the stated constraints.

## Alternatives and edge cases
- **First-row candidates with binary search:** Binary-searching every first-row value in every other row uses $O(mn\log n)$ time and $O(1)$ extra space.
- **Explicit linear membership search:** Scanning each row separately for every first-row candidate can require $O(mn^2)$ time.
- **Pointer alignment:** Maintaining one pointer per row and repeatedly advancing rows below the current maximum takes linear total pointer advances and $O(m)$ space.
- **Single row:** Every value is common to the only row, so its first value is the answer.
- **One column:** A common element exists only when every row's sole value is equal.
- **Several common values:** The sorted final-row scan returns the smallest one before any larger common value.
- **No common value:** The complete scan ends without any count reaching $m$ and returns `-1`.
- **Strict increase:** No row contains duplicates, which is essential for raw frequency counts to represent row membership.
