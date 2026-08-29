### 1. Description

You are given an integer array `nums` and an integer `k`.

Initially, you have `k` units of resources.

You must process the elements of `nums` from left to right. To process the $i^{\text{th}}$ element, you need $\text{nums}[i]$ resources.

If your available resources are less than $\text{nums}[i]$, you may perform an operation that increases your available resources by `k`. The value of `k` is fixed and does not change throughout the process. The first such operation incurs a cost of 1, the second incurs a cost of 2, and so on.

After processing the $i^{\text{th}}$ element, your available resources decrease by $\text{nums}[i]$.

Return an integer denoting the **minimum total cost** required to process all elements. Since the answer may be very large, return it **modulo** $10^{9} + 7$.

### 2. Function Contract

`solve(nums, k) -> int`

Let $n=\lvert\texttt{nums}\rvert$ and let $M=$10^{9}$+7$.

**Inputs**

- `nums`: A nonempty array of positive resource requirements, processed in index order.
- `k`: The positive number of resource units initially available and added by every operation.

Before processing element `i`, one or more operations may be performed only when the current resource is less than $\text{nums}[i]$. If the operation being performed is the $j$-th operation overall, it costs $j$. Processing the element then decreases the resource by $\text{nums}[i]$.

**Output**

Return the minimum total cost of all operations needed to process every element, reduced modulo $M$.

### 3. Examples

#### Example 1

- **Input:** nums = [1,2,3,4], k = 4

- **Output:** 3

- **Explanation:** 

- After processing $\text{nums}[0]$, we have $4 - 1 = 3$ units of resources left.

- After processing $\text{nums}[1]$, we have $3 - 2 = 1$ unit of resources left.

- Since $\text{nums}[2] = 3$ and only 1 unit of resources is available, we perform the first operation costing 1. After processing $\text{nums}[2]$, we have $1 + 4 - 3 = 2$ units of resources left.

- Since $\text{nums}[3] = 4$ and only 2 units of resources are available, we perform the second operation costing 2, to have $2 + 4 = 6$ units of resources, which is enough to process $\text{nums}[3]$.

- Thus, the total cost is $1 + 2 = 3$.

#### Example 2

- **Input:** nums = [1,1,7,14], k = 4

- **Output:** 15

- **Explanation:** 

- After processing $\text{nums}[0]$, we have $4 - 1 = 3$ units of resources left.

- After processing $\text{nums}[1]$, we have $3 - 1 = 2$ units of resources left.

- Since $\text{nums}[2] = 7$ and only 2 units of resources are available, we perform two operations costing $1 + 2 = 3$. After processing $\text{nums}[2]$, we have $2 + 4 + 4 - 7 = 3$ units of resources left.

- Since $\text{nums}[3] = 14$ and only 3 units of resources are available, we perform three operations costing $3 + 4 + 5 = 12$, to have $3 + 4 + 4 + 4 = 15$ units of resources, which is enough to process $\text{nums}[3]$.

- Thus, the total cost is $3 + 12 = 15$.

#### Example 3

- **Input:** nums = [1,2,3,4], k = 10

- **Output:** 0

- **Explanation:** To process all elements, we can use the initial 10 units of resources without performing any operations. Thus, the total cost required is 0.

### 4. Constraints

- $1 \le \text{nums.length} \le 10^{5}$

- $1 \le \text{nums}[i] \le 10^{9}$

- $1 \le k \le 10^{9}$
