## General

**Follow the only possible removal order**

Every operation removes the current last element, so choosing a different order is impossible. The first $t$ operations always collect exactly the suffix of `nums` with length $t$. The task is therefore to find the shortest suffix that contains every integer from $1$ through $k$.

Scan `nums` from right to left and maintain a set `seen` of required values encountered so far. Add a value only when it is at most `k`; values above `k` are irrelevant to coverage, although processing them still increases the operation count. A set naturally prevents duplicate occurrences from being counted more than once.

After processing each value, compare `len(seen)` with `k`. Equality means that every one of the $k$ possible target values has appeared. The current count is feasible because those values have all been removed and collected. It is also minimal: every smaller count corresponds to a shorter suffix examined at an earlier iteration, when at least one target value was still absent. The input guarantee ensures the scan reaches this stopping condition.

## Complexity detail

Let $n = \lvert\texttt{nums}\rvert$. Each array element is inspected at most once, and expected set insertion takes constant time, so the running time is $O(n)$. At most the $k$ required values are stored, giving $O(k)$ auxiliary space.

The benchmark uses $n$ as `size` and places every value from $1$ through $n$ exactly once, forcing a complete reverse scan at sizes 8, 24, and 50. The set-based method scales linearly. A correct implementation that checks the growing collection with a linear list search completes all tiers but exhibits quadratic scaling.

## Alternatives and edge cases

- **Boolean occurrence array:** A Boolean array of length `k + 1` offers the same $O(n)$ time and $O(k)$ space while avoiding hash operations.
- **Bit mask:** Since $k \le 50$, one integer can mark collected targets in $O(1)$ auxiliary space, though the set representation states the intent more directly.
- **Linear list membership:** Keeping distinct targets in a list is correct, but each membership test can cost $O(k)$ and the total time can become $O(nk)$, which is quadratic when $k = n$.
- **Values above `k`:** They never contribute to the target set, but removing them still counts as an operation.
- **Duplicate targets:** Repeated occurrences do not increase the number of distinct required values collected.
- **Earliest stopping point:** Return immediately when all targets are present; scanning farther would produce a valid but nonminimal operation count.
- **Guaranteed feasibility:** Every target from $1$ through $k$ occurs somewhere in `nums`, so no failure return is needed for valid inputs.
