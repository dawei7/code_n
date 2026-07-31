## General

Read `s` from left to right while a stack represents the irreducible result of the prefix already processed. Before adding the next character, only one new removable occurrence can have appeared: the pair formed by the stack's last character and the incoming character.

If that pair is `"AB"` or `"CD"`, pop the stack instead of pushing the new character. This performs the removal immediately. The new stack top is now adjacent to the next unprocessed character, so any later pair exposed by the deletion will be detected in exactly the same way. Otherwise, append the character because it cannot participate as the right endpoint of a currently available removal.

After each input character, the stack contains the fully reduced form of that prefix. A pop applies a permitted operation, while a push retains a character when the only newly possible suffix is not removable. Earlier positions were already irreducible, so no valid pair is missed. At the end, the stack therefore has the same length as a fully reduced string, and its length is the minimum obtainable.

## Complexity detail

Let $n = \lvert s \rvert$. Every character is pushed at most once and popped at most once, so the running time is $O(n)$. The stack can retain all $n$ characters when no removal is possible, requiring $O(n)$ space.

The source caps $n$ at $100$. Across that complete legal range, the runtime harness cannot reliably separate the linear stack from a correct repeated-replacement simulation because process and call overhead dominate. The bounded-domain certificate therefore verifies the one-pass push/pop work and the relevant boundary properties instead of reporting a misleading scaling verdict.

## Alternatives and edge cases

- **Repeated `replace`:** Removing one found pair and restarting is correct, but immutable string searches and copies can make the total work quadratic.
- **Repeated full scans:** Building a new string on each round removes several pairs at once, yet adversarial cascades can still require many rounds.
- **In-place character buffer:** A preallocated array plus a top pointer implements the same stack idea and can reduce allocation overhead without changing the complexity.
- Pair direction matters: `"BA"` and `"DC"` are not removable.
- Removing one pair can expose the other kind, as in `"ACDB"`.
- The final string may be empty, so returning zero is valid.
- Characters other than `A`, `B`, `C`, and `D` are never removed but can separate reducible regions.
