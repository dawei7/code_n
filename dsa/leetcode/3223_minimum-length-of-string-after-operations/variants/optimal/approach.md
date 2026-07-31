## General

**Treat each character independently.** An operation chooses three occurrences of one character and removes two of them. It never changes the count of another character. The exact positions affect which copies disappear, but not whether a character with at least three copies can supply a left, middle, and right occurrence.

**Preserve the count's parity.** Every operation subtracts two. Therefore, a positive odd frequency can never fall below one, and a positive even frequency can never fall below two. These bounds are attainable: while at least three occurrences remain, choose any non-end occurrence as the middle; its nearest equal neighbors can be deleted. Repeating leaves one copy from an odd count or two copies from an even count.

Count the 26 lowercase letters once. Add `1` for every positive odd frequency and `2` for every positive even frequency. Summing these independent minima gives the minimum final string length.

## Complexity detail

Let $n=\lvert\texttt{s}\rvert$. Counting the string takes $O(n)$ time, and inspecting the fixed 26-entry frequency array takes constant time. Because the lowercase alphabet has fixed size, auxiliary space is $O(1)$.

## Alternatives and edge cases

- **Simulate concrete deletions:** Maintaining the changing string and locating triples is correct but can require $O(n^2)$ time because deletions and rescans repeat.
- **Keep one of every present character:** This is wrong for a positive even count because subtracting two preserves even parity, so the minimum is two.
- Frequencies one and two cannot be reduced at all.
- A frequency of three reduces to one in exactly one operation.
- Operations on one character never prevent reductions of another character.
- A one-character input remains length one.
