## General

**Accumulate the value of each word directly**

Visit the words in their given order. For each character, subtract the code point of `'a'` from its code point to obtain an index from 0 through 25, then add the corresponding entry of `weights` to the current word's total.

Only the residue of that total modulo 26 affects the output. Residue 0 must produce `'z'`, and each increment moves one letter backward, so subtracting the residue from the code point of `'z'` gives the mapped character directly. Append that character and continue with the next word.

The accumulated total equals the defined word weight because it includes the assigned weight of every character exactly once. Taking its residue applies the required modulo operation, and the code-point subtraction implements every pair in the reverse mapping from `0 -> 'z'` through `25 -> 'a'`. Since characters are appended in input order, joining them yields exactly the required result string.

## Complexity detail

Let $W$ be the number of words and $S$ their total number of characters. Every character is inspected once, so the time complexity is $O(S)$. The list of mapped characters and the returned string contain $W$ characters, giving $O(W)$ space including the output construction; the numeric accumulator itself uses constant auxiliary space.

The benchmark fixes every word length at 10 and defines size as $S$. The accepted direct scan and an independent lookup-table formulation grow linearly in $S$. A correct control that searches all word positions before processing each selected word introduces another factor of $W$ and therefore grows quadratically on these tiers.

## Alternatives and edge cases

- **Prebuilt letter dictionary:** Map each lowercase character to its supplied weight and use that lookup while summing. This has the same $O(S)$ time and uses constant-size additional storage for the 26-letter alphabet.
- **Nested word-position search:** For every output position, scan all input word positions to locate the matching index before summing its characters. It remains correct but takes $O(W^2+S)$ time.
- **Residue zero:** A word weight divisible by 26 maps to `'z'`, not `'a'`.
- **Residue 25:** The other endpoint maps to `'a'`, confirming that the alphabet order is reversed.
- **Repeated words:** Each occurrence contributes its own mapped character and must remain in its original position.
- **Large word totals:** A length-10 word can weigh 1,000, so reduction must happen before converting the residue to a character.
