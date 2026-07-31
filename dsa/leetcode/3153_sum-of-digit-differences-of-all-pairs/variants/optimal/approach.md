## General

The total can be separated by decimal position. A pair that differs in three positions contributes one at each of those positions, so counting differing pairs independently at every position and then adding the counts produces exactly the required sum.

Maintain ten frequency counters for each of the $D$ digit positions. Process the values from left to right. When the current value is the element at index `seen`, exactly `seen` earlier values can pair with it. At one position, `counts[position][digit]` of those earlier values have the same digit; the other

$$
\texttt{seen}-\texttt{counts[position][digit]}
$$

values differ there and each contributes one new digit difference. Add that quantity, increment the matching frequency, remove the current units digit with integer division, and continue to the next position.

Every unordered pair is considered exactly once, when its later array element is processed. At each digit position, the formula adds one for that pair exactly when the two digits differ and zero when they match. Summing over all positions therefore gives that pair's digit difference, and summing as every later element arrives gives the required total over all pairs.

## Complexity detail

Let $n = \lvert\texttt{nums}\rvert$ and let $D$ be the common number of decimal digits. Each value exposes exactly $D$ digits, so the running time is $O(nD)$.

The frequency table contains $10D$ counters. Since ten is constant, the auxiliary space is $O(D)$. Under the stated bound, $D \le 9$.

## Alternatives and edge cases

- **Count all digits, then subtract matches:** For each position, compute $\binom{n}{2}-\sum_d\binom{c_d}{2}$. This is also $O(nD)$ time and $O(D)$ space, but the streaming form avoids a separate combination pass.
- **String conversion:** Converting every value to text makes positions convenient to index, but retaining all strings uses $O(nD)$ space instead of the digit-frequency table alone.
- **Enumerate every pair:** Comparing all $\binom{n}{2}$ pairs directly is correct but requires $O(n^2D)$ time; it is the principal slower benchmark comparison.
- Repeated equal values are distinct elements, but their mutual pair contributes zero at every position.
- One-digit inputs use the same method with $D=1$.
- The equal-digit-length guarantee means no leading-zero padding is needed.
- The total can exceed a 32-bit integer even though each individual pair contributes at most nine.
