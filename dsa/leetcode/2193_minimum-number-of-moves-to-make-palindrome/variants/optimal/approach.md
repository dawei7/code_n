## General

**Fix the outermost pair first**

Work on a mutable character array between pointers `left` and `right`. Search
backward from `right` for the rightmost occurrence matching
`characters[left]`. If one exists, bubble that occurrence rightward until it
reaches `right`. Each adjacent swap is counted, and the equal boundary
characters can then be excluded from further work.

Choosing the rightmost available match minimizes the distance needed to fill
the current right boundary. Pairing the left boundary with an earlier equal
character would cross the chosen match or move at least as many intervening
characters. Exchanging those pair choices cannot reduce the remaining cost,
so fixing this closest right-side partner is safe.

**Move the unmatched character toward the center**

If the backward search reaches `left`, the current character has no partner
inside the active interval. Since a palindrome is guaranteed, this is the sole
odd-frequency character and must occupy the center. Swap it one position to
the right, count that move, and retry the same boundaries. Repeating this
slides it inward until another character can form the outer pair.

Every performed swap is necessary either to carry the selected partner across
the characters between it and the right boundary or to carry the unique
center character inward. After fixing a pair, no optimal completion needs to
disturb it. Induction on the shrinking active interval therefore shows that
the accumulated swaps are achievable and minimal.

## Complexity detail

Let $n=\lvert s\rvert$. A boundary step may scan and shift across $O(n)$
characters, and there are $O(n)$ such steps, giving $O(n^2)$ time. The mutable
character array uses $O(n)$ space.

## Alternatives and edge cases

- **Revalidate frequencies after every swap:** Rebuild the complete character
  frequency table after each greedy adjacent swap. It preserves the result
  but adds an unnecessary $O(n)$ scan per swap and can take $O(n^3)$ time.
- **Enumerate palindromic targets:** Generate possible half-string
  permutations and compute the swap distance to each. The number of distinct
  targets can be factorial.
- A length-one string is already a palindrome and needs zero moves.
- An existing palindrome also returns zero without changing its center.
- With odd length, exactly one odd-frequency character must reach the center.
- Repeated equal characters require choosing the rightmost available partner,
  not merely the first match after `left`.
- Only adjacent swaps count; a displacement across $d$ positions costs $d$
  moves.
