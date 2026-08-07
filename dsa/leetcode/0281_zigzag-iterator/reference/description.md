### 1. Description

Given two vectors of integers `v1` and `v2`, implement an iterator to return their elements alternately.

Implement the `ZigzagIterator` class:

- `ZigzagIterator(List<int> v1, List<int> v2)` initializes the object with the two vectors `v1` and `v2`.

- `boolean hasNext()` returns `true` if the iterator still has elements, and `false` otherwise.

- `int next()` returns the current element of the iterator and moves the iterator to the next element.

### 2. Function Contract

**Inputs**

- `v1`: The first integer vector.
- `v2`: The second integer vector.

**Return value**

The app adapter repeatedly calls the native iterator's `next()` method while `hasNext()` is true and returns the resulting list of integers.

### 3. Examples

#### Example 1

- **Input:** $v1 = [1,2], v2 = [3,4,5,6]$
- **Output:** `[1,3,2,4,5,6]`
- **Explanation:** By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,3,2,4,5,6].
#### Example 2

- **Input:** $v1 = [1], v2 = []$
- **Output:** `[1]`
#### Example 3

- **Input:** $v1 = [], v2 = [1]$
- **Output:** `[1]`

### 4. Constraints

- $0 \le \text{v1.length}, \text{v2.length} \le 1000$

- $1 \le \text{v1.length} + \text{v2.length} \le 2000$

- $-2^{31} \le \text{v1}[i], \text{v2}[i] \le 2^{31} - 1$

**Follow up:** What if you are given `k` vectors? How well can your code be extended to such cases?

**Clarification for the follow-up question:**

The "Zigzag" order is not clearly defined and is ambiguous for `k > 2` cases. If "Zigzag" does not look right to you, replace "Zigzag" with "Cyclic".

**Follow-up Example:**

- **Input:** $v1 = [1,2,3], v2 = [4,5,6,7], v3 = [8,9]$
- **Output:** `[1,4,8,2,5,9,3,6,7]`