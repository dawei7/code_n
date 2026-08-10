## General

**Model letters as a directed weighted graph**

Each lowercase English letter is a node. A rule saying that character `x` may become character `y` for cost `z` is a directed edge from `x` to `y` with weight `z`. Direction matters: permission to change `'a'` into `'b'` does not automatically permit the reverse change.

A position may undergo any number of operations. Therefore, the cheapest way to turn one letter into another is not necessarily a direct rule. It may be a path through intermediate letters. If `a -> c` costs one and `c -> b` costs two, then `a` can become `b` for three even when there is no direct `a -> b` rule.

The code converts a character to an integer from zero through 25 with `ord(character) - ord('a')`. It creates a $26 \times 26$ matrix `g`, initially filled with infinity. Entry `g[x][y]` means the smallest conversion cost currently known from letter $x$ to letter $y$.

**Initialize the direct possibilities carefully**

Every letter can remain itself for zero cost, so the diagonal is set with `g[i][i] = 0`. For every supplied rule, the code executes `g[x][y] = min(g[x][y], z)`.

The minimum is important because the description explicitly allows duplicate source/destination rule pairs. If one rule converts `a` to `b` for ten and another does so for three, retaining whichever rule appeared last would be unsafe. Keeping three is always at least as good in every future path.

**Compute every cheapest letter-to-letter route**

Floyd–Warshall considers each of the 26 letters as a possible intermediate. When processing intermediate $k$, it updates every ordered pair $(i,j)$ by comparing:

- the best route from $i$ to $j$ already known, and
- the route from $i$ to $k$, followed by the route from $k$ to $j$.

The update is `g[i][j] = min(g[i][j], g[i][k] + g[k][j])`. After intermediate letters zero through $k$ have been processed, `g[i][j]` is the least cost of a path whose internal nodes come from that processed set. This invariant starts with direct edges and zero-length diagonal routes. Adding one possible intermediate preserves it by dividing every newly allowed route at $k$. Once all 26 letters have served as intermediates, every possible conversion chain has been considered.

All costs are positive, so there are no negative cycles or incentives to repeat a cycle. Infinity behaves safely in the arithmetic: an unreachable partial path plus any finite cost remains infinity.

**Why positions can be optimized independently**

An operation changes one selected character, not every occurrence of that character in the string. Operations at one index do not alter the letter or available choices at another index. Consequently, a complete conversion is just the sum of independent cheapest conversions for corresponding positions.

The final loop zips `source` with `target`. When the characters already match, no operation is needed and the code skips the lookup. Otherwise it converts both letters to indices and reads `g[x][y]`. If this value is still infinite, no rule chain reaches the required target letter, so the whole string conversion is impossible and the method immediately returns `-1`. If it is finite, the cost is added to `ans`.

For example, suppose a source position contains `'a'` and the target contains `'d'`. Direct `a -> d` may cost 20, while `a -> b -> c -> d` costs $2+3+4=9$. Floyd–Warshall stores nine, and the string scan uses that value. A different occurrence of `'a'` pays nine separately because operations select positions independently.

**Why summing these values is globally optimal**

For every mismatching position, any successful full conversion must perform some valid path from its source letter to its target letter. Its cost is at least the shortest-path value in `g`. Summing these per-position lower bounds gives a lower bound for every complete strategy.

Conversely, execute a shortest conversion path independently at every mismatching position. These operations are all permitted, do not interfere, and achieve exactly the sum stored by the algorithm. The lower bound is therefore attainable, making the sum globally minimal.

If one position is unreachable, no amount of work at other positions can repair it, which proves the early `-1` return.

## Complexity detail

Let $N$ be the common string length, $K$ the number of conversion rules, and $A=26$ the alphabet size. Matrix initialization costs $O(A^2)$. Loading rules costs $O(K)$. Floyd–Warshall costs $O(A^3)$, and the final position scan costs $O(N)$. The full bound is $O(N+K+A^3)$.

The matrix uses $O(A^2)$ auxiliary space. Since $A$ is fixed at 26, this is constant with respect to $N$ and $K$, but keeping $A$ explicit explains the algorithm. The string scan uses constant additional state, and neither input string nor rule array is modified.

## Alternatives and edge cases

- **Run Dijkstra only when a pair is needed:** Positive weights permit Dijkstra, but with only 26 nodes, one Floyd–Warshall pass is simpler and makes every later lookup constant time.
- **Use only direct rules:** This misses cheaper or uniquely possible multi-step conversions through intermediate letters.
- **Treat rules as undirected:** Conversions are directional. Adding reverse edges would invent operations not present in the input.
- **Duplicate rules:** The matrix must keep the cheapest direct edge before shortest paths are computed.
- **Matching characters:** Their cost is zero even if no explicit self-conversion rule exists; the diagonal and final skip both express this.
- **Unreachable position:** A single infinite lookup makes the entire conversion impossible, so returning `-1` immediately is correct.
- **Repeated character pairs:** Their shortest cost is computed once in `g` but added once per position, because each occurrence needs its own operations.
- **Large total cost:** The sum can exceed a 32-bit integer; Python integers represent it safely.
- **Input preservation:** The algorithm builds a separate matrix and only reads all supplied sequences.
