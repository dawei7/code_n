## General

**Define depth from the current container**

The outermost input array is visited with `depth = 0`. While scanning a container at depth $d$, a nested array value is expanded only when:

$$
d<n.
$$

If expanded, its contents are visited with depth $d+1$. If not expanded, that entire nested array is appended as one output value.

This convention matches the statement:

- with $n=0$, even arrays directly inside the outer array are not flattened;
- with $n=1$, those direct subarrays are flattened, but arrays nested inside them remain intact;
- larger $n$ permits correspondingly deeper expansion.

Thinking of `depth` as the number of array boundaries already flattened on the path avoids off-by-one confusion.

**Use one result array for the whole traversal**

`result` begins empty and is captured by recursive helper `visit`.

The helper loops through `values` from left to right. For each `value`:

- if it is an array and current `depth < n`, recurse into it;
- otherwise, append it to `result`.

All recursive calls write into the same output. This avoids constructing and repeatedly concatenating intermediate arrays, which could copy already-produced elements many times.

**Why `Array.isArray` is the right type test**

JavaScript reports arrays as objects under `typeof`. Therefore `typeof value === "object"` cannot distinguish a nested array from an ordinary object.

`Array.isArray(value)` performs the intended distinction. Only nested arrays are containers to flatten; numbers are appended, and under a broader JSON-style input an ordinary object would also remain a value.

The contract specifically describes integers and arrays, so every leaf is a number, but using the precise built-in predicate keeps the recursive rule explicit.

**Depth-first traversal preserves order**

When the helper decides to expand a subarray, it completely visits that subarray before continuing to the next value of the parent.

This is exactly the order produced by replacing a nested array in place with its contents. For parent sequence

`[A, [B, C], D]`,

flattening the middle array must yield `A, B, C, D`, not move its children after $D$.

Recursive depth-first traversal naturally maintains that left-to-right order at every nesting level.

**Trace the depth boundary**

Consider:

`[1, [2, [3, 4]], 5]`.

With $n=0$, the helper scans the outer container at depth zero. Since `depth < n` is false, it appends the nested `[2,[3,4]]` unchanged. The result has the same top-level structure.

With $n=1$, the outer helper sees the first nested array while $0<1$ and recurses at depth one. Inside it:

- two is appended;
- `[3,4]` is an array, but $1<1$ is false, so that subarray is appended intact.

The result is `[1,2,[3,4],5]`.

With $n=2$, the second array boundary is also expanded, producing `[1,2,3,4,5]`.

**Why unexpanded arrays remain the same values**

When the depth limit is reached, the code executes `result.push(value)`. It does not copy that subarray.

The returned outer array is new, but any nested array preserved by the depth limit is the same reference that appeared in the input. The problem asks for a flattened arrangement, not a deep clone.

This is observable only if code later mutates those nested arrays, but it accurately follows the exact solution.

**A structural induction proves correctness**

For a call `visit(values, depth)`, claim that it appends precisely the flattened representation of `values` allowed from that depth, in source order.

For each element:

- a leaf is appended directly, which is its correct representation;
- an array at or beyond the limit is appended directly, as no boundary may be removed;
- an array below the limit is delegated to `visit` at the next depth, which by the same claim appends exactly its permitted flattened contents.

Processing elements sequentially concatenates their correct representations in the required order. The outer call at depth zero therefore produces the requested result.

**Why every visited value is handled once**

If an array is expanded, the array container is inspected and its children are visited. If it is not expanded, the algorithm appends it and does not inspect its descendants.

No child can be reached through two different parents in the challenge's tree-shaped JSON input. Consequently, work is proportional to the portion of the nested structure actually traversed, plus the produced output.

**Recursion depth and the language stack**

The recursive helper mirrors the nesting structure and is easy to reason about. Its maximum active call depth is the smaller of the input nesting depth and the requested flattening depth, plus the outer call.

The constraints allow depth up to 1000. Many JavaScript runtimes can handle this in the challenge environment, but recursion limits are runtime-specific. An explicit stack can reproduce the same traversal if stack-overflow robustness is required.

**Why built-in `flat` is not used**

`Array.prototype.flat(n)` directly performs depth-limited flattening, but the prompt explicitly forbids it. Reimplementing the traversal demonstrates the depth test, ordering, and recursion mechanics that the built-in method would otherwise hide.

## Complexity detail

Let $V$ be the number of array containers and values actually visited, and let $R$ be the number of items placed in the result. The traversal performs constant work per visited item, so time is $O(V)$, with $R\le V$ under a node-count interpretation.

The result requires $O(R)$ space. The recursion stack uses $O(D)$ space, where $D$ is the expanded nesting depth. Together this is $O(R+D)$, conservatively written as $O(V+D)$ in the manifest.

The input is not mutated.

## Alternatives and edge cases

- **Explicit stack:** Avoid recursion-depth limits; push elements in reverse order so popping preserves left-to-right output.
- **Queue with repeated splicing:** Can preserve order but may shift or copy many elements and become inefficient.
- **Built-in `Array.flat`:** Direct but explicitly forbidden.
- **`n = 0`:** No nested array is expanded, though a new outer result array is still produced.
- **Depth exceeds maximum nesting:** Every subarray is flattened and all numeric leaves appear in order.
- **Empty outer array:** The traversal appends nothing and returns an empty array.
- **Empty nested array:** Expanding it contributes no values; preserving it at the limit contributes the empty array itself.
- **Preserved nested reference:** An unflattened subarray is appended without cloning.
- **Order preservation:** Complete each expanded subarray before continuing with its parent's next item.
- **Deep nesting:** Recursion uses one call frame per expanded level and may motivate an iterative stack in stricter runtimes.
