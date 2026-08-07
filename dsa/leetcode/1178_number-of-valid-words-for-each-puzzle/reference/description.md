### 1. Description

With respect to a given `puzzle` string, a `word` is *valid* if both the following conditions are satisfied:

- `word` contains the first letter of `puzzle`.

- For each letter in `word`, that letter is in `puzzle`.

		<li>For example, if the puzzle is `"abcdefg"`, then valid words are `"faced"`, `"cabbage"`, and `"baggage"`, while

- invalid words are `"beefed"` (does not include `'a'`) and `"based"` (includes `'s'` which is not in the puzzle).

	</li>

Return *an array *`answer`*, where *$\text{answer}[i]$* is the number of words in the given word list *`words`* that is valid with respect to the puzzle *$\text{puzzles}[i]$.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

- **Input:** $words = ["aaaa","asas","able","ability","actt","actor","access"], puzzles = ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]$
- **Output:** `[1,1,3,2,4,0]`
- **Explanation:**
1 valid word for "aboveyz" : "aaaa"
1 valid word for "abrodyz" : "aaaa"
3 valid words for "abslute" : "aaaa", "asas", "able"
2 valid words for "absoryz" : "aaaa", "asas"
4 valid words for "actresz" : "aaaa", "asas", "actt", "access"
There are no valid words for "gaswxyz" cause none of the words in the list contains letter 'g'.
#### Example 2

- **Input:** $words = ["apple","pleas","please"], puzzles = ["aelwxyz","aelpxyz","aelpsxy","saelpxy","xaelpsy"]$
- **Output:** `[0,1,3,2,0]`

### 4. Constraints

- $1 \le \text{words.length} \le 10^{5}$

- $4 \le \text{words}[i].length \le 50$

- $1 \le \text{puzzles.length} \le 10^{4}$

- $\text{puzzles}[i].length = 7$

- $\text{words}[i]$ and $\text{puzzles}[i]$ consist of lowercase English letters.

- Each $\text{puzzles}[i]$does not contain repeated characters.