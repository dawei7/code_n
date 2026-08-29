## General

**Replace two absolute scores with one score difference**

At first, the game appears to require tracking Alice's score, Bob's score, whose turn it is, and every possible sequence of moves. Most of that state is unnecessary. From any remaining suffix, the important quantity is how far the player whose turn it is can finish ahead of the other player.

Define `dfs(i)` as the maximum value of

$$
\text{current player's future score} - \text{other player's future score}
$$

when the first remaining stone is `stoneValue[i]`. The phrase “current player” is deliberate. At `dfs(0)` it means Alice, after Alice moves it means Bob, and after Bob moves it means Alice again. Defining the state by role instead of by name lets the same function describe both players.

A positive value means the player about to move can force a win on that suffix. A negative value means that player must finish behind under optimal play. Zero means both can force the same final score difference.

**Why the next state is subtracted**

Suppose the current player takes stones whose values sum to `s` and leaves the suffix beginning at `j + 1`. On that suffix, the opponent becomes the current player. By definition, `dfs(j + 1)` is how far that opponent can finish ahead during the rest of the game.

From the original player's perspective, the opponent's advantage is a disadvantage. Therefore, the resulting difference is

$$
s - \operatorname{dfs}(j + 1).
$$

This subtraction is the central idea. It automatically models an optimal opponent. There is no separate minimizing function: when roles swap, the opponent maximizes their own difference, and subtracting that best difference gives its effect on the present player.

For example, if taking some stones earns 6 points and the opponent can obtain a future difference of 7, the current move leads to a difference of $6 - 7 = -1$. If the opponent's best future difference is $-4$, subtracting it yields $s + 4$ because the opponent is actually forced to lose that suffix by four points.

**The base case**

The first statement inside `dfs` is:

```python
if i >= len(stoneValue):
    return 0
```

At or beyond the end, no stones remain and neither player can gain more points. Their future score difference is zero. The comparison uses `>=` rather than only equality, making the base case robust even though the loop calls the function at most three positions past a starting index and normally lands no farther than `len(stoneValue)`.

**Trying every legal move**

The current player may take one, two, or three stones, but may not pass and may not go beyond the array. The code initializes `ans = -inf` because stone values may be negative. Starting from zero would be wrong: in a suffix containing only negative stones, every legal move can have a negative outcome, yet the player must choose one.

The local variable `s` starts at zero. The loop visits `j` from `i` through `i + 2`. Each time a valid stone is reached, `s += stoneValue[j]` extends the taken prefix by one stone:

- At `j == i`, `s` is the value of taking one stone.
- At `j == i + 1`, `s` is the sum for taking two stones.
- At `j == i + 2`, `s` is the sum for taking three stones.

If `j` reaches the array length, `break` prevents an invalid move. For every legal choice, `s - dfs(j + 1)` computes the final difference that optimal continuation produces. The assignment

```python
ans = max(ans, s - dfs(j + 1))
```

selects the move most favorable to the current player. This is exactly what “both play optimally” requires at every state.

**Why memoization is essential**

Different move sequences reach the same suffix. For example, taking one stone and then two stones removes the same total number of positions as taking two and then one. Without caching, `dfs(i)` would be recomputed along many branches, producing an exponential recursion tree.

The `@cache` decorator stores the returned value for each index. Once `dfs(5)` has been solved, every later call with argument 5 returns the stored result. The suffix and the player role are fully determined by `i`, so no other cache key is necessary. Absolute accumulated scores do not belong in the state because `dfs` returns only the optimal future difference, which can be combined through subtraction.

**A trace for `[1, 2, 3, 7]`**

Working backward conceptually makes the recurrence concrete:

| State | Best achievable difference for the player to move |
|---|---:|
| `dfs(4)` | 0, because no stones remain |
| `dfs(3)` | 7, by taking the final stone |
| `dfs(2)` | 10, by taking `3 + 7` |
| `dfs(1)` | 12, by taking `2 + 3 + 7` |
| `dfs(0)` | -1, the best of taking one, two, or three stones |

At index zero, the three candidates are `1 - dfs(1) = -11`, `1 + 2 - dfs(2) = -7`, and `1 + 2 + 3 - dfs(3) = -1`. Alice chooses the least harmful result, negative one, by taking three stones. Bob then takes 7 and wins by one point. The DP does not assume that locally taking the largest immediate sum is always right; it evaluates what the opponent can force afterward.

**Converting the difference into the required word**

The outer call `res = dfs(0)` describes Alice's final score minus Bob's final score because Alice moves first. The final conditions translate the sign:

- `res == 0` returns `'Tie'`.
- `res > 0` returns `'Alice'`.
- Otherwise, `res < 0` and the code returns `'Bob'`.

This remains correct with negative stone values. A player may be forced to take a negative stone, and winning means having the numerically greater total, not necessarily a positive total.

**Why the recurrence proves optimal play**

The base state is correct because an empty suffix contributes no score. Assume `dfs(k)` is correct for every index greater than `i`. Every legal first move from `i` takes exactly one, two, or three leading stones and reaches one of those already-defined suffixes. For each move, subtracting the opponent's optimal difference gives the current player's true final difference. Taking the maximum selects the best among all legal moves, so `dfs(i)` is correct. By this backward reasoning, `dfs(0)` gives the outcome of the complete game.

## Complexity detail

Let $n$ be the number of stones. There are $n + 1$ meaningful indices from zero through $n$. Memoization computes each nonempty state once. A state tests at most three moves, and all arithmetic and cache lookups inside a move are constant time. The total running time is therefore $O(n)$.

The cache stores one score difference for each reachable index, which requires $O(n)$ space. The recursive call stack can also become $O(n)$ deep because evaluating the one-stone choice follows `dfs(i + 1)` before returning. Thus the exact top-down implementation uses $O(n)$ auxiliary space, matching the manifest.

The values themselves remain within ordinary bounds: across the whole game, the magnitude of a score difference cannot exceed the sum of the absolute stone values. The complexity depends on the number of positions, not on the magnitudes of those integers.

## Alternatives and edge cases

- **Bottom-up dynamic programming:** Compute the same difference recurrence from right to left in an array. It has $O(n)$ time and $O(n)$ storage, avoids recursive-call overhead, and is safer in environments with a shallow recursion limit.
- **Rolling four-slot DP:** Since a state needs only the next three states, a cyclic array of four values reduces auxiliary storage to $O(1)$. It is asymptotically more space-efficient than this stored Optimal implementation but requires careful modular indexing.
- **Tracking maximum absolute score:** One can compute the best score obtainable from each suffix and compare it with the suffix sum. That formulation works, but the score-difference recurrence expresses the role swap more directly and avoids separately deriving the opponent's share.
- **Naive minimax recursion:** Exploring all one-, two-, and three-stone moves without `@cache` repeats identical suffixes and grows exponentially, so it is unsuitable for as many as $5 \cdot 10^4$ stones.
- **Greedy immediate sum:** Taking the one, two, or three stones with the largest current sum can lose because it ignores which suffix is handed to the opponent. The recurrence explicitly includes the opponent's best response.
- **One remaining stone:** The player must take it. If its value is negative, `dfs(i)` is negative, which is valid and is why `ans` cannot start at zero.
- **Two remaining stones:** The loop considers taking either one or both and stops before a nonexistent third stone.
- **All negative values:** Players still must take stones. The DP chooses the move that makes the player's final difference as large as possible, even if every immediate choice lowers that player's own score.
- **A tie:** The algorithm compares the exact final difference with zero. It does not infer a tie from equal move counts or equal numbers of stones taken.
- **Large input and recursion depth:** The mathematical top-down algorithm has linear depth in the worst case. A Python runtime with its usual small recursion limit may require an adjusted execution environment or the equivalent bottom-up formulation for the maximum constraint; this is an implementation-stack concern, not a change to the recurrence.
