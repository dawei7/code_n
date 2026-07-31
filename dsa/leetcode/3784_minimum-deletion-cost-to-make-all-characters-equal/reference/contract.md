## Function Contract

**Inputs**

- `s`: A nonempty string of lowercase English letters.
- `cost`: A positive deletion cost for each corresponding character of `s`.

Let $N=\lvert s\rvert=\lvert\texttt{cost}\rvert$. A deletion removes a character from the result but does not change the cost associated with any other original position. At least one character must remain.

**Return value**

Return the minimum total cost of deletions that leaves a nonempty string containing only one distinct character.
