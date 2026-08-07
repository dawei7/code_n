### 1. Description

You are given an array of `k` linked-lists `lists`, each linked-list is sorted in ascending order.

*Merge all the linked-lists into one sorted linked-list and return it.*

### 2. Function Contract

**Inputs**

- `lists`: The array of ascending-sorted linked-list heads.

Let $k = \lvert\texttt{lists}\rvert$.

**Return value**

Return the head of one ascending-sorted list containing every input node.

### 3. Examples

#### Example 1

- **Input:** $lists = [[1,4,5],[1,3,4],[2,6]]$
- **Output:** `[1,1,2,3,4,4,5,6]`
- **Explanation:** The linked-lists are:
[
1->4->5,
1->3->4,
2->6
]
merging them into one sorted linked list:
1->1->2->3->4->4->5->6
#### Example 2

- **Input:** $lists = []$
- **Output:** `[]`
#### Example 3

- **Input:** $lists = [[]]$
- **Output:** `[]`

### 4. Constraints

- $k = \text{lists.length}$

- $0 \le k \le 10^{4}$

- $0 \le \text{lists}[i].length \le 500$

- $-10^{4} \le \text{lists}[i][j] \le 10^{4}$

- $\text{lists}[i]$ is sorted in **ascending order**.

- The sum of $\text{lists}[i].length$ will not exceed $10^{4}$.