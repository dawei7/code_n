## Description

You have one chocolate bar that consists of some chunks. Each chunk has its own sweetness given by the array `sweetness`.

You want to share the chocolate with your `k` friends so you start cutting the chocolate bar into $k + 1$ pieces using `k` cuts, each piece consists of some **consecutive** chunks.

Being generous, you will eat the piece with the **minimum total sweetness** and give the other pieces to your friends.

Find the **maximum total sweetness** of the piece you can get by cutting the chocolate bar optimally.
### Function Contract

**Inputs**

- `sweetness`: The sweetness values of the chocolate chunks in their fixed order.
- `k`: The number of friends and the exact number of cuts to make.

Let $n = \lvert\texttt{sweetness}\rvert$. Exactly `k` cuts divide the bar into `k + 1` nonempty contiguous pieces. Define the total sweetness as

$$
S = \sum_{i=0}^{n-1} \texttt{sweetness[i]}.
$$

After the division, your piece is the one with minimum total sweetness among all pieces.

**Return value**

Return the greatest minimum piece sweetness achievable over every valid placement of the `k` cuts.

### Examples
#### Example 1

- **Input:** $sweetness = [1,2,3,4,5,6,7,8,9], k = 5$
- **Output:** `6`
- **Explanation:** You can divide the chocolate to [1,2,3], [4,5], [6], [7], [8], [9]
#### Example 2

- **Input:** $sweetness = [5,6,7,8,9,1,2,3,4], k = 8$
- **Output:** `1`
- **Explanation:** There is only one way to cut the bar into 9 pieces.
#### Example 3

- **Input:** $sweetness = [1,2,2,1,2,2,1,2,2], k = 2$
- **Output:** `5`
- **Explanation:** You can divide the chocolate to [1,2,2], [1,2,2], [1,2,2]
### Constraints

- $0 \le k < \text{sweetness.length} \le 10^{4}$

- $1 \le \text{sweetness}[i] \le 10^{5}$