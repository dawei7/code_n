### 1. Description

You are given the `head` of a linked list with `n` nodes.

For each node in the list, find the value of the **next greater node**. That is, for each node, find the value of the first node that is next to it and has a **strictly larger** value than it.

Return an integer array `answer` where $\text{answer}[i]$ is the value of the next greater node of the $$i^{\text{th}}$$ node (**1-indexed**). If the $$i^{\text{th}}$$ node does not have a next greater node, set $\text{answer}[i] = 0$.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

![](images/linkedlistnext1.jpg)

- **Input:** $head = [2,1,5]$
- **Output:** `[5,5,0]`
#### Example 2

![](images/linkedlistnext2.jpg)

- **Input:** $head = [2,7,4,3,5]$
- **Output:** `[7,0,5,5,0]`

### 4. Constraints

- The number of nodes in the list is `n`.

- $1 \le n \le 10^{4}$

- $1 \le \text{Node.val} \le 10^{9}$