### 1. Description

You are given an integer array `ranks` and a character array `suits`. You have `5` cards where the $$i^{\text{th}}$$ card has a rank of $\text{ranks}[i]$ and a suit of $\text{suits}[i]$.

The following are the types of **poker hands** you can make from best to worst:

- `"Flush"`: Five cards of the same suit.

- `"Three of a Kind"`: Three cards of the same rank.

- `"Pair"`: Two cards of the same rank.

- `"High Card"`: Any single card.

Return *a string representing the **best** type of **poker hand** you can make with the given cards.*

### 2. Function Contract

**Inputs**

- `ranks`: Input parameter (`List[int]`).
- `suits`: Input parameter (`List[str]`).

**Return value**

- Returns `str`.

### 3. Note

that the return values are **case-sensitive**.

### 4. Examples

#### Example 1

- **Input:** $ranks = [13,2,3,1,9], suits = ["a","a","a","a","a"]$
- **Output:** `"Flush"`
- **Explanation:** The hand with all the cards consists of 5 cards with the same suit, so we have a "Flush".

#### Example 2

- **Input:** $ranks = [4,4,2,4,4], suits = ["d","a","a","b","c"]$
- **Output:** `"Three of a Kind"`
- **Explanation:** The hand with the first, second, and fourth card consists of 3 cards with the same rank, so we have a "Three of a Kind".
Note that we could also make a "Pair" hand but "Three of a Kind" is a better hand.
Also note that other cards could be used to make the "Three of a Kind" hand.

#### Example 3

- **Input:** $ranks = [10,10,2,12,9], suits = ["a","b","c","a","d"]$
- **Output:** `"Pair"`
- **Explanation:** The hand with the first and second card consists of 2 cards with the same rank, so we have a "Pair".
Note that we cannot make a "Flush" or a "Three of a Kind".

### 5. Constraints

- $\text{ranks.length} = \text{suits.length} = 5$

- $1 \le \text{ranks}[i] \le 13$

- $'a' \le \text{suits}[i] \le 'd'$

- No two cards have the same rank and suit.
