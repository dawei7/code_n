## Description

Given an array of integers `arr` and an integer `d`. In one step you can jump from index `i` to index:

- $i + x$ where: $i + x < \text{arr.length}$ and $0 < x \le d$.

- $i - x$ where: $i - x \ge 0$ and $0 < x \le d$.

In addition, you can only jump from index `i` to index `j` if $\text{arr}[i] > \text{arr}[j]$ and $\text{arr}[i] > \text{arr}[k]$ for all indices `k` between `i` and `j` (More formally `min(i, j) < k < max(i, j)`).

You can choose any index of the array and start jumping. Return *the maximum number of indices* you can visit.

Notice that you can not jump outside of the array at any time.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples

#### Example 1

![](images/meta-chart.jpeg)

- **Input:** `arr = [6,4,14,6,8,13,9,7,10,6,12], d = 2`
- **Output:** `4`
- **Explanation:** You can start at index 10. You can jump 10 --> 8 --> 6 --> 7 as shown.
Note that if you start at index 6 you can only jump to index 7. You cannot jump to index 5 because 13 > 9. You cannot jump to index 4 because index 5 is between index 4 and 6 and 13 > 9.
Similarly You cannot jump from index 3 to index 2 or index 1.
#### Example 2

- **Input:** `arr = [3,3,3,3,3], d = 3`
- **Output:** `1`
- **Explanation:** You can start at any index. You always cannot jump to any index.
#### Example 3

- **Input:** `arr = [7,6,5,4,3,2,1], d = 1`
- **Output:** `7`
- **Explanation:** Start at index 0. You can visit all the indicies.
### Constraints

- $1 \le \text{arr.length} \le 1000$

- $1 \le \text{arr}[i] \le 10^{5}$

- $1 \le d \le \text{arr.length}$