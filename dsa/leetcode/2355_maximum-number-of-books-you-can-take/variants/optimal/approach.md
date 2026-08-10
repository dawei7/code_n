## General

**Fix the rightmost shelf and maximize everything to its left**

Suppose a chosen section ends at shelf `i` and takes all `books[i] = v` books there. Moving one shelf left, strict increase permits at most `v - 1` books; another step left permits at most `v - 2`, and so on.

Within a suffix not limited by shelf capacities, the optimal taken amounts form a descending-by-one arithmetic progression when viewed right to left.

The dynamic state `dp[i]` is the maximum total for a valid contiguous section ending at `i` while taking exactly `books[i]` from that final shelf.

**Transform capacity constraints with books[i] minus i**

Extending the progression from `i` back to earlier index `j` would demand

`books[i] - (i-j)`

books at `j`. Shelf `j` can support this exactly when

`books[j] >= books[i] - (i-j)`,

equivalently

`books[j] - j >= books[i] - i`.

The list `nums[i] = books[i] - i` makes this comparison constant and exposes a previous-smaller-element problem.

**Find the nearest boundary with a monotonic stack**

`left[i]` is the nearest previous index `j` satisfying

`nums[j] < nums[i]`.

The stack keeps indices with strictly increasing `nums` values. Before pushing current `i`, it pops while the top value is greater than or equal to current. The remaining top, if any, is the nearest strictly smaller boundary.

Every index is pushed once and popped at most once, so all boundaries are found in linear time.

At this boundary, shelf `j` cannot simply continue the arithmetic ramp controlled by shelf `i`; it is better represented by its already optimized `dp[j]`. Shelves `j+1` through `i` form the new progression segment.

**Compute the progression sum**

The segment can contain at most `i-j` shelves after boundary `j`. It also cannot contain more than `v` positive terms, because continuing farther would reach zero or negative books.

Thus

`cnt = min(v, i-j)`.

The rightmost term is `v` and the leftmost positive term is

`u = v-cnt+1`.

Their arithmetic-series sum is

`s = (u+v) * cnt / 2`.

Integer division is exact because one of the two factors in the standard series product is even.

If `j == -1`, no earlier smaller boundary exists and the progression supplies the entire chosen section, possibly starting later than index zero when `v < i+1`.

If `j != -1`, its existence implies the segment can connect to `dp[j]` with a strict increase, and the state becomes `dp[j] + s`.

**Why combining at j remains contiguous**

`dp[j]` represents a section ending at `j` and taking `books[j]` there. The first amount in the new segment at `j+1` is greater than `books[j]` because `books[j]-j < books[i]-i`.

Therefore the concatenation across boundary `j,j+1` is strictly increasing and has no gap. The whole chosen section remains contiguous.

When `cnt < i-j`, the progression starts later than `j+1`. This can occur only when `j = -1`; a real smaller boundary that far left would contradict nonnegative `books[j]` and the transformed inequality. Thus no invalid gap is combined with `dp[j]`.

**Take the best possible ending shelf**

Every valid section has some rightmost shelf. For a fixed right endpoint, taking fewer than its available books cannot improve the maximum total; increasing the endpoint amount relaxes or raises possible amounts to the left. The recurrence therefore covers an optimum ending at each `i`.

`ans` tracks the maximum `dp[i]` across all endpoints, yielding the global answer.

## Complexity detail

Let `n` be the number of shelves. Building transformed values is `O(n)`. Each index enters and leaves the monotonic stack at most once, and the DP loop is linear, so total time is `O(n)`.

`nums`, `left`, `stk`, and `dp` each use `O(n)` space. Other variables are constant-size, giving `O(n)` auxiliary space.

The input is not modified. Python integers safely hold arithmetic-series totals.

## Alternatives and edge cases

- **Walk left from every endpoint:** Directly constructing the best progression costs `O(n^2)` in decreasing-capacity patterns.
- **Use only a greedy global segment:** Local capacity boundaries create restart points, so dynamic programming is needed to combine earlier optimal segments.
- **Previous smaller on raw books:** The relevant comparison is `books[i]-i`, which incorporates the one-per-position slope.
- **Pop only strictly greater stack values:** Equal transformed values must also pop because the boundary requires strictly smaller.
- **One shelf:** Its `dp` equals its available books and is the answer.
- **Zero-book shelf:** A segment taking positive amounts cannot pass through it; the formulas produce a zero-length contribution when it is the endpoint.
- **Increasing capacities:** Long sections may use most or all shelves.
- **Very small right endpoint value:** `cnt <= v` prevents zero or negative terms.
- **No previous boundary:** The progression begins at the later of index zero and the point where its leftmost term is one.
- **Boundary exists:** `dp[j]` joins a progression over `j+1..i` with strict inequality at the join.
- **Equal transformed values:** The earlier index is popped so it cannot be used as a strictly smaller boundary.
- **Maximum over endpoints:** The best section need not end at the last shelf.
- **Input preservation:** All transformed and DP state is separate from `books`.
