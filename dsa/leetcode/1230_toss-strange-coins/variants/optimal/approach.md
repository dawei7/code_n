## General
**Track probabilities by the current head count.** Let `dp[h]` be the probability that the coins processed so far have produced exactly `h` heads. Before any toss, `dp[0] = 1` and every positive head count has probability zero. Counts above `target` never need to be stored because later tosses cannot reduce the number of heads.

**Combine the two outcomes of each coin.** For a coin with head probability `p`, ending with `h` heads can happen in two disjoint ways: the previous state already had `h` heads and this coin lands tails, or the previous state had `h - 1` heads and this coin lands heads. Update `dp[h]` to `dp[h] * (1 - p) + dp[h - 1] * p`.

**Update head counts from high to low.** Descending order preserves every previous-layer value until it has supplied all transitions that need it. After updating positive counts, multiply `dp[0]` by `1 - p`, since zero heads remains possible only through another tail.

The two transition cases partition all outcome sequences according to the current coin's result. Induction over the processed coins therefore makes every `dp[h]` the exact probability of `h` heads, and `dp[target]` is the requested value after the final toss.

## Complexity detail
For each of the $n$ coins, at most $t$ positive head-count states are updated, giving $O(nt)$ time. The rolling array contains $t+1$ probabilities, so auxiliary space is $O(t)$.

## Alternatives and edge cases
- **Enumerate every outcome subset:** Summing the probability of each subset with exactly `target` heads is correct but takes $O(2^n)$ time.
- **Two-dimensional dynamic programming:** Storing one row per coin follows the same recurrence but uses $O(nt)$ space.
- **Zero target:** Only the zero-head state is needed, and its value becomes the product of all tail probabilities.
- **Target equal to `n`:** Every coin must land heads, so the result is the product of all head probabilities.
- **Certain coin:** A probability of `1` shifts all probability mass up one head; a probability of `0` leaves head counts unchanged.
- **In-place direction:** Updating from low to high would reuse the current coin and overcount outcomes.
- **Floating-point arithmetic:** The recurrence uses ordinary probability additions and multiplications; no modular reduction applies.
