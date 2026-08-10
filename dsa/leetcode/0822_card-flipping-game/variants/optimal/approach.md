## General

**Identify values that can never be good**

A value is good after choosing card orientations when it is face down on at least one card and face up on no card.

Consider a card whose front and back both show the same value `x`. Flipping this card changes which physical side faces up, but the visible number remains `x`. One side showing `x` is always up and the other is always down. Consequently, `x` can never satisfy “not facing up on any card.”

The set comprehension

`s = {a for a, b in zip(fronts, backs) if a == b}`

collects exactly these permanently impossible values. `zip` pairs the front and back belonging to the same card, and the equality filter retains values printed on both sides of one card.

**Why no other value is impossible**

Now take a value `x` that appears somewhere in `fronts` or `backs` but is not in `s`. Every card containing `x` has a different number on its other side, because there is no `x/x` card.

We can choose orientations as follows:

- pick one card containing `x` and orient it so `x` faces down;
- for every other card containing `x`, orient that card so its different side faces up;
- cards that do not contain `x` may be oriented arbitrarily.

After these choices, `x` is down on the selected card and up on no card. Thus, every appearing value outside `s` can be made good.

This proves a complete characterization:

$$
\text{possible good values}
=
(\text{all printed values})\setminus s.
$$

The exact arrangement does not need to be constructed because the function asks only for the smallest possible value.

**Scan both sides for candidates**

`chain(fronts, backs)` iterates through every front value and then every back value without building a concatenated list. The generator keeps only `x not in s`.

A valid good value may initially appear only face up or only face down; either occurrence is enough because cards can be flipped. Therefore, both arrays must be scanned. Restricting candidates to just `backs` would incorrectly depend on the initial orientation.

Duplicate appearances are harmless. `min` returns the smallest numeric value regardless of how many times it occurs.

**Why the minimum expression returns the answer**

The generator contains every value that can be made good and excludes every value that cannot. Taking `min` over it therefore returns the minimum possible good integer.

If the generator is empty, every printed value belongs to the impossible set. The `default=0` argument makes `min` return 0, exactly as required when no good integer exists.

For `fronts = [1,2,4,4,7]` and `backs = [1,3,4,1,3]`, cards `1/1` and `4/4` make 1 and 4 impossible. The remaining printed candidates include 2, 3, and 7, whose minimum is 2. The second card can be flipped so its 2 faces down, while no 2 faces up elsewhere.

For one card `1/1`, set `s` is `{1}`. Both occurrences are filtered out, the generator is empty, and the answer is 0.

**Why local equal-sided cards control a global condition**

The “not face up on any card” condition sounds global, but each card can be oriented independently. For a candidate `x`, the only unavoidable obstruction is a card where both orientations expose `x`. That happens exactly when both sides are `x`.

When every card containing `x` has a different opposite value, each can independently hide `x`. We deliberately leave it down on one of them to satisfy the existence requirement. This independence is why no search over `2^n` flip combinations is necessary.

## Complexity detail

Let `n` be the number of cards. Building the impossible set examines `n` paired sides, taking `O(n)` expected time. The chained candidate scan examines `2n` values, and expected set membership is constant time, so it also takes `O(n)`. Total expected time is `O(n)`.

The set contains at most one value per card, so it uses `O(n)` auxiliary space. `chain` and the generator are lazy and require only `O(1)` iterator state; no combined two-array copy is created.

If value bounds were used, a fixed boolean array could replace the set. The hash-set form stays directly tied to the values that actually occur.

## Alternatives and edge cases

- **Enumerate every flip configuration:** There are `2^n` orientations, which is unnecessary once the equal-sided obstruction is recognized.

- **Try candidates in numeric order and simulate:** It can work, but repeatedly checking cards adds avoidable work. Building the bad set characterizes all candidates in two scans.

- **Look only at initially face-down backs:** Flipping changes which side is down, so a front-only value may still become good. Both arrays belong to the candidate pool.

- **Equal values on different cards:** That alone is not fatal. Only a single card with the value on both sides makes it unavoidable face up.

- **One `x/x` card:** It permanently disqualifies `x` even if other cards could hide their copies of `x`.

- **Candidate appears once:** If its card has a different opposite side, orient the candidate down and it is good.

- **Candidate appears on many cards:** Hide it on all but at least one card; the absence of an equal-sided card makes this possible independently.

- **All values disqualified:** The filtered generator is empty and `default=0` returns the required sentinel.

- **Several valid values:** Numeric `min` chooses the smallest, not the first encountered.

- **Duplicate candidate occurrences:** They do not affect the minimum or require deduplication.

- **No flips needed:** The characterization includes arrangements using zero flips; the algorithm asks what is possible, not how many flips are used.

- **No input mutation:** `zip`, `chain`, and the generator only read the arrays.
