## General

Any palindrome of length at least $4$ contains a palindrome of length $2$ or $3$ at its center. Therefore, a string is beautiful exactly when each character differs from the previous character and from the character two positions earlier. This turns a global-looking restriction into two constant-time local checks.

To obtain the immediate lexicographic successor, treat the string like a number whose digits come from the first `k` letters. Try the rightmost position first. At a chosen position `i`, test larger letters in ascending order and accept the first one that differs from `s[i - 1]` and `s[i - 2]` when those positions exist. If no letter works, move left as a carry would.

Once a position can be increased, the unchanged prefix is already beautiful and the increase makes the whole result strictly larger than `s`; later characters no longer need to remain above their old values. Rebuild the suffix from left to right. At each position, choose the smallest alphabet letter different from the previous two characters. Since $k \ge 4$, at most two letters are forbidden, so a choice always exists.

Trying change positions from right to left preserves the longest possible prefix of `s`, which is necessary for the smallest larger string. At the selected position, trying candidates in ascending order chooses the smallest valid increase. Finally, the left-to-right suffix construction makes the earliest suffix character as small as possible before considering later positions. These three greedy choices establish that the returned string is beautiful and precedes every other beautiful string larger than `s`. If every position overflows, no larger permitted string exists.

## Complexity detail

Let $n$ be the length of `s`. Each position tests at most $k$ characters while searching for the carry position or constructing the suffix, giving $O(nk)$ time. Because $4 \le k \le 26$, this is also linear in $n$. The mutable character list uses $O(n)$ space.

The benchmark uses `size` as $n$ and supplies the lexicographically greatest beautiful string for `k = 4`, forcing the carry search to inspect the entire input. A correct alternative that rebuilds and revalidates a complete candidate for every possible carry position finishes all tiers but takes $O(n^2)$ time.

## Alternatives and edge cases

- **Enumerate following strings:** Increment the whole base-`k` string repeatedly and test beauty. This is correct but can inspect exponentially many candidates.
- **Revalidate every candidate prefix:** For each possible carry position, construct a candidate and scan it for palindromes. It avoids exponential enumeration but can take $O(n^2)$ time.
- Length-two and length-three palindromes are the only patterns that need direct checks; every longer palindrome contains one of them.
- For a one-character string, beauty is automatic, so the answer is the next letter unless the character is already the alphabet maximum.
- A failed rightmost increment must carry left; suffix characters may then become lexicographically smaller than their originals.
- The guarantee $k \ge 4$ ensures greedy suffix construction never runs out of locally valid letters.
- If the input is already the greatest beautiful string of its length, every carry attempt fails and the answer is empty.
