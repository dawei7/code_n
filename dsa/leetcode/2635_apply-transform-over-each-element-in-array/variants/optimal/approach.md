## General

**Mapping produces one output for every input position**

The required relationship is:

$$
\texttt{transformed[i]}
=
\texttt{fn(arr[i], i)}.
$$

Unlike filtering, mapping never decides whether to keep an element. Every source position contributes exactly one result, so output length always equals input length.

The callback result replaces the source value in the new array; the source itself remains unchanged.

**Create a separate result**

`transformed` begins as a new empty array. The loop runs `index` from zero while `index < arr.length`.

For each index, it evaluates:

`fn(arr[index], index)`

and immediately pushes that returned integer onto `transformed`.

Because one push occurs on every iteration, the $i$-th callback result becomes the $i$-th output element.

**Why the index is supplied**

Callbacks may depend only on value:

`n => n + 1`.

They may instead use both value and position:

`(n, i) => n + i`.

Passing both values supports either form. JavaScript ignores extra arguments when a function declares fewer parameters, so no branching based on callback arity is needed.

The order is important: `arr[index]` is the first argument, and `index` is the second.

**Trace a value-only transformation**

For `arr = [1,2,3]` and `fn(n) = n + 1`:

- index zero produces two;
- index one produces three;
- index two produces four.

The new array is `[2,3,4]`. The source remains `[1,2,3]`.

The callback is invoked three times even though its output rule is simple. The map helper does not inspect or optimize the callback's implementation.

**Trace an index-aware transformation**

For the same input and `fn(n,i) = n + i`:

- at index zero, $1+0=1$;
- at index one, $2+1=3$;
- at index two, $3+2=5$.

The result is `[1,3,5]`. Supplying a stale, one-based, or omitted index would produce the wrong sequence.

**A constant callback still runs once per item**

If `fn` always returns 42, every output position receives 42:

`[10,20,30]` becomes `[42,42,42]`.

Although a human can see that the callback is constant, it is an arbitrary function object to the mapping helper. Calling it once per source element preserves general semantics and any permitted side effects.

**Order and positional correspondence**

The indexed loop is strictly left to right. The first push creates output index zero, the second creates output index one, and so on.

There is no sorting and no conditional omission. Therefore, the returned array preserves positional correspondence even when transformed values themselves are equal or unrelated to source ordering.

This also means callbacks with side effects execute in deterministic source order.

**Loop invariant proves the exact result**

Before iteration $i$, maintain:

> `transformed` has length $i$, and for every $j<i$, `transformed[j] = fn(arr[j], j)` as evaluated during iteration $j$.

Initially, $i=0$ and the empty result satisfies the statement.

At iteration $i$, the code calls `fn(arr[i], i)` and pushes its result. The array length becomes $i+1$, earlier entries remain unchanged, and the required equality now also holds at $i$.

When the loop ends at $i=n$, the invariant covers every source index. The returned array has length $n$ and the required transformed value at each position.

**Why the source is not reused as output**

An in-place loop could assign:

`arr[index] = fn(arr[index], index)`.

That would use constant additional storage, but it would destroy the caller's original array. The problem asks for a new array, and the exact solution honors that expectation.

A separate result also prevents earlier transformations from changing later callback inputs through shared source positions.

**Why one pass is optimal**

Every output position depends on one callback evaluation for its corresponding input. With an arbitrary `fn`, no output can generally be inferred from another.

The algorithm performs exactly $n$ evaluations and one output write per result. Any correct method must produce $n$ values, giving an $\Omega(n)$ time and output-size lower bound.

**Dynamic append versus preallocation**

Using `push` grows a dense JavaScript array in order. Push is amortized $O(1)$, so $n$ pushes remain linear.

Because output length is known to equal input length, preallocating `new Array(arr.length)` and assigning by index would also be reasonable. The exact implementation chooses the concise append form without changing the asymptotic bound.

**Callback return type**

The contract guarantees that `fn` returns an integer. The mapping function itself does not validate or coerce that result; it stores exactly what the callback returns.

This separation of responsibility is correct: the helper controls traversal and argument passing, while the supplied callback controls transformation.

**Empty input**

When `arr.length` is zero, the loop condition is false immediately. The method returns the newly created empty `transformed` array and never invokes `fn`.

This satisfies the one-output-per-input rule with zero positions.

**Dense-array semantics**

The valid input is a standard integer array. The explicit loop visits every integer index.

For arbitrary sparse JavaScript arrays, this behavior would call `fn` on holes as undefined, whereas built-in `map` skips holes while preserving them. That distinction lies outside the stated domain but explains why this implementation should be understood against the challenge contract rather than every exotic array object.

## Complexity detail

Let $n=\texttt{arr.length}$. The loop executes once per element and invokes `fn` once each time. Assuming constant-time callback work, total time is $O(n)$.

The returned array always contains $n$ transformed values, so output space is $O(n)$. The loop index and current callback evaluation use $O(1)$ auxiliary space beyond the result.

The source array is read only.

## Alternatives and edge cases

- **Built-in `Array.map`:** Directly expresses the operation but is explicitly forbidden.
- **Preallocate result length:** Assign `transformed[index]` instead of pushing; same $O(n)$ bounds.
- **In-place transformation:** Saves output allocation but mutates the source and violates the new-array requirement.
- **Empty array:** Returns a new empty array without invoking `fn`.
- **Value-only callback:** The extra index argument is harmlessly ignored.
- **Index-aware callback:** Receives the correct zero-based source position.
- **Constant callback:** It still runs once per input and fills every result position.
- **Negative source values:** They are passed unchanged to `fn`; the mapping helper imposes no arithmetic assumption.
- **Repeated output values:** They remain separate positions, preserving output length.
- **Callback side effects:** They occur exactly once per source element in left-to-right order.
