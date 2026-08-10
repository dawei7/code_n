## General

**Compare possible decoded lengths without constructing the original string**

A numeric token represents some number of unknown lowercase characters. The actual characters are not known, so explicitly generating decoded strings would create an enormous search space.

The source instead scans positions in both encoded strings and tracks a signed `balance`:

- a positive balance means `s1` has produced that many unmatched unknown original characters;
- a negative balance means `s2` has produced `-balance` unmatched unknown characters;
- zero means both decoded prefixes currently have equal length.

Only literal letters need character-by-character comparison. Unknown positions merely change or consume the balance.

**Define the memoized state precisely**

`compatible(first, second, balance)` asks whether suffix `s1[first:]` and suffix `s2[second:]` can complete a common original string, given the unmatched decoded-length difference from the prefixes.

The two indices record exactly how much encoded input has been consumed. The balance summarizes all unresolved wildcard characters. No other history affects future compatibility, so this is a complete dynamic-programming state.

`lru_cache` stores each state result and prevents repeated exploration of the same ambiguity.

**Why consecutive digits require branching**

Adjacent digit characters might come from one numeric replacement or several consecutive replacements whose decimal strings were concatenated.

For example, `"123"` may be parsed as 123, as 1 followed by 23, as 12 followed by 3, or as 1, 2, and 3. These interpretations represent different numbers of unknown characters.

When a digit begins at `first`, the source extends `end` through at most three digit positions and incrementally builds `value = value * 10 + digit`. After every digit, it recursively tries consuming that entire prefix as one number and adds `value` to the balance.

The recursive call may parse remaining adjacent digits as another number, so all partitions of a run are covered.

**Parsing digits from the second encoding**

The same process applies at `second` in `s2`, but its unknown length is subtracted:

`balance - value`.

This sign convention maintains

$$
\text{decoded length from }s1-\text{decoded length from }s2.
$$

Digit parsing is attempted on both sides before literal-consumption logic. This is important because either or both current positions may begin an ambiguous numeric token.

**Consume a literal against positive balance**

If `balance > 0`, the decoded prefix from `s1` is ahead by unknown characters. The next literal letter from `s2` can match one of those unknown positions regardless of which lowercase character it is.

The source therefore requires `s2[second]` to exist and be alphabetic, consumes it, and decreases balance by one.

It does not consume a literal from `s1` in this branch, because that would make the already-ahead side even longer rather than resolving the mismatch.

**Consume a literal against negative balance**

When `balance < 0`, `s2` is ahead. A literal from `s1` can match one unknown position from `s2`, so `first` advances and balance increases by one.

Again, the literal character need not be compared with a known character: it is being matched against an unspecified position represented by a number.

**Compare letters only at equal decoded length**

When balance is zero, neither side has unmatched wildcard positions. If the current characters are letters, they represent the same next original-string position and must be equal.

The final return expression verifies that both indices exist, both characters are alphabetic, and the letters match before advancing both indices.

Different letters at balance zero prove incompatibility for that branch.

**Finish only with equal total decoded length**

If both encoded indices reach their ends, compatibility requires `balance == 0`. A nonzero balance means one encoding still represents unmatched original characters even though neither has input left to cover them.

If only one encoded string ends, recursion may still succeed by parsing numbers or consuming letters from the other side against an existing balance. The ordinary transitions handle this without a separate one-ended base case.

**Trace `"internationalization"` and `"i18n"`**

The initial `i` letters match at balance zero. Parsing 18 from the second string changes balance to negative eighteen, meaning `s2` represents eighteen unknown positions ahead.

The source consumes the next eighteen literal letters from the first string, raising balance one step at a time to zero. The final `n` letters then match directly, and both inputs finish with zero balance.

**Why the search is correct**

Every numeric-loop choice corresponds to one legal grouping of consecutive encoded digits. Balance updates record exactly how many unknown positions that grouping contributes.

Positive and negative balance branches consume only the lagging side's literal against those unknown positions. At zero, known letters must agree. Thus every successful recursive path describes a consistent common original string.

Conversely, any common original string induces some grouping of each digit run and a sequence of wildcard-versus-letter or letter-versus-letter matches. The recursion includes each such choice, so a valid interpretation cannot be missed.

## Complexity detail

Let $N_1$ and $N_2$ be encoded lengths, and let $B$ be the number of reachable signed balance values. There are at most $O(N_1N_2B)$ cached states. Each state tries only a constant number of digit prefixes because runs are capped at three, plus one literal transition.

Time and cache space are therefore $O(N_1N_2B)$. Recursion depth is bounded by the amount of encoded input consumed plus wildcard balance consumption, and remains within the finite state bound.

## Alternatives and edge cases

- **Breadth-first state search:** Explore the same index-index-balance graph iteratively and avoid recursion.
- **Materialize wildcard strings:** Infeasible because numeric tokens may represent hundreds of unknown characters with many possible contents.
- **One-, two-, or three-digit grouping:** Every prefix length must be tried; choosing only the largest number misses valid encodings.
- **Adjacent numeric replacements:** Recursive re-entry on remaining digits covers partitions such as 1 plus 23.
- **Positive balance:** Only a literal from `s2` can consume one unmatched position.
- **Negative balance:** Only a literal from `s1` can consume one unmatched position.
- **Zero balance with different letters:** That branch fails immediately.
- **Both inputs exhausted:** Success requires zero balance.
- **One input exhausted:** May still match an outstanding balance through the other suffix.
- **Digits 1–9 only:** Numeric tokens never contain leading zero.
- **Three-digit-run guarantee:** Bounds branching and numeric-prefix length.
- **Input preservation:** Both strings are immutable and only indices are advanced.
