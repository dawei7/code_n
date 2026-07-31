## General

Store the calculator's current numeric state in one instance property initialized by the constructor. Each arithmetic method replaces that property with the result of applying its operator and the supplied value.

After updating the property, return `this`. Because `this` is the same object on which the method was called, the next method in a chain observes the preceding operation's updated result. `getResult` is the terminal accessor and returns the property rather than the instance.

Division checks its argument before updating state. When it is zero, throw `new Error("Division by zero is not allowed")`; otherwise perform ordinary JavaScript division. Exponentiation uses the current result as the base. By induction over a chain, the stored property equals the left-to-right evaluation after every method: it is true after construction, and each method applies exactly its named operation to the prior value. Therefore `getResult` returns the requested outcome unless the required division error terminates evaluation.

## Complexity detail

Let $q$ be the number of actions. Every arithmetic call and `getResult` performs $O(1)$ work, so evaluating the full chain takes $O(q)$ time. The instance stores only one running number and uses $O(1)$ auxiliary space. The benchmark uses `size` as $q$.

## Alternatives and edge cases

- **Store an operation list:** Deferring evaluation can preserve chaining, but it requires $O(q)$ space and later replay instead of updating the result immediately.
- **Return a new calculator per method:** Immutable chaining is possible but allocates $O(q)$ short-lived objects and is not required.
- **Build and evaluate an expression string:** Repeated parsing or reevaluation adds unnecessary complexity and can become quadratic.
- Every arithmetic method must return the calculator instance, not the numeric result.
- Operations apply in chain order; multiplication and power do not receive mathematical precedence over earlier calls.
- Division by zero throws the exact required message before changing state.
- Fractional, negative, and exponentiated results use JavaScript numeric semantics.
- `getResult` returns a number and does not alter the stored state.
