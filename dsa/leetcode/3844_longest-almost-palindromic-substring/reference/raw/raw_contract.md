## Function Contract

**Inputs**

- `s`: The lowercase English string in which a contiguous substring is chosen.

For substring boundaries $0\le l\le r<\lvert\texttt{s}\rvert$, the candidate is `s[l:r + 1]`. It is almost-palindromic exactly when there is an index $k$ with $l\le k\le r$ such that

$$
\texttt{s}[l:k]\mathbin{+}\texttt{s}[k+1:r+1]
$$

is a palindrome. This expression deletes one character, `s[k]`, while preserving the order of every other character.

**Return value**

Return the maximum value of $r-l+1$ over all almost-palindromic substrings. Since $\lvert\texttt{s}\rvert\ge2$, an answer of at least `2` always exists: deleting either character from any length-two substring leaves a one-character palindrome.
