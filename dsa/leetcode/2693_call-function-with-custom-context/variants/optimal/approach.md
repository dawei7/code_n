## General

**Add one shared method to all functions**

JavaScript function objects inherit from `Function.prototype`. Assigning `callPolyfill` there makes the method available to ordinary functions through prototype lookup.

When code evaluates `fn.callPolyfill(context, ...args)`, the `this` value inside `callPolyfill` is `fn` itself. The implementation can therefore install and invoke the function without receiving it as a separate parameter.

The prototype method is shared rather than recreated for every function object.

**Create a collision-free temporary property**

To make `context` become `this` inside `fn` without using built-in `Function.call`, the solution temporarily makes the function a method of `context`.

It creates `const key = Symbol()`. Every new Symbol is unique, even if another Symbol has the same description.

Using that symbol as a property key guarantees it cannot collide with any existing string key or independently created symbol key on the context object.

**Why method-call syntax sets the receiver**

JavaScript determines a regular function's dynamic `this` from the call form.

After:

`context[key] = this`,

the expression:

`context[key](...args)`

is a method call whose base object is `context`. JavaScript therefore invokes the stored function with `this === context`.

This reproduces the central behavior of `call` without invoking the forbidden built-in method.

**Forward every additional argument**

The polyfill signature uses a rest parameter `...args`. It gathers all arguments after `context` in their original order.

The invocation spreads that array back into the target function. A call with values 10 and 1.1 therefore behaves as though the function were written as a method and called with exactly those two positional arguments.

Zero additional arguments also works because spreading an empty array supplies none.

**Return the target function's result**

The method immediately returns `context[key](...args)` from inside the `try` block.

If the target returns a number, string, Boolean, array, object, null, or undefined, `callPolyfill` forwards that result unchanged.

It does not wrap, serialize, or otherwise transform the value.

**Always clean up with `finally`**

The temporary symbol property should exist only during invocation.

The `finally` block executes `delete context[key]` whether the target:

- returns normally;
- returns early;
- throws an exception.

Without `finally`, a thrown callback would skip ordinary cleanup and leave an unexpected property on the context.

After cleanup, the original exception still propagates and a normal return value still returns.

**Trace the addition example**

Suppose:

`fn` returns `this.a + b`, the context is `{a: 5}`, and the extra argument is 7.

`callPolyfill` stores `fn` under a fresh symbol on the context. Calling that property gives the function receiver `{a: 5}` and passes 7 as `b`.

The function computes 12. The symbol property is deleted, and 12 is returned.

The context's ordinary key `a` is untouched.

**Why a normal string key is riskier**

Using a temporary key such as `context.fn` might overwrite a real `fn` property already owned by the caller.

It would also require remembering and restoring the previous descriptor exactly. A fresh Symbol is guaranteed not to exist beforehand, so deletion restores the context's original own-property set.

Symbols are also omitted by common string-key enumeration such as `Object.keys`, reducing incidental visibility during the call.

**The context is temporarily mutated**

The technique does add and later delete one property on `context`. That is an implementation mechanism, not a persistent output change.

The contract guarantees a non-null object context suitable for the operation. A non-extensible or frozen object would reject adding the symbol and is outside those ordinary assumptions.

Any changes that `fn` itself deliberately makes through `this` are not undone; binding context is supposed to allow the function to interact with that object.

**Regular functions versus arrow functions**

Regular JavaScript functions receive dynamic `this` from method-call syntax, so the technique works as required.

Arrow functions capture `this` lexically and ignore call-site rebinding. No implementation based on `call`, `apply`, `bind`, or method syntax can change an arrow function's lexical receiver. The examples and intended interface use functions whose context is bindable.


Inside the prototype method, `this` identifies the target function. The fresh symbol stores that exact function as an own method of the requested context without colliding with existing properties.

Calling through the context supplies the exact receiver and spreads every remaining argument in order. The return statement forwards the result, and `finally` removes the only temporary property on every completion path.

Therefore the polyfill has the required observable invocation behavior without using `Function.call`.

## Complexity detail

Let $a$ be the number of additional arguments. Collecting the rest parameter and spreading it into the target both require $O(a)$ time. Symbol creation, property assignment, lookup, deletion, and result forwarding are $O(1)$ expected operations, excluding the target function's own work.

The rest-argument array uses $O(a)$ space. The Symbol and temporary property require $O(1)$ additional state. Cleanup prevents persistent storage growth across calls.

## Alternatives and edge cases

- **Built-in `call`:** Directly solves context binding but is explicitly forbidden.
- **Built-in `apply`:** Could pass the argument array and context, but bypasses the intended polyfill mechanism.
- **`bind(context)(...args)`:** Creates a bound function and works for regular functions, but relies on another built-in binding facility.
- **Temporary string key:** Risks overwriting an existing context property.
- **Target returns normally:** Its value is forwarded after cleanup.
- **Target throws:** `finally` deletes the symbol and the exception propagates.
- **No extra arguments:** The target is called with an empty argument list.
- **Many arguments:** Rest and spread preserve their order.
- **Target mutates `this`:** Those deliberate context changes persist; only the temporary symbol is removed.
- **Frozen or non-extensible context:** Cannot accept the temporary property and is outside the guaranteed JSON-object use.
- **Arrow function target:** Its lexical `this` cannot be rebound by JavaScript call syntax.
- **Prototype modification:** Appropriate for this challenge but should be used cautiously in shared production environments.
