## General

An adjacent swap moves a character by exactly one position. The algorithm constructs matching outer pairs greedily and counts the physical displacement needed to bring each partner to the opposite boundary.

The string is converted to mutable list `cs`. Pointers `i` and `j` describe the left and right positions still being arranged. At each step, the algorithm tries to match `cs[i]` with the rightmost equal character in the active interval.

**Search from the right boundary inward**

The loop examines `k` from `j` down to `i + 1`. The first equal character found is therefore the rightmost available partner for `cs[i]`.

If a match exists at `k`, the inner while-loop swaps it rightward one position at a time until it reaches `j`. This costs exactly `j - k` adjacent swaps.

Afterward, `cs[i] == cs[j]`, so those positions form a correct palindrome pair. The right pointer decreases, the left pointer later increases, and that fixed pair is never disturbed again.

**Why choose the rightmost matching occurrence**

The left-boundary character must eventually be paired with an equal character at the right boundary unless it is the unique center character.

Among all matching occurrences in the active interval, the rightmost one requires the fewest swaps to reach `j`. Choosing an earlier equal occurrence would cross at least as many intervening characters.

Pairing the current leftmost occurrence with the rightmost available equal occurrence also avoids unnecessary crossings between equal-character pairs. An exchange argument can replace any optimal solution's farther-left partner with the rightmost partner without increasing swaps; the characters between them shift no more than before.

Thus the greedy pair can be fixed while preserving the existence of an optimal completion inside the remaining boundaries.

**Realize displacement with actual adjacent swaps**

The assignment

`cs[k], cs[k + 1] = cs[k + 1], cs[k]`

moves the chosen match one step right and shifts the crossed character one step left. Incrementing `k` repeats this until the match occupies `j`.

Each iteration corresponds to one allowed move, so increasing `ans` once per swap gives an exact cost rather than an abstract distance estimate.

The list mutation is important for later searches: all unpaired characters now appear in the relative order produced by those swaps.

**Recognize the unique center character**

If no matching character exists from `i + 1` through `j`, `cs[i]` cannot form an outer pair in the active multiset.

Because the input is guaranteed rearrangeable into a palindrome, at most one character has odd total frequency. In an odd-length palindrome, its unmatched occurrence must occupy the center. For an even-length valid input, this no-match case cannot occur.

The boolean named `even` is set true when a partner is found. Despite its name, it really means “the current boundary character was paired.”

**Charge movement to the center without modifying the list**

When no partner is found, the code adds

`n // 2 - i`

to `ans`. This is the number of adjacent positions from the current left index to the fixed center index `n // 2`.

Conceptually, the unique unmatched character is removed from the active left boundary and moved to the center. The source does not perform those swaps in `cs` and does not decrease `j`; it simply advances `i`.

This shortcut is safe because removing a character from the left of every still-active paired character shifts all of them together by one. Their relative order and their distances to the active right boundary remain unchanged. The unmatched character will never be needed as a partner, so leaving its physical list entry behind the advancing left pointer cannot affect future searches.

For `"ntiin"`, the outer n characters already pair. At the next left position, t has no mate and must become the center, costing one move. The remaining two i characters pair, for total one.

**Why the center distance is unavoidable**

The unmatched character begins at active position `i` and must end at global position `n // 2`. Each adjacent swap changes its index by at most one, so at least `n // 2 - i` swaps involving it are necessary.

Moving it across exactly that many neighboring characters achieves the center placement. The shortcut therefore charges both a lower bound and an achievable cost.

**Why the full greedy count is minimal**

At each paired step, the rightmost equal partner minimizes the necessary displacement to close the current outer pair. Fixing that pair leaves the same problem on a smaller multiset of interior characters.

At the sole unpaired step, the character is forced to the center and the code charges its exact displacement. By applying these arguments repeatedly, every counted local cost is unavoidable and compatible with an optimal arrangement of the remainder.

The process ends when `i >= j`. All outer positions have matching partners, and any single remaining center position needs no partner. The accumulated swaps are sufficient to produce a palindrome and no solution can use fewer.

For `"aabb"`, the first a finds its rightmost partner at index one and moves it two places to the right boundary, producing the necessary outer a pair. The remaining b pair already matches, so the total is two.

## Complexity detail

Let $n$ be the string length. For each left boundary, the backward search may scan $O(n)$ positions, and bubbling a match may also perform $O(n)$ swaps. Across at most $O(n)$ boundary iterations, total time is $O(n^2)$.

The mutable character list contains $n$ entries, so auxiliary space is $O(n)$. All pointers and counters use $O(1)$ additional space. The manifest's $O(n^2)$ time and $O(n)$ space match the exact source.

## Alternatives and edge cases

- **Standard two-ended greedy:** Search for a match to the left character; if none exists, swap that character one step toward the center and retry. It is easier to visualize but may perform center moves explicitly rather than charging them at once.
- **Build a target palindrome then count inversions:** Choose a pairing and use a Fenwick tree to count adjacent swaps. This can improve asymptotic performance but makes correct duplicate pairing more involved.
- **Breadth-first search over strings:** It guarantees a minimum only for tiny inputs; the permutation state space is far too large for length 2000.
- **Already a palindrome:** Every boundary finds its match at `j`, so no swaps are added.
- **Length one:** The loop never runs and the answer is zero.
- **Even length:** Every character frequency is even, so each active left character finds a partner.
- **Odd length:** Exactly one odd-frequency character may require the center shortcut.
- **Repeated equal characters:** Searching from the right chooses the match with minimum boundary displacement.
- **Match already at right boundary:** The bubbling loop performs zero swaps before shrinking both sides.
- **No-match shortcut:** The source counts center movement but intentionally leaves the list unchanged outside the future active left boundary.
- **Palindrome feasibility guarantee:** It rules out two different unmatched character types, which the shortcut would not handle.
- **Adjacent-swap accounting:** Each physical bubble increments `ans` once, exactly matching the allowed operation.
- **Input preservation:** The immutable string remains unchanged; mutations occur in the copied list `cs`.
