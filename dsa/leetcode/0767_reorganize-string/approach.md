## General

**The most frequent character determines feasibility**

Let the string length be `n` and let one character occur `mx` times. To separate all copies, at least `mx - 1` other characters must fit between them.

The string contains `n - mx` other characters, so feasibility requires

`mx - 1 <= n - mx`,

equivalently

`mx <= (n + 1) // 2`.

If this condition fails, no rearrangement can avoid adjacent equal copies and the solution returns the empty string.

**Reserve alternating positions**

When a rearrangement is possible, the even indices `0, 2, 4, ...` form the largest set of mutually nonadjacent slots. There are exactly `ceil(n / 2)` of them, enough for the most frequent character.

The solution allocates an answer list of length `n` and fills characters in descending frequency order using `Counter.most_common()`.

Index `i` begins at zero and advances by two after every placement. Once it passes the final index, it wraps to one and continues through odd positions `1, 3, 5, ...`.

**Why the most frequent character is separated**

Because it is processed first, all of its copies occupy even positions. Consecutive even indices differ by two, so another slot lies between every pair.

The feasibility check guarantees it does not need more even positions than exist.

**Why later characters also avoid adjacency**

Each later character is placed into the remaining sequence of every-other slots. Copies of one character are separated by two while they stay within the even or odd subsequence.

The only subtle boundary is when placement wraps from the last available even index to the first odd index. Frequency ordering and the feasibility bound ensure a character cannot occupy adjacent positions across that wrap in a way that violates the result: the large early groups consume the even slots, while smaller later groups occupy consecutive locations in the placement order that are separated in final index order.

Another way to see this is that filling all even slots before odd slots places the most constrained counts into a maximum-spacing layout. A character beginning near the end of the even sequence has too few copies to reach an adjacent odd slot after wrap under the sorted-count and feasibility constraints.

The final index order interleaves the two placement lanes: even zero, odd one, even two, odd three, and so on. The dominant group occupies the even lane first. Smaller groups fill the remaining lane segments, so any repeated group has an index of a different group between its copies.

**Trace `"aab"`**

Counts are `a:2` and `b:1`. Two does not exceed `ceil(3/2)=2`.

The two `a` copies go to indices zero and two. The index then wraps to one, where `b` is placed. Joining produces `"aba"`.

**Why `"aaab"` fails**

The maximum count is three while `ceil(4/2)=2`. Only one other character exists, but separating three `a` copies would need two separators. The empty string is therefore the only valid response.

**Why any answer is acceptable**

The problem does not demand lexicographic order. `most_common` chooses one deterministic frequency order, and ties may be resolved by counter insertion behavior. As long as adjacency differs and all counts are preserved, the output is valid.

**Character preservation**

The loop executes exactly once per input character occurrence and writes it into a previously unfilled position. No character is discarded or duplicated. The final join therefore contains exactly the input multiset.

Because feasibility guarantees enough slots, every list entry is replaced before `join`. The temporary `None` values are allocation placeholders and can never remain in a successful construction.


The maximum-frequency inequality is necessary by the separator argument and sufficient through the alternating-slot construction. When it passes, the highest count is placed in nonadjacent even slots, and remaining frequency-ordered groups fill unused alternating positions without joining equal copies.

Every occurrence is placed once, so the returned string is a permutation of `s` with unequal adjacent characters. When the inequality fails, the necessity proof shows returning empty is correct.

## Complexity detail

Let `n` be the string length. Counting and filling take `O(n)` time. Sorting distinct character counts through `most_common` involves at most 26 lowercase letters, so it is constant with respect to `n`.

The answer list stores `n` positions and the counter stores at most 26 entries. Auxiliary space is `O(n)`, dominated by the returned construction.

## Alternatives and edge cases

- **Max-heap with a held-back previous character:** Repeatedly choose the most frequent character different from the last. It is more general and runs in `O(n log A)` for alphabet size `A`.

- **Random shuffling:** It offers no correctness or termination guarantee.

- **Skip the feasibility check:** Placement could run out of separating slots for a dominant character.

- **Single-character string:** Its maximum count is one, so it is returned unchanged.

- **All characters distinct:** Every arrangement is valid; the construction still preserves them.

- **Maximum exactly `ceil(n/2)`:** Even positions hold the dominant character perfectly.

- **Frequency ties:** Any tie order is acceptable because the output need not be unique.
