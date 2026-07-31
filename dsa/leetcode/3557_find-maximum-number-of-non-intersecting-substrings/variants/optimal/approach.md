## General

After the end of the most recently selected substring, record the first position at which each letter appears. At a new position `i`, the current letter can close a valid substring exactly when its recorded first position is at most `i - 3`. Using that first occurrence is always at least as helpful as using a later occurrence because it gives the greatest possible length.

As soon as any valid substring can end, select it, increase the answer, and clear all recorded positions. Clearing starts the next search strictly after the chosen endpoint, so selected substrings never intersect.

This is the classic earliest-finish interval rule applied without explicitly generating all intervals. The chosen substring has the smallest possible ending position among every feasible substring remaining. Replacing the first substring of any optimal solution with this one cannot reduce the number of later choices: the replacement ends no later and therefore leaves at least as much suffix available. Applying the same argument after every reset proves the greedy count is optimal.

## Complexity detail

Let $n=\lvert\texttt{word}\rvert$. Each position is processed once, and every dictionary operation is constant time. The total time is $O(n)$. At most the 26 lowercase letters are stored, so the auxiliary space is $O(1)$.

## Alternatives and edge cases

- **Generate all valid intervals:** Enumerating every equal-letter endpoint pair can produce $O(n^2)$ intervals before interval scheduling even begins.
- **Quadratic dynamic programming:** Trying every possible start for each ending position is correct but costs $O(n^2)$ time.
- **Choose the longest interval:** A long early choice may consume positions that could support several shorter disjoint substrings; earliest finishing time is the relevant greedy criterion.
- **Length boundary:** Endpoints at indices differing by exactly three form a valid length-four substring.
- **Shared endpoint:** Two selected substrings cannot reuse an endpoint because that position would belong to both.
- **Reset after selection:** The closing character is not recorded as a start for the next interval, which prevents endpoint intersection.
- **Short input:** A string of length below four cannot contain a valid substring and returns zero.
