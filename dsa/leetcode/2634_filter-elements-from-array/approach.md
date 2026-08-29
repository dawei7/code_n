## General

**Filtering decides inclusion without transforming the value**

For every source position $i$, callback `fn(arr[i], i)` decides whether the original element belongs in the result.

The callback's return value is interpreted through JavaScript truthiness:

$$
\text{include }\texttt{arr[i]}
\quad\Longleftrightarrow\quad
\texttt{Boolean(fn(arr[i], i))}=\texttt{true}.
$$

If included, the output receives `arr[i]` itself—not the callback's result. This distinguishes filtering from mapping.

**Build a new output array**

`filtered` starts empty. The indexed loop visits every original position from zero through `arr.length - 1`.

At each position, the code evaluates the callback exactly once:

`if (fn(arr[index], index))`.

JavaScript's `if` condition automatically applies Boolean coercion. If the result is truthy, `filtered.push(arr[index])` appends the original source value. Otherwise, the loop advances without appending.

The source is never overwritten or shortened.

**Why both value and index are passed**

Some predicates depend only on the element, such as `n => n > 10`. Others depend on where the element appears, such as `(n, i) => i === 0`.

The exact call supplies both arguments in the required order:

- first: current value;
- second: current numeric index.

A JavaScript callback declaring only one parameter simply ignores the extra index. Supplying both therefore supports both allowed forms without inspecting `fn.length`.

**Truthiness is broader than Boolean true**

The callback does not need to return literal `true` or `false`. JavaScript treats values such as nonzero numbers and nonempty strings as truthy, while zero, an empty string, null, undefined, false, and `NaN` are falsy.

In the example callback `n => n + 1`:

- input $-2$ returns $-1$, which is truthy, so $-2$ is kept;
- input $-1$ returns zero, which is falsy, so $-1$ is removed;
- input zero returns one, which is truthy, so zero is kept.

Notice that the source element zero can be retained. It is the callback result, not the element itself, whose truthiness controls inclusion.

**Stable order follows from appending**

The loop visits indices in increasing order, and accepted values are always pushed to the end of `filtered`.

If accepted source indices are:

$$
i_0<i_1<\cdots<i_k,
$$

the output becomes:

$$
[\texttt{arr}[i_0],\texttt{arr}[i_1],\ldots,\texttt{arr}[i_k]].
$$

Thus filtering preserves relative order automatically. No sorting step is needed or allowed.

**Why every element needs one predicate evaluation**

`fn` is arbitrary. Without calling it for position $i$, the algorithm cannot know whether that element belongs in the result.

The exact solution performs the minimum necessary number of callback calls: one per array element. It neither re-evaluates accepted items nor calls the predicate after constructing the result.

If the callback has side effects, those effects occur once per element in left-to-right order.

**Trace the greater-than-ten example**

For `arr = [0,10,20,30]`:

- predicate on zero is false, so append nothing;
- predicate on ten is false;
- predicate on twenty is true, so append twenty;
- predicate on thirty is true, so append thirty.

The returned array is `[20,30]`. The original remains `[0,10,20,30]`.

**Trace an index-based predicate**

For `arr = [1,2,3]` and predicate `(n,i) => i === 0`:

- index zero returns true and appends one;
- indices one and two return false.

The result is `[1]` even though the callback does not need the numerical values.

**Loop invariant proves correctness**

Before iteration $i$, maintain:

> `filtered` contains exactly the elements from source prefix `arr[0..i-1]` whose callback results were truthy, in original order.

The empty prefix makes this true initially. At index $i$, a falsy result correctly leaves the output unchanged; a truthy result appends exactly the current source element after all earlier accepted elements. The invariant is preserved.

After the final index, the prefix is the complete array, so `filtered` is the required output.

**Why preallocation is not necessary**

The final number of accepted items is not known until predicates run. Dynamic `push` grows the result as needed and is amortized constant time per accepted item.

One could allocate length $n$ and track a write index, then shrink the result. That may reduce some resizing overhead but does not improve asymptotic complexity and adds bookkeeping.

**Dense-array assumption**

The problem provides an integer array, so each index from zero to length minus one contains a value. The explicit indexed loop invokes `fn` for every such position.

JavaScript's built-in `filter` has nuanced behavior around sparse-array holes, but those semantics are irrelevant to the valid input domain.

## Complexity detail

Let $n=\texttt{arr.length}$. The loop performs $n$ callback calls and constant additional work per element. Assuming `fn` is $O(1)$, time is $O(n)$.

In the worst case every item is accepted, so the returned array holds $n$ values and uses $O(n)$ output space. Aside from output, loop variables use $O(1)$ auxiliary space.

The input array is not mutated.

## Alternatives and edge cases

- **Built-in `Array.filter`:** Provides the same core behavior but is explicitly forbidden.
- **Preallocated output:** Store accepted values at a write pointer and truncate; same $O(n)$ bounds with more bookkeeping.
- **In-place compaction:** Can use $O(1)$ extra space but mutates the source, unlike the exact solution.
- **Empty array:** No callback calls occur and a new empty array is returned.
- **All predicates false:** The output stays empty.
- **All predicates true:** Every original value appears in source order.
- **Index-dependent callback:** Passing the numeric index is required for correct decisions.
- **Non-Boolean callback result:** Ordinary JavaScript truthiness determines inclusion.
- **Falsy source value:** It may still be kept when the callback result is truthy.
- **Callback side effects:** They occur exactly once per element from left to right.
