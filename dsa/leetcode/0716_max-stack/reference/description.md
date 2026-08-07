## Description

Design a max stack data structure that supports the stack operations and supports finding the stack's maximum element.

Implement the `MaxStack` class:

- `MaxStack()` Initializes the stack object.

- `void push(int x)` Pushes element `x` onto the stack.

- `int pop()` Removes the element on top of the stack and returns it.

- `int top()` Gets the element on the top of the stack without removing it.

- `int peekMax()` Retrieves the maximum element in the stack without removing it.

- `int popMax()` Retrieves the maximum element in the stack and removes it. If there is more than one maximum element, only remove the **top-most** one.

You must come up with a solution that supports `O(1)` for each `top` call and `O(logn)` for each other call.
### Function Contract

`solve(operations: list[list]) -> list[int]`

**Inputs**

- `operations`: an ordered sequence of app-adapted calls. A `push` row contains its integer argument; every other row contains only the operation name.

**Source operations**

- `MaxStack()`: initialize an empty max stack.
- `push(x)`: place `x` on the stack top and return nothing.
- `pop()`: remove and return the current top element.
- `top()`: return the current top element without removing it.
- `peekMax()`: return the greatest stored value without removing it.
- `popMax()`: remove and return the greatest stored value. If that value occurs more than once, remove its top-most occurrence.

**Return value**

The app adapter constructs one `MaxStack`, executes the rows in order, and returns the result of every call other than `push`. Source-style constructor and `push` results are `null`; the app omits those entries from its returned list.

### Examples
#### Example 1

```
**Input**
["MaxStack", "push", "push", "push", "top", "popMax", "top", "peekMax", "pop", "top"]
[[], [5], [1], [5], [], [], [], [], [], []]
**Output**
[null, null, null, null, 5, 5, 1, 5, 1, 5]

**Explanation**
MaxStack stk = new MaxStack();
stk.push(5);   // [**<u>5</u>**] the top of the stack and the maximum number is 5.
stk.push(1);   // [<u>5</u>, **1**] the top of the stack is 1, but the maximum is 5.
stk.push(5);   // [5, 1, **<u>5</u>**] the top of the stack is 5, which is also the maximum, because it is the top most one.
stk.top();     // return 5, [5, 1, **<u>5</u>**] the stack did not change.
stk.popMax();  // return 5, [<u>5</u>, **1**] the stack is changed now, and the top is different from the max.
stk.top();     // return 1, [<u>5</u>, **1**] the stack did not change.
stk.peekMax(); // return 5, [<u>5</u>, **1**] the stack did not change.
stk.pop();     // return 1, [**<u>5</u>**] the top of the stack and the max element is now 5.
stk.top();     // return 5, [**<u>5</u>**] the stack did not change.
```
### Constraints

- $-10^{7} \le x \le 10^{7}$

- At most $10^{5}$ calls will be made to `push`, `pop`, `top`, `peekMax`, and `popMax`.

- There will be **at least one element** in the stack when `pop`, `top`, `peekMax`, or `popMax` is called.