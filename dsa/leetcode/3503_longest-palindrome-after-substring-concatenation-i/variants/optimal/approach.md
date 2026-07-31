## General

Let `r = t[::-1]`. Matching the first character chosen from `s` with the last character chosen from `t` is then the same as matching characters at aligned positions in `s` and `r`. Several consecutive matches supply equally long outer pieces of the final palindrome. After those outer pairs, the middle may be empty, a palindrome continuing in `s`, or a palindrome continuing in `r`â€”the last case corresponds to a palindrome immediately before the matched piece in the original `t`.

For every index $i$, let $P_s[i]$ be the longest palindromic substring of `s` that starts at $i$. Define $P_r[j]$ analogously for `r`. Expand around every odd and even center in each string; whenever an expansion spans `[left, right]`, update the value for `left`. This enumerates every palindromic substring and therefore computes both arrays exactly. Their overall maximum already covers solutions that choose an empty substring from the other input.

Now define $D[i][j]$ as the greatest palindrome length whose outermost cross-string pair uses `s[i]` and `r[j]`. If those characters differ, no such palindrome starts there. If they match, remove that outer pair. The remaining middle has exactly three useful forms: a palindrome beginning at `s[i + 1]`, a palindrome beginning at `r[j + 1]`, or another cross-string palindrome beginning at both next positions. Thus,

$$
D[i][j] = 2 + \max\bigl(P_s[i+1], P_r[j+1], D[i+1][j+1]\bigr)
$$

when `s[i] == r[j]`, with out-of-range and nonexistent values treated as zero. Process indices from right to left so the diagonal successor is already known. Only the next and current rows are needed.

Every constructed value is valid: its equal outer characters surround one of the three palindromic middle forms. Conversely, any palindrome using both strings has some number of mirrored cross-string pairs followed by exactly one of those middle forms. Repeatedly removing its outer pair follows the recurrence to its center, so the dynamic program considers every valid choice.

## Complexity detail

Let $n=\lvert\texttt{s}\rvert$ and $m=\lvert\texttt{t}\rvert$. Center expansion takes $O(n^2+m^2)$ time in the worst case. The cross-string table has $nm$ states with constant work per state, for total time $O(n^2+m^2+nm)$. The palindrome-start arrays and two rolling rows occupy $O(n+m)$ space.

The benchmark grows $n$ and $m$ together on strings whose many palindromic substrings exercise both quadratic preprocessing and cross-string states. It contrasts the dynamic program with a correct method that restarts and extends a matching diagonal from every pair `(i, j)`, requiring $O(nm\min(n,m))$ time when all characters match.

## Alternatives and edge cases

- **Enumerate both substrings:** Trying every substring of `s` with every substring of `t` and checking each concatenation is straightforward under the small limits, but can take $O(n^2m^2(n+m))$ time.
- **Restart every matching diagonal:** Extending equal characters afresh from each pair of starting positions avoids enumerating complete substring pairs, but repeats suffix comparisons and takes $O(nm\min(n,m))$ time in the worst case.
- **Full dynamic-programming tables:** Storing all $D[i][j]$ states is correct but uses $O(nm)$ space; only the following diagonal row is required.
- **Palindrome boolean tables:** A conventional interval DP can compute the one-string centers in quadratic space, whereas center expansion records the same longest-starting values in linear space.
- **Empty selection:** The best answer may lie wholly inside either input, so the maximum of $P_s$ and $P_r$ must seed the result.
- **Unequal chosen lengths:** After the shorter outer side is exhausted, the remaining consecutive portion of the longer side must itself be the palindromic center captured by $P_s$ or $P_r$.
- **Even center:** If both matched sides end together, the recurrence uses a zero-length middle and contributes only the mirrored pairs.
- **Odd center:** A one-character palindrome from either side can sit between the matched outer pieces.
- **Substring boundaries:** Starting the dynamic program at every pair `(i, j)` permits discarding arbitrary prefixes and suffixes rather than forcing either whole input.
- **Reversal mapping:** A palindrome starting after position $j$ in `r` maps to a palindrome ending immediately before the matched substring in `t`, which preserves the required `s`-then-`t` concatenation order.
