## Function Contract

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
