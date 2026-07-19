## General
Convert the string to a mutable character list. Visit only indices `1, 3, 5, ...`, which are exactly the digit positions guaranteed by the contract. For each one, convert its digit character to an integer, add that offset to the character code of the preceding even-indexed letter, and convert the sum back to a character.

Earlier replacements never affect later shifts because every odd index refers to `i - 1`, an even index that is never modified. Each replacement therefore implements its own `shift` independently and exactly once. Even-indexed positions remain untouched, so joining the list yields precisely the required all-letter string.

## Complexity detail
The loop processes half of the $n$ positions and the final join processes all $n$, giving $O(n)$ time. The mutable list and returned string use $O(n)$ space; beyond the output representation, the algorithm uses $O(1)$ auxiliary state.

## Alternatives and edge cases
- **Repeated immutable concatenation:** Appending one character at a time can copy an ever-growing prefix and take $O(n^2)$ time in languages without optimized builders.
- **Mapping every index:** Branching on every character is correct but does unnecessary digit-versus-letter checks when index parity already identifies the role.
- **Zero shift:** Digit `'0'` becomes the same letter as its predecessor.
- **Largest valid shift:** The guarantee permits a result of exactly `'z'` but never beyond it.
- **Odd string length:** The last even-indexed letter has no digit after it and remains unchanged.
- **Single character:** There are no odd indices, so return the original letter.
- **Local dependency:** Each digit uses the immediately preceding even-indexed input letter, not a previously generated odd-index character.
