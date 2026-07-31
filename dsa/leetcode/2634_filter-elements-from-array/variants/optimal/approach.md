## General

Create an empty result array and inspect the source from index zero through `arr.length - 1`. At each position, call `fn(arr[index], index)` exactly once. JavaScript's `if` condition applies the required `Boolean` conversion automatically, so append the original value when that result is truthy.

**One left-to-right pass preserves relative order**

Every source element is considered once at its own numeric index. An element is appended if and only if its callback result passes the contract's truthiness test, establishing exact membership. Appends occur in increasing source-index order and never rearrange existing entries, so the relative order of all retained elements is preserved.

Return the separate result array after the scan. If the source is empty or no callback result is truthy, no append occurs and the correct result is the empty array.

## Complexity detail

Let $n$ be the source length and treat each callback evaluation as $O(1)$. The loop calls the callback once per element, giving $O(n)$ time. In the worst case every element is retained, so the returned array requires $O(n)$ space. Apart from the required output, the algorithm uses $O(1)$ auxiliary state.

## Alternatives and edge cases

- **Built-in `Array.filter`:** It provides the intended operation directly, but the problem explicitly forbids using it.
- **`reduce` with mutation:** Pushing into an accumulator is also $O(n),$ but a direct loop makes the callback arguments and truthiness decision clearer.
- **Spread on every match:** Replacing the result with `[...result, value]` is correct, but recopies all earlier matches and can require $O(n^2)$ time.
- **Empty input:** Return a new empty array without calling the callback.
- **Index-aware callbacks:** Pass the numeric position as the second argument; omitting it changes valid predicates such as `i === 0`.
- **Truthy rather than equal to `true`:** Test the callback result directly. Values such as nonzero numbers are truthy even though they are not the boolean `true`.
- **Falsy numeric zero:** A callback returning `0` rejects the element, including when the source value itself is otherwise valid.
- **Stable order:** Append matches during the left-to-right traversal and never sort the result.
