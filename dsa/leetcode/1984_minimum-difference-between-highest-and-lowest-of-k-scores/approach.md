## General

**Sort so that closeness becomes visible**

The original positions do not matter because any $k$ students may be selected. Sorting the scores in ascending order places numerically close values next to one another.

For any selected group, its objective depends only on its minimum and maximum:

$$
\text{difference}=\text{maximum}-\text{minimum}.
$$

Values chosen between those endpoints do not change the difference. This observation lets the method replace an arbitrary subset search with a scan of fixed-size sorted windows.

**Why some optimal group is consecutive after sorting**

Suppose a selected group of $k$ scores has sorted endpoints `nums[l]` and `nums[r]`. All selected scores lie inside that interval. If the group skips an array value between its endpoints, that skipped value could replace a selected interior value without changing either endpoint.

More directly, an interval containing the $k$ selected values contains at least $k$ sorted positions. Choose any $k$ consecutive positions inside that interval. Their minimum is no smaller than the old minimum and their maximum is no larger than the old maximum, so their difference cannot increase.

Therefore, from every arbitrary optimal selection, one can obtain a consecutive sorted block of $k$ values with an equally good or better difference. It is sufficient to inspect only such blocks.

**Evaluate every fixed-size block**

After `nums.sort()`, a window beginning at index `i` contains positions `i` through `i + k - 1`. Because the array is sorted, its lowest score is `nums[i]` and its highest is `nums[i + k - 1]`. Its difference is

`nums[i + k - 1] - nums[i]`.

The starting index ranges from zero through `len(nums) - k`. The generator expression creates exactly these candidates, and `min` returns the best one.

There is always at least one candidate because the constraints guarantee $1\le k\le N$.

**Trace the example**

For `nums = [9, 4, 1, 7]` and $k=2$, sorting produces `[1, 4, 7, 9]`.

The length-two windows have differences three, three, and two. The last window selects scores seven and nine, so the minimum possible difference is two.

The pair one and nine is not considered as a consecutive window, but it cannot be optimal because including the large gap only makes the objective worse. Sorting exposes this immediately.

**Why a window contains exactly the right information**

The task does not ask for the selected students' identities or their sum. Once a sorted window is fixed, the two endpoints completely determine its score. The $k-2$ interior selections merely ensure that $k$ students are chosen.

Conversely, the consecutive-window argument proves that at least one globally optimal selection appears among the generator's candidates. Taking their minimum can neither exceed the optimum nor produce an impossible value, so it equals the optimum.

**The $k=1$ case**

Every one-element window has the same value as both minimum and maximum. The expression subtracts a score from itself and produces zero. This is the smallest possible difference, and the general code handles it without a special branch.

**Input mutation in the exact source**

`nums.sort()` rearranges the caller-provided list in place. The problem only asks for a numeric result, so this does not affect the computation, but it is an observable side effect. A nonmutating version could use `sorted(nums)` at the cost of an explicit new list.

**Why sorting is justified despite the small constraints**

Enumerating all $\binom{N}{k}$ selections grows rapidly. Sorting costs only $O(N\log N)$ and turns the remaining work into one linear pass. The solution uses numerical ordering to eliminate combinatorial structure rather than attempting to compare subsets individually.

## Complexity detail

Let $N$ be the number of scores. In-place sorting takes $O(N\log N)$ time, and the generator evaluates $N-k+1$ windows in $O(N)$ time. Total time is $O(N\log N)$.

Python's Timsort can use $O(N)$ temporary memory in the worst case, matching the manifest. The generator and scalar indices add only $O(1)$ space. The input list itself is reused and mutated.

## Alternatives and edge cases

- **Enumerate all $k$-subsets:** Correct but combinatorial and unnecessary because only endpoints matter.
- **Heap selection:** Finding some small or large values does not identify the tightest interval of $k$ scores.
- **Counting sort:** Scores are bounded by $10^5$, so a frequency approach is possible, but it spends space on the value range and is less direct.
- **Use `sorted(nums)`:** Preserves input order with the same time bound and an explicit $O(N)$ copy.
- **$k=1$:** Every candidate difference is zero.
- **$k=N$:** There is one window, and the answer is global maximum minus global minimum.
- **Duplicate scores:** A window can have difference zero, which is immediately optimal.
- **Already sorted input:** The logic is unchanged; Timsort may benefit in practice.
- **Large gaps:** Windows crossing a gap are naturally less competitive.
- **Multiple optimal windows:** Only the minimum difference is requested.
- **Nonnegative scores:** Subtraction is straightforward, though the proof would also work for negative scores.
- **Input side effect:** The exact solution leaves `nums` sorted.
