## General

Each active string in `s` represents either one team or an already-formed group whose eventual winner advances. A round pairs the strongest remaining group with the weakest, the second strongest with the second weakest, and so on.

The solution begins:

`s = [str(i + 1) for i in range(n)]`.

So the active entries are team labels `"1"` through `str(n)` in rank order, strongest first.

**Pair symmetric positions.** While more than one active group remains, the loop runs over the first half:

`for i in range(n >> 1)`.

The expression `n >> 1` divides the current active count by two. Because the source guarantees a power of two, every round has an even number of groups until only one remains.

Group `i` is paired with group `n - i - 1`. These are symmetric positions from the beginning and end of the active segment:

- zero pairs with `n - 1`;
- one pairs with `n - 2`;
- and so forth.

The new match string:

`f"({s[i]},{s[n - i - 1]})"`

keeps the stronger-side group on the left and weaker-side group on the right, separated by a comma and enclosed in parentheses.

The new string overwrites `s[i]`. After all pairs in the round are built, the first `n / 2` entries hold the next round's active groups. Entries beyond that prefix are no longer active and are ignored.

Then `n >>= 1` halves the active count for the next round.

**Why overwriting does not destroy a value still needed in the same round.** The loop writes only indices in the first half. It reads opponents from mirrored indices in the second half. These read positions are strictly outside the write range, so a newly constructed left-side match never replaces a right-side source before it is used.

For four teams, the first round creates:

- `s[0] = "(1,4)"`;
- `s[1] = "(2,3)"`.

After halving `n` to two, the next round pairs these two active strings and writes:

`"((1,4),(2,3))"`.

For eight teams, the first active prefix becomes:

`["(1,8)", "(2,7)", "(3,6)", "(4,5)"]`.

The next symmetric pairings are first with fourth and second with third, yielding:

`["((1,8),(4,5))", "((2,7),(3,6))"]`.

The final round joins those groups into the required full bracket.

**What ordering the active prefix represents.** At the start of each round, active groups are ordered according to the strongest original rank that can emerge from them. Pairing symmetric ends applies the same strong-versus-weak strategy recursively. The construction therefore preserves the intended seed separation through every level.

**Why parentheses encode the tournament correctly.** A leaf label represents a team. If `left` and `right` already encode two valid sub-brackets from the same completed number of rounds, then `(left,right)` represents their winners meeting in the next round. By induction, every active string is a valid bracket for its contained teams, and the final one represents the complete contest.

**Why every team appears exactly once.** Initially each label occurs once. Every round concatenates disjoint active group strings in pairs and never copies a group into two matches. Thus the union of labels is preserved without duplication or loss. After the final round, `s[0]` contains all teams exactly once.

The code mutates only the helper list of strings. The numeric parameter `n` is reused as the active length; the original team count is no longer needed after initialization.

## Complexity detail

Let the original team count be $N$. The final string has $O(N\log N)$ characters because each of $N$ labels is nested through $\log N$ rounds and parentheses/commas are added throughout.

Python f-strings copy the full contents of both child strings when forming a parent. In round $r$, the total size copied across active matches is $O(Nr)$. Summing over $\log N$ rounds gives $O(N\log^2 N)$ time, matching the manifest.

The list retains strings from active and inactive positions, and the nested bracket text occupies $O(N\log N)$ characters under the manifest's storage accounting. Temporary construction strings have the same order. The final output itself is necessarily large.

## Alternatives and edge cases

- **Recursive direct writer:** Derive each team's final placement and emit characters into a buffer, potentially avoiding repeated copying.
- **Build explicit tournament nodes:** It makes bracket structure tangible but adds objects when strings already encode the tree.
- **Pair adjacent groups:** This would make strong teams meet too early and violates strongest-versus-weakest pairing.
- **Read and write overlapping halves:** The implementation avoids this by reading all opponents from the untouched second half.
- **`n = 2`:** One round immediately returns `"(1,2)"`.
- **Power-of-two guarantee:** Every round pairs all active groups with no bye handling.
- **Multi-digit labels:** Converting labels with `str` preserves them as whole team identifiers.
- **Active prefix:** Entries beyond current `n` are stale and intentionally ignored.
- **Left-right order:** The smaller rank/stronger group stays on the left side of each generated pair.
- **Final state:** When `n == 1`, `s[0]` is the only active bracket and is returned.
- **Input size up to 4096:** Repeated string copying explains why output-sensitive complexity matters despite few rounds.
