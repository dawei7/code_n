# Insert Greatest Common Divisors in Linked List

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2807 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Linked List, Math, Number Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/) |

## Problem Description

### Goal

You are given the head of a nonempty singly linked list whose nodes contain positive integers. Modify the list by inserting one new node between every pair of nodes that were adjacent in the original list. The inserted node's value must be the greatest common divisor of the two neighboring original values.

The greatest common divisor of two positive integers is the largest positive integer that divides both without a remainder. Preserve every original node and its order, connect all inserted nodes into the same list, and return the head of the resulting list. A one-node list has no adjacent pair and therefore remains unchanged.

### Function Contract

**Inputs**

- `head`: The first node of a singly linked list containing $n$ nodes, where $1 \leq n \leq 5000$ and each node value is between $1$ and $1000$, inclusive. App-local cases serialize the list as an integer array.

Let $V$ denote the largest node value.

**Return value**

Return the original head after inserting a new GCD-valued node between each pair of originally adjacent nodes. App-local output is the serialized sequence of values.

### Examples

#### Example 1

- **Input:** `head = [18, 6, 10, 3]`
- **Output:** `[18, 6, 6, 2, 10, 1, 3]`
- **Explanation:** The inserted values are $\gcd(18,6)=6$, $\gcd(6,10)=2$, and $\gcd(10,3)=1$.

#### Example 2

- **Input:** `head = [7]`
- **Output:** `[7]`
- **Explanation:** A single node has no adjacent pair, so nothing is inserted.

#### Example 3

- **Input:** `head = [50, 28]`
- **Output:** `[50, 2, 28]`
- **Explanation:** The only inserted node contains $\gcd(50,28)=2$.
