## General
**Define the interval decision**

Let $D(i,j)$ be the minimum insertions needed for substring `s[i:j + 1]`. A substring of length zero or one is already palindromic, so its value is 0.

If `s[i] == s[j]`, those boundary characters can face each other in the final palindrome without insertion, giving $D(i,j)=D(i+1,j-1)$. If they differ, at least one boundary needs a matching character inserted on the opposite side. Matching `s[i]` leaves `s[i + 1:j + 1]` to solve, while matching `s[j]` leaves `s[i:j]`; choose the better option:

$$
D(i,j)=1+\min(D(i+1,j),D(i,j-1)).
$$

These are exhaustive choices because the two unequal original boundary characters cannot face one another in a palindrome, and inserting a match for either boundary is always feasible. Filling intervals from shorter to longer therefore produces the optimal answer $D(0,n-1)$.

**Compress the interval table to one row**

Process `i` from right to left and `j` from `i + 1` to the end. Before an update, `dp[j]` stores $D(i+1,j)$; after updating `j - 1`, `dp[j - 1]` stores $D(i,j-1)$. A scalar `diagonal` preserves the overwritten $D(i+1,j-1)$. These are exactly the three states used by the recurrence, so the full two-dimensional table is unnecessary.

## Complexity detail
There are $O(n^2)$ index intervals, and each update takes constant time, for $O(n^2)$ time. The compressed `dp` row has $n$ entries and the remaining state is constant, so auxiliary space is $O(n)$.

## Alternatives and edge cases
- **Longest palindromic subsequence:** The answer is $n-L$, where $L$ is the longest palindromic subsequence length; computing an LCS between `s` and its reverse also takes $O(n^2)$ time, usually with a less direct explanation.
- **Full interval table:** A two-dimensional $D(i,j)$ table is straightforward and supports reconstruction, but uses $O(n^2)$ space when only the count is needed.
- **Unmemoized recursion:** Following both mismatch branches without caching is correct but can take exponential time because the same intervals are solved repeatedly.
- **Already palindromic:** Every matching boundary eventually reaches a base interval, so the result is 0.
- **One character:** No insertion is needed.
- **All distinct characters:** At least $n-1$ insertions are necessary, and mirroring all but one character achieves that bound.
- **Insertions preserve order:** The recurrence never moves or deletes an original character; it only chooses which boundary receives a new match.
