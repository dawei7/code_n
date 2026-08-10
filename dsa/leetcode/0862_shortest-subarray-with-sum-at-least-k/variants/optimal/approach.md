## General

**Express every subarray sum with prefix sums**

Define prefix sum `s[i]` as the sum of the first `i` array values, with `s[0]=0`. Then the subarray from index `j` through `i-1` has:

$$
\operatorname{sum}(j,i)=s[i]-s[j],
$$

and length `i-j`.

We need indices `j<i` satisfying:

$$
s[i]-s[j]\ge k,
$$

while minimizing `i-j`.

Negative input values prevent a normal sliding window: extending or shrinking a window does not change its sum monotonically. A monotonic deque over prefix sums restores the needed structure.

**What the deque stores**

Deque `q` stores candidate prefix indices in:

- increasing index order from front to back;
- strictly increasing prefix-sum order:

$$
s[q[0]]<s[q[1]]<\cdots.
$$

Every stored index might serve as the start of an optimal future subarray.

The loop processes prefix index `i` and value `v=s[i]` from left to right.

**Front rule: remove starts that already make a valid subarray**

If:

`v - s[q[0]] >= k`,

then prefix `q[0]` forms a valid subarray ending at `i-1`. The algorithm updates:

`ans = min(ans, i - q.popleft())`.

It continues while the condition holds, because later deque entries have larger prefix sums but also later indices. Some may still be feasible and yield a shorter length.

**Why a feasible front can be removed forever**

Once `q[0]=j` forms a valid subarray ending at current `i`, any future end `i'>i` using the same start has length `i'-j > i-j`. It cannot improve upon the valid length already considered from `j`.

Therefore, `j` never needs to remain for future iterations.

Processing all feasible fronts also exposes the latest feasible candidate in the increasing-prefix deque, which can give the shortest current ending.

**Back rule: remove dominated starts**

Before appending current index `i`, the code removes back index `j` while:

`s[j] >= v`.

Current index `i` dominates such `j` for every future end `r`:

- `i > j`, so starting at `i` produces a shorter subarray;
- `s[i] <= s[j]`, so `s[r]-s[i] >= s[r]-s[j]`, making the sum at least as large.

If old `j` can form a valid future subarray, current `i` can form one no longer and with no smaller sum. Old `j` can never be uniquely optimal and is safely discarded.

After all dominated backs are removed, appending `i` preserves strictly increasing prefix sums.

**Why the two while loops are ordered this way**

The algorithm first extracts every valid subarray ending at current `i` using earlier starts. Only afterward does it consider current `i` as a start for future subarrays.

This guarantees nonempty subarrays: `i` is never paired with itself at the same iteration. The condition `k>=1` would also prevent zero sum from qualifying, but the ordering makes the index relation explicit.

**Trace `[2,-1,2]` with `k=3`**

Prefix sums are `[0,2,1,3]`.

- Index 0 enters deque.
- At prefix 2, no valid difference reaches 3; index 1 enters.
- At prefix 1, index 1's prefix value 2 is at least 1, so it is dominated and removed. Deque becomes indices for prefix values 0 and 1.
- At prefix 3, difference from front prefix 0 is 3, so length `3-0=3` is recorded and front is removed.

No shorter qualifying subarray exists, so answer is three.

**Why the answer is correct**

The deque discards a prefix index only for one of two proven reasons:

- it already produced its shortest possible future-relevant candidate;
- a later index with no larger prefix sum dominates it.

Thus, no index capable of being the unique start of a better solution is lost.

For every end index, the front-removal loop evaluates all currently feasible nondominated starts. Therefore, the globally shortest qualifying subarray is considered, and `ans` stores its length.

If no qualifying difference is ever found, `ans` remains infinity and the function returns `-1`.

## Complexity detail

Let `n = len(nums)`. Building the `n+1` prefix sums takes `O(n)` time and space.

Each prefix index is appended to the deque once. It can be removed from the front at most once and from the back at most once. Although there are nested while loops, total deque operations across the scan are `O(n)`.

Total time is `O(n)`. Prefix sums and the deque each use `O(n)` space, giving `O(n)` auxiliary space.

## Alternatives and edge cases

- **Ordinary sliding window:** It fails with negative numbers because removing or adding an element need not move the sum predictably.

- **Priority queue of prefix sums:** It can find feasible starts in `O(n\log n)` time, but does not exploit both index and prefix dominance as efficiently.

- **Monotonic stack plus binary search:** Another valid approach, generally `O(n\log n)`.

- **Single qualifying element:** Prefix difference finds length one, the smallest possible answer.

- **No qualifying subarray:** Infinity remains and maps to `-1`.

- **Negative prefix sums:** They are valid and often valuable starts; numeric ordering in the deque handles them.

- **Equal prefix sums:** The earlier index is dominated by the later one and removed through `>=`.

- **Several feasible fronts:** Pop all because later indices may give shorter current subarrays.

- **Future use of a popped feasible start:** It would only create a longer subarray than the one already measured.

- **Prefix index zero:** It represents subarrays beginning at original index zero.

- **Nonempty requirement:** Current prefix is appended only after comparisons with earlier indices.

- **Large sums:** Python integers avoid overflow when accumulating values up to the given bounds.

- **Input immutability:** Prefix sums are built separately; `nums` is unchanged.
