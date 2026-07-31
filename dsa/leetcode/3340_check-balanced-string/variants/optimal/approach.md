## General

Track one signed difference rather than two separate sums. Digits at even indices contribute positively, while digits at odd indices contribute negatively. After scanning a prefix,

$$
\textit{difference}
=
\sum_{\substack{0\le i<r\\i\text{ even}}}\operatorname{digit}(\texttt{num}[i])
-
\sum_{\substack{0\le i<r\\i\text{ odd}}}\operatorname{digit}(\texttt{num}[i]).
$$

Convert each character to its numeric value and add or subtract it according to the zero-based index parity. At the end, the two required sums are equal exactly when `difference == 0`.

The maintained value is the even-index sum minus the odd-index sum for the processed prefix: initialization is correct for the empty prefix, and each step adds the next digit with precisely its required sign. Therefore the final zero test is equivalent to the definition of a balanced string.

## Complexity detail

Let $n=\lvert\texttt{num}\rvert$. Every digit is inspected once, so the time complexity is $O(n)$. The running difference, index, and converted digit use $O(1)$ auxiliary space.

The scan is asymptotically optimal. In an all-zero balanced string, changing any single digit to `1` makes one alternating sum larger. Because every position can independently change the result, any correct algorithm must inspect all $n$ digits in the worst case, establishing an $\Omega(n)$ lower bound.

## Alternatives and edge cases

- **Build two digit lists:** Slicing or collecting even- and odd-index digits works but allocates unnecessary $O(n)$ storage.
- **Convert the whole string to an integer:** Numeric magnitude does not preserve the positional groups, and leading zeroes would be lost.
- **Use one-based parity:** The contract uses zero-based indices, so the first digit belongs to the even-index sum.
- **Leading zeroes:** They contribute zero but still occupy positions and affect the parity of later indices.
- **Odd length:** The even-index side contains one more position, but the string can still be balanced.
- **All zeroes:** Both sums are zero, so the result is true.
- **Maximum length:** The difference remains small, but every digit is still semantically relevant and must be read.
