# Convert Binary Number in a Linked List to Integer

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1290 |
| Difficulty | Easy |
| Topics | Linked List, Math |
| Official Link | [LeetCode](https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/) |

## Problem Description
### Goal
A nonempty singly-linked list stores the binary representation of a number. Every node contains either zero or one, and the head node holds the most significant bit. Moving toward the tail therefore moves from higher to lower binary place values.

Return the decimal integer represented by the complete linked list. The list contains at most 30 nodes, is guaranteed to be nonempty, and must be interpreted without changing the order of its bits.

### Function Contract
**Inputs**

- `head`: the first node of a nonempty singly-linked list containing $n$ binary digits, where $1 \le n \le 30$.

**Return value**

The nonnegative integer whose base-two digits, from most significant to least significant, are the node values encountered from `head` to the tail.

### Examples
**Example 1**

- Input: `head = [1,0,1]`
- Output: `5`
- Explanation: The stored binary number is $101_2$, which equals $5$.

**Example 2**

- Input: `head = [0]`
- Output: `0`

**Example 3**

- Input: `head = [1,1,1,1]`
- Output: `15`

### Required Complexity
- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

Process nodes from the head toward the tail while maintaining the integer represented by the prefix already visited. When the next bit is $b$, shifting the prefix left by one binary place and adding $b$ produces the value of the longer prefix. In executable arithmetic, update the accumulator with `value = value * 2 + node.val`.

The accumulator begins at zero, the value of the empty prefix. After every update it equals the exact binary value of all visited nodes. Once the tail has been processed, that prefix is the entire list, so the accumulator is the requested decimal value. This forward calculation avoids reversing the list or separately computing positional powers.

#### Complexity detail

The traversal visits each of the $n$ nodes exactly once and performs constant work per node, for $O(n)$ time. The accumulator and traversal pointer use $O(1)$ auxiliary space. Since the source contract limits $n$ to 30, the domain is too narrow for an honest measured scaling verdict; the package uses bounded-domain regression instead.

#### Alternatives and edge cases

- **Collect bits into a string:** Converting a binary string with a library routine is straightforward but uses $O(n)$ additional storage.
- **Reverse or recurse from the tail:** Positional powers can be accumulated from the least significant bit, but reversal mutates the list and recursion uses $O(n)$ stack space.
- **Single zero:** A one-node list containing zero returns zero.
- **Leading zeroes:** The recurrence naturally preserves the same numeric value while processing them.
- **Maximum length:** Thirty one-bits produce $2^{30}-1$, which remains within the stated domain.

</details>
