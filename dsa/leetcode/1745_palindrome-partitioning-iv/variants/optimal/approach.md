## General
**Precompute every palindromic interval**

Let `palindrome[left][right]` indicate whether the inclusive substring from `left` through `right` is a palindrome. It is true when the endpoint characters match and the enclosed interval is empty, one character, or already known to be palindromic:

$$
\texttt{palindrome[left][right]}
=
(s_{\textit{left}}=s_{\textit{right}})
\land
(\textit{right}-\textit{left}<2
\lor
\texttt{palindrome[left+1][right-1]}).
$$

Fill left endpoints from right to left so every enclosed state is available before it is needed.

**Represent a partition by two cut endpoints**

Let the first piece end at `first` and the second end at `second`. Nonempty pieces require $0 \le \textit{first} < \textit{second} < n-1$. The three table lookups are then `[0, first]`, `[first + 1, second]`, and `[second + 1, n - 1]`.

**Accept only when all three intervals agree**

Enumerate legal cut pairs and return true when all three corresponding states are true. The table entries exactly encode the palindrome definition, and every possible three-piece partition has one unique pair of cut endpoints, so this search finds a valid partition if and only if one exists.

## Complexity detail
There are $O(n^2)$ substring intervals, each filled in constant time. There are also $O(n^2)$ legal cut pairs, each checked with three constant-time table accesses. Total time is $O(n^2)$ and the table occupies $O(n^2)$ space.

## Alternatives and edge cases
- **Check each substring for every cut pair:** Directly scanning the three pieces repeatedly is simple but can take $O(n^3)$ time.
- **Center expansion:** Palindromic prefixes, middle intervals, and suffixes can be derived with center expansion and less storage, but coordinating the two cuts is more intricate.
- **Length three:** Cutting between every character creates three one-character palindromes, so every length-three input succeeds.
- **One-character pieces:** Either endpoint piece or the middle piece may have length one.
- **Exactly three pieces:** A string that is itself a palindrome still needs two legal nonempty cuts.
- **Repeated characters:** Many intervals may be palindromes; the algorithm may return after finding any one valid cut pair.
- **No valid first prefix:** If no proper prefix ending before the final two characters is palindromic, no partition can succeed.
