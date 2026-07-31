## General

The reducer defines a sequence of dependent state updates: the input to one call is the output of the preceding call. Initialize one variable to `init`, then visit `nums` from left to right and replace that variable with `fn(accumulator, value)` for each element.

**The accumulator represents the processed prefix**

Before the loop, the accumulator is `init`, which is exactly the reduction result for an empty prefix. After processing `nums[i]`, it equals the contract's nested application of `fn` through the prefix ending at index `i`. The next iteration therefore supplies the required previous result and next element in the correct argument order.

When the traversal finishes, the processed prefix is the entire array, so the accumulator is the requested final value. If the array is empty, the loop performs no updates and the unchanged `init` value is returned, also matching the contract.

## Complexity detail

Let $n$ be the length of `nums` and treat one reducer call as $O(1)$. The algorithm makes exactly $n$ calls and otherwise does constant work per element, for $O(n)$ time. It stores only one accumulator and the current element, so its auxiliary space is $O(1)$.

## Alternatives and edge cases

- **Indexed loop:** Iterating by index is equally optimal and may make the exact call count especially explicit, but it does not change the state transition.
- **Built-in `Array.reduce`:** It implements the same fold directly but is forbidden by the problem contract.
- **Copy plus repeated `shift()`:** Consuming a copied array from the front preserves the original and produces the right value, but front removals can reindex all remaining elements and make the traversal $O(n^2)$.
- **Recursive fold:** Recursing once per element preserves order, but it uses $O(n)$ call-stack space and can overflow on large inputs.
- **Empty input:** Return `init` without invoking `fn`; a reducer with side effects must therefore be called zero times.
- **Order-sensitive reducers:** Do not regroup, reverse, or parallelize calls. Subtraction and similar reducers demonstrate that only the specified left-to-right sequence is valid.
- **Initial value:** Always begin with `init`, even for a nonempty array; the first element is never used as an implicit accumulator.
