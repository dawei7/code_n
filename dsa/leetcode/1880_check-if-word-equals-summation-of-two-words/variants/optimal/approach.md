## General
**Read each word as a decimal number**

Let $S$ be the total number of characters across the three words. Convert a word from left to right. If the accumulated prefix has value $v$ and the next letter represents digit $d$, the extended prefix has value $10v+d$. This is ordinary decimal place-value evaluation and naturally discards leading zeros.

**Compare the three values**

Apply the conversion independently to the two addends and the target, then test their integer equality after addition. Every character contributes its exact prescribed digit once, so induction over the word length shows the conversion equals the stated concatenation. The final Boolean comparison is therefore true exactly for the required equation.

## Complexity detail
Each of the $S$ characters is processed once, giving $O(S)$ time. The conversion keeps only three integers plus loop variables, so it uses $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Build digit strings:** Joining mapped digits and parsing them is correct but allocates $O(S)$ temporary space.
- **Repeated place-value powers:** Computing a fresh power of ten for every character is correct but costs $O(S^2)$ time.
- **Leading `'a'` letters:** They represent leading zeros and do not change a word's integer value.
- **All `'a'` letters:** Words of different lengths can all represent zero.
- **Carry between addends:** Compare integer values; digitwise concatenation alone is not addition.
- **Single letters:** They map directly to digits from $0$ through $9$.
