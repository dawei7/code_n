## General

Decrementing a non-`a` character makes it smaller, but decrementing `a` wraps it to `z` and makes it larger. Lexicographic order is decided at the first changed position, so skip every leading `a`: including any of them would worsen the string before a later improvement could matter.

Begin the operation at the first non-`a` character. Continue through the entire maximal block of non-`a` characters. Every additional character in that block decreases while the earlier prefix stays fixed, so stopping sooner cannot improve the result. Stop before the next `a`, because wrapping that `a` to `z` would make the otherwise identical result larger. Characters after that boundary are left unchanged because the operation selects one contiguous substring.

If the string contains only `a`, every legal operation introduces at least one `z`. To postpone the first worsening position as far as possible, select only the final character.

## Complexity detail

The scan advances through the leading `a` run and at most one following non-`a` block, touching each character at most once. Converting to and joining a mutable character array also takes $O(n)$ time, so the total is $O(n)$ for $n=\lvert s\rvert$. The mutable output array uses $O(n)$ auxiliary space.

## Alternatives and edge cases

- **Enumerate all substrings:** Applying the operation at every pair of endpoints and comparing results is correct but requires $O(n^2)$ candidates and up to $O(n^3)$ total character work.
- **Decrement every non-a character:** Separate non-`a` blocks cannot all be selected by one contiguous operation without wrapping intervening `a` characters.
- **Always change the first character:** This is wrong when the string begins with `a`, because it creates an early `z`.
- An all-`a` string must still perform an operation, so only its last character should wrap.
- A single non-`a` character is decremented normally; a single `a` becomes `z`.
- The selected block may extend to the end of the string.
- The first internal `a` after the selected block must remain unchanged.
