## General

**Count compatible pieces instead of removed intervals**

Removing one nonempty contiguous subarray leaves an optional prefix and an optional suffix. Their concatenation is strictly increasing precisely when the retained prefix is strictly increasing, the retained suffix is strictly increasing, and the last prefix value is smaller than the first suffix value whenever both pieces exist.

The $N$ up to $10^5$ constraint rules out enumerating all $O(N^2)$ removals. The exact solution finds all usable increasing prefixes and suffixes with two monotone pointers and counts compatible boundary pairs in bulk.

**Locate the maximal increasing prefix**

Pointer `i` advances from zero while adjacent values satisfy `nums[i] < nums[i + 1]`. Thus positions zero through `i` are strictly increasing, and either `i = n - 1` or the next adjacency is the first failure.

If the whole array is already strictly increasing, removing any nonempty subarray leaves a subsequence of that increasing array, which remains strictly increasing. Every one of the $N(N+1)/2$ nonempty subarrays is valid, so the method returns that formula immediately.

Assume now that the array is not fully increasing. A retained prefix can end at any position from zero through `i`, or be empty. No longer prefix is internally valid.

**First count removals that reach the end**

The initialization `ans = i + 2` counts cases with an empty retained suffix. Choose a retained prefix endpoint $p$ from $-1$ through `i`, where $p=-1$ means no retained prefix. Removing positions $p+1$ through $N-1$ is nonempty and leaves a strictly increasing prefix. There are `i + 2` choices.

This separate initialization makes the later loop responsible only for removals that retain a nonempty suffix.

**Walk through all increasing suffixes**

The suffix pointer `j` begins at `n - 1`. A one-element suffix is strictly increasing. For this fixed suffix start, the bridge condition requires `nums[p] < nums[j]` for a nonempty retained prefix.

Because prefix values increase with $p$, the code moves `i` left while `nums[i] >= nums[j]`. Once the loop ends, every endpoint $p$ from zero through `i` bridges successfully, while every greater endpoint from the original increasing prefix does not. The empty prefix is also valid, so there are `i + 2` compatible choices. Each corresponds to removing the middle interval $[p+1,j-1]$.

After counting the current suffix, the code tests `nums[j - 1] >= nums[j]`. If true, extending the suffix left would make it non-increasing, so the scan stops. Otherwise it decrements `j` and processes the longer increasing suffix.

**Why the removed interval stays nonempty**

In the non-fully-increasing branch, the initial prefix ends before the increasing suffix can merge into an already increasing whole array. The boundary choices counted by the pointer relation leave at least one position between retained pieces to remove. The special fully increasing case was handled separately because there every pair of retained boundaries needs different care to exclude an empty removal.

**Monotonicity makes the scan linear**

As `j` moves left through an increasing suffix, `nums[j]` becomes smaller. The bridge requirement therefore becomes stricter. A prefix endpoint rejected because its value was at least a previous, larger suffix start cannot become acceptable for the new, smaller start. Pointer `i` only moves left and never needs to be restored.

For `nums = [6, 5, 7, 8]`, `i` initially stops at zero and the empty-suffix cases contribute two. Suffix `[8]` accepts the empty prefix and `[6]`, adding two. Suffix `[7,8]` also adds two. Suffix `[5,7,8]` forces `i` to $-1$ because six is not below five, so it adds only the empty-prefix case. The total is seven.

**Why the count is exact**

Every valid removal that reaches the array’s end appears once among the initialized prefix endpoints. Every other valid removal has a unique nonempty retained suffix start `j`. That suffix must be strictly increasing, so `j` is visited. Its retained prefix endpoint must be $-1$ or at most the adjusted `i`, so the corresponding one of `i + 2` choices counts it.

Conversely, each counted choice has an internally increasing prefix, an internally increasing suffix, and a strict bridge. Their concatenation is strictly increasing, so its removed middle is incremovable. Unique prefix/suffix boundaries prevent double counting.

This is the same linear structure as the smaller “I” version, but here it is essential rather than merely an optimization because the input can be much larger.

## Complexity detail

Let $N$ be the length of `nums`. The prefix scan advances `i` at most $N-1$ times. In the second phase, `j` moves left at most $N-1$ times and `i` also moves left at most $N$ total times. Neither pointer oscillates, so the running time is $O(N)$.

Only `i`, `j`, `n`, and `ans` are stored, giving $O(1)$ auxiliary space. The input array is never modified. The count can be $\Theta(N^2)$, but Python integers represent it safely.

## Alternatives and edge cases

- **Enumerate all removals:** There are $O(N^2)$ intervals before even checking whether the remainder is increasing, which is too slow for $N=10^5$.
- **Prefix/suffix arrays plus binary search:** Precomputing validity and binary-searching a bridge can reach $O(N\log N)$ with $O(N)$ space, but monotone pointers achieve $O(N)$ time and $O(1)$ space.
- **Already strictly increasing:** All $N(N+1)/2$ nonempty removals work, including removal of the whole array.
- **Strict equality trap:** Equal adjacent retained values are invalid; `>=` correctly rejects them.
- **Entire array removed:** The remainder is empty and, by the problem’s note, strictly increasing.
- **Empty retained prefix:** This is the $p=-1$ choice and accounts for the extra one in `i + 2`.
- **Empty retained suffix:** These cases are counted in the initial `i + 2`, not the suffix loop.
- **One retained element:** Any one-element remainder is strictly increasing and arises naturally from the boundary counting.
- **Input preservation:** Both pointers only read `nums`.
