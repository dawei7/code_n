## General

**Defining a game state**

The only information that affects future play is the number of stones remaining. The inner function `dfs(i)` answers:

> Does the player whose turn begins with `i` stones have a forced win under optimal play?

This interpretation is independent of whether the current player is Alice or Bob. Both have the same legal moves and both play optimally.

The decorator `@cache` memoizes answers by `i`, so once a state is solved, every later request for it returns the stored Boolean instead of rebuilding the entire game tree.

**The losing base case**

When `i == 0`, no positive square number can be removed. The player to move loses immediately, so `dfs(0)` returns false.

This base case also makes perfect-square starting positions easy. If a player removes all `i` stones, the opponent receives state zero and loses.

**Winning and losing recurrence**

From state `i`, legal moves remove `j * j` stones for every positive `j` satisfying `j * j <= i`.

The current state is winning if at least one legal move sends the opponent to a losing state. That is why the code tests

`if not dfs(i - j * j): return True`.

If every legal square leads to a state where the next player can force a win, the current player has no safe move and `dfs(i)` returns false.

This is the standard optimal-play recurrence:

$$
win(i)
=
\bigvee_{j^2\le i} \neg win(i-j^2).
$$

The loop tries squares in increasing order beginning with one. Returning immediately on the first losing successor avoids examining larger moves once a winning strategy is known.

**Why the recurrence proves optimal play**

Use strong induction on `i`. State zero is losing by the rules. Assume every smaller state is classified correctly.

Every legal move from `i` reaches a smaller nonnegative state, so the inductive answers describe what the opponent can force there. If any successor is losing, the current player chooses that move and wins. If all successors are winning, every possible choice lets the opponent force a win, so the current state is losing.

Thus `dfs(i)` is correct for every state through `n`, and `dfs(n)` answers whether Alice, the initial player, wins.

**How memoization changes the search**

Without caching, different move sequences repeatedly reach the same remaining-stone count, causing an exponential recursion tree. With `@cache`, the body of `dfs(i)` is evaluated at most once per reachable `i`. Later calls reuse its result.

The cached state is only the stone count. No turn bit is necessary because `dfs` always describes the player about to move; changing players is represented by negating the successor result.

The source assumes `cache` is available, normally from `functools`.

This state definition also prevents accidental duplication between otherwise identical Alice-turn and Bob-turn positions.

**A practical recursion-depth limitation**

The loop tries `j = 1` first. On the initial uncached descent, it calls `dfs(n - 1)`, which calls `dfs(n - 2)`, continuing toward zero before results are available. This can create recursion depth proportional to `n`.

Python's common recursion limit is around one thousand, while the constraint allows one hundred thousand. Therefore, the mathematical algorithm and asymptotic bounds are correct, but the exact recursive implementation can raise `RecursionError` on valid large inputs unless the environment raises the limit. An iterative dynamic program avoids this runtime hazard.

## Complexity detail

There are at most $n+1$ cached states. Solving state `i` may test up to $\lfloor\sqrt i\rfloor$ squares. Summing those costs gives

$$
\sum_{i=1}^{n} O(\sqrt i)
=
O(n\sqrt n).
$$

Early returns can reduce actual work, but the worst-case bound remains $O(n\sqrt n)$.

The cache stores one Boolean per solved state, using $O(n)$ space. The recursion stack can also grow to $O(n)$ because the one-square move is tried first. Total auxiliary space is $O(n)$, matching the manifest, though the stack depth is a practical failure risk.

## Alternatives and edge cases

- **Bottom-up dynamic programming:** Fill winning states from zero through n using the same recurrence. It has $O(n\sqrt n)$ time and $O(n)$ space without recursion-limit risk.
- **Propagate from losing states:** Whenever a state is losing, mark states reachable by adding a square as winning. This has the same asymptotic bounds.
- **Uncached recursion:** It repeats states exponentially and is infeasible.
- **n equals one:** Alice removes one square stone and leaves zero, so the result is true.
- **Perfect square:** Alice can remove all stones immediately and win.
- **State zero:** It appears only as a recursive base under the positive-input contract and is losing for the player to move.
- **Only winning successors:** Such a state is losing because every legal move gives the opponent a forced win.
- **First losing successor:** Returning early is safe because one winning move is sufficient.
- **Large n:** The exact recursion order can exceed Python's stack limit; iterative DP is safer.
- **Required import:** `cache` must be supplied from `functools`.
