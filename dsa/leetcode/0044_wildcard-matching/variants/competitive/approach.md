## General

**Match greedily until a star provides flexibility**

Pointers `s_ptr` and `p_ptr` identify the next unmatched input character and pattern token. A literal equal to the input character, or a `'?'`, consumes exactly one character from each side. Those matches are forced, so both pointers advance.

When the current pattern token is `'*'`, the algorithm initially lets it match an empty sequence. It advances `p_ptr` past the star and remembers two restart positions. `last_p_ptr` is the pattern position immediately after that star, and `last_s_ptr` is the input position at which the star's current matched sequence ends. At first that end equals `s_ptr`, representing zero consumed characters.

This choice is greedy in the sense of trying the shortest star match first. If the following pattern later fails, the stored star is expanded one character at a time until the suffix matches or the input is exhausted.

**Recovering from a mismatch**

A mismatch occurs when the current tokens do not match, the current pattern token is not a star, or the pattern has ended while input remains. If a prior star exists, `last_p_ptr != -1` permits recovery.

The code increments `last_s_ptr`, assigning one additional input character to the remembered star. It resets `s_ptr` to that new endpoint and resets `p_ptr` to the token just after the star. The pattern suffix is then tried again against the shorter remaining input suffix.

For example, with a pattern like `"*ab"`, the first attempt makes `'*'` empty and tries `"ab"` at the start of the string. If that fails, the star absorbs the first input character and `"ab"` is retried one position later. This continues until a full suffix match is found or no input remains.

If no previous star exists, a mismatch cannot be repaired. Literals and `'?'` have fixed width, and no token is available to absorb or release characters, so the method returns false.

**Why remembering only the latest star works**

When another star is encountered, its restart positions replace those of an earlier star. Everything before the new star has already been matched successfully. If the later suffix fails, varying the most recent star is sufficient to change the division between that star and the suffix; revisiting an earlier star would only shift a prefix that the newer star can absorb as part of its arbitrary sequence.

The algorithm therefore stores one star checkpoint rather than a stack of all stars. This is the source of its constant auxiliary space.

**Finishing after the input is consumed**

The main loop stops when `s_ptr == len(s)`. Pattern tokens may remain. Only trailing stars can match an empty input suffix, so the second loop skips consecutive `'*'` tokens. The final comparison `p_ptr == len(p)` returns true only if the whole pattern is then exhausted. Any remaining literal or `'?'` makes the result false.

This final step also handles an empty input: the main loop never runs, and a pattern made entirely of stars is accepted after being skipped.

**The role of `count` and its assertions**

`count` does not participate in matching decisions. It records iterations for a complexity safety check. Before a false return and before the final result, the source asserts that the count did not exceed `(len(p)+1) * (len(s)+1)`. This bound corresponds to the finite grid of pointer relationships that backtracking can explore.

Assertions can be disabled in optimized Python execution, but removing them would not change the matching result. They are diagnostic guards, not algorithmic state.

**Why the greedy recovery is correct**

Before any remembered star, literal and `'?'` matches are forced. At a star, trying zero characters first cannot lose a solution because every longer choice is preserved by the checkpoint. Each mismatch expands that same star by exactly one character and retries the entire following pattern suffix. Hence all relevant star lengths are considered in increasing order.

If a full match exists using the remembered star, one of those lengths aligns the suffix correctly and the forward scan reaches the end. If every possible length fails, input becomes exhausted and the trailing-pattern check rejects any mandatory tokens. The algorithm accepts only after both input and pattern are completely accounted for, so partial matches cannot produce true.

**Selected source versus the extra classes**

The file also defines rolling DP, full-table DP, and slow recursive implementations as `Solution2`, `Solution3`, and `Solution4`. The harness selects the class named `Solution`, which is the greedy constant-state algorithm. Those additional classes do not run as part of this method.

## Complexity detail

Forward pointer motion is often close to $O(n+m)$, but after a star expands, `p_ptr` resets and can rescan a pattern suffix. In the worst case, a suffix of length proportional to $m$ may be retried for many input positions, giving $O(nm)$ time. This conservative bound matches both the manifest and the source's assertion ceiling. Describing the method as unconditionally linear would ignore those repeated suffix scans.

The selected `Solution` stores four pointers, one counter, and a few temporary comparisons. It allocates no table, stack, or substring copies, so auxiliary space is $O(1)$. This is stronger than the manifest's $O(m)$ allowance. The input strings are immutable and are not modified.

## Alternatives and edge cases

- **Rolling dynamic programming:** Track prefix-match states using two rows. It gives a straightforward $O(nm)$ guarantee and $O(m)$ space, at the cost of visiting the full state grid even when greedy matching finishes quickly.
- **Memoized recursion:** Define a state by string and pattern indices and cache star choices. It is direct and provably $O(nm)$ time, but can store $O(nm)$ states and use a deep call stack.
- **Collapse consecutive stars:** Replacing each run of stars with one star preserves semantics and can reduce redundant checkpoints and scans. The selected source remains correct without preprocessing.
- **No star and a mismatch:** There is no flexible checkpoint, so false is returned immediately.
- **Star matches empty:** Advancing `p_ptr` when the star is first seen explicitly tries this required possibility.
- **Star matches the whole remaining string:** Repeated recovery increments `last_s_ptr` until all remaining input has been assigned to it.
- **Trailing stars:** They are skipped after input exhaustion because each can represent an empty sequence.
- **Trailing literal or `?`:** It cannot match empty input, so the final pointer equality is false.
- **Both inputs empty:** Both loops are skipped and the equal end pointers produce true.
- **Consecutive stars:** Each new star updates the checkpoint. They remain equivalent to one arbitrary-sequence wildcard.
- **Diagnostic counter:** The assertions may raise only if the traversal exceeds the intended state bound; `count` does not make a failed match succeed or a successful one fail under normal operation.
