## General

**Rephrase a group as an alternating run.** A group contains exactly three consecutive circular tiles. Its middle tile must differ from both neighbors. Because there are only two colors, this is equivalent to both adjacent pairs being different. A virtual sequence of colors is alternating across a window exactly when every neighboring pair in that window differs.

Instead of checking three tiles separately for every possible middle, the exact source tracks the length `cnt` of the alternating suffix ending at the current virtual position:

- if the current color equals the previous color, alternation breaks and the suffix restarts with length one;
- otherwise, the current tile extends the alternating suffix, so `cnt` increases by one.

Whenever `cnt >= 3`, the last three virtual tiles form an alternating group.

**Linearize the circle with modulo indexing.** The array is circular, so a group may cross from index $n-1$ back to index $0$. The code scans virtual indices

$$
0,1,\ldots,2n-1
$$

using `colors[i % n]`. The second copy is not physically allocated; modulo simply reads the original array again. The predecessor is `colors[(i - 1) % n]`.

Scanning two copies supplies enough history for every circular length-three window. The source uses `range(n << 1)`; shifting $n$ left by one bit produces $2n$.

**Count only one representative of each circular group.** If the algorithm counted whenever `cnt >= 3` throughout the full doubled scan, ordinary non-wrapping windows would appear twice. It instead adds a group only when `i >= n`. The counted endpoints are the $n$ virtual positions

$$
n,n+1,\ldots,2n-1.
$$

A length-three window ending at virtual `i` starts at `i-2`. Reducing those starts modulo $n$ produces every circular starting index exactly once. Thus the second-half gate counts $n$ candidates—one for each possible middle or start—without duplication.

The expression

`ans += i >= n and cnt >= k`

uses Python Booleans as integers. It adds one only when both conditions are true and adds zero otherwise. Here `k` is fixed to three.

**Why the running length is accurate.** After virtual position `i` is processed, `cnt` equals the greatest length $L$ such that the virtual segment ending at `i` and containing $L$ tiles has unequal colors across every adjacent boundary. At `i=0`, the suffix contains only one tile, so incrementing from zero gives one. At later positions, equality with the predecessor prevents any alternating segment from crossing that boundary, so resetting to one is exact. Inequality extends every alternating suffix by the current tile, so incrementing is exact.

It follows that `cnt >= 3` precisely when the last three tiles alternate. For two colors, those three must have pattern $0,1,0$ or $1,0,1$, which means the middle differs from both sides. This proves every counted endpoint is a valid group and every valid circular group is counted at its unique second-half endpoint.

**Trace a boundary case.** For `colors = [0,1,0,0,1]`, the ordinary sequence alternates across the first three tiles, breaks between the two zeros at indices $2$ and $3$, then alternates again. Continuing into the virtual second copy also tests the boundary from the last $1$ to the first $0$. The suffix counter identifies exactly the windows whose two internal adjacencies differ, including those wrapping around the physical end. Restricting endpoints to the second half yields three groups.

For `[1,1,1]`, every transition sees equal colors and resets `cnt` to one. It never reaches three, so the answer remains zero.

**The code is a run-length method, not explicit neighbor checking.** The manifest summary says both neighbors of every middle are checked once. That describes an equivalent $O(n)$ idea, but the exact source instead performs a doubled circular scan and maintains alternating suffix length. The bounds agree; the data flow differs.

## Complexity detail

Let $n$ be the number of tiles. The loop performs exactly $2n$ iterations. Every iteration uses constant-time indexing, comparison, arithmetic, and Boolean accumulation, so total time is $O(n)$.

Only `n`, `ans`, `cnt`, `i`, and constant `k=3` are stored. The doubled circle is virtual rather than copied, so auxiliary space is $O(1)$. The input list is read only.

The constraints fix colors to zero or one, although the adjacent-inequality run method would work for more than two colors if “alternating” were defined merely as neighboring values being different. The middle-differs-from-both equivalence here follows directly from the three-tile definition.

## Alternatives and edge cases

- **Check each middle directly:** For every index `i`, test whether `colors[i]` differs from `colors[(i-1)%n]` and `colors[(i+1)%n]`. This is simpler for fixed length three and has the same optimal bounds.
- **Append the first two tiles:** Build a linear array of length $n+2$ and inspect every length-three window. It is clear but uses $O(1)$ extra elements only because the window size is fixed; modulo avoids mutation.
- **Check every three-tile window independently:** This is still $O(n)$ for fixed length three, but repeats adjacent comparisons that the run counter shares.
- **All tiles equal:** Every adjacent comparison breaks, so zero groups exist.
- **Perfect alternation with even $n$:** The circular boundary also alternates, and all $n$ possible groups count.
- **Linear alternation with odd $n$:** A two-color odd cycle must repeat a color at the wrap boundary. Windows crossing that one break are excluded correctly.
- **Minimum length three:** There are three circular groups distinguished by their starting positions, even though they use the same three physical tiles in different cyclic orders.
- **Wrap-around predecessor:** At virtual `i=n`, current index zero is compared with physical index $n-1$, exactly testing the circular seam.
- **Long run:** Once `cnt` exceeds three, every new endpoint contributes another overlapping length-three window.
- **Boolean addition:** Python evaluates the conjunction to `True` or `False`, which add as one or zero.
- **No duplicate counting:** Only endpoints in the second virtual copy contribute; the first copy exists solely to build history.
- **Input preservation:** Modulo indexing simulates repetition without appending to `colors`.
