## General

**View indices as a directed acyclic graph.** Index `j` can precede later index `i` when three conditions hold:

- `j < i`, preserving subsequence order;
- `groups[j] != groups[i]`;
- `words[j]` and `words[i]` have equal length and Hamming distance exactly one.

Draw a directed edge from every compatible earlier `j` to later `i`. All edges point forward, so there is no cycle. The requested subsequence is a longest path in this implicit graph.

**Compatibility helper.** Nested function `check(s, t)` first requires equal lengths. It then zips corresponding characters and sums Boolean comparisons `a != b`. In Python, each true comparison contributes one. The words are compatible exactly when the total is one.

Equal length must be checked separately. `zip` stops at the shorter string, so without the length test two unequal-length words could appear to differ once across only their shared prefix.

**Dynamic-programming meaning.** `f[i]` is the maximum valid subsequence length ending exactly at index `i`. Every single word is a valid length-one subsequence, so all entries start at one. `g[i]` stores the predecessor index used by one optimum ending at `i`, or `-1` when the word starts its chain.

For each current index `i` and every earlier index `j`, the source tests different groups, whether `f[j] + 1` improves `f[i]`, and word compatibility. When all hold, it sets `f[i] = f[j] + 1` and `g[i] = j`.

Appending current word to an optimal chain ending at `j` is legal because only the new adjacent pair needs checking; every earlier adjacency was already validated inside `f[j]`.

**Why the recurrence finds the optimum ending at `i`.** Any valid subsequence ending at `i` either contains only `i` or has some penultimate index `j<i` compatible with `i`. Removing `i` leaves a valid subsequence ending at `j` whose length is at most `f[j]`. Therefore the best possible ending at `i` is one plus the greatest compatible predecessor value. The nested loop examines every such `j`, so it cannot miss the optimum.

**Track the global length.** `mx` starts at one. Whenever a transition improves `f[i]`, the code updates `mx = max(mx, f[i])`. If no transition occurs anywhere, all entries remain one and `mx` correctly remains one.

After DP, the source scans from index zero upward until it finds the first `i` with `f[i] == mx`. Multiple longest endings are allowed, and the problem permits any answer, so stopping at the first one is valid.

**Reconstruct with parent links.** Starting from that ending index, the code appends `words[j]` and repeatedly sets `j = g[j]` until reaching `-1`. This walks the chain backward from last word to first. `ans[::-1]` reverses it into increasing index order.

Each parent is strictly smaller than its child because transitions use only earlier indices. Reconstruction therefore terminates and returns a genuine subsequence.

**Trace the first example conceptually.** `"bab"` at index zero is compatible with both later `"dab"` and `"cab"` by one-character difference and unequal groups. Each later word can form a length-two chain. Since the two later words share group two, neither can legally follow the other. `mx` is two, and the reconstruction returns one of the two valid chains.

**Exact implementation details.** The inner loop is written `enumerate(groups[:i])`. That slice creates a new prefix list on every outer iteration. It is not necessary—`range(i)` would avoid it—but total slice work is $O(n^2)$ and does not exceed the Hamming-check bound. The helper also counts all differences rather than exiting as soon as the second is found.

## Complexity detail

There are $\Theta(n^2)$ ordered index pairs. Checking a pair takes $O(L)$ time for maximum word length $L$, so total time is $O(n^2L)$. The repeated `groups[:i]` slices add $O(n^2)$ copying time, absorbed when $L\ge1$.

Arrays `f` and `g` use $O(n)$ space, reconstruction output uses up to $O(n)$, and the largest temporary group slice uses $O(n)$. Total auxiliary plus output space is $O(n)$. These bounds match the manifest.

## Alternatives and edge cases

- **Early-exit Hamming check:** Stop after finding a second differing character; it improves constants without changing $O(L)$ worst-case time.
- **Use `range(i)`:** Avoid the repeated `groups[:i]` allocations while keeping the same DP.
- **Unequal word lengths:** They are immediately incompatible even if their shared prefix differs once.
- **Hamming distance zero:** Equal words would not be compatible because the required distance is exactly one.
- **Group equality:** Compatible spelling alone is insufficient; adjacent selected group labels must differ.
- **Single input word:** Its length-one chain is returned.
- **Multiple optima:** The first ending with length `mx` and its stored parents provide an allowed arbitrary optimum.
- **Parent reversal:** Backtracking produces reverse order, so the final reversal is required.
- **Character scan counts the full distance:** The exact source sums every unequal aligned pair rather than stopping early. This is still correct: compatibility is accepted only when the final mismatch total is exactly one.
