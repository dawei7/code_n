## General

**Exploit monotonicity for a fixed ending position.** A substring is valid if at least one character appears $k$ or more times. For a fixed right endpoint, extending its start farther left only adds characters. Thus valid starts form one continuous prefix: if start $p$ is valid, every start smaller than $p$ is also valid.

The source keeps `l` as the boundary immediately after all valid starts. At each right endpoint, the number of valid substrings ending there is therefore `l`.

**Maintain an invalid active suffix.** `cnt` stores frequencies in the current suffix beginning at `l` and ending at the newly processed character. At the end of every iteration, no character in that suffix reaches $k$ occurrences.

When new character `c` arrives, only `cnt[c]` changes. Every other frequency was below $k$ by the invariant and remains so. Therefore `c` is the only character that can make the active suffix valid.

The loop `while cnt[c] >= k` removes characters from the left. If a removed character is unrelated to `c`, its count falls but the active suffix remains valid through `c`. When one occurrence of `c` is finally removed and its count drops below $k$, the loop stops. Now every character count is again below the threshold.

**Why all starts before `l` are valid.** Immediately before the final removal that made the active suffix invalid, that substring contained $k$ copies of `c`. Any earlier start includes that valid substring and possibly more leading characters, so it is also valid. There are `l` such zero-based starts, numbered zero through `l-1`.

Any start at or after `l` creates a substring contained inside the current invalid suffix. Removing more characters cannot increase a frequency, so none of those starts is valid. This proves `ans += l` counts exactly the substrings ending at the current position.

**Why checking just the incoming character is sufficient.** A general “some frequency reaches $k$” problem might seem to require scanning 26 counters after every update. The maintained invalid-suffix invariant removes that need. Before insertion no character qualifies; insertion changes one count; shrinking only decreases counts. The one changed character is the only possible trigger.

**Example boundary movement.** For `"abacb"` with $k=2$, the second `a` makes the active suffix valid. The loop removes from the left through the first `a`, advancing `l` to one. Exactly the start-zero substring ending there is valid. When the final `b` arrives, the boundary advances again, counting the newly valid endings collectively.

**Each substring is counted exactly once.** A substring has one unique right endpoint. During that endpoint's iteration, it is counted precisely when its start lies below the proven boundary. It cannot be counted at any other iteration because those represent different endpoints.

**The nested loop remains linear for version II.** The right endpoint processes each of $n$ characters once. The left pointer never retreats and can advance at most $n$ times over the entire run. The sum of all inner-loop iterations is therefore $O(n)$, not $O(n)$ per outer iteration. This is what makes the method safe for $n=3\cdot10^5$.

When $k=1$, every new character immediately qualifies. Shrinking removes the entire one-character extension until `l` becomes right index plus one. The contribution is then the number of all substrings ending at that index, so the final result is $n(n+1)/2$.

## Complexity detail

Every character is added once and removed at most once. Expected-time `Counter` access makes total time $O(n)$. Only 26 lowercase keys can occur, so counter storage is $O(26)=O(1)$ relative to input length. The other state is scalar.

The answer may be quadratic in $n$ even though computation is linear. Python integers expand as needed; a fixed-width implementation should use a 64-bit integer.

## Alternatives and edge cases

- **Enumerate all start/end pairs:** It costs $O(n^2)$ even with incremental frequency updates and is infeasible for version II.
- **Array of 26 counts:** Direct character indexing removes hashing overhead and retains deterministic constant auxiliary space.
- **Maintain a qualifying-character total:** It is a valid more general design, but the invalid-suffix invariant lets this source observe only `cnt[c]`.
- **`k = 1`:** Every nonempty substring is valid.
- **No character occurs $k$ times globally:** The inner loop never runs and the answer stays zero.
- **Several letters qualify in a larger prefix:** They need not be tracked simultaneously; the algorithm maintains the smallest suffix where none qualifies.
- **Long repeated run:** Each new threshold crossing moves `l` just enough to leave $k-1$ copies in the active suffix.
- **Zero-count keys:** Counter entries may remain at zero, but the fixed alphabet keeps space constant.
- **Large result:** At $n=300000$, the count exceeds 32-bit range by a wide margin.
- **Lowercase-only contract:** It is what turns dictionary storage into $O(1)$ rather than $O(n)$.
- **Version I comparison:** The exact source is identical, but linearity is essential rather than optional under the larger limit.
- **Boundary interpretation:** `l` is the first invalid start, not the first valid start; confusing those meanings causes an off-by-one error.
- **Empty substrings:** None are counted because each candidate ends at an actual processed character and starts no later than it.
