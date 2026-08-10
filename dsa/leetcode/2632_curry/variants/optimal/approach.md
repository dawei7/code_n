## General

**Collect arguments across an unknown number of calls**

A curried wrapper may receive the original function's parameters in any grouping:

- one at a time;
- several at once;
- empty batches between nonempty batches;
- all at once.

The original function should execute only when the total number of collected arguments reaches its declared arity `fn.length`.

The exact solution represents the history as immutable linked chunks rather than repeatedly copying one growing argument array.

**What `fn.length` means**

For a function with explicitly declared parameters, `fn.length` is its declared arity. A function `function sum(a, b, c)` has length three; `function life()` has length zero.

The problem guarantees explicitly defined parameters and a total supplied argument count matching this arity. Therefore, counting received positional arguments tells the wrapper when it has enough information to call `fn`.

**`extend` creates the next curried stage**

Helper `extend(previous, count)` returns a function named `curried`.

- `previous` points to the most recent stored argument chunk, or null at the beginning.
- `count` is the total number of arguments collected across that linked history.

Calling `extend(null, 0)` creates the initial wrapper with no history.

Every returned stage closes over its own `previous` and `count`. This makes its history persistent and private.

**Store one invocation as one linked node**

When a curried stage receives `...nextArgs`, it creates:

`const node = { previous, values: nextArgs }`.

This node stores only the new batch and a link to earlier batches. It does not concatenate all preceding arguments.

`total = count + nextArgs.length` computes how many arguments the full chain now contains.

If `total < fn.length`, the wrapper returns `extend(node, total)`, producing another function that remembers the newly extended history.

**Why linked chunks avoid repeated copying**

A simple implementation might build:

`allArgs = [...previousArgs, ...nextArgs]`

after every partial call. If arguments arrive one at a time, that copies one item, then two, then three, and so on:

$$
1+2+\cdots+n=O(n^2).
$$

The linked design stores each incoming argument exactly once in its batch array. Earlier chunks are referenced, not recopied. Flattening occurs only once, at final evaluation.

This is why the manifest includes both the number of arguments and the number of partial calls in a linear bound.

**Reconstruct original order at completion**

Nodes point backward, so traversing from the newest node visits chunks in reverse call order. The code first pushes each `current.values` array into `chunks` while following `current.previous` to null.

It then iterates `chunks` backward, from oldest to newest, and spreads each batch into `args`.

Suppose calls are `curried(1,2)(3)(4,5)`. The node traversal sees:

$$
[4,5], [3], [1,2].
$$

The reverse chunk loop appends:

$$
[1,2], [3], [4,5],
$$

producing final argument list `[1,2,3,4,5]`.

Only after this reconstruction does the solution call `fn(...args)`.

**Empty calls behave correctly**

A call with no arguments creates a node whose `values` array is empty and leaves `total` unchanged.

If more parameters are still needed, another curried function is returned. At completion, the empty chunk contributes nothing when spread. Thus `curried()()(1,2,3)` behaves exactly like `curried(1,2,3)`.

The empty nodes do add to the partial-call count $p$, which is honestly reflected in time and space analysis.

**Zero-arity functions**

If `fn.length === 0`, the initial returned function must be invoked once according to the contract. On that invocation, even with no arguments:

$$
\texttt{total}=0\ge0.
$$

The code enters the completion branch, reconstructs an empty argument list, and calls `fn()`. A function such as `life` then returns 42.

No special case is required.

**Immutable histories allow safe branching**

Because nodes are never modified, one partial stage can be reused:

- create `const addOne = curried(1)`;
- evaluate `addOne(2,3)`;
- separately evaluate `addOne(4,5)`.

Both new branches point to the same immutable first chunk but create different later nodes. Neither evaluation changes the other's history.

A single mutable shared argument array could accidentally mix these branches or become unusable after one completion. The linked representation has persistent-data-structure semantics.


For every function returned by `extend(previous, count)`:

- the linked nodes reachable from `previous` contain exactly all argument batches supplied so far;
- reading those nodes oldest to newest yields the original call order;
- `count` equals the sum of their batch lengths.

Creating a new node adds exactly the current batch and updates count by its length, preserving the invariant. Before completion, returning another `extend` retains this complete history.

At completion, reverse traversal reconstructs exactly the supplied argument sequence, so `fn(...args)` receives the same positional arguments as an ordinary direct call. This proves all allowed batching patterns produce the original result.

**Extra arguments**

The code tests `total >= fn.length` rather than strict equality. If an invocation supplied more arguments than the declared arity, all collected values would be forwarded to `fn`; JavaScript functions normally ignore extras unless they inspect `arguments` or rest parameters.

The constraints say the flattened input count equals `fn.length`, so challenge executions complete at equality.

## Complexity detail

Let $n$ be the total number of supplied arguments and $p$ the number of curried invocations, including empty calls.

Creating nodes and rest arrays across all partial calls stores $n$ argument entries and $p$ node objects. At completion, traversing chunks costs $O(p)$ and flattening arguments costs $O(n)$. Total time is $O(n+p)$ rather than quadratic.

Persistent history plus final temporary `chunks` and `args` arrays use $O(n+p)$ space. The helper does not recurse while reconstructing, so call-stack depth stays $O(1)$ during traversal.

## Alternatives and edge cases

- **Repeated array concatenation:** Simpler but can take $O(n^2)$ total copying when arguments arrive one at a time.
- **One mutable collection:** Linear for a single chain but makes branching from a partial curried function unsafe.
- **`Function.bind` accumulation:** Can implement partial application but may obscure arity and batching behavior.
- **Empty argument batch:** It advances the call chain without increasing the collected count.
- **All arguments at once:** Completion occurs on the first invocation.
- **One argument per call:** Nodes form a length-$n$ chain and are flattened once.
- **Zero-arity function:** The first empty invocation calls `fn()`.
- **Branched partial application:** Immutable linked nodes let branches share history safely.
- **Argument order:** Backward node traversal must be reversed before invoking `fn`.
- **Receiver context:** The exact `fn(...args)` call does not forward the curried wrapper's `this` because the contract is argument-based.
