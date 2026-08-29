## General

**A length alone is not enough**

Ordinary longest-increasing-subsequence dynamic programming records the best length ending at each index. This problem also asks how many index subsequences achieve the global best length.

The exact solution stores two parallel states for every endpoint `i`:

- `f[i]`: the length of the longest strictly increasing subsequence ending at index `i`;
- `cnt[i]`: the number of such length-`f[i]` subsequences ending at `i`.

“Ending at `i`” is important. It makes each transition choose a definite final predecessor and prevents counting one subsequence at multiple endpoints.

**Initialize one-element subsequences**

Every individual array element forms a strictly increasing subsequence of length one. There is exactly one such index subsequence ending at that index.

Therefore, both arrays begin filled with ones:

`f[i] = 1` and `cnt[i] = 1`.

These values remain correct for an element that cannot extend any earlier smaller value.

**Try every earlier predecessor**

For each endpoint `i`, the inner loop examines every `j < i`.

If `nums[j] < nums[i]`, any increasing subsequence ending at `j` can append `nums[i]` while remaining strictly increasing. Its candidate length is:

`f[j] + 1`.

The strict comparison excludes equal values. Replacing `<` with `<=` would count non-decreasing subsequences and solve a different problem.

**When a longer ending length is discovered**

If `f[j] + 1 > f[i]`, all previously counted subsequences ending at `i` are shorter than the newly discovered best. They must be discarded.

The code sets:

- `f[i] = f[j] + 1`;
- `cnt[i] = cnt[j]`.

Every best subsequence ending at `j` can append index `i`, so there are exactly `cnt[j]` newly best subsequences through this predecessor.

**When another predecessor ties the best length**

If `f[j] + 1 == f[i]`, this predecessor provides additional longest subsequences ending at `i`. The code adds `cnt[j]` to `cnt[i]`.

These subsequences are distinct from those counted through a different predecessor because their penultimate indices differ. Even if two predecessor values are equal, the index sequences are different and should be counted separately.

If the candidate is shorter than `f[i]`, it cannot contribute to the longest subsequences ending at `i` and is ignored.

**Track the global length and count during the same pass**

After finishing all predecessors for `i`, `f[i]` and `cnt[i]` are final.

`mx` stores the largest endpoint length seen so far, and `ans` stores the total number of subsequences with that length across processed endpoints.

- If `f[i] > mx`, a new global maximum has appeared. Set `mx = f[i]` and replace `ans` with `cnt[i]` because all earlier global candidates are shorter.
- If `f[i] == mx`, add `cnt[i]` because another endpoint contributes distinct globally longest subsequences.

The input is guaranteed nonempty. At index zero, `f[0] = 1 > mx = 0`, so `ans` is assigned before it is ever read.

**A walkthrough**

For `[1, 3, 5, 4, 7]`:

- One has state length one, count one.
- Three extends one, giving length two, count one.
- Five extends three, giving length three, count one.
- Four also extends three, giving length three, count one.
- Seven can extend both five and four. Each predecessor offers candidate length four. The first sets count one; the tie adds another one.

The global longest length is four and its count is two, corresponding to `[1, 3, 5, 7]` and `[1, 3, 4, 7]`.

**All equal values**

For `[2, 2, 2, 2, 2]`, no pair passes the strict predecessor check. Every index keeps `f = 1` and `cnt = 1`. Each endpoint ties the global maximum length one, so `ans` accumulates to five.

This demonstrates that subsequences are identified by indices, not merely by their value sequence.

**Why the dynamic program is correct**

Every increasing subsequence ending at `i` is either the one-element subsequence or has a unique penultimate index `j < i` with `nums[j] < nums[i]`.

By induction, `f[j]` and `cnt[j]` correctly describe all best subsequences ending at every earlier `j`. Comparing candidate lengths finds the maximum possible ending length for `i`. Replacing counts on a strict improvement and adding counts on ties counts exactly all subsequences achieving that maximum.

Every global LIS ends at one unique index. The `mx` and `ans` updates sum counts over exactly the endpoints whose best length equals the maximum. Thus the returned count is correct.

## Complexity detail

Let `N` be the array length.

The outer loop runs `N` times, and index `i` compares against all `i` earlier positions. The total number of comparisons is `N(N - 1) / 2`, so the exact running time is `O(N^2)`.

The two arrays `f` and `cnt` each store `N` integers, giving `O(N)` auxiliary space.

The manifest advertises `O(N log N)` time. That stronger bound requires a Fenwick tree or segment tree over coordinate-compressed values, storing the best length-and-count pair for value ranges. The literal nested-loop source does not implement that structure and is quadratic.

## Alternatives and edge cases

- **Fenwick tree with coordinate compression:** Query all smaller values for the best `(length, count)` pair and update the current value. This achieves `O(N log N)` time and matches the manifest, but merging counts correctly is more advanced.

- **Segment tree:** It supports the same range maximum-and-count aggregation in `O(log N)` per element with more explicit tree storage.

- **Patience sorting tails alone:** It finds LIS length in `O(N log N)` but does not directly retain the number of distinct LISs. Additional counting structure is required.

- **Top-down memoization:** Compute length and count for every endpoint recursively. It has the same `O(N^2)` transition count and adds recursion overhead.

- **All values equal:** Strict inequality prevents extension, so the answer is `N` length-one subsequences.

- **Strictly increasing array:** There is one LIS containing every element.

- **Strictly decreasing array:** Every single element is an LIS of length one, so the answer is `N`.

- **Duplicate predecessor values:** Different indices produce distinct subsequences, and their counts must be added when candidate lengths tie.

- **Continuous versus noncontinuous:** `j` may be any earlier index, not only `i - 1`. This problem counts subsequences, not subarrays.

- **One element:** The first global update sets `ans = 1` and returns one.

- **Negative values:** Only comparisons matter; signs require no special logic.

- **Replacing rather than adding after a longer candidate:** Previously counted shorter subsequences are no longer longest for endpoint `i` and must be discarded.

- **Adding on equal candidate length:** Omitting this step would find the LIS length but undercount alternative index paths.

- **Answer initialization:** The exact source relies on the nonempty-input guarantee so the first iteration initializes `ans`.
