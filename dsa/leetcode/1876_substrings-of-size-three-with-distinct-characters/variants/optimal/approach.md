## General
**Enumerate only windows of the required length**

A length-three substring starts at each index from `0` through `N - 3`. Scan exactly those starts. There is no reason to generate substrings of any other length.

**Test pairwise distinctness directly**

Three characters are all distinct precisely when the first differs from the second, the first differs from the third, and the second differs from the third. Add the Boolean result of these three comparisons to the count for each window.

**Why occurrences are counted correctly**

Each possible length-three occurrence has one unique starting index and is examined once, including occurrences that overlap or contain the same text as another window. The pairwise test accepts exactly the good windows, so the accumulated total equals the requested occurrence count.

## Complexity detail
There are at most $N-2$ candidate windows, and each uses three constant-time comparisons. Total time is therefore $O(N)$. The scan stores only an index and count, using $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Three-character set:** Checking `len(set(s[i:i+3])) == 3` is clear and remains $O(N)$ because the window size is fixed, though it allocates tiny temporary objects.
- **Enumerate every substring:** It eventually finds the correct length-three windows but performs $O(N^2)$ unnecessary enumeration.
- **String shorter than three:** The answer is zero.
- **Exactly three distinct characters:** The sole window contributes one.
- **Repeated first and third characters:** A window such as `"aba"` is not good even though adjacent characters differ.
- **Overlapping windows:** Each valid start is counted independently.
- **Repeated text:** Separate occurrences of the same good substring all count.
