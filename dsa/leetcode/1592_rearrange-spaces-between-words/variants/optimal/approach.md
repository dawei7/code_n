## General
**Separate content from whitespace**

Split `text` on whitespace to recover the words without any empty entries, and count all literal space characters in the original string. Let the counts be $W$ words and $S$ spaces. The output must retain those exact words, their order, and all $S$ spaces.

**Divide spaces among actual gaps**

When $W>1$, there are exactly $W-1$ internal gaps. Euclidean division gives

$$
S=q(W-1)+r,
$$

where $q=\lfloor S/(W-1)\rfloor$ and $0\le r<W-1$. Put exactly $q$ spaces in every gap and append the remaining $r$ spaces. No larger common gap is possible because it would require more than $S$ spaces, so this distribution is maximal.

When $W=1$, there are no internal gaps. Division by $W-1$ is undefined and no space can be placed between words, so append all $S$ spaces after the sole word.

Joining the words with the computed separator and adding the trailing remainder preserves every word and every space. Its length is the total word-character count plus $q(W-1)+r$, equal to the original length, which proves all contract conditions.

## Complexity detail
Splitting, counting, joining, and producing the result each process or emit $O(L)$ characters, for $O(L)$ total time. The word list and returned string require $O(L)$ space.

## Alternatives and edge cases
- **Manual one-pass tokenizer:** collect words and count spaces while scanning characters. It has the same $O(L)$ time and space bounds.
- **Repeated string copying:** append output characters by rebuilding the full prefix each time. It is correct but can take $O(L^2)$ time because earlier characters are copied repeatedly.
- **Single word:** append all spaces after it; never divide by zero.
- **No spaces:** joining leaves the already adjacent content unchanged; under the source contract this occurs only for one word.
- **Uneven division:** append the remainder only at the end, not across selected gaps.
- **Leading and trailing input spaces:** they are part of the total pool and lose their original positions.
- **Many consecutive spaces:** splitting must not create empty words.
- **Length preservation:** the output must contain exactly the input's word characters and total space count.
