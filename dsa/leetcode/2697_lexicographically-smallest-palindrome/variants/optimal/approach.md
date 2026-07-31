## General

Every position belongs to exactly one mirrored pair, except for the middle character of an odd-length string. A palindrome requires the two characters in each pair to be equal, and choices made for one pair cannot affect any other pair.

**Minimum replacements for one pair**

If the two letters already match, changing either one would waste an operation, so keep both. If they differ, at least one replacement is necessary. One replacement is also sufficient by copying either endpoint onto the other, so every minimum-operation result uses exactly one of the pair's original letters.

**Lexicographically smallest minimum result**

For a differing pair, copy the smaller letter to both positions. Choosing the larger letter would use the same one operation but would make the result larger at the pair's left position, which is encountered before its mirrored right position in lexicographic comparison. A third letter cannot improve the answer within the minimum-operation budget because making both endpoints equal to a third value would require two replacements.

Use two pointers at the first and last characters. Resolve their pair as above, then move both pointers inward until they meet or cross. Each pair is assigned its unique smallest choice among all minimum-operation possibilities, so the completed string is both a palindrome and the lexicographically smallest result with the minimum number of replacements.

## Complexity detail

Let $n = \lvert s \rvert$. Copying the immutable input into a mutable character list, visiting each mirrored pair once, and joining the result take $O(n)$ time. The character list contains $n$ entries, so the implementation uses $O(n)$ auxiliary space.

## Alternatives and edge cases

- **Build a separate result from both ends:** Appending the chosen character to left and right buffers is also linear, but joining and reversing the buffers adds bookkeeping without improving the bound.
- **Repeated immutable slicing:** Reconstructing the entire string after each unequal pair is correct, but it can take $O(n^2)$ time because every replacement copies $O(n)$ characters.
- **Copy the larger letter:** This preserves the minimum operation count but fails the lexicographic tie-break.
- A one-character string needs no replacement, and its middle character remains unchanged.
- An already palindromic pair must remain unchanged because replacing it would exceed the minimum number of operations.
- Even-length strings have no middle position; the pointers simply cross after the final pair.
