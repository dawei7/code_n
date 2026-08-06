## Function Contract

**Class Interface**

- `WordDistance(wordsDict: List[str])`: Initializes the object with the list of strings `wordsDict` ($1 \le \text{wordsDict.length} \le 3 \times 10^4$).
- `shortest(word1: str, word2: str) -> int`: Returns the minimum index distance $\lvert i - j \rvert$ between `word1` at index $i$ and `word2` at index $j$, where `word1 != word2`.
