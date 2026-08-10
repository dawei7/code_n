## General

**A closure remembers whether the opportunity was used**

`once(fn)` returns a wrapper that may forward at most one invocation to `fn`.

Local Boolean `called` begins false and is captured by the returned function. Because it belongs to the wrapper's lexical environment, it persists across every later call.

The entire policy is:

- when `called` is false, mark it true and invoke `fn`;
- when it is true, do nothing.

Falling off a JavaScript function without a return statement produces `undefined`, exactly the required later-call result.

**Forward the first call's arguments**

The wrapper accepts `...args`. Rest syntax gathers every supplied positional argument into an array in order.

On the first call:

`fn(...args)`

spreads that array back into positional arguments for the original function.

Thus, a call `onceFn(1,2,3)` behaves like `fn(1,2,3)` on its one permitted execution. The wrapper does not know or need to know the original function's arity.

**Mark before invoking**

Inside the first-call branch, the exact order is:

1. `called = true`;
2. `return fn(...args)`.

Setting the flag before running `fn` matters for two subtle cases.

First, `fn` might synchronously call the wrapper again. The recursive call sees `called === true` and is suppressed rather than invoking `fn` recursively without limit.

Second, `fn` might throw. The first call was still an attempted and actual call to `fn`. Because the flag was already set, a later wrapper call does not retry it.

This matches “called at most once” more robustly than setting the flag only after successful return.

**Return the exact first result**

The wrapper returns `fn(...args)` directly.

If `fn` returns a number, string, object, Promise, undefined, or any other value, the wrapper returns the same value. It does not transform, cache, or wrap the result.

If `fn` throws, that exception propagates to the first caller because no catch block intercepts it.

**Later calls are suppressed completely**

After the flag becomes true, the `if` body is skipped.

The wrapper:

- does not call `fn`;
- ignores the new arguments;
- performs no state change;
- reaches the function end and returns undefined.

Even if the first result itself was undefined, later behavior remains distinguishable through whether `fn` was executed, not through return-value truthiness.

**Trace the sum example**

Create a once-wrapper around three-argument sum.

The first call with $(1,2,3)$ sees false, sets true, invokes sum, and returns six.

The second call with $(2,3,6)$ sees true and returns undefined without computing eleven.

The underlying call count is one.

**Each wrapper has independent state**

Calling `once(fn)` twice creates two separate `called` bindings.

Each returned wrapper may invoke the same original `fn` once. Using one wrapper does not consume the allowance of another.

A flag stored globally or on `fn` itself would incorrectly couple separate wrappers.

**No result cache is needed**

This contract differs from memoization. Later calls must return undefined, not repeat the first result.

Therefore, the wrapper stores only whether invocation occurred. It does not retain the first arguments or return value.

This keeps persistent state constant even if the first result is a large object.

**Invocation context**

The exact implementation calls `fn(...args)` and does not forward the wrapper's dynamic `this`.

For the supplied arithmetic-style functions, behavior depends only on arguments. A general utility intended for object methods might instead call `fn.apply(this, args)`.

This distinction is worth knowing because argument forwarding and receiver forwarding are separate concerns in JavaScript.


Before every wrapper invocation:

- `called === false` exactly when `fn` has not yet been invoked through this wrapper;
- `called === true` exactly after the first forwarded invocation has begun.

The first call changes false to true before forwarding and returns the original result. Every later call leaves true unchanged and does not forward.

Therefore, `fn` is invoked at most once, the first wrapper call has identical argument/result behavior, and all subsequent calls yield undefined.

**Why a counter is unnecessary**

The wrapper only distinguishes zero previous calls from one-or-more previous calls. A Boolean contains exactly the needed information.

An integer call count would work but represent irrelevant states two, three, and so on.

## Complexity detail

Persistent wrapper state is one Boolean and one reference to `fn`, so retained space is $O(1)$.

Ignoring the original function's own work, the branch and flag update are $O(1)$. Collecting and spreading $a$ arguments costs $O(a)$ on the first call and rest collection may cost $O(a)$ on later calls as written. Under the problem's bounded argument size, the manifest treats invocation overhead as $O(1)$.

## Alternatives and edge cases

- **Cache and return the first result:** Implements a different contract because later calls should return undefined.
- **Set flag after `fn` returns:** Allows reentrant calls or retries after an exception, violating strict at-most-once semantics.
- **Numeric call counter:** Works but stores more state than a Boolean needs.
- **First call returns undefined:** It still consumes the one allowed invocation.
- **First call throws:** The error propagates and later calls remain suppressed.
- **Reentrant first call:** Pre-setting the flag prevents a second underlying invocation.
- **Several arguments:** Rest and spread preserve their order.
- **No arguments:** Empty argument list forwards correctly.
- **Independent wrappers:** Each factory call owns a separate flag.
- **Method receiver:** The exact source forwards arguments but not dynamic `this`.
