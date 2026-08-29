## General

**Compress all possible jump paths into one frontier**

A direct search could branch from every position to many later positions. That is unnecessary because `nums[i]` is a maximum jump length: from a reachable index `i`, every landing position from `i` through `i + nums[i]` is also permitted. Reachable positions therefore form a continuous prefix of the array.

`mx` is the rightmost index in that known reachable prefix. Initially `mx = 0` because the starting index is reachable without a jump. As the scan processes a reachable index `i`, `i + nums[i]` is the farthest new destination available from it, and `mx = max(mx, i + x)` combines that option with every earlier option.

The algorithm never needs to remember which jump sequence achieved `mx`. Only existence matters, and the prefix property guarantees all indices before the frontier are available for further expansion as well.

**Why the gap test must come before using a position**

At each iteration, `if mx < i` asks whether the current index lies beyond the farthest reachable point established by all earlier reachable positions. If it does, index `i` cannot be used as a launch point. Its jump length is irrelevant because there is no legal way to stand there.

Because the scan moves left to right, failing to reach `i` also means there is a gap before every later index. Forward-only jumps cannot begin on the far side of that gap, so the last index is unreachable and the method can return `False` immediately.

Only after confirming `i <= mx` does the source use `i + x` to extend the frontier. Reversing this order would incorrectly let an unreachable position contribute its jump length.

**The continuous-prefix invariant**

Before processing index `i`, every position at or below `mx` is reachable from index 0, and `mx` is the farthest destination discovered from already processed reachable indices.

The base case holds with the prefix containing only index 0. If `i <= mx`, then `i` is reachable. From it, every landing through `i + nums[i]` is legal because any jump length from zero through the maximum is allowed. Taking the maximum expands or preserves the reachable prefix, so the invariant continues to hold.

If `i > mx`, no processed index can jump far enough to reach it, by the definition of `mx`. Since all possible launch indices before this gap have already been examined, no unexplored path can cross it.

**Trace of a successful input**

For `[2, 3, 1, 1, 4]`, index 0 extends `mx` to 2. Index 1 is inside that prefix and extends it to 4. Every remaining index is then known reachable, including the destination. Later updates do not need to reconstruct the particular successful path; the existence of frontier 4 is sufficient.

**Trace of a blocked input**

For `[3, 2, 1, 0, 4]`, index 0 reaches through index 3. Indices 1 and 2 do not extend beyond 3, and index 3 has jump length zero. When the loop reaches index 4, `mx` is still 3, so the gap test returns false. This captures why every possible path is trapped even though several different early jumps exist.

**Why finishing the scan means success**

If the loop processes every index without finding `mx < i`, then in particular the final index was within the reachable prefix when its iteration began. The function returns `True`. It could return early once `mx >= n - 1`, but continuing remains linear and keeps the implementation simple.

For an array of length one, index 0 is the start and destination. The gap test passes, and the method returns true regardless of its jump length.

## Complexity detail

The scan visits each of the $n$ elements at most once and may stop earlier at the first unreachable gap. Every iteration performs constant-time comparisons and arithmetic, so time is $O(n)$.

Only the frontier, loop index, and current value are stored. There is no queue, visited array, recursion stack, or input slice, so auxiliary space is $O(1)$, matching the manifest. The input list is not modified.

## Alternatives and edge cases

- **Backward greedy goal:** Start with the final index as the goal and move the goal left whenever an index can reach it. If the goal reaches 0, the destination is reachable. It has the same bounds.
- **Boolean dynamic programming:** Mark each index reachable from earlier indices. It is direct but can require $O(n^2)$ time and $O(n)$ space.
- **Breadth-first search:** Treat jumps as edges. Explicitly enumerating every possible landing repeats interval work and needs extra queue/visited storage.
- **Early true return:** Once `mx >= len(nums) - 1`, success is already proven. The selected source instead finishes the scan without changing its asymptotic bound.
- **Single element:** No jump is required, so the result is true even when `nums[0]` is zero.
- **Zero inside a reachable prefix:** It cannot extend the frontier, but another reachable index may already jump past it.
- **Frontier stops before a zero barrier:** The first index beyond `mx` triggers false; unreachable later large values cannot help.
- **Overshooting the array:** A frontier larger than the final index is harmless and proves reachability.
- **Maximum versus exact jump:** Prefix continuity relies on being allowed to choose any shorter jump. If jumps had to use the exact listed length, one scalar frontier would not be sufficient.
- **Input preservation:** The method only reads `nums`.
