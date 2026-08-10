## General

Each operation removes some elements whose indices and values are both strictly increasing. Because every element must eventually be removed, the problem is equivalent to placing every array element into a group such that, within each group, the original indices increase and the values strictly increase. Each group can then be removed in one operation. The question is therefore: what is the smallest number of strictly increasing subsequences needed to partition the whole array?

**Turn the minimum partition into a maximum obstruction.** Consider any non-increasing subsequence: its values go down or stay equal while its indices move to the right. A strictly increasing removed subsequence can contain at most one member of this non-increasing subsequence. Two of its members cannot be in the same operation, because their values do not strictly increase. Consequently, if the longest non-increasing subsequence has length $L$, at least $L$ operations are unavoidable.

That lower bound is also achievable. A standard chain-partition result says that a sequence can be partitioned into exactly as many strictly increasing subsequences as the length of its longest non-increasing subsequence. There is also an intuitive greedy view: process the numbers from left to right and place each number after a smaller ending value whenever possible; open a new subsequence only when no such ending exists. The number of simultaneously needed subsequences matches the longest non-increasing obstruction. Thus the desired answer is exactly $L$.

The solution computes $L$ with the tails technique used for longest-subsequence problems. The list `g` is kept in non-increasing order. After processing a prefix of `nums`, its length is the maximum non-increasing subsequence length found in that prefix. More precisely, position `k` represents a candidate final value for a non-increasing subsequence of length `k + 1`. These representatives are maintained so that later values have the best possible opportunities to extend them.

**Why the binary-search condition is reversed.** For a new value `x`, the code finds the first position `l` at which `g[l] < x`. Every earlier entry is therefore greater than or equal to `x`. Appending `x` after any such earlier tail respects a non-increasing order, including the equality case. Replacing the first smaller entry by `x` keeps `g` non-increasing and gives that subsequence length a larger tail. A larger tail is more flexible for a future non-increasing extension, because more future values can be less than or equal to it.

The search interval is half-open: initially `l = 0` and `r = len(g)`. At each step, `mid` divides the remaining interval. If `g[mid] < x`, the first smaller entry is at `mid` or somewhere to its left, so `r` becomes `mid`. Otherwise `g[mid] >= x`, that position is allowed before `x` and the sought replacement position must be farther right, so `l` becomes `mid + 1`. When the loop ends, `l` is exactly the first smaller position.

If no entry is smaller, `l == len(g)`. Then all current representative tails are at least `x`, so `x` extends the longest represented non-increasing subsequence and is appended. Otherwise, `g[l]` is replaced by `x`. Replacement does not claim that all values stored in `g` form one literal subsequence. As in the classic tails method, the entries summarize the best tails for different lengths. Only the length of this summary is needed.

For example, process `[5, 3, 1, 4, 2]`. The first three values extend the summary to `[5, 3, 1]`. For `4`, the first smaller entry is `3`, so the summary becomes `[5, 4, 1]`. For `2`, the first smaller entry is `1`, producing `[5, 4, 2]`. Its length is three, agreeing with the three required removals. The representatives changed, but their length continued to record the optimum.

**Why equal values require the right-biased behavior.** A non-increasing subsequence may contain equal values, while each removed subsequence must be strictly increasing. For `[2, 2, 2]`, no operation can remove two elements, so the answer is three. The comparison `g[mid] < x` makes equal entries move the search right and therefore appends all three twos. Searching for the first entry less than or equal to `x` would incorrectly compute a strictly decreasing subsequence and return one.

The lower-bound argument proves that fewer than `len(g)` operations are impossible. The tails update proves that `len(g)` is the longest non-increasing subsequence length, and the sequence-partition equivalence proves that this many strictly increasing removals are sufficient. Returning `len(g)` therefore gives the minimum number of operations.

## Complexity detail

Let $n$ be the number of elements in `nums`. The outer loop processes every element once. At that moment, `g` has at most $n$ entries, and the manual binary search takes $O(\log n)$ time. The total running time is $O(n\log n)$.

The list `g` can grow to $n$ entries, as it does for a non-increasing array, so the auxiliary space usage is $O(n)$. The few indices and the current value use $O(1)$ additional space. The algorithm does not modify `nums`.

The logarithmic search is what makes the method suitable for the constraint $n \le 10^5$. A direct dynamic program that computes the best subsequence ending at every index would compare many pairs and require $O(n^2)$ time, which is too large here.

## Alternatives and edge cases

- **Greedy construction with subsequence endings:** One can explicitly maintain the ending value of every removal group and place each new number after the largest ending value that is strictly smaller. With an ordered multiset this also takes $O(n\log n)$ and directly constructs the partition, but Python has no built-in balanced multiset and the construction is unnecessary when only the count is requested.
- **Quadratic dynamic programming:** Define the longest non-increasing subsequence ending at each position by checking every earlier position. This is easy to derive and useful as a small-input oracle, but $O(n^2)$ time is infeasible for $10^5$ elements.
- **Repeatedly choosing an increasing subsequence:** Actually simulating removals is tempting, but choosing a locally long subsequence does not by itself establish a minimum number of rounds. It also repeats work. The longest non-increasing obstruction gives the exact optimum without constructing any operation.
- **All values strictly increasing:** Every element belongs to one strictly increasing subsequence. Each new value replaces the first smaller tail rather than extending `g`, so the final length is one.
- **All values strictly decreasing:** Every new value extends the non-increasing subsequence. No removal can take more than one element after the preceding larger value, and the algorithm returns $n$.
- **Duplicate values:** Equal elements cannot share a strictly increasing removal. The binary search deliberately treats equality as extendable for the non-increasing subsequence, so duplicates contribute the necessary extra operations.
- **Single element:** The initially empty `g` receives that element, and the answer is one, which is the one operation needed to empty the array.
- **Representative tails are not the removal groups:** Replacing an entry in `g` is safe because `g` is a compact optimization summary. Reading it as a concrete partition can be misleading; the proof depends on subsequence lengths and optimal tails, not on the stored values forming all final groups.
