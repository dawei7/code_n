## General

`createHelloWorld` is a higher-order function because its return value is another function. Return an inner variadic function so callers may supply any permitted argument list. The inner function does not inspect those arguments; it immediately returns the exact string literal `"Hello World"`.

No mutable closure state is necessary. For every possible invocation, control reaches the same literal return statement, so the result has the required spelling, capitalization, and spacing regardless of argument count or contents. Creating multiple returned functions is also harmless because none of them share or modify state.

## Complexity detail

Creating the function and invoking it each take $O(1)$ time and retain only a fixed function object, giving $O(1)$ space. Although JavaScript receives an argument list, the implementation never iterates through or copies its elements, so its own work does not depend on the number of supplied arguments.

An asymptotic-optimality certificate verifies this bound: returning one value already requires $\Omega(1)$ work, and the accepted function performs exactly one constant literal return.

## Alternatives and edge cases

- **Named inner function:** Returning a named declaration behaves equivalently but adds a name that the contract does not require.
- **Capture a constant variable:** Storing the text in an outer binding also works, but returning the literal directly is simpler and needs no captured data.
- **Use an arrow function:** An arrow such as `() => "Hello World"` is valid, though the ordinary function form mirrors the supplied interface clearly.
- Calling with zero arguments must return the same value as calling with ten.
- Argument values may include `null`, objects, arrays, booleans, numbers, or strings; none should be inspected.
- The output is case-sensitive and contains exactly one space, with no punctuation or extra whitespace.
