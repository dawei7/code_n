### 1. Description

Given a non-negative integer represented as a linked list of digits, *plus one to the integer*.

The digits are stored such that the most significant digit is at the `head` of the list.

### 2. Function Contract

**Inputs**

- `head`: The first node of the most-significant-digit-first linked-list representation; cOde(n) cases serialize the chain as a list of values.

**Return value**

Return the head of a linked list representing the original nonnegative integer plus one, including any carry that creates a new leading digit.

### 3. Examples

#### Example 1

- **Input:** $head = [1,2,3]$
- **Output:** `[1,2,4]`

#### Example 2

- **Input:** $head = [0]$
- **Output:** `[1]`

### 4. Constraints

- The number of nodes in the linked list is in the range `[1, 100]`.

- $0 \le \text{Node.val} \le 9$

- The number represented by the linked list does not contain leading zeros except for the zero itself.
