## General

**Use shared characters only once**

A supersequence must preserve every character of both input strings in order, but it may interleave the two strings. If one character can serve as the same subsequence position for both strings, including it once is better than including it twice. The greatest number of such shared positions is the length of a longest common subsequence, or LCS.

If `str1` has length $m$, `str2` has length $n$, and their LCS has length $L$, then a shortest common supersequence has length $m+n-L$. Every character not shared must appear separately, while each of the $L$ shared characters replaces two required appearances with one. This connection lets the solution first compute LCS lengths and then reconstruct an actual shortest supersequence.

**Define the dynamic-programming table**

`f[i][j]` stores the LCS length between prefixes `str1[:i]` and `str2[:j]`. Row zero or column zero represents an empty prefix, whose LCS with anything has length zero. The initialized zero border is therefore the complete base case.

For positive `i` and `j`, compare the last characters of the two prefixes:

- If `str1[i - 1] == str2[j - 1]`, that character can extend a common subsequence of the two shorter prefixes. The recurrence is `f[i][j] = f[i - 1][j - 1] + 1`.
- If the characters differ, they cannot both be the final character of one common subsequence position. The best LCS must omit at least one of them, so the recurrence takes `max(f[i - 1][j], f[i][j - 1])`.

The nested loops fill shorter-prefix states before states that depend on them. By induction over prefix lengths, every table entry is the correct LCS length.

**Walk backward while emitting every necessary character**

The table stores lengths rather than strings, so the second phase reconstructs the answer. It starts at `i = m` and `j = n`, representing both complete strings, and builds `ans` backward from the end.

If `i == 0`, no characters from `str1` remain. Every remaining character of `str2[:j]` is necessary, so the algorithm decrements `j` and appends that character. The `j == 0` case is symmetric.

When both prefixes are nonempty, the table values tell which movement preserves an LCS:

- If `f[i][j] == f[i - 1][j]`, an LCS of the current prefixes exists without `str1[i - 1]`. That character is not merged at this step, but a supersequence must still contain it. The code decrements `i` and appends `str1[i]`.
- Otherwise, if `f[i][j] == f[i][j - 1]`, the same reasoning applies to `str2[j - 1]`. The code decrements `j` and appends it.
- If neither equality holds, the current characters match and the LCS length came from the diagonal plus one. The code moves both indices diagonally and appends that shared character only once.

When the two non-diagonal choices tie, the first condition prefers consuming from `str1`. That choice may change which valid shortest supersequence is returned, but not its length. The contract permits any shortest answer.

**Why the reverse construction is valid and shortest**

Every step consumes at least one remaining character, so the walk terminates at `i = j = 0`. A horizontal or vertical move appends the one character that belongs only to the consumed side at that moment. A diagonal move appends one matching character for both sides. Consequently, reversing the collected characters preserves the original left-to-right order of each input, making both inputs subsequences.

Exactly $L$ diagonal moves correspond to one chosen LCS. Those moves merge two obligations into one character. Every other character from both inputs is appended separately, so the constructed length is $m+n-L$. No common supersequence can merge more than $L$ ordered matching pairs, because those merged pairs would themselves form a common subsequence longer than the LCS. Therefore, no shorter result exists.

The characters were appended from right to left, so `ans[::-1]` reverses their order before `''.join(...)` creates the returned string.

## Complexity detail

There are $(m+1)(n+1)$ table cells. Each interior cell performs constant work, so table construction takes $O(mn)$ time. The reconstruction decreases `i` or `j` on every iteration and therefore takes at most $m+n$ steps. Since both strings are nonempty, $mn$ dominates the linear reconstruction term in the package’s $O(mn)$ bound.

The table holds $O(mn)$ integers. The answer list and final string use $O(m+n)$ space, which does not exceed the table bound for positive $m$ and $n$. Total space is $O(mn)$ when the required output is included.

Storing the full table is important for this reconstruction because the walk needs values above and to the left of arbitrary cells. An LCS length alone can be computed with two rows, but recovering an answer then needs a more sophisticated divide-and-conquer reconstruction or stored decisions.

## Alternatives and edge cases

- **Direct SCS-length dynamic programming:** Store the shortest-supersequence length for every prefix pair and reconstruct from that table. It has the same $O(mn)$ time and space and avoids explicitly naming the LCS relationship.
- **Store whole strings in DP cells:** This is conceptually direct, but repeated concatenation makes time and memory much larger than storing integer lengths and reconstructing once.
- **Memoized recursion:** Recurrence states are the same prefix pairs, but recursion adds call-stack overhead and reconstruction details. Bottom-up filling is predictable for lengths up to one thousand.
- **Space-optimized LCS:** Two rows reduce length-computation memory to $O(n)$, but they do not by themselves retain enough information for the backward walk used here.
- **Identical strings:** Every position is a diagonal LCS move, so each character is appended once and the result equals the input.
- **No common characters:** The LCS length is zero. Reconstruction appends every character of both strings, yielding length $m+n$ in one of several valid interleavings.
- **Repeated characters:** DP handles positions rather than sets of characters, so it preserves ordering and does not confuse separate occurrences.
- **Multiple LCS choices:** A tie is resolved by the first branch. Different tie choices can produce different answers of the same minimum length, all allowed.
- **One string already a subsequence:** Its entire length can be shared with the longer string, so reconstruction can return the longer string itself.
- **Nonempty-input guarantee:** Empty-string border states are still required internally even though the external strings each have length at least one.
- **Reverse accumulation:** Returning `''.join(ans)` without reversing would produce the supersequence backward and violate both subsequence orders.
