## Description

You are given two integer arrays `forward` and `backward`, both of size `n`. You are also given another integer array `queries`.

There are `n` houses *arranged in a circle*. The houses are connected via roads in a special arrangement:

- For all $0 \le i \le n - 2$, house `i` is connected to house $i + 1$ via a road with length $\text{forward}[i]$ meters. Additionally, house $n - 1$ is connected back to house 0 via a road with length $forward[n - 1]$ meters, completing the circle.

- For all $1 \le i \le n - 1$, house `i` is connected to house $i - 1$ via a road with length $\text{backward}[i]$ meters. Additionally, house 0 is connected back to house $n - 1$ via a road with length $\text{backward}[0]$ meters, completing the circle.

You can walk at a pace of **one** meter per second. Starting from house 0, find the **minimum** time taken to visit each house in the order specified by `queries`.

Return the **minimum** total time taken to visit the houses.
### Function Contract

- Refer to method signature.

### Examples
#### Example 1

<div class="example-block">
**Input:** forward = [1,4,4], backward = [4,1,2], queries = [1,2,0,2]

**Output:** 12

**Explanation:**

The path followed is $<u>0</u>^(0) → <u>1</u>^(1) →​​​​​​​ <u>2</u>^(5) <u>→</u> 1^(7) <u>→</u>​​​​​​​ <u>0</u>^(8) <u>→</u> <u>2</u>^(12)$.

**Note:** The notation used is $node^(total time)$, `→` represents forward road, and `<u>→</u>` represents backward road.

</div>
#### Example 2

<div class="example-block">
**Input:** forward = [1,1,1,1], backward = [2,2,2,2], queries = [1,2,3,0]

**Output:** 4

**Explanation:**

The path travelled is `<u>0</u> →​​​​​​​ <u>1</u> →​​​​​​​ <u>2</u> →​​​​​​​ <u>3</u> → <u>0</u>`. Each step is in the forward direction and requires 1 second.

</div>
### Constraints

- $2 \le n \le 10^{5}$

- $n = \text{forward.length} = \text{backward.length}$

- $1 \le \text{forward}[i], \text{backward}[i] \le 10^{5}$

- $1 \le \text{queries.length} \le 10^{5}$

- $0 \le \text{queries}[i] < n$

- $\text{queries}[i] \neq queries[i + 1]$

- $\text{queries}[0]$ is not 0.