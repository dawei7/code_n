### 1. Description

Given an `m x n` grid of characters `board` and a string `word`, return `true` *if* `word` *exists in the grid*.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

### 2. Function Contract

**Inputs**

- `board`: A rectangular grid of uppercase or lowercase English letters.
- `word`: The letter sequence to construct.

**Return value**

Return `true` if one non-reusing, horizontally or vertically adjacent cell path spells `word`; otherwise return `false`.

### 3. Examples

#### Example 1

![](images/word2.jpg)

- **Input:** $board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"$
- **Output:** `true`

#### Example 2

![](images/word-1.jpg)

- **Input:** $board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"$
- **Output:** `true`

#### Example 3

![](images/word3.jpg)

- **Input:** $board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"$
- **Output:** `false`

### 4. Constraints

- $m = \text{board.length}$

- $n = \text{board}[i].length$

- $1 \le m, n \le 6$

- $1 \le \text{word.length} \le 15$

- `board` and `word` consists of only lowercase and uppercase English letters.

**Follow up:** Could you use search pruning to make your solution faster with a larger `board`?
