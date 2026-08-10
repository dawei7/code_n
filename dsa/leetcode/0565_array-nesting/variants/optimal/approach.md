## General

Because `nums` is a permutation of indices zero through `n - 1`, treating each index `i` as pointing to `nums[i]` creates a directed graph where every node has exactly one outgoing edge and exactly one incoming edge. Such a graph is a collection of disjoint cycles.

The set `s[k]` described by the problem is exactly the cycle reached by repeatedly following those pointers from index `k`.

The solution visits each cycle once and records its length.

Array `vis` marks indices whose cycle has already been explored. The outer loop considers every index `i`. If `vis[i]` is true, that index lies in a cycle counted earlier and can be skipped.

**Start following the new cycle.** For an unvisited `i`:

- `cur = nums[i]` selects the first element required by the definition of `s[i]`;
- `m = 1` counts it;
- `vis[cur] = True` marks that reached index.

The loop continues while `nums[cur] != nums[i]`.

Here, `nums[i]` is the first value in the sequence. When following one more pointer would return to that first value, the cycle is complete and adding it again would create the first duplicate.

Inside the loop, `cur = nums[cur]` advances one pointer, `m` increases, and the newly reached index is marked.

For `nums = [5,4,0,3,1,6,2]` starting with `i = 0`:

- first value is five;
- then `nums[5] = 6`;
- then `nums[6] = 2`;
- then `nums[2] = 0`;
- the next pointer `nums[0]` returns to five.

The four distinct values are counted, so `m = 4`.

**Why a repeat must return to the starting cycle value.** A permutation gives every value exactly one predecessor. While following pointers, encountering any earlier cycle value closes the deterministic cycle. Starting inside that cycle means the closure returns through the same sequence; the chosen condition detects return to its first recorded value.

**Why globally visited cycles can be skipped.** Disjoint permutation cycles cannot merge: if an unvisited path entered a previously visited cycle, one cycle node would have two different incoming indices, contradicting uniqueness of permutation values. Therefore an unvisited start always belongs to a wholly new cycle.

After a cycle length is found, `res = max(res, m)` keeps the longest.

For identity permutation `[0,1,2]`, every index points to itself. Each new cycle initializes length one, its loop condition is immediately false, and the result remains one.

**Why all elements are counted exactly once across searches.** Every index belongs to exactly one cycle. The first outer-loop index from that cycle marks all its members. Later members are skipped. No other cycle shares them.

**Why the value sequence and index sequence align.** Every array value is itself a legal index. The next set element `nums[current]` is exactly the outgoing graph edge. Thus marking `cur` tracks both the produced value and the next position.

The algorithm does not modify `nums`. This differs from in-place marking approaches that overwrite values.

At the beginning of a new outer-loop traversal, none of that cycle's members can be marked. Suppose one were marked earlier. The earlier traversal would have followed deterministic outgoing edges around the complete cycle and marked every member, including the current start `i`; then the outer loop would not have entered this branch. This establishes that initialization at length one never joins a partially processed cycle.

The loop condition can also be understood through the exact set definition. `cur` is the most recently added value. If `nums[cur]` equals the first value `nums[i]`, adding the next value would create the first duplicate, so the algorithm stops immediately before it. Otherwise that next value is new within this cycle and is safe to add and count.

For a two-cycle such as `nums = [1, 0]`, starting at zero records one. Its next value is zero, which is not the first recorded value one, so zero is added and length becomes two. Now the next pointer returns to one and traversal stops. Both outer indices are marked, so the second start is skipped.

## Complexity detail

Let $n$ be the permutation length. Although there is a while loop inside a for loop, each index is marked during exactly one cycle traversal. Total pointer advances across all starts are $O(n)$, and the outer checks are $O(n)$, so time is $O(n)$.

The visited Boolean list uses $O(n)$ space, matching the manifest. Cycle counters and pointers use $O(1)$ additional storage.

No recursion is used, so cycle length does not create call-stack risk.

The answer variable begins at zero, but the nonempty permutation guarantee ensures at least one new cycle is processed and raises it to at least one.

## Alternatives and edge cases

- **Start a fresh traversal from every index:** Without global visited state, the same cycle is walked once per member and can take $O(n^2)$ time.
- **Mark in place:** Add `n` or use another sentinel in `nums` to avoid a visited array, but this mutates the input.
- **Use a set per start:** It detects repetition but allocates and repeats work unnecessarily.
- **Identity permutation:** Every cycle has length one.
- **One large cycle:** The first start marks every index and returns `n`.
- **Several equal-length cycles:** The maximum is unchanged whichever is discovered first.
- **Starting in the middle of a cycle:** It still visits every cycle member before returning.
- **Permutation guarantee:** It ensures disjoint pure cycles with no tails.
- **Visited starting index:** It is skipped because its full cycle was already counted.
- **Input immutability:** Separate `vis` preserves the original permutation.
