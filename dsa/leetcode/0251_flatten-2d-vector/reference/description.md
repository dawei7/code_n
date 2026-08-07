## Description

Design an iterator to flatten a 2D vector. It should support the `next` and `hasNext` operations.

Implement the `Vector2D` class:

- `Vector2D(int[][] vec)` initializes the object with the 2D vector `vec`.

- `next()` returns the next element from the 2D vector and moves the pointer one step forward. You may assume that all the calls to `next` are valid.

- `hasNext()` returns `true` if there are still some elements in the vector, and `false` otherwise.
### Function Contract

**Class Interface**

`Vector2D`

**Methods**

- $__init__(vec: List[\text{List}[int]])$: Initializes the object with 2D vector `vec`.
- `next() -> int`: Returns next element from 2D vector and moves pointer forward.
- `hasNext() -> bool`: Returns `true` if there are remaining elements, otherwise `false`.

### Examples

#### Example 1

```
**Input**
["Vector2D", "next", "next", "next", "hasNext", "hasNext", "next", "hasNext"]
[[[[1, 2], [3], [4]]], [], [], [], [], [], [], []]
**Output**
[null, 1, 2, 3, true, true, 4, false]

**Explanation**
Vector2D vector2D = new Vector2D([[1, 2], [3], [4]]);
vector2D.next();    // return 1
vector2D.next();    // return 2
vector2D.next();    // return 3
vector2D.hasNext(); // return True
vector2D.hasNext(); // return True
vector2D.next();    // return 4
vector2D.hasNext(); // return False
```
### Constraints

- $0 \le \text{vec.length} \le 200$

- $0 \le \text{vec}[i].length \le 500$

- $-500 \le \text{vec}[i][j] \le 500$

- At most $10^{5}$ calls will be made to `next` and `hasNext`.

**Follow up:** As an added challenge, try to code it using only <a href="http://www.cplusplus.com/reference/iterator/iterator/" target="_blank">iterators in C++</a> or <a href="http://docs.oracle.com/javase/7/docs/api/java/util/Iterator.html" target="_blank">iterators in Java</a>.