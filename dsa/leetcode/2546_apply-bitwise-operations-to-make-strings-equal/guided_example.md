# Guided Example: Apply Bitwise Operations to Make Strings Equal

## 1. The instance we will solve

Take the binary string

- `s = "1010"`, whose set-bit positions are $0$ and $2$;
- `target = "0110"`, whose set-bit positions are $1$ and $2$;

so the common length is $n = 4$. One allowed move picks two **different** indices $i$ and $j$, then replaces

$$
s[i] \leftarrow s[i] \lor s[j], \qquad s[j] \leftarrow s[i] \oplus s[j]
$$

**simultaneously**, meaning the new value of $s[j]$ is computed from the old value of $s[i]$, not from the value just written into $s[i]$. Moves may be applied any number of times, including zero times, and the question is whether `s` can be made equal to `target`. For this instance the answer is **true**.

The instance is worth tracing because it contains a *tempting but wrong* reading of the problem: the two strings hold the same number of ones, which invites a counting argument. It also forces the subtle move where a set bit travels from index $0$ to index $1$, which is where careless reasoning about "one move changes exactly one position" breaks down.

## 2. The complete local algebra of a single move

Write the chosen pair as $(a, b) = (s[i], s[j])$. There are only four possible pairs, so the entire behaviour of a move is contained in this table.

| Old pair $(a, b)$ | New $s[i] = a \lor b$ | New $s[j] = a \oplus b$ | Resulting pair | Pair OR $a \lor b$ before and after |
|---|---|---|---|---|
| `(0, 0)` | `0` | `0` | `(0, 0)` | `0` |
| `(0, 1)` | `1` | `1` | `(1, 1)` | `1` |
| `(1, 0)` | `1` | `1` | `(1, 1)` | `1` |
| `(1, 1)` | `1` | `0` | `(1, 0)` | `1` |

Reading the table column by column gives the two facts that decide the whole problem.

- **The pair's OR is unchanged.** In every row the resulting pair's OR equals the old pair's OR, because $(a \lor b) \lor (a \oplus b) = a \lor b$. A move redistributes the "at least one set bit" property of the pair, but never creates it and never destroys it.
- **A move can add set bits, but it can never remove the last one.** The rows `(0, 1)` and `(1, 0)` turn one set bit into two; the row `(1, 1)` turns two set bits into one; the row `(0, 0)` does nothing at all. In particular, a move applied to a pair of zeros is a no-op: an all-zero string has no move that changes anything.

Note also that the operation is **not** symmetric in the two indices: swapping $i$ and $j$ changes the outcomes, because the OR is written into $i$ and the XOR into $j$.

## 3. The invariant that survives every move

Because each move preserves the OR of exactly the two positions it touches, and leaves every other position literally untouched, the OR of the *entire* string is invariant:

$$
I(s) \;=\; \bigvee_{k=0}^{n-1} s[k]
$$

is the same before and after any move. Since the digits are binary, $I$ takes only the value `0` (the string is all zeros) and the value `1` (the string contains at least one `1`). So the single boolean

$$
\texttt{nonzero}(s) \;\equiv\; \bigl(\exists\, k : s[k] = 1\bigr)
$$

is a genuine invariant of the move system: every string reachable from `s` has the same value of $\texttt{nonzero}$ as `s`. For our instance, both `s = "1010"` and `target = "0110"` contain a `1`, so the invariant does not rule the target out — the trace of Section 5 must show that it is actually reached.

This is also why the rule "count the ones in each string and compare the totals" is the wrong invariant even though it happens to agree on this instance: the count is not preserved. The string `"11"` has two ones, and one move on the pair `(1, 1)` produces `"10"`, which has one.

## 4. The two primitive moves that generate everything else

Two rows of the table in Section 2 are the only tools needed to construct any reachable configuration.

| Primitive | Old pair | New pair | What it accomplishes |
|---|---|---|---|
| Spread | `(0, 1)` or `(1, 0)` | `(1, 1)` | Copies a set bit into a position that held `0`, adding one `1` |
| Erase | `(1, 1)` | `(1, 0)` | Clears one of two set bits, keeping the other as the witness |

A **relocation** is a spread followed by an erase: with $n = 2$, starting from a lone set bit at index $0$, the spread turns `"10"` into `"11"`, and the erase then turns `"11"` into `"01"`. The set bit has moved one position to the right in two moves, and at no point was the string all zeros — the invariant of Section 3 is respected at every intermediate state. This is the mechanism by which individual bit positions are free even though the aggregate OR is frozen.

Both primitives require two *different* indices, which is exactly why the constraint $n \ge 2$ matters. With $n = 1$ there is no legal move at all, and the reachable set from `s` would be only `s` itself.

## 5. Turning `1010` into `0110` step by step

The goal is to clear index $0$ and set index $1$, while leaving index $2$ at `1` and index $3$ at `0`. Index $0$ currently holds the set bit that index $1$ needs, so we relocate it: spread it into index $1$ using the pair `(s[1], s[0]) = (0, 1)`, then erase index $0$ using the pair `(s[1], s[0]) = (1, 1)`.

| Step | Chosen $(i, j)$ | Old pair $(s[i], s[j])$ | New pair | String `s` afterwards | Set-bit positions |
|---|---|---|---|---|---|
| 0 | none | none | none | `1010` | $\{0, 2\}$ |
| 1 | $(1, 0)$ | `(0, 1)` | `(1, 1)` | `1110` | $\{0, 1, 2\}$ |
| 2 | $(1, 0)$ | `(1, 1)` | `(1, 0)` | `0110` | $\{1, 2\}$ |

Verify step 1 against the operation definition with the old pair $(a, b) = $ `(0, 1)`: the new $s[1]$ is $0 \lor 1 = 1$, and the new $s[0]$ is $0 \oplus 1 = 1$. Verify step 2 with the old pair $(a, b) = $ `(1, 1)`: the new $s[1]$ is $1 \lor 1 = 1$, and the new $s[0]$ is $1 \oplus 1 = 0$. The string after step 2 is `0110`, identical to `target`, so the instance is accepted after two moves.

Notice what the trace shows about the roles of $i$ and $j$: in both moves the *surviving* set bit sits at the index used as $i$, and the index used as $j$ is the one rewritten into its final form. Choosing the indices the other way round would write the OR into index $0$ and the XOR into index $1$, producing `1110` and then — because that pair would still be `(1, 1)` — `1100`, which is not the target. Index order is part of the decision, not a detail.

## 6. The decision rule the trace justifies

Combining the invariant with the constructive primitives gives a rule that depends on nothing but the two nonzeroness flags.

| `s` contains a `1`? | `target` contains a `1`? | Reachable? | Reason |
|---|---|---|---|
| yes | yes | `true` | Sufficient: fill every position, then erase the positions the target keeps at `0` |
| no | no | `true` | Both are the all-zero string, and zero moves are allowed |
| no | yes | `false` | The invariant forbids it: an all-zero string can never produce a `1` |
| yes | no | `false` | The invariant forbids it: the last `1` can never be erased |

| Instance | `s` | `target` | Verdict | Deciding fact |
|---|---|---|---|---|
| representative | `1010` | `0110` | `true` | Both nonzero; the trace of Section 5 constructs the target |
| absorbing state | `11` | `00` | `false` | `s` is nonzero and `target` is not |
| zero moves needed | `010101` | `010101` | `true` | Already equal, which is inside the "any number of times" allowance |
| count changes | `00000001` | `11111111` | `true` | One set bit becomes eight; the counts differ while the invariant agrees |
| one set bit travels | `100000` | `000001` | `true` | Spread then erase, exactly as in Section 4 |
| minimum height | `00` | `10` | `false` | An all-zero string cannot gain its first `1` |

## 7. Boundaries and traps

| Trap | What it tempts you to conclude | Correct treatment |
|---|---|---|
| Comparing the number of set bits | `00000001` to `11111111` looks impossible | Counts are not preserved: `(0, 1)` becomes `(1, 1)`, so a count may grow and may shrink |
| Treating the two writes as sequential | You derive a different four-row table, in which `(0, 1)` would map to `(1, 0)` | The statement replaces both entries simultaneously; the new $s[j]$ uses the old $s[i]$ |
| Ignoring the index roles | You assume a move is symmetric in $i$ and $j$ | The OR lands in $i$ and the XOR in $j$; the same pair gives different strings when the roles swap |
| Treating the all-zero string as ordinary | You look for a move that creates the first `1` | Every row of the table except `(0, 0)` needs an existing `1` in the pair, so the all-zero string is absorbing |
| Forgetting that $n$ must be at least $2$ | You assume `"1"` could be rearranged | No move exists with a single index; the constraint $2 \le n$ is what makes nonzero strings mutually reachable |
| Assuming a positive number of moves | You reject an instance in which `s` already equals `target` | "Any number of times" includes zero operations |
| Comparing lengths | You look for a length mismatch to reject | The constraint $n = \text{s.length} = \text{target.length}$ guarantees equal lengths, so length never decides anything |

One instructive near-miss: if the pair rewrite were misread as sequential — write the OR into $s[i]$ first, then compute $s[j]$ from the *updated* $s[i]$ — the four-row table would change, yet $a \lor b$ would still be preserved by both formulas, so the final yes/no rule would coincidentally be the same. The mistake would still surface as a wrong move count in a constructed trace, which is why the simultaneity stated in the problem deserves to be read carefully rather than assumed.

## 8. Why the reasoning is correct

The argument has two directions, and both are needed: rejecting an instance requires an invariant, and accepting one requires a construction.

**Necessity (no unreachable pair is accepted).** For a chosen pair, $(a \lor b) \lor (a \oplus b) = a \lor b$ holds by the absorption and complement laws of Boolean algebra, so every move leaves $I(s) = \bigvee_k s[k]$ unchanged. By induction on the number of moves, every string reachable from `s` satisfies $I(\cdot) = I(s)$. Since $\texttt{nonzero}(s)$ is simply $I(s)$ read as a boolean, a target whose flag differs from that of `s` can never be reached. This covers the false row "`s` nonzero, `target` all zeros" and the false row "`s` all zeros, `target` nonzero".

**Sufficiency (no reachable pair is rejected).** Suppose both strings contain a `1`, and fix a witness index $p$ with `target[p] = 1`. First ensure $s[p] = 1$: if it is not, spread from any index holding a `1` into $p$ in one move. Second, for every index $k$ with $s[k] = 0$, spread from $p$ into $k$; this makes every position `1` and never changes $p$. Third, for every index $k$ with `target[k] = 0`, erase $k$ using the pair $(i, j) = (p, k)$, whose old value is `(1, 1)`: the new $s[p]$ is $1 \lor 1 = 1$ and the new $s[k]$ is $1 \oplus 1 = 0$. The witness $p$ is never the erased index, so it stays `1` throughout and every erase remains legal. The final string holds `1` exactly at the positions where the target holds `1` and `0` exactly where the target holds `0`, so it equals the target. Hence agreement of the two flags is also sufficient.

The construction uses at most $n$ spreads and at most $n$ erases, so it certifies reachability within $2n$ moves; the instance in Section 5 needed only $2$ of them. The invariant of Section 3 is therefore not merely necessary — together with the case in which both strings are all zeros, it is a complete characterisation of reachability, which is why the answer never depends on the arrangement of the bits, only on whether each string has one at all.

## 9. Complexity: time and auxiliary space

**Time.** Reading both strings to evaluate the two flags is a single pass over each, so the worst case is $\Theta(n)$ character inspections; the scan can stop early as soon as one `1` has been found in each string, so a favourable arrangement finishes in $O(1)$ inspections. No move is ever simulated, because Section 8 replaced simulation with an existence proof, so $n$ is never multiplied by the number of moves. With $n \le 10^{5}$ this is trivially within budget.

**Auxiliary space.** The decision needs one boolean per string and a couple of indices, so the extra space is $O(1)$; the two input strings are read-only and are not counted as auxiliary storage. Reporting the decision as a comparison of two flags means no position list, count array, or simulated copy of the target is ever materialised, so the memory cost does not grow with $n$.
