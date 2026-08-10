## General

**The game is repeated function application.** From player `i`, one pass moves to `receiver[i]`. After two passes, the ball is at `receiver[receiver[i]]`. The value `k` can be as large as $10^{10}$, so simulating all passes for every possible start would require $O(nk)$ work.

Binary lifting precomputes what happens over blocks whose lengths are powers of two. The binary digits of `k` then combine a logarithmic number of those blocks.

**Define two tables for one block.** Let $2^j$ be a block length.

`f[i][j]` is the player holding the ball after exactly $2^j$ passes starting from player `i`.

`g[i][j]` is the sum of the indices of the first $2^j$ players who touch the ball during that block, starting with `i` but excluding the final holder after all $2^j$ passes.

That exclusion may seem unusual, but it prevents adjacent blocks from double-counting their shared boundary. The final holder is added exactly once after all selected blocks have been processed.

**Initialize a one-pass block.** For $j=0$, the block has $2^0=1$ pass. Starting at `i`, the endpoint is `receiver[i]`, so `f[i][0] = receiver[i]`. The one player included before that endpoint is `i` itself, so `g[i][0] = i`.

For example, a one-pass path $i\to r$ has touched-player score $i+r$. The table stores $i$ in `g` and $r$ in `f`; the caller adds the endpoint later.

**Double a shorter block.** A block of $2^j$ passes is two consecutive blocks of $2^{j-1}$ passes. The first begins at `i` and ends at `f[i][j-1]`. Call that middle player $p$.

The full endpoint is the endpoint of a second half-block beginning at $p$:

`f[i][j] = f[f[i][j - 1]][j - 1]`.

The touched players before the full endpoint consist of the first half's included players plus the second half's included players:

`g[i][j] = g[i][j - 1] + g[f[i][j - 1]][j - 1]`.

The middle player is not double-counted. It is excluded as the first block's endpoint but included as the second block's starting player.

Induction on `j` proves that both table meanings are correct for every power-of-two block.

**Use exactly enough columns.** `m = k.bit_length()` is the number of binary positions needed to represent positive `k`. Therefore, columns zero through `m - 1` cover every power of two that may appear in `k`.

**Evaluate one starting player.** For a candidate start `i`, variable `p` is the current holder after all pass blocks already selected, and `t` is the sum of all players touched before `p`. Initially `p = i` and `t = 0`.

The loop checks every binary position `j`. If bit `j` of `k` is set, the next $2^j$ passes are appended:

- Add `g[p][j]` to `t`.
- Move `p` to `f[p][j]`.

The order from low bits to high bits is valid because function-iteration blocks can be concatenated in any decomposition whose lengths sum to `k`. Each block always starts from the endpoint produced by the previous selected block.

After all set bits, `p` is the holder after exactly `k` passes. `t` contains the preceding `k` touched indices. Adding `p` gives all `k+1` terms required by the score, including the original start and final receiver.

**Why repeated players cause no difficulty.** The tables describe a deterministic walk, not a set of vertices. If the path enters a cycle or a self-loop, the same index may appear repeatedly in `g` sums. This is correct because the score includes repetitions.

**Maximize over starts.** The final outer loop evaluates all $n$ possible starting players and stores the largest `t + p`. Since every legal game is determined completely by its start, this exhaustive start comparison is complete.

**A block-boundary example.** Suppose `k = 5 = 1 + 4`. The source first applies column zero, adding the original start and moving one pass. It then applies column two from that new holder, adding the next four pre-endpoint players and moving four more passes. The final `p` is added once. Exactly six touched players appear, which is correct for five passes.

**The exact space differs from the manifest.** The manifest reports $O(n)$ space, which is possible with more specialized composition or rolling techniques. This source allocates two $n$ by `m` tables. Its actual retained space is $O(n\log k)$.

## Complexity detail

Let $L=\lfloor\log_2 k\rfloor+1$. Filling `f` and `g` performs constant work for every pair of player and bit position, taking $O(nL)=O(n\log k)$ time.

Evaluating all starts also checks $L$ bits for every player, another $O(n\log k)$ time. Total time is $O(n\log k)$.

Each of the two tables stores $nL$ Python integers, so auxiliary space is $O(n\log k)$. This contradicts the manifest's $O(n)$ space claim for the exact implementation. Per-start variables use constant additional space.

Scores can be as large as roughly $(k+1)(n-1)$, which exceeds 32-bit range. Python's arbitrary-precision integers preserve the exact score.

The table construction does not mutate `receiver`.

## Alternatives and edge cases

- **Cycle decomposition for every start:** Functional graphs consist of trees feeding cycles. One can derive long-walk sums through component preprocessing, but handling every start and prefix length is more involved than binary lifting.
- **Rolling doubled blocks:** If queries were organized differently, endpoint and sum arrays for one power could be updated in place, lowering retained space. The exact code keeps all columns because each start later needs every set-bit block.
- **Direct simulation:** It takes $O(nk)$ time and is impossible when `k` reaches $10^{10}$.
- **Self-loop:** Every pass stays at the same player, and binary sums correctly repeat that index `k+1` times.
- **Duplicate receivers:** Many players may merge into one future path; table lookups naturally share the same later states.
- **Cycle shorter than `k`:** No cycle detection is needed because doubling composes repeated traversal algebraically.
- **Final endpoint:** It is excluded from every selected `g` block and added once as `p` after all blocks.
- **Set bits processed low to high:** Endpoint composition, not numeric order alone, ensures the blocks form one continuous walk.
- **`k = 1`:** There is one table column, and the result for start `i` is `i + receiver[i]`.
- **Maximum score start:** Every player is evaluated; a large initial index is not necessarily best because later receivers also contribute.
- **No modulo:** The problem asks for the full integer maximum, so sums remain exact.
