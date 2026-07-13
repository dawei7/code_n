# Integer Break

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 343 |
| Difficulty | Medium |
| Topics | Math, Dynamic Programming |
| Official Link | [LeetCode](https://leetcode.com/problems/integer-break/) |

## Problem Description
### Goal
Given an integer `n` from `2` through `58`, split it into a sum of at least two positive integers. You may choose any number of parts and may repeat the same part value when their total remains exactly `n`.

Return the maximum product obtainable by multiplying all chosen parts. The one-part decomposition `[n]` is forbidden even when it would have a larger product than a required split. Different decompositions may tie, and only the largest product is returned rather than the selected parts. Every part must be positive, so zero and negative padding are invalid.

### Function Contract
**Inputs**

- `n`: an integer from `2` through `58`

**Return value**

- The maximum product of a decomposition of `n` into two or more positive integers.

### Examples
**Example 1**

- Input: `n = 10`
- Output: `36`
- Explanation: $10 = 3 + 3 + 4$, whose product is $3 \cdot 3 \cdot 4 = 36$.

**Example 2**

- Input: `n = 3`
- Output: `2`

**Example 3**

- Input: `n = 2`
- Output: `1`

### Required Complexity

- **Time:** $O(\log n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Eliminate part sizes that cannot be optimal**

The search over all partitions disappears once we understand which part sizes can occur in an optimal product.

Any part $x \ge 5$ should be split into `3` and $x - 3$, because

$3(x - 3) \ge x$

for every $x \ge 5$, with a strict improvement beyond the boundary. Repeating this replacement eliminates all large parts. A part `1` is also never useful next to a part $x \ge 3$, since replacing $1 + x$ by $x + 1$ as a single part increases that local product from `x` to $x + 1$. Consequently, an optimal decomposition uses only `2`, `3`, and possibly `4`, where `4` may be viewed as $2 + 2$ without changing the product.

**Prefer threes without leaving a one**

Between `2`s and `3`s, three is more productive for the same sum: replacing $2 + 2 + 2$ with $3 + 3$ changes the product from `8` to `9`. Therefore take as many `3`s as possible, except when doing so would leave a remainder of `1`.

Let $n = 3q + r$:

- If $r = 0$, use `q` copies of `3`.
- If $r = 1$, replace one planned `3` and the leftover `1` with $2 + 2$, producing $3^{(q - 1)} \cdot 4$.
- If $r = 2$, keep the final `2`, producing $3^{q} \cdot 2$.

**Respect the mandatory split for small inputs**

The small inputs `2` and `3` need explicit handling because the problem requires at least two parts. Although leaving them whole would have the larger product, they must be split, giving answers `1` and `2` respectively.

**Trace the remainder-one repair**

For $n = 10$, division by three gives quotient `3` and remainder `1`. The remainder rule converts $3 + 1$ into $2 + 2$, leaving $3 + 3 + 2 + 2$ and product `36`. The replacement arguments exclude every other part size and show that each remainder case is optimal, rather than merely greedy.

#### Complexity detail

The formula performs one division and one exponentiation. Exponentiation by squaring uses $O(\log n)$ arithmetic multiplications and $O(1)$ explicit auxiliary storage in this implementation. Under the problem's fixed bound $n \le 58$, the number of operations and result width are also bounded constants.

#### Alternatives and edge cases

- **Dynamic programming over every first split:** uses $O(n^2)$ time and $O(n)$ space; it is useful for discovering the pattern but unnecessary after the mathematical structure is proven.
- **Enumerate integer partitions:** grows much faster and repeats equivalent choices in different orders.
- The mandatory split changes the answers for $n = 2$ and $n = 3$; neither value may be left whole.
- A remainder of one must not become its own factor: replace $3 + 1$ with $2 + 2$, improving the product from `3` to `4`.

</details>
