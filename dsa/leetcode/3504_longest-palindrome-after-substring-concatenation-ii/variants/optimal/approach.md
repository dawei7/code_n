## General

Reverse `t` into `r`. A chosen prefix on the left side of the final palindrome and its mirrored suffix from `t` now appear as equal, forward-moving segments of `s` and `r`. Once those cross-string outer pairs stop, the remaining center is either empty, a palindrome continuing in `s`, or a palindrome continuing in `r` (which maps back to a palindrome immediately before the matched segment in the original `t`).

For each position $i$, let $P_s[i]$ be the greatest length of a palindrome starting at `s[i]`; define $P_r[j]$ the same way for `r`. Compute odd and even Manacher radii in each string. Every maximal radius identifies a palindrome's left boundary and length. Record that length at its boundary. Removing one character from both ends preserves palindromicity, moves the start right by one, and reduces the length by two, so a single left-to-right pass applies

$$
P[i] \gets \max(P[i], P[i-1]-2).
$$

This recovers the best palindrome beginning at every later position inside each maximal radius. A longer candidate at one start continues to dominate every shorter candidate after both lose the same two characters per step.

Next let $D[i][j]$ be the best palindrome whose first cross-string pair is `s[i]` with `r[j]`. Unequal characters cannot form that outer pair. Equal characters contribute two positions and surround whichever of three middle choices is longest:

$$
D[i][j] = 2 + \max\bigl(P_s[i+1], P_r[j+1], D[i+1][j+1]\bigr).
$$

Missing positions contribute zero. Traverse both strings from right to left, keeping only the row for $i+1$ and the row being built. Seed the result with the largest value in $P_s$ or $P_r$ so solutions using only one input remain available.

Every recurrence value is constructible because equal outer characters surround a palindromic middle. Conversely, repeatedly removing the outer characters of any valid cross-string palindrome eventually leaves exactly one of the three recorded middle forms. The recurrence therefore includes every allowed pair of substrings, while Manacher preprocessing avoids the quadratic center expansions that become costly under the larger limits.

## Complexity detail

Let $n=\lvert\texttt{s}\rvert$ and $m=\lvert\texttt{t}\rvert$. Manacher's algorithm and the boundary-propagation passes take $O(n+m)$ time. The cross-string dynamic program evaluates $nm$ states in constant time, so total time is $O(nm+n+m)$. The four radius/palindrome arrays and two rolling rows require $O(n+m)$ space.

The benchmark grows $n$ while holding $m$ fixed. The accepted implementation is therefore linear in the authored size, whereas a correct version that discovers $P_s$ by expanding every center takes $\Theta(n^2)$ time on the uniform strings.

## Alternatives and edge cases

- **Quadratic center expansion:** Expanding around every odd and even center computes the same palindrome-start arrays correctly, but a uniform length-$n$ string forces $\Theta(n^2)$ comparisons.
- **Interval palindrome table:** A Boolean substring DP also supplies $P_s$ and $P_r$, but needs quadratic time and space for each input before the cross-string phase.
- **Store the full cross table:** Keeping all $nm$ recurrence values is unnecessary; every state reads only its diagonal successor from the next row.
- **Enumerate substring pairs:** Materializing every choice from both inputs and checking concatenations is infeasible at length $1000$.
- **Empty selection:** The best palindrome may occur wholly within `s` or `t`, so the one-string maxima must be included independently of cross matches.
- **Empty center:** When matched outer pieces meet exactly, the recurrence's zero boundary value produces an even palindrome.
- **Center in either input:** Unequal chosen lengths are valid only when the unmatched consecutive portion is itself palindromic; $P_s$ and $P_r$ encode precisely those choices.
- **Proper substrings:** Considering every state `(i, j)` permits arbitrary discarded prefixes and suffixes instead of forcing either full input.
- **Uniform strings:** All radii and cross pairs are large, yet Manacher and the rolling recurrence retain their stated bounds.
- **Length-one input:** Its radius array and propagation remain valid, and it can serve as a single outer character or as the entire answer.
