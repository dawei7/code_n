## Function Contract

**Inputs**

- `wordsDict`: A list of strings ($1 \le \text{wordsDict.length} \le 10^5$).
- `word1`: A string present in `wordsDict`.
- `word2`: A string present in `wordsDict` (may be equal to `word1`).

**Return value**

Return an integer representing the minimum index distance $\lvert i - j \rvert$ between distinct occurrences of `word1` at index $i$ and `word2` at index $j$ ($i \neq j$).
