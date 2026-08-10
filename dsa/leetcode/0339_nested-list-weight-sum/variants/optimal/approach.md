## General

**The recursive structure of the data already matches the calculation.**

Every `NestedInteger` is one of two things:

- an integer, which contributes its value multiplied by its current depth;
- a list, whose contained elements must be processed one level deeper.

The source mirrors those two cases with a recursive helper. It does not convert the interface objects into ordinary Python lists, flatten the input, or store a separate depth for every integer. The call stack naturally remembers which enclosing list is being processed.

**Define the helper's contract.**

`dfs(nestedList, depth)` returns the complete weighted sum of all integers contained in the supplied list, assuming elements directly inside that list have the given `depth`.

The public call is `dfs(nestedList, 1)`. This starting value is crucial because every top-level integer is inside the outer input list once and therefore has depth one. Starting at zero would underweight every integer by one level.

Inside a call, `depth_sum` begins at zero and accumulates the contributions of the list's direct elements. Each direct element is processed exactly once in the `for` loop.

**Handle an integer element.**

When `item.isInteger()` is true, `item.getInteger()` retrieves its stored value. Because the item is directly inside the list represented by the current call, its required contribution is

$$
\text{item.getInteger()}\times\text{depth}.
$$

The source adds that product to `depth_sum`. It does not recurse because an integer has no children.

The interface check must happen before calling `getInteger()`. The contract says that accessor returns an integer only when the object actually stores one. The source respects the abstraction instead of assuming how `NestedInteger` is implemented internally.

**Handle a nested-list element.**

When `item.isInteger()` is false, the object stores a nested list. `item.getList()` retrieves its direct children. Every integer anywhere inside that child list has one more enclosing list than elements in the current list, so the recursive call uses `depth + 1`.

The returned value is the complete weighted sum of that nested region and is added to the current accumulator:

`depth_sum += dfs(item.getList(), depth + 1)`.

This makes the recursion compositional. A parent does not need to inspect how deeply a child list continues. It only supplies the correct next depth, and the child call handles all remaining levels.

**Walk through `[1,[4,[6]]]`.**

The outer call begins at depth one.

- Integer `1` is directly inside the outer list, so it contributes $1\cdot1=1$.
- The object `[4,[6]]` is a list, so the helper recurses on it at depth two.
- Inside that call, integer `4` contributes $4\cdot2=8$.
- The object `[6]` causes another call at depth three.
- Integer `6` contributes $6\cdot3=18$.

The deepest call returns `18`. Its parent adds `8` and returns `26`. The outer call adds the top-level `1` and returns

$$
1+8+18=27.
$$

Notice that a list object has no numeric contribution by itself. Its only effect is to increase the depth of the elements contained beneath it.

**Why sibling lists do not affect each other's depth.**

The `depth` argument belongs to one call frame. Recursing with `depth + 1` creates a new argument value for that child call; it does not modify the parent's local `depth`. When the child returns, the next sibling is still processed at the correct parent depth.

This is safer than maintaining one mutable global depth counter, which would require carefully decrementing after every recursive return and could easily leak a deeper value into a sibling branch.

**Why the accumulated sum is correct.**

Use structural induction on a nested list.

For a list containing no elements, the loop performs no additions and returns zero, which is its correct contribution. For a nonempty list, assume every nested-list child call correctly returns the weighted sum of its contents at the supplied deeper depth.

Each direct integer contributes exactly its value times the current depth. Each direct list contributes exactly its recursively correct total at one greater depth. These direct elements are disjoint and together contain every integer below the current list. Adding their contributions therefore gives the current list's complete weighted sum.

The outer call applies this correct helper contract at depth one, so the returned value matches the problem's definition for every stored integer.

**The traversal does not confuse values with positions.**

Depth depends only on the number of enclosing lists, not on an element's index or on how many siblings appear before it. Negative integers are multiplied normally, zero contributes zero, and repeated values are each counted as distinct occurrences because each interface object is visited separately.

## Complexity detail

Let $N$ be the total number of `NestedInteger` elements across all list levels, counting both integer-holding objects and list-holding objects, and let $D$ be the maximum nesting depth.

Every element appears directly inside exactly one list, so exactly one loop iteration processes it. Integer work is constant, and each list object leads to one recursive call whose own loop handles different child elements. Total time complexity is $O(N)$.

The deepest active recursion chain contains one call per nested list level, so the call stack uses $O(D)$ auxiliary space. Each frame stores only a depth value, an accumulator, and iteration state. The source creates no structure proportional to the full input. Since $D\le N$, the worst-case space can also be stated as $O(N)$, but the tighter bound is $O(D)$ as listed in the manifest.

## Alternatives and edge cases

- **Breadth-first traversal:** Put all top-level objects in a queue, process one depth layer at a time, and enqueue child-list elements for the next layer. This also takes $O(N)$ time but can require $O(N)$ queue space for a wide level rather than the DFS stack's $O(D)$.

- **Explicit depth stack:** Store `(object, depth)` pairs and iteratively process them. It avoids recursion and retains $O(N)$ worst-case storage, which can be helpful if nesting exceeds the language's call-stack limit.

- **Flatten first:** Producing a list of `(integer, depth)` pairs and summing afterward works, but stores information that the recursive accumulation can consume immediately.

- **Top-level integer:** It is processed by the initial depth-one call and receives weight one.

- **Empty nested list:** Its recursive loop has no iterations and returns zero, so it has no effect on the sum.

- **Integer zero:** Its contribution is zero at every depth, but it is still handled correctly as an integer object.

- **Negative values:** Multiplication by depth preserves the negative sign, and normal addition includes the negative contribution as required.

- **Maximum depth:** The contract caps integer depth at `50`, so the recursive stack is shallow for valid inputs.

- **Interface discipline:** Call `getInteger()` only after `isInteger()` is true, and call `getList()` only in the list case. The source does not depend on any hidden representation of `NestedInteger`.
