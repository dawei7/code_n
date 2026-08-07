## Function Contract

**Inputs**

- `s`: A non-empty string containing only lowercase English letters, spaces, and digits.

Let $N=\lvert\texttt{s}\rvert$. A character contributes to the consonant count only when it is an English letter that is not one of the five vowels; spaces and digits do not contribute to either count.

**Return value**

Return $\lfloor v/c\rfloor$ when the consonant count $c$ is positive. Return `0` when $c=0$.
