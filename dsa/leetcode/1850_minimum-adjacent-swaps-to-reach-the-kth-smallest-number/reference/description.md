## Description

You are given a string `num`, representing a large integer, and an integer `k`.

We call some integer **wonderful** if it is a **permutation** of the digits in `num` and is **greater in value** than `num`. There can be many wonderful integers. However, we only care about the **smallest-valued** ones.

- For example, when $num = "5489355142"$:

		<li>The 1^st smallest wonderful integer is `"5489355214"`.

- The 2^nd smallest wonderful integer is `"5489355241"`.

- The 3^rd smallest wonderful integer is `"5489355412"`.

- The 4^th smallest wonderful integer is `"5489355421"`.

	</li>

Return *the **minimum number of adjacent digit swaps** that needs to be applied to *`num`* to reach the *$$k^{\text{th}}$$*** smallest wonderful** integer*.

The tests are generated in such a way that $$k^{\text{th}}$$ smallest wonderful integer exists.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples

#### Example 1

- **Input:** $num = "5489355142", k = 4$
- **Output:** `2`
- **Explanation:** The 4^th smallest wonderful number is "5489355421". To get this number:
- Swap index 7 with index 8: "5489355<u>14</u>2" -> "5489355<u>41</u>2"
- Swap index 8 with index 9: "54893554<u>12</u>" -> "54893554<u>21</u>"
#### Example 2

- **Input:** $num = "11112", k = 4$
- **Output:** `4`
- **Explanation:** The 4^th smallest wonderful number is "21111". To get this number:
- Swap index 3 with index 4: "111<u>12</u>" -> "111<u>21</u>"
- Swap index 2 with index 3: "11<u>12</u>1" -> "11<u>21</u>1"
- Swap index 1 with index 2: "1<u>12</u>11" -> "1<u>21</u>11"
- Swap index 0 with index 1: "<u>12</u>111" -> "<u>21</u>111"
#### Example 3

- **Input:** $num = "00123", k = 1$
- **Output:** `1`
- **Explanation:** The 1^st smallest wonderful number is "00132". To get this number:
- Swap index 3 with index 4: "001<u>23</u>" -> "001<u>32</u>"
### Constraints

- $2 \le \text{num.length} \le 1000$

- $1 \le k \le 1000$

- `num` only consists of digits.