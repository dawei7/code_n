## Function Contract

**Platform interface**

- `Node.evaluate()` abstract method returning the integer evaluation of the expression tree rooted at `self`.
- `TreeBuilder.buildTree(postfix)` builds and returns the root `Node` of the expression tree constructed from a postfix token array.

**Return value**

`evaluate()` returns an integer value representing the evaluated result of the expression.
