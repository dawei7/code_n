## General

Any adjacent pair whose values are already known is unaffected by the replacements. Its absolute difference is therefore an immediate lower bound on the answer.

Now collect the known values that touch at least one `-1`. Let $L$ and $R$ be their minimum and maximum. For a candidate limit $d$, it is sufficient to test the canonical replacement pair

$$
x=L+d, \qquad y=R-d.
$$

Every boundary value must lie within distance $d$ of at least one selected replacement. Moving the smaller selected value toward $L+d$ and the larger toward $R-d$ cannot make coverage of the extreme boundary values worse. Thus, if any global pair can satisfy the limit, this canonical pair can satisfy the same boundary obligations.

**Check each missing run by its length.** A leading or trailing run touches only one known value, which merely has to be within $d$ of either $x$ or $y$. An internal run containing exactly one `-1` must use one replacement value adjacent to both known endpoints. For an internal run of at least two missing positions, there are four relevant forms: use only $x$, use only $y$, start with $x$ and end with $y$, or start with $y$ and end with $x$. The mixed forms additionally require $\lvert x-y\rvert\le d$; extra positions can repeat either value without introducing a larger difference.

These constant-size checks are performed while scanning the array and measuring each missing run. A limit that succeeds remains feasible for every larger limit, so binary search finds the smallest feasible $d$. The search begins at the largest fixed-to-fixed adjacent difference. When missing values touch known values, $\lceil(R-L)/2\rceil$ is a safe upper bound; if no known value touches a missing position, the fixed lower bound is already the answer.

## Complexity detail

Let $n=\lvert\texttt{nums}\rvert$ and let $U$ be the range between the smallest and largest known boundary values. Each feasibility check scans the array in $O(n)$ time, and binary search performs $O(\log U)$ checks. Total time is $O(n\log U)$ and auxiliary space is $O(1)$.

The benchmark size is $n$, the array length. Its single long internal missing run forces every feasibility check to traverse the full array. The reference therefore scales as $O(n\log U)$, while a baseline that redundantly rechecks the complete run for every missing position scales as $O(n^2\log U)$.

## Alternatives and edge cases

- **Dynamic programming over replacement choices:** For a fixed pair, two states per missing position are enough, but searching many possible pairs makes this much slower than using the canonical pair for each candidate limit.
- **Treat every missing position independently:** This misses the global restriction that all replacements must come from the same two chosen values.
- **Collapse every run to one missing value:** That is valid only for a run of length one; a longer run may transition from $x$ to $y$ and attain a smaller maximum difference.
- **All values missing:** Choose equal positive integers for $x$ and $y$, producing answer zero.
- **No missing values:** Only fixed adjacent differences matter, so the answer is their maximum.
- **Leading or trailing run:** It has only one known boundary and never needs an $x$-to-$y$ transition.
- **One-position internal run:** Its single value must be close enough to both endpoints simultaneously.
- **Long internal run:** Only its first and last replacements touch known values; repeated interior choices add no new condition beyond a possible $x$-$y$ transition.
- **Crossed canonical values:** When $x>y$, the same two numbers are still a valid unordered pair, and the four run checks remain unchanged.
