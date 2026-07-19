## General
**Partition the string into maximal equal-character runs.** Scan from left to right while tracking the length of the current run. When the character changes, the previous run ends and a new length-one run begins. No qualifying substring can cross that boundary because it would contain both neighboring character values.

**Count by the ending position.** When the current run has length $L$, exactly $L$ valid substrings end at its newest character: the length-one suffix, the length-two suffix, and so on through the entire run. Add $L$ immediately at each position. Over a completed run of length $L$, these contributions total

$$
1+2+\cdots+L=\frac{L(L+1)}{2}.
$$

Every single-distinct-letter substring lies wholly within one maximal run and has one unique ending position, so this accumulation counts every valid occurrence exactly once.

## Complexity detail
The scan visits each of the $n$ characters once, giving $O(n)$ time. The answer, current run length, and previous character use $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Enumerate every start and extend while equal:** This is correct, but an all-equal string makes it examine $O(n^2)$ start-end pairs.
- **Materialize maximal runs first:** Splitting or grouping the runs and then summing $L(L+1)/2$ is also linear, but storing all run lengths can use $O(n)$ space.
- **Single character:** The only substring qualifies, so the answer is `1`.
- **All characters equal:** Every non-empty substring qualifies, yielding $n(n+1)/2$.
- **All adjacent characters differ:** Only the $n$ length-one substrings qualify.
- **Repeated text at different positions:** Each index interval is a separate substring occurrence and must be counted.
