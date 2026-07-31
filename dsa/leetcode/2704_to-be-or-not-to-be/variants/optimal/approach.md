## General

The outer `expect` call creates an object whose two methods close over `val`. This retains the original value without exposing mutable assertion state or requiring a class.

`toBe` compares its argument with `val` using `===`. If the comparison fails, it throws `new Error("Not Equal")`; otherwise it returns `true`. `notToBe` uses the complementary `===` test: equality triggers `new Error("Equal")`, and inequality returns `true`.

Using strict equality is essential because the contract names `===` and `!==`. Coercive comparison would incorrectly make values such as `5` and `"5"` equal. Each method has only the two required outcomes, and failed assertions throw rather than returning a boolean, so the returned object exactly implements both behaviors.

## Complexity detail

Creating the assertion object and invoking either method use a fixed number of property, comparison, and return-or-throw operations. Time is therefore $O(1)$ per call, and the closure plus two fixed methods use $O(1)$ space. The complexity certificate records the matching $\Omega(1)$ lower bound and boundary behavior instead of a meaningless runtime scaling test.

## Alternatives and edge cases

- **Loose equality:** Using `==` or `!=` permits type coercion and violates the explicitly required strict comparisons.
- **Return `false` on failure:** This resembles a predicate but does not satisfy the assertion contract, which requires an `Error` with an exact message.
- **Store the value on `this`:** A class or mutable object property can work, but a closure is smaller and prevents method call context from affecting the captured value.
- The two error messages are case-sensitive and belong to opposite assertion failures.
- Objects and arrays compare by reference under strict equality, not by structural content.
- `null`, booleans, strings, and numbers must retain their ordinary JavaScript strict-equality semantics.
- A successful assertion always returns the boolean `true`.
