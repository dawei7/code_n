## General

**A valid window is contained in an alternating run.** A group of $k$ consecutive circular tiles is valid exactly when every adjacent pair inside it has different colors. Track `cnt`, the length of the longest alternating suffix ending at the current virtual tile:

- if current and previous colors are equal, no alternating segment crosses that boundary, so set `cnt = 1`;
- if they differ, extend the suffix with `cnt += 1`.

Then the length-$k$ window ending at the current position is alternating exactly when `cnt >= k`. A run longer than $k$ contributes overlapping valid windows, one at each new endpoint.

**Walk around the circle without copying it.** Virtual index `i` reads physical tile `colors[i % n]`. The source scans `range(n << 1)`, which means indices zero through $2n-1$. This behaves as though two copies of the array were concatenated, but no extra array is allocated.

The doubled traversal is sufficient because the constraint guarantees $k\le n$. Any circular window of length $k$ crosses the physical boundary at most once and fits within two copies.

At every position after zero, the code compares the current virtual tile with `colors[(i - 1) % n]`. In particular, virtual position $n$ compares physical index zero with physical index $n-1$, explicitly incorporating the circular seam.

**Choose exactly $n$ window endpoints.** A circle of $n$ tiles has exactly $n$ distinct starting positions for a length-$k$ group. The source counts only when `i >= n`, so candidate endpoints are

$$
n,n+1,\ldots,2n-1.
$$

There are exactly $n$ of them. Their corresponding starts are `i-k+1`, and reducing those starts modulo $n$ yields every circular starting index once. The first virtual copy builds enough alternating history; it does not contribute answers.

The compact statement

`ans += i >= n and cnt >= k`

adds the Boolean conjunction. Python treats `True` as one and `False` as zero.

**Why `cnt` is an exact invariant.** At position zero, the only suffix has length one. Suppose the invariant is true after position `i-1`. If the next color is equal, any segment of length at least two ending here contains that equal boundary and is not alternating; the best suffix is the single current tile. If the colors differ, appending the current tile to the previous longest alternating suffix remains alternating, and no longer suffix could exist without contradicting previous maximality. The update is exact by induction.

Therefore `cnt >= k` if and only if the last $k$ virtual positions form a valid group. Since the counted endpoints map one-to-one to circular starts, `ans` is exactly the number requested.

**Trace a wrap-around pattern.** For `colors = [0,1,0,0,1,0,1]` and $k=6$, equality between the two middle zeros breaks the run. The doubled scan later continues from the final $1$ to the first $0$, allowing a run that crosses the boundary. Each second-half endpoint whose suffix has reached six contributes one, producing the two valid circular groups without appending values to the list.

**Why scanning $2n$ rather than $n+k-1$ is still linear.** Only the first $k-1$ positions beyond one copy are strictly needed to form all circular windows. The source scans a full second copy and counts a shifted set of $n$ endpoints instead. Because $k\le n$, both approaches take $O(n)$ time. The extra constant-factor positions simplify the gate.

## Complexity detail

The loop executes exactly $2n$ iterations and performs constant work in each, so time is $O(n)$. Modulo operations are constant-time for the bounded indices.

The algorithm stores only counters and loop variables. It does not extend or copy `colors`, so auxiliary space is $O(1)$. The input remains unchanged.

The bound does not depend multiplicatively on $k$; `cnt` summarizes all window lengths ending at the current position. This is the improvement over checking all $k-1$ adjacencies independently for every start.

## Alternatives and edge cases

- **Scan $n+k-1$ virtual positions:** Start counting as soon as a full window exists and stop after all $n$ starts are represented. This may inspect fewer positions but has the same $O(n)$ bound because $k\le n$.
- **Append the first $k-1$ tiles:** It turns circular windows into linear windows but uses $O(k)$ extra space and mutates the input in some implementations.
- **Check every window independently:** Testing $k-1$ adjacencies for each of $n$ starts costs $O(nk)$.
- **Two-pass seam handling:** Scan the physical array, then only the necessary prefix while carrying the run length. It matches the editorial and stays constant-space.
- **All tiles equal:** `cnt` resets to one at every step, so no valid group exists for $k\ge3$.
- **Fully alternating even cycle:** The seam differs too, the run never breaks, and all $n$ starts count.
- **Odd two-color cycle:** Perfect circular alternation is impossible; at least one equal seam or internal boundary excludes windows containing it.
- **$k=n$:** Each start uses every tile but a different circular boundary ordering. The second-half endpoint mapping still evaluates exactly $n$ candidates.
- **Run length exactly $k$:** The endpoint contributes once. Each further alternating tile produces another overlapping group.
- **Equality reset:** Resetting to zero would be wrong because the current tile itself begins a new run of length one.
- **Boolean accumulation:** The conjunction must be parenthesized mentally as two tests; only second-half endpoints with sufficient run length add one.
- **Binary colors:** The method only needs neighbor inequality, so it remains correct for a larger color alphabet under the same alternation definition.
- **Input preservation:** Circular behavior comes from modulo indexing, not list extension.
