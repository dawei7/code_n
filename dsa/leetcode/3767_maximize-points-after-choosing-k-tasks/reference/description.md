## Description

You are given two integer arrays, `technique1` and `technique2`, each of length `n`, where `n` represents the number of tasks to complete.

- If the $$i^{\text{th}}$$task is completed using technique 1, you earn$\text{technique1}[i]$ points.

- If it is completed using technique 2, you earn $\text{technique2}[i]$ points.

You are also given an integer `k`, representing the **minimum** number of tasks that **must** be completed using technique 1.

You **must** complete **at least** `k` tasks using technique 1 (they do not need to be the first `k` tasks).

The remaining tasks may be completed using **either** technique.

Return an integer denoting the **maximum total points** you can earn.
### Function Contract

**Inputs**

- `technique1`: Points earned by using technique 1 on each task.
- `technique2`: Points earned by using technique 2 on the corresponding tasks.
- `k`: The inclusive lower bound on how many tasks must use technique 1.

The arrays have the same nonzero length. Choices are independent across indices except for the global technique-1 quota. Let $N$ be their common length and let $K = \texttt{k}$.

**Return value**

Return the greatest possible sum of the selected point values. More than `k` tasks may—and should—use technique 1 whenever doing so increases the total.

### Examples
#### Example 1

<div class="example-block">
**Input:** technique1 = [5,2,10], technique2 = [10,3,8], k = 2

**Output:** 22

**Explanation:**

We must complete at least $k = 2$ tasks using `technique1`.

Choosing $\text{technique1}[1]$ and $\text{technique1}[2]$ (completed using technique 1), and $\text{technique2}[0]$ (completed using technique 2), yields the maximum points: $2 + 10 + 10 = 22$.

</div>
#### Example 2

<div class="example-block">
**Input:** technique1 = [10,20,30], technique2 = [5,15,25], k = 2

**Output:** 60

**Explanation:**

We must complete at least $k = 2$ tasks using `technique1`.

Choosing all tasks using technique 1 yields the maximum points: $10 + 20 + 30 = 60$.

</div>
#### Example 3

<div class="example-block">
**Input:** technique1 = [1,2,3], technique2 = [4,5,6], k = 0

**Output:** 15

**Explanation:**

Since $k = 0$, we are not required to choose any task using `technique1`.

Choosing all tasks using technique 2 yields the maximum points: $4 + 5 + 6 = 15$.

</div>
### Constraints

- $1 \le n = \text{technique1.length} = \text{technique2.length} \le 10^{5}$

- $1 \le \text{technique1}[i], technique2​​​​​​​[i] \le 10^​​​​​​​5$

- $0 \le k \le n$