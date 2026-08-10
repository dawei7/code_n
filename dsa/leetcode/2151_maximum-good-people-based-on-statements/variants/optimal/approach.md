## General

The crucial asymmetry is that every statement made by a good person must be true, while statements made by a bad person impose no constraint at all. A bad person may lie or tell the truth. Therefore the algorithm can guess exactly which people are good and validate only the rows belonging to that guessed set.

With at most 15 people, all subsets can be represented and examined as bitmasks.

**Encode an assignment as a mask**

For a mask `mask`, bit `i` is one when person `i` is assumed good and zero when assumed bad. The expression `mask >> i & 1` extracts that bit.

The outer generator tests masks from `1` through `(1 << n) - 1`. These are all non-empty candidate good sets. The all-bad mask is omitted, but its good-person count would be zero. Every invalid mask also returns zero from `check`, so omitting the all-bad assignment cannot increase or decrease the maximum numeric answer.

Since $n \ge 2$, the range of non-empty masks itself is not empty.

**Ignore statements from assumed bad people**

The helper loops through people `i` and their statement row. It enters the inner validation loop only when `mask >> i & 1` is one.

This is not an optimization that weakens the rules. It exactly reflects the definition: a bad person might make either a true or false statement, so no observation from that row can contradict an assignment. Requiring bad people to lie would be incorrect.

**Validate every informative statement from a good person**

For each entry `x = statements[i][j]`:

- `x == 0` says person `j` is bad;
- `x == 1` says person `j` is good;
- `x == 2` gives no information.

The condition `x < 2` selects only actual claims. For such a claim, `mask >> j & 1` is the assumed status of person `j`. If it differs from `x`, a person assumed good has made a false statement, so the entire mask is impossible and `check` returns zero immediately.

Statements with value two are skipped. The diagonal is always two, but the same logic safely handles every no-statement entry.

**Count a mask only after its row is proven consistent**

The variable `cnt` increases once for each assumed-good person after that person’s entire row has passed. If any later good row creates a contradiction, the function returns zero, discarding the partial count.

If all good-person rows pass, `cnt` equals the number of one bits in the mask and is returned. The outer `max(...)` chooses the greatest count among all consistent assignments.

For a person assumed bad, it does not matter whether their row happens to agree with the mask. This permits the sample scenario where a bad person tells the truth as well as one where a bad person lies.

**Why exhaustive masks prove optimality**

Every possible division of the $n$ people into good and bad corresponds to exactly one bitmask. `check` accepts a mask precisely when every statement made by its good people matches that same mask.

If `check` returns a positive count, all truthfulness requirements are satisfied; bad people’s statements are unrestricted, so the assignment is feasible. Conversely, any feasible assignment appears among the masks, and every one of its good rows passes, so `check` returns its exact number of good people. Taking the maximum therefore returns the greatest feasible count.

**Why propagation is not required**

One could begin with a good person’s statements and propagate forced statuses. The bitmask already supplies a complete proposed status for everyone, so validation reduces each statement to a constant-time equality check. With $n \le 15$, exhaustive complete assignments are simpler and safely bounded.

**Early rejection**

As soon as one good person’s claim disagrees, no later statement can repair that falsehood. Returning zero immediately can make many masks much faster than the worst case, while leaving the worst-case bound unchanged.

## Complexity detail

There are $2^n-1$ tested masks. In the worst case, `check` inspects all $n$ rows and all $n$ entries in each good row, so one mask costs $O(n^2)$. Total worst-case time is $O(2^n n^2)$.

The generator passed to `max` evaluates one mask at a time and does not store all results. `check` uses only scalar loop variables and the existing statement rows. Auxiliary space is $O(1)$, excluding the input.

The integers used as masks need $n$ bits. Under $n \le 15$, shifts and bit counts represented by `cnt` are constant-size operations in this analysis.

## Alternatives and edge cases

- **Backtracking with propagation:** Assign people one by one and propagate statements from those declared good. Contradiction pruning can reduce practical work but requires more mutable state.
- **Precompute row masks:** Encode each person’s good and bad claims into bitsets, then validate a candidate with bitwise operations. This can improve constants while keeping exponential subset enumeration.
- **Assume bad people always lie:** This is wrong; bad people may tell the truth or lie, so their rows must be ignored rather than inverted.
- **All-good mask:** It is valid only if every explicit statement made by every person labels everyone consistently with good status.
- **All-bad assignment:** It is always logically possible because no truth constraints remain. The code omits mask zero, but invalid non-empty checks return zero, so the maximum still correctly can be zero.
- **One assumed-good person:** Only that person’s row constrains the assignment; every assumed-bad row is irrelevant.
- **No-statement value two:** It must never be compared with a status bit. The `x < 2` guard excludes it.
- **Self entries:** They are guaranteed to be two, so no person constrains their own status directly.
- **Mutually supportive people:** If two assumed-good people call each other good, those claims are consistent when both bits are one.
- **Contradictory good rows:** If two assumed-good people give opposite statuses for the same person, at least one comparison fails and rejects the mask.
- **Bad truthful statement:** It has no effect, exactly as allowed by “might tell the truth.”
- **Bad false statement:** It likewise has no effect.
- **Early return value zero:** Zero serves both invalid-mask signaling and the size of the omitted all-bad assignment; only the maximum count is needed, so this ambiguity is harmless.
- **Generator memory:** `max(check(i) for i in ...)` streams results rather than allocating an exponential list.
- **Input preservation:** Validation reads the statement matrix and never changes it.
