## General

**Sort jobs so the remaining choices form a suffix**

Each job is represented by a matching start time, end time, and profit. `zip(startTime, endTime, profit)` combines these parallel entries, and `sorted` creates tuples ordered first by start time, then by end time and profit when starts tie.

After sorting, if the algorithm is considering index `i`, every job that could still be chosen is in the suffix from `i` onward. This makes one index sufficient to describe a dynamic-programming subproblem.

`dfs(i)` means the maximum profit obtainable using only jobs at indices `i` through the end.

If `i >= n`, no jobs remain, so the maximum additional profit is zero.

**Every optimal schedule makes one of two choices**

At job `i`, an optimal schedule either skips that job or takes it.

- Skipping earns nothing immediately and leaves `dfs(i + 1)`.
- Taking earns the current profit `p` and requires jumping past every job that starts before the current end time `e`.

The recurrence is

\[
\texttt{dfs}(i)
=
\max\bigl(
\texttt{dfs}(i+1),
p+\texttt{dfs}(j)
\bigr),
\]

where `j` is the first compatible later job.

These choices are exhaustive and mutually exclusive, so choosing the larger result is safe.

**Find the next compatible job with binary search**

Jobs are sorted by start time. The contract permits a new job to start exactly when the current one ends, so compatibility requires `next_start >= e`.

The source uses:

`bisect_left(jobs, e, lo=i + 1, key=lambda x: x[0])`.

With a key function, `bisect_left` compares `e` against the start-time key `x[0]` of each job. It returns the first index whose start is not less than `e`. The lower bound `i + 1` restricts the search to later jobs.

This is exactly the jump needed by the take branch. Every job between `i + 1` and `j - 1` starts too early and overlaps the current job. Job `j` and any later job are candidates because their starts are at least `e`.

**Why memoization matters**

Without caching, skip and take branches create an exponential recursion tree. Many branches reach the same suffix index. `@cache` stores the result for each `i` after its first computation, so every suffix is solved once.

There are only \(n+1\) possible indices, including the base state. Each real state performs one binary search and constant work around its two cached recursive calls.

**Following the first example**

After sorting, jobs include `(1,3,50)` and `(3,6,70)`. Taking the first job searches for the first start at least three and can jump to the job starting at three. These jobs touch at the boundary but do not overlap, so their profits combine to 120.

At every index, the recurrence also considers skipping. Thus a tempting low-profit job cannot force the schedule to miss a better later combination. The maximum at index zero becomes 120.

In the example where three jobs all start at one, taking one jumps beyond every other job that starts before its end. Skipping explores the next same-start alternative. The recursion compares their profits and returns six from the job ending at three, rather than greedily choosing the earliest end or longest duration.

**Why simple greedy rules fail**

Choosing the earliest finishing job maximizes the number of compatible jobs in unweighted interval scheduling, but here profits differ. One long profitable job can be better than several short low-profit jobs, or vice versa. The skip/take recurrence evaluates total future profit rather than using one local property.


Assume `dfs(r)` is correct for all indices greater than `i`. Any valid schedule from suffix `i` either excludes job `i`, in which case its profit is at most `dfs(i + 1)`, or includes it. If it includes it, no job before `j` can follow without overlap, and the best compatible continuation is `dfs(j)`, giving at most `p + dfs(j)`.

Both bounds are achievable by the corresponding recursive choices. Their maximum is therefore exactly the optimal suffix profit. Induction from the empty suffix proves `dfs(0)` is the global maximum.

**Exact Python behavior**

`sorted(zip(...))` materializes a new list of job tuples and does not reorder the three input arrays. The code relies on `bisect_left` supporting `key` and on `cache` being available.

The recursion can follow the skip branch one index at a time, reaching depth \(O(n)\). With up to 50,000 jobs, a typical default Python recursion limit may be insufficient unless the environment raises it. The verified package source ran in its accepted environment, but an iterative formulation is more portable.

## Complexity detail

Let \(n\) be the number of jobs. Building and sorting `jobs` takes \(O(n\log n)\) time. Memoization computes \(O(n)\) states, and each performs an \(O(\log n)\) binary search, for another \(O(n\log n)\). Total time is \(O(n\log n)\).

The job list, cache, and worst-case recursion stack each use \(O(n)\) space, so auxiliary space is \(O(n)\). The temporary tuples created by `zip` are consumed into the sorted list.

## Alternatives and edge cases

- **Bottom-up suffix DP:** Fill an array from right to left using the same binary-search jump. It keeps \(O(n\log n)\) time and \(O(n)\) space while eliminating recursion-depth risk.
- **Priority queue by end time:** Process jobs by start time and maintain completed schedule profits in a min-heap. It also achieves \(O(n\log n)\) with different invariants.
- **Quadratic predecessor scan:** Search linearly for the next compatible job at every state. This raises time to \(O(n^2)\).
- **Greedy earliest finish:** Correct for maximizing job count, not weighted profit. It can discard a more profitable schedule.
- **Touching intervals:** A job starting exactly at the previous end is compatible because `bisect_left` searches for start greater than or equal to `e`.
- **Equal start times:** Tuple sorting groups them together, and skip branches compare all relevant alternatives.
- **All jobs overlap:** The recurrence chooses the single most profitable job.
- **No jobs overlap:** Taking every positive-profit job is optimal, and the jump moves to the next compatible index.
- **Large timestamps:** Binary search compares integers only; their magnitude does not change complexity.
- **Recursion limit:** A portable implementation for 50,000 jobs should prefer bottom-up DP or explicitly provide a safe stack environment.
- **Required library support:** Standalone code needs `cache` from `functools` and `bisect_left` from `bisect`, and the `key` parameter requires a modern Python version.
