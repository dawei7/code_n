## General

**Identify what a swap can never change**

The strings have positions $0,1,2,3$. Requiring $j-i=2$ leaves only two possible swaps: positions $0$ and $2$, or positions $1$ and $3$. Both endpoints of either swap have the same parity. Consequently, characters in even positions can never move to odd positions, and characters in odd positions can never move to even positions.

This proves necessity: if `s1` and `s2` contain different multisets at positions $\{0,2\}$, or different multisets at positions $\{1,3\}$, no sequence of operations can make them equal.

**Show that the parity condition is sufficient**

Each parity class contains only two positions, and the corresponding allowed operation swaps those two positions directly. If the even-position multisets agree, then the even pair is already in target order or one swap places it there. The same independent statement holds for the odd pair. Performing the needed even and odd swaps therefore reaches `s2` whenever both parity multisets agree.

Sort the two even-position characters from each string and compare them, then do the same for the odd-position characters. Both comparisons succeeding is exactly the necessary-and-sufficient condition above.

## Complexity detail

Every legal string has length exactly four. The method extracts and sorts two arrays of two characters from each string, so both its work and temporary storage are bounded by fixed constants: $O(1)$ time and $O(1)$ auxiliary space.

There is no legal scalable input-length axis: a benchmark cannot grow beyond four characters without changing the problem contract. The bounded-domain certificate therefore replaces runtime tiers with a fixed-work proof and boundary cases covering both independent swaps, no swaps, both swaps, repeated characters, and impossible cross-parity movement.

## Alternatives and edge cases

- **Enumerate the four reachable strings:** Apply neither swap, only the even swap, only the odd swap, or both swaps to one input. This is also constant work but describes outcomes less directly than the parity invariant.
- **Frequency maps keyed by parity:** Count each character separately in even and odd positions. This generalizes to longer strings but is unnecessary for two-character groups.
- **Direct conditional comparisons:** Check both possible orders of each parity pair with Boolean expressions. It avoids sorting but is easier to write incorrectly.
- **Zero operations:** Identical strings are already equal and must return `true`.
- **One parity swap:** Either the even pair or the odd pair may need swapping while the other pair remains fixed.
- **Both parity swaps:** The two operations are independent and may both be required.
- **Repeated characters:** Equal characters can make the original and swapped orders indistinguishable; multiset comparison handles this naturally.
- **Cross-parity anagrams:** Having the same four characters overall is insufficient when a character would need to move between an even and an odd index.
