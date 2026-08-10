## General

**A returned function needs persistent private state**

`createCounter(n)` finishes before the returned counter is called. Nevertheless, each future call must remember the value left by the previous call.

JavaScript closures provide exactly this behavior. A function retains access to variables from the lexical environment in which it was created, even after the outer function has returned.

The inner anonymous function closes over parameter `n`. That binding becomes the counter's private mutable state.

**Understand what the outer call creates**

Calling `createCounter(10)` performs two conceptual actions:

1. create a lexical binding `n` initialized to ten;
2. create and return an inner function that references that binding.

Because the returned function still needs `n`, JavaScript keeps the binding alive. It is not copied anew on every counter call, and it is not discarded when `createCounter` returns.

The caller receives only the function, not direct access to the enclosed variable. This gives simple encapsulation: the sequence can advance through calls, but outside code cannot normally assign the private `n` binding directly.

**Postfix increment returns before advancing**

The function body is:

`return n++;`

The postfix increment operator has two linked effects:

- the expression's value is the old value of `n`;
- the stored binding is then incremented by one.

Therefore, with initial $n=10$:

- first call evaluates to ten, then stores eleven;
- second call evaluates to eleven, then stores twelve;
- third call evaluates to twelve, then stores thirteen.

This order exactly matches the requirement that the first result be the supplied starting value.

Using prefix increment `++n` without adjusting initialization would be wrong because the first call would return $n+1$.

**Why the mutation persists**

Each invocation executes in a new call frame, but all invocations refer to the same captured `n` binding from the one outer call. The statement does not create a local shadowing variable, so its increment updates that shared closure state.

The returned results need no separate history array. At any moment, the next answer is fully summarized by one number.

This is a useful state-compression observation: although behavior depends on how many calls occurred, the counter does not need to remember those calls individually.

**Independent counters have independent environments**

Calling `createCounter` twice creates two distinct lexical environments:

- `const a = createCounter(0)` captures one binding;
- `const b = createCounter(0)` captures another binding.

Calling `a()` does not change the state used by `b()`. Both may start at the same numeric value, but their bindings are different.

This independence would be lost if the implementation stored the count in one global variable. A global counter would make unrelated returned functions interfere.

**Negative and zero starting values need no special handling**

Incrementing is arithmetic, so the same logic works across negative values:

$$
-2,-1,0,1,2,\ldots
$$

There is no boundary case when crossing zero. The first result always equals the captured starting number, and each subsequent stored state is one larger.

If the returned function is never called, no increment occurs. Creating the closure alone does not evaluate `n++`.

**A simple invariant proves the sequence**

Before the counter's $c$-th call, using zero-based $c$, maintain:

$$
n=n_{\text{start}}+c.
$$

Before the first call, $c=0$, so the invariant holds by initialization.

During the call, postfix increment returns the current value $n_{\text{start}}+c$, which is exactly the required result for that call. It then stores

$$
n_{\text{start}}+c+1,
$$

establishing the invariant before the next call. By induction, every returned value is correct.

**Why returning a function matters**

The problem does not ask `createCounter` to produce the first number immediately. It asks for a reusable callable object whose behavior changes over time.

Returning the inner function delays each observation and state transition until the caller invokes it. This factory pattern lets callers create as many counters as needed with different starting states.

**JavaScript numeric semantics**

Within the stated range and number of calls, values remain safely representable as ordinary JavaScript numbers. The postfix operator converts its operand to a numeric value, but `n` is already guaranteed to be an integer.

The inner function accepts no declared parameters. Extra arguments supplied by a caller would simply be ignored because the implementation never reads them.

**Why the minimal implementation is still complete**

There is no need for an object with a `count` field, a class, or a separate initialization flag. The closure supplies storage, and postfix increment combines the return and transition in one expression.

Short code is not automatically self-explanatory, but here every language feature directly corresponds to a contract requirement:

- closure gives persistence;
- captured parameter gives initial state;
- postfix increment returns current value;
- mutation prepares the next value.

## Complexity detail

Creating a counter allocates one function and one captured numeric binding, so creation takes $O(1)$ time and $O(1)$ space.

Each call performs one numeric read, one increment, one write, and one return. Per-call time is $O(1)$, and the retained state remains $O(1)$ regardless of the number of calls.

If $q$ calls are considered together, total execution time is $O(q)$, but the manifest correctly states the per-operation bound of $O(1)$.

## Alternatives and edge cases

- **Explicit local state variable:** Copy `n` into `let current = n` and return `current++`; behavior and complexity are the same.
- **Increment before return:** Initialize to $n-1$, then use prefix increment. This works but is less direct.
- **Class instance:** A class with a field and method models the state but adds unnecessary syntax for one operation.
- **Global variable:** Incorrect because separately created counters would interfere.
- **Negative start:** Postfix increment naturally produces the required increasing sequence through zero.
- **Zero calls:** The closure is created, but its state is never changed or observed.
- **Multiple counters:** Each factory call captures a separate binding.
- **Extra call arguments:** They are ignored and do not affect state.
- **Prefix versus postfix:** `n++` returns the old value; `++n` would return the incremented value.
- **Encapsulation:** The captured binding is not exposed as a writable public object property.
