## General

**Traverse the receiver directly**

The method is installed on `Array.prototype`, so inside a normal function expression `this` is the array on which `forEach` was called. Walk integer indices from `0` through `this.length - 1`. At index `i`, the required callback arguments are exactly `this[i]`, `i`, and `this`.

This loop reaches every element once and in increasing index order. Passing the receiver itself as the third argument means callback mutations affect the same array rather than a copy. Because the value expression `this[i]` is evaluated at invocation time, a later callback can observe changes that an earlier callback made to a future position.

**Bind the requested callback context**

Calling `callback(...)` directly would choose its `this` value from ordinary JavaScript call semantics. Instead use `callback.call(context, currentValue, index, array)`. The first argument to `call` establishes the requested function context, while the remaining arguments preserve the exact callback signature.

No explicit return statement is needed. JavaScript then returns `undefined`, as required. Since the loop invokes the callback for every index and each invocation receives the correct value, index, array reference, and context, all required observable behavior is produced.

## Complexity detail

Let $n$ be `arr.length`. The method performs one traversal and one callback invocation per element, giving $O(n)$ traversal time in addition to whatever work the supplied callback performs. It stores only the loop index, so auxiliary space is $O(1)$.

Every element must trigger an observable callback call, establishing an $\Omega(n)$ lower bound. The accepted implementation matches it, so an asymptotic-optimality certificate replaces runtime scaling.

## Alternatives and edge cases

- **Delegate to the built-in `forEach`:** This defeats the purpose of implementing the method and becomes recursive after replacing the prototype property.
- **Use `map` or `reduce`:** These are also built-in array methods, allocate or accumulate unnecessary results, and do not match the required void contract.
- **Copy the array before traversal:** A copy prevents the callback's third argument from being the actual receiver and hides live mutations.
- An empty array performs no callback calls and still returns `undefined`.
- Use a normal function for the prototype method so `this` is determined by the receiving array; an arrow function would capture lexical `this`.
- Use `callback.call`, not an arrow wrapper that accidentally fixes or discards the requested callback context.
- The callback's return value is ignored; only its side effects matter.
- Mutating an existing element is visible to subsequent iterations because the original array reference is passed each time.
