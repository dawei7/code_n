## General

**Define a game state by all remaining pile sizes.** Inner `dfs(st)` returns true when the player whose turn it is can force a win from tuple `st`, and false when every legal move gives the opponent a winning state. A tuple is immutable and hashable, so it can serve as the key for `@cache`.

**Generate every legal move.** The tuple is copied to mutable list `lst`. For each pile index `i` with size `x`, inner loop `j = 1..x` considers removing every positive number of stones that does not exceed the pile. `lst[i] -= j` creates that successor state, and `dfs(tuple(lst))` asks whether the opponent can win from it.

After a losing successor for the opponent is found, the current state immediately returns true. If the successor is winning, `lst[i] += j` restores the original pile before trying the next removal. Although `j` changes, each trial begins from the restored original `x`, so the method tests sizes `x-1, x-2, ..., 0` correctly.

**Use the standard winning-state recurrence.** A position is winning if at least one legal move reaches a losing position. It is losing if no such move exists. The condition `if not dfs(...): return True` implements the first rule; falling through every loop and returning false implements the second.

**The empty position is the base case without a branch.** When every pile is zero, every `range(1, x + 1)` is empty. No move can be generated, so DFS reaches `return False`. This matches normal play: the player unable to move loses. States with some zero piles also work because those piles simply contribute no choices.

**Why memoization matters.** Different move sequences can produce the same ordered tuple of remaining sizes. Without caching, the recursive tree repeats those subgames many times. `@cache` evaluates each distinct tuple once and reuses its Boolean result thereafter.

Pile order is retained even though Nim piles are conceptually interchangeable. States like `(1,2)` and `(2,1)` are cached separately, so the implementation does not exploit permutation symmetry. It remains correct but explores more states than a normalized representation would.

**Trace two unit piles.** From `(1,1)`, Alice can only reach `(0,1)` or `(1,0)`. In either state Bob removes the final stone and reaches `(0,0)`, which is losing for the next player. Therefore both of Alice's successors are winning for Bob, and `dfs((1,1))` returns false.

For one pile `(1)`, removing its stone reaches the losing empty state, so the initial call returns true.

**Why the recursion is correct.** The total number of stones strictly decreases on every move, so recursion cannot cycle and eventually reaches the empty base. Assume DFS classifies all smaller-total states correctly. It tests every legal current move and returns true exactly when one leads to a correctly classified losing successor. Otherwise every move lets the opponent win and it returns false. Induction on total stones proves the result.

**The public method preserves input.** It converts `piles` to a tuple and mutates only local list copies inside states. The original list remains unchanged.

## Complexity detail

The exact source is not the manifest's linear-time Nim solution. If pile `i` begins with size $p_i$, there can be up to

$$
\prod_i (p_i+1)
$$

ordered states, because each coordinate ranges from zero to its initial value. Each evaluated state tries up to $\sum_i p_i$ removal choices in a broad bound. Time is therefore $O((\sum p_i)\prod(p_i+1))$, which under $n\le7$ and $p_i\le7$ is exponentially bounded by roughly $O(7n\cdot8^n)$.

The cache can retain the same product number of states, each with an $n$-element tuple, so storage is exponential in $n$ in a generalized analysis. Recursion depth is at most the total number of stones, because every move removes at least one. This differs fundamentally from the manifest's $O(N)$ time and $O(1)$ space labels.

The small original constraints make search possible, but the follow-up's linear goal requires the mathematical XOR theorem described below.

## Alternatives and edge cases

- **Nim-sum theorem:** XOR all pile sizes. The position is winning exactly when the XOR is nonzero, giving $O(n)$ time and $O(1)$ space. This is the true optimal approach but is not what the checked-in source executes.
- **Normalize sorted pile states:** Sorting tuples before caching merges permutations of equal game structure and can reduce search, though it remains exponential.
- **No stones:** The statement starts piles positive, but recursive empty state naturally returns false.
- **One pile:** Any positive pile is winning because the current player removes all stones.
- **Zero pile inside recursion:** It generates no moves and does not need removal from the tuple.
- **Early winning move:** DFS returns immediately without restoring the local list, which is safe because that frame terminates and the list is not shared.
- **Repeated state through different histories:** Cache reuse is valid because only remaining pile sizes and the current turn matter.
- **Recursion depth:** With the stated maximum total of 49 stones, depth is modest. Larger generalized inputs could exceed interpreter limits.
- **Manifest mismatch:** The documentation must not call this recursive state enumeration linear or constant-space; those bounds belong to the XOR alternative.
