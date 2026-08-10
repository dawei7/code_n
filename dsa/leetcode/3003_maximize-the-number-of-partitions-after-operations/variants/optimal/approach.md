## General

**Simulate the mandatory greedy partitioning**

Once the optional character change is chosen, the partition process is deterministic. A current partition grows while adding the next character keeps its number of distinct letters at most `k`. If adding a letter would exceed `k`, the current partition closes and a new one begins at that character.

The code represents the current partition’s letters with a 26-bit mask `cur`. Bit $j$ means the corresponding lowercase letter is present. `bit_count()` gives the number of distinct letters.

**Define the memoized state**

`dfs(i, cur, t)` returns the maximum number of partitions counted from position `i` onward, including the partition currently represented by `cur`. Parameter `t` is one when the single replacement is still available and zero after it has been consumed.

At the end of the string, the function returns one. That one counts the current final partition. Every time a new character forces a boundary earlier, the transition adds another one.

For the unchanged character, the code forms `v`, its one-bit mask, and `nxt = cur | v`. If `nxt` has more than `k` bits, the current partition must close; recursion restarts with `v` and the result adds one. Otherwise recursion continues with `nxt` and no added partition.

**Try the optional replacement exactly where it can matter**

When `t` is one, the code loops over all 26 possible replacement letters. For each letter $j$, it repeats the same forced-boundary logic with bit `1 << j` and recurses with `t=0`.

Trying the original letter as a “replacement” is harmless. That branch duplicates an unchanged outcome while consuming the option. The separate no-change branch retains the option and is at least as flexible, so the duplicate cannot create an invalid larger result.

Because the operation is “at most one” change, a path may reach the end with `t=1`. No special action is required.

**Why the state contains enough history**

Future greedy choices depend only on:

- the next index;
- which letters are already in the open partition;
- whether replacement remains available.

The exact order of characters inside the current partition and earlier completed partitions cannot affect future boundaries. Therefore, two paths reaching the same tuple have identical optimal continuations, and `@cache` may safely merge them.


Fix any legal decision: either no change, or replace one position with one letter. At each index, the recurrence contains the corresponding character choice. Its mask check exactly implements the required longest-prefix partition rule, so this decision maps to a recursion path with exactly its partition count.

Conversely, every recursion path uses original characters except for at most one transition that changes `t` from one to zero. Its boundary decisions are forced by distinct-count overflow. Thus every path represents a legal changed string and its mandated partitioning.

Taking the maximum over paths yields the optimum.

**Actual state complexity and manifest mismatch**

Let $A=26$. A general state universe contains $N$ positions, two replacement flags, and masks from $0$ through $2^A-1$. A conservative exact bound is $O(NA2^A)$ time because replacement-available states try $A$ letters, and $O(N2^A)$ cache space. With the alphabet fixed, these are linear in $N$ in the formal sense, though reachable states are usually far fewer.

The manifest’s $O(1)$ space label does not describe this source. The cache stores input-dependent states, and recursion alone can be linear in string length.

**A confirmed recursion failure**

The protected solution does not raise Python’s recursion limit. Running it on the legal input `s = "a" * 10000` with `k=26` raises `RecursionError: maximum recursion depth exceeded` before completing the unchanged chain.

This is a genuine full-constraint robustness defect. An iterative rolling-state DP can preserve the same state logic without a call stack, but that is not what the exact source executes.

## Complexity detail

Parameterized by alphabet size $A$, the safe memoized-state bounds are $O(NA2^A)$ time and $O(N2^A)$ auxiliary space, plus $O(N)$ recursion depth. For fixed lowercase $A=26$, time is conventionally described as $O(N)$ with a very large alphabet-dependent constant; actual reachable masks determine practical work.

It is not accurate to call the executable implementation $O(1)$ space. Both cache size and stack depth depend on $N$.

## Alternatives and edge cases

- **Iterative rolling DP:** It avoids the confirmed recursion failure and can discard states from earlier positions.
- **Precompute left/right greedy segments:** The editorial derives an $O(N)$, $O(N)$ enumeration without mask-state recursion.
- **Try every changed string and rescan:** $26N$ full scans cost $O(26N^2)$ and repeat unchanged prefix work.
- **`k = 26`:** No character can force more than 26 distinct letters, so the answer is one; the exact recursion still risks stack overflow for long input.
- **`k = 1`:** Every adjacent character change can strongly affect boundaries, and the state logic remains valid.
- **No replacement used:** The unchanged transition preserves `t` all the way to the end.
- **Replacement with the same letter:** It is redundant but cannot improve beyond the legal no-change branch.
- **Base return one:** It counts the final open partition; split transitions count earlier closures.
- **Manifest space mismatch:** Cache and recursion make auxiliary space input-dependent.
