## General

**Count windows containing a value, not just its occurrences.** An integer is almost missing when it appears in exactly one length-$k$ subarray. Repeated appearances inside one window count as presence in that one window, while one occurrence can belong to several overlapping windows. The source avoids explicit window enumeration by separating the two extreme window sizes from the general case.

**When \(k=1\), windows and positions are identical.** Every length-one subarray contains exactly one array position. A value appears in exactly as many size-one windows as its total frequency in `nums`. The source builds `Counter(nums)` and considers exactly the entries whose count is one. `max(..., default=-1)` returns the largest globally unique value or $-1$ when none exists.

For `nums = [0,0]` and `k=1`, zero has frequency two, so the generator contains no candidate and the answer is $-1$.

**When \(k=n\), there is only one window.** The whole array is the sole subarray of size $n$. Every value present in `nums` appears in that same single window, even when the value occurs multiple times. Therefore, every distinct input value is almost missing and the largest answer is simply `max(nums)`.

This case shows why global uniqueness is not a universal rule. Duplicates matter differently when all occurrences are contained in the only possible window.

**For \(1<k<n\), only array endpoints can supply a candidate.** Index zero belongs only to the window starting at zero. Index $n-1$ belongs only to the window starting at $n-k$. Every interior index belongs to at least two length-$k$ windows under these strict inequalities.

To see the interior claim, a window containing index $i$ may start anywhere from

$$
\max(0,i-k+1)
$$

through

$$
\min(i,n-k).
$$

For $0<i<n-1$, $1<k<n$ ensures this valid start interval contains at least two integers. Thus any value occurring at an interior position appears in at least two different windows and cannot be almost missing.

An endpoint value qualifies only if it occurs nowhere else. If `nums[0]` appears at another index, that other occurrence belongs to some window other than the unique window starting at zero, so the value appears in at least two windows. The same argument applies to the last endpoint. If both endpoints have the same value, each endpoint lies in a different boundary window because $k<n$, so it also fails.

**Test global uniqueness of each endpoint.** Helper `f(k)` uses its parameter as an index, despite the confusing reuse of the name `k`. It scans all positions and returns $-1$ if another index contains the same value as `nums[k]`. Otherwise, it returns that endpoint value.

The general branch computes

`max(f(0), f(len(nums) - 1))`.

These are the only two possible almost-missing values. Values are nonnegative, so the sentinel $-1$ is safely smaller than every real candidate. If neither endpoint is globally unique, the maximum of the two sentinels is $-1$.

For `nums = [3,9,2,1,7]` and `k=3`, both endpoint values $3$ and $7$ occur once. Each belongs only to its corresponding boundary window, so both qualify and the maximum is $7$. Interior values are excluded because their positions occur in multiple windows.

For `nums = [3,9,7,2,1,7]` and `k=4`, the first endpoint value $3$ is unique and qualifies. The last endpoint value $7$ also appears at index two, so it occurs in multiple windows and helper `f` rejects it. The answer is $3$.

**Why the three-way case split is complete.** The size-one case reduces window presence to occurrence frequency. The full-size case collapses all values into one window. For every remaining $k$, the containment-count argument proves that an almost-missing value must occur only at one endpoint, and the uniqueness scan recognizes exactly those endpoint values. Each branch therefore returns the largest member of the complete candidate set.

The source's shortcut is stronger than sliding a window and maintaining value sets: it uses where an index lies relative to all windows to reduce the candidate set to at most two.

## Complexity detail

For `k == 1`, building the counter and scanning its entries take $O(n)$ time and $O(n)$ space in the worst case. For `k == n`, `max(nums)` takes $O(n)$ time and $O(1)$ auxiliary space. In the middle case, helper `f` is called twice and each scans at most $n$ positions, so time is $O(n)$ and auxiliary space is $O(1)$.

Across all inputs, the worst-case bounds are $O(n)$ time and $O(n)$ auxiliary space, matching the manifest. The $O(n)$ space is reached only by the counter branch; the endpoint branch does not allocate a frequency table.

Given the small constraint $n\le50$, a direct window-set method could pass, but the structural argument achieves the best asymptotic time and clarifies why only boundary values matter.

## Alternatives and edge cases

- **Count raw occurrences for every \(k\):** A single occurrence can lie in several overlapping windows, so frequency alone is insufficient except when `k == 1` or for the endpoint uniqueness test.
- **Enumerate every window and every distinct value in it:** This can require $O(nk)$ work and hides the endpoint structure.
- **Sliding sets with a per-value window counter:** It is correct but more machinery than needed for this special question.
- **Interior unique value:** Even one occurrence belongs to at least two windows when $1<k<n$, so uniqueness does not make it a candidate.
- **Duplicate endpoint value:** Any second occurrence creates presence in another window and invalidates that endpoint candidate.
- **Same value at both endpoints:** Because `k < n` in the middle branch, the two endpoint windows differ, so the value is not almost missing.
- **\(k=1\):** Only globally unique values appear in exactly one singleton window.
- **\(k=n\):** Every present value appears in the sole whole-array window, regardless of frequency.
- **One-element array:** Both boundary cases coincide with `k=n=1`, and `max(nums)` returns the sole value.
- **Value zero:** The sentinel is $-1$, so a qualifying zero is preserved as a valid answer.
- **No candidate:** Empty counter filtering or two rejected endpoints correctly yields $-1$.
- **Helper parameter naming:** The nested `f(k)` receives an array index, not the original window size; reading it as an index is necessary to understand the source.
