## General

**Track score difference and Bob's previous creature.** Alice's moves are fixed. Bob has three choices each round but may not repeat his immediately previous choice. The memoized state `dfs(i, j, k)` means: process rounds from index $i$ onward when the current score difference is $j=\text{AlicePoints}-\text{BobPoints}$ and Bob's previous creature code is $k$.

Bob wins exactly when the final difference is negative. The initial call uses round zero, difference zero, and previous code `-1` so all three first moves are allowed.

**Encode round outcomes with `calc`.** Mapping `F -> 0`, `W -> 1`, and `E -> 2` represents Alice's creature as `x` and Bob's as `y`. `calc(x,y)` returns the change to Alice-minus-Bob score: zero for equal creatures, one when Alice wins, and negative one when Bob wins.

The special cyclic cases implement Fire over Earth, Water over Fire, and Earth over Water. For example, $x=0$ and $y=2$ means Alice uses Fire against Bob's Earth, so `calc` returns one. Alice Fire against Bob Water falls into the other branch and returns negative one.

**Enumerate only legal next moves.** For each round, the loop tries creature code `l` from zero to two and skips `l == k`. It advances to

`dfs(i + 1, j + calc(d[s[i]], l), l)`.

Changing the last-move component ensures the next round enforces non-repetition. Every legal Bob sequence follows exactly one path through these choices, and no illegal consecutive duplicate is generated.

**Terminal success condition.** When `i >= len(s)`, all rounds have been played. `int(j < 0)` returns one for a Bob victory and zero for a tie or Alice victory. Strict inequality matches “Bob beats Alice.”

**Safe impossibility pruning.** Before the terminal check, the source tests `len(s) - i <= j`. Let $r$ be the remaining rounds. Even if Bob wins every one, the difference can decrease by at most $r$. If $r\le j$, the final difference is at least zero, so strict victory is impossible and the state contributes zero.

This test is also safe at $i=n$. If $j\ge0$, it returns zero immediately. If $j<0$, condition $0\le j$ is false and execution reaches the successful terminal case.

**Memoization controls the exponential tree.** Without `@cache`, there are roughly $3\cdot2^{n-1}$ legal Bob sequences to explore. State outcomes depend only on $i$, difference $j$, and last creature $k$. At round $i$, $j$ lies between $-i$ and $i$, so there are $O(i)$ differences and three previous moves. Summed over all rounds, there are $O(n^2)$ states.

Each state tries at most two legal moves and reduces the running sum modulo $10^9+7$. Therefore cached recursion counts all distinct winning sequences efficiently. `dfs.cache_clear()` releases the function cache before returning; it does not change the already computed `ans`.
At a state, every valid remaining sequence begins with exactly one creature different from $k$, and the loop creates precisely those disjoint first-move groups. `calc` updates the score exactly, and the recursive result counts winning completions of each group. Summing counts all and only legal winning completions. Terminal and prune cases are exact, completing the induction.

**Actual space differs from the manifest.** The manifest describes a rolling $O(n)$ dynamic program. The exact source is top-down memoization and can retain $O(n^2)$ state results. Its recursion depth is $O(n)$; with $n=1000$, it is also close to or beyond ordinary Python recursion limits once decorator frames are considered.

## Complexity detail

There are $O(n^2)$ reachable combinations of round and score difference, with a constant factor for the last creature. Each evaluates at most three candidate codes, so time is $O(n^2)$.

The cache contains $O(n^2)$ entries. Recursion adds $O(n)$ stack frames, dominated asymptotically by the cache. The exact auxiliary-space bound is $O(n^2)$, not the manifest's $O(n)$ rolling-space claim. Clearing the cache at the end lowers retained memory after completion but not peak memory.

## Alternatives and edge cases

- **Rolling bottom-up DP:** Store counts by current difference and last creature for one round at a time. It achieves $O(n^2)$ time and $O(n)$ space, matching the manifest.
- **Full sequence enumeration:** It grows exponentially and is impossible at $n=1000$.
- **No consecutive-repeat rule:** The last-creature state is exactly what enforces it; removing that dimension would overcount invalid sequences.
- **First round:** Previous code `-1` differs from every legal code, so all three choices are permitted.
- **Tie after all rounds:** Difference zero is not a Bob victory and contributes zero.
- **Bob already leads:** A negative intermediate `j` does not guarantee victory; later Alice wins can erase it, so recursion continues.
- **Alice leads by at least remaining rounds:** Even perfect Bob outcomes cannot make the final difference negative, validating the prune.
- **Modulo:** Counts are reduced during every state sum, preventing exponential-size integers while preserving the final residue.
- **Creature cycle:** The numeric codes are not a simple ordinary ordering; `calc` explicitly handles the Fire-Earth wrap.
- **Repeated Alice moves:** They impose no restriction. Only Bob is forbidden from repeating.
- **Cache cleanup:** `cache_clear` is useful because the nested cached function closes over the input string.
- **Recursion depth:** A length-1000 path can exceed standard Python recursion capacity; iterative DP is more robust.
- **Manifest discrepancy:** The exact memoized recursion uses quadratic cache space rather than a linear rolling table.
